# Generated by Django 4.1.7 on 2023-12-23 15:31

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("username", models.CharField(max_length=255)),
                ("apikey", models.CharField(max_length=32, null=True)),
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("dob", models.DateField(blank=True, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female"), ("N", "N/A")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "country",
                    models.CharField(
                        choices=[
                            ("AD", "Andorra"),
                            ("AE", "United Arab Emirates"),
                            ("AF", "Afghanistan"),
                            ("AG", "Antigua & Barbuda"),
                            ("AI", "Anguilla"),
                            ("AL", "Albania"),
                            ("AM", "Armenia"),
                            ("AO", "Angola"),
                            ("AQ", "Antarctica"),
                            ("AR", "Argentina"),
                            ("AS", "Samoa (American)"),
                            ("AT", "Austria"),
                            ("AU", "Australia"),
                            ("AW", "Aruba"),
                            ("AX", "Åland Islands"),
                            ("AZ", "Azerbaijan"),
                            ("BA", "Bosnia & Herzegovina"),
                            ("BB", "Barbados"),
                            ("BD", "Bangladesh"),
                            ("BE", "Belgium"),
                            ("BF", "Burkina Faso"),
                            ("BG", "Bulgaria"),
                            ("BH", "Bahrain"),
                            ("BI", "Burundi"),
                            ("BJ", "Benin"),
                            ("BL", "St Barthelemy"),
                            ("BM", "Bermuda"),
                            ("BN", "Brunei"),
                            ("BO", "Bolivia"),
                            ("BQ", "Caribbean NL"),
                            ("BR", "Brazil"),
                            ("BS", "Bahamas"),
                            ("BT", "Bhutan"),
                            ("BV", "Bouvet Island"),
                            ("BW", "Botswana"),
                            ("BY", "Belarus"),
                            ("BZ", "Belize"),
                            ("CA", "Canada"),
                            ("CC", "Cocos (Keeling) Islands"),
                            ("CD", "Congo (Dem. Rep.)"),
                            ("CF", "Central African Rep."),
                            ("CG", "Congo (Rep.)"),
                            ("CH", "Switzerland"),
                            ("CI", "Côte d'Ivoire"),
                            ("CK", "Cook Islands"),
                            ("CL", "Chile"),
                            ("CM", "Cameroon"),
                            ("CN", "China"),
                            ("CO", "Colombia"),
                            ("CR", "Costa Rica"),
                            ("CU", "Cuba"),
                            ("CV", "Cape Verde"),
                            ("CW", "Curaçao"),
                            ("CX", "Christmas Island"),
                            ("CY", "Cyprus"),
                            ("CZ", "Czech Republic"),
                            ("DE", "Germany"),
                            ("DJ", "Djibouti"),
                            ("DK", "Denmark"),
                            ("DM", "Dominica"),
                            ("DO", "Dominican Republic"),
                            ("DZ", "Algeria"),
                            ("EC", "Ecuador"),
                            ("EE", "Estonia"),
                            ("EG", "Egypt"),
                            ("EH", "Western Sahara"),
                            ("ER", "Eritrea"),
                            ("ES", "Spain"),
                            ("ET", "Ethiopia"),
                            ("FI", "Finland"),
                            ("FJ", "Fiji"),
                            ("FK", "Falkland Islands"),
                            ("FM", "Micronesia"),
                            ("FO", "Faroe Islands"),
                            ("FR", "France"),
                            ("GA", "Gabon"),
                            ("GB", "Britain (UK)"),
                            ("GD", "Grenada"),
                            ("GE", "Georgia"),
                            ("GF", "French Guiana"),
                            ("GG", "Guernsey"),
                            ("GH", "Ghana"),
                            ("GI", "Gibraltar"),
                            ("GL", "Greenland"),
                            ("GM", "Gambia"),
                            ("GN", "Guinea"),
                            ("GP", "Guadeloupe"),
                            ("GQ", "Equatorial Guinea"),
                            ("GR", "Greece"),
                            ("GS", "South Georgia & the South Sandwich Islands"),
                            ("GT", "Guatemala"),
                            ("GU", "Guam"),
                            ("GW", "Guinea-Bissau"),
                            ("GY", "Guyana"),
                            ("HK", "Hong Kong"),
                            ("HM", "Heard Island & McDonald Islands"),
                            ("HN", "Honduras"),
                            ("HR", "Croatia"),
                            ("HT", "Haiti"),
                            ("HU", "Hungary"),
                            ("ID", "Indonesia"),
                            ("IE", "Ireland"),
                            ("IL", "Israel"),
                            ("IM", "Isle of Man"),
                            ("IN", "India"),
                            ("IO", "British Indian Ocean Territory"),
                            ("IQ", "Iraq"),
                            ("IR", "Iran"),
                            ("IS", "Iceland"),
                            ("IT", "Italy"),
                            ("JE", "Jersey"),
                            ("JM", "Jamaica"),
                            ("JO", "Jordan"),
                            ("JP", "Japan"),
                            ("KE", "Kenya"),
                            ("KG", "Kyrgyzstan"),
                            ("KH", "Cambodia"),
                            ("KI", "Kiribati"),
                            ("KM", "Comoros"),
                            ("KN", "St Kitts & Nevis"),
                            ("KP", "Korea (North)"),
                            ("KR", "Korea (South)"),
                            ("KW", "Kuwait"),
                            ("KY", "Cayman Islands"),
                            ("KZ", "Kazakhstan"),
                            ("LA", "Laos"),
                            ("LB", "Lebanon"),
                            ("LC", "St Lucia"),
                            ("LI", "Liechtenstein"),
                            ("LK", "Sri Lanka"),
                            ("LR", "Liberia"),
                            ("LS", "Lesotho"),
                            ("LT", "Lithuania"),
                            ("LU", "Luxembourg"),
                            ("LV", "Latvia"),
                            ("LY", "Libya"),
                            ("MA", "Morocco"),
                            ("MC", "Monaco"),
                            ("MD", "Moldova"),
                            ("ME", "Montenegro"),
                            ("MF", "St Martin (French)"),
                            ("MG", "Madagascar"),
                            ("MH", "Marshall Islands"),
                            ("MK", "North Macedonia"),
                            ("ML", "Mali"),
                            ("MM", "Myanmar (Burma)"),
                            ("MN", "Mongolia"),
                            ("MO", "Macau"),
                            ("MP", "Northern Mariana Islands"),
                            ("MQ", "Martinique"),
                            ("MR", "Mauritania"),
                            ("MS", "Montserrat"),
                            ("MT", "Malta"),
                            ("MU", "Mauritius"),
                            ("MV", "Maldives"),
                            ("MW", "Malawi"),
                            ("MX", "Mexico"),
                            ("MY", "Malaysia"),
                            ("MZ", "Mozambique"),
                            ("NA", "Namibia"),
                            ("NC", "New Caledonia"),
                            ("NE", "Niger"),
                            ("NF", "Norfolk Island"),
                            ("NG", "Nigeria"),
                            ("NI", "Nicaragua"),
                            ("NL", "Netherlands"),
                            ("NO", "Norway"),
                            ("NP", "Nepal"),
                            ("NR", "Nauru"),
                            ("NU", "Niue"),
                            ("NZ", "New Zealand"),
                            ("OM", "Oman"),
                            ("PA", "Panama"),
                            ("PE", "Peru"),
                            ("PF", "French Polynesia"),
                            ("PG", "Papua New Guinea"),
                            ("PH", "Philippines"),
                            ("PK", "Pakistan"),
                            ("PL", "Poland"),
                            ("PM", "St Pierre & Miquelon"),
                            ("PN", "Pitcairn"),
                            ("PR", "Puerto Rico"),
                            ("PS", "Palestine"),
                            ("PT", "Portugal"),
                            ("PW", "Palau"),
                            ("PY", "Paraguay"),
                            ("QA", "Qatar"),
                            ("RE", "Réunion"),
                            ("RO", "Romania"),
                            ("RS", "Serbia"),
                            ("RU", "Russia"),
                            ("RW", "Rwanda"),
                            ("SA", "Saudi Arabia"),
                            ("SB", "Solomon Islands"),
                            ("SC", "Seychelles"),
                            ("SD", "Sudan"),
                            ("SE", "Sweden"),
                            ("SG", "Singapore"),
                            ("SH", "St Helena"),
                            ("SI", "Slovenia"),
                            ("SJ", "Svalbard & Jan Mayen"),
                            ("SK", "Slovakia"),
                            ("SL", "Sierra Leone"),
                            ("SM", "San Marino"),
                            ("SN", "Senegal"),
                            ("SO", "Somalia"),
                            ("SR", "Suriname"),
                            ("SS", "South Sudan"),
                            ("ST", "Sao Tome & Principe"),
                            ("SV", "El Salvador"),
                            ("SX", "St Maarten (Dutch)"),
                            ("SY", "Syria"),
                            ("SZ", "Eswatini (Swaziland)"),
                            ("TC", "Turks & Caicos Is"),
                            ("TD", "Chad"),
                            ("TF", "French S. Terr."),
                            ("TG", "Togo"),
                            ("TH", "Thailand"),
                            ("TJ", "Tajikistan"),
                            ("TK", "Tokelau"),
                            ("TL", "East Timor"),
                            ("TM", "Turkmenistan"),
                            ("TN", "Tunisia"),
                            ("TO", "Tonga"),
                            ("TR", "Turkey"),
                            ("TT", "Trinidad & Tobago"),
                            ("TV", "Tuvalu"),
                            ("TW", "Taiwan"),
                            ("TZ", "Tanzania"),
                            ("UA", "Ukraine"),
                            ("UG", "Uganda"),
                            ("UM", "US minor outlying islands"),
                            ("US", "United States"),
                            ("UY", "Uruguay"),
                            ("UZ", "Uzbekistan"),
                            ("VA", "Vatican City"),
                            ("VC", "St Vincent"),
                            ("VE", "Venezuela"),
                            ("VG", "Virgin Islands (UK)"),
                            ("VI", "Virgin Islands (US)"),
                            ("VN", "Vietnam"),
                            ("VU", "Vanuatu"),
                            ("WF", "Wallis & Futuna"),
                            ("WS", "Samoa (western)"),
                            ("YE", "Yemen"),
                            ("YT", "Mayotte"),
                            ("ZA", "South Africa"),
                            ("ZM", "Zambia"),
                            ("ZW", "Zimbabwe"),
                        ],
                        default="IN",
                        max_length=2,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=core.models.image_file_path
                    ),
                ),
                (
                    "profession",
                    models.CharField(
                        choices=[("S", "Student"), ("P", "Professional")],
                        default="S",
                        max_length=1,
                    ),
                ),
                ("is_verified", models.BooleanField(default=False)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="AIModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("model_id", models.CharField(max_length=255)),
                ("model_name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("created_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Community",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=50, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
            options={
                "verbose_name_plural": "Communities",
            },
        ),
        migrations.CreateModel(
            name="Domain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=50, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Industry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
            ],
            options={
                "verbose_name_plural": "Industries",
            },
        ),
        migrations.CreateModel(
            name="Institute",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Major",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="UserAIModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "aimodel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.aimodel"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150)),
                ("content", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to=core.models.image_file_path
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "community",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.community"
                    ),
                ),
                ("tags", models.ManyToManyField(blank=True, to="core.tag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Like",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now=True)),
                (
                    "reaction",
                    models.CharField(
                        choices=[
                            ("L", "Like"),
                            ("H", "Helpful"),
                            ("S", "Smart"),
                            ("F", "Funny"),
                            ("U", "Uplifting"),
                        ],
                        default="L",
                        max_length=1,
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="core.comment",
                    ),
                ),
                (
                    "post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="likes",
                        to="core.post",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="likes",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="community",
            name="domain",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="communities",
                to="core.domain",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to="core.post",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="replied_to",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="children",
                to="core.comment",
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="ai_models",
            field=models.ManyToManyField(through="core.UserAIModel", to="core.aimodel"),
        ),
        migrations.AddField(
            model_name="user",
            name="following",
            field=models.ManyToManyField(to="core.community"),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="industry",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.industry",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="institute",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.institute",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="major",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="core.major",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.permission",
                verbose_name="user permissions",
            ),
        ),
    ]
