"""
Database Models
"""
import os
import uuid
import secrets
from pytz import country_names

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)


def image_file_path(instance, filename):
    """Generate file path for new post and profile image."""
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"
    return os.path.join("uploads", getattr(instance, "class_name"), filename)


class Domain(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Community(models.Model):
    class Meta:
        verbose_name_plural = "Communities"

    domain = models.ForeignKey(
        Domain, on_delete=models.CASCADE, related_name="communities"
    )
    name = models.CharField(max_length=50, db_index=True, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Industry(models.Model):
    class Meta:
        verbose_name_plural = "Industries"

    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Institute(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Major(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, db_index=True, unique=True)

    def __str__(self):
        return self.name


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user"""
        if not email:
            raise ValueError("User must have and email address.")
        email = self.normalize_email(email)

        username = email.split("@")[0]
        extra_fields["username"] = username
        apikey = secrets.token_urlsafe(32)
        extra_fields["apikey"] = apikey
        print(extra_fields)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password, **extra_fields):
        """Create and return a new superuser."""
        user = self.create_user(email=email, password=password, **extra_fields)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system"""

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255)

    apikey = models.CharField(max_length=64, null=True)
    ai_models = models.ManyToManyField("AIModel", through="UserAIModel")

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    dob = models.DateField(null=True, blank=True)
    GENDER_CHOICES = [("M", "Male"), ("F", "Female"), ("N", "N/A")]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    country = models.CharField(max_length=2, choices=country_names.items(), null=True)
    image = models.ImageField(upload_to=image_file_path, null=True)

    profession_choices = [("S", "Student"), ("P", "Professional")]
    profession = models.CharField(max_length=1, choices=profession_choices, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True)
    institute = models.ForeignKey(Institute, on_delete=models.SET_NULL, null=True)
    major = models.ForeignKey(Major, on_delete=models.SET_NULL, null=True)

    following = models.ManyToManyField(Community)

    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get("email"))

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserManager()

    class_name = "user"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    content = models.TextField()
    image = models.ImageField(upload_to=image_file_path, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    class_name = "post"

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Comment and reply in posts."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="comments",
    )
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    # If comment is a reply
    replied_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="children", blank=True, null=True
    )


class Like(models.Model):
    """Like/Dislike either Post or Comment"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="likes",
    )
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="likes", blank=True, null=True
    )
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="likes", blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now=True)
    REACTION_CHOICES = [
        ("L", "Like"),
        ("H", "Helpful"),
        ("S", "Smart"),
        ("F", "Funny"),
        ("U", "Uplifting"),
    ]
    reaction = models.CharField(max_length=1, choices=REACTION_CHOICES, default="L")


class AIModel(models.Model):
    model_id = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)

    def __str__(self):
        return self.model_name


class UserAIModel(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    aimodel = models.ForeignKey(AIModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.name} - {self.aimodel.model_name}"
