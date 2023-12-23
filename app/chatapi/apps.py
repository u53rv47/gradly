from django.apps import AppConfig


class ChatapiConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chatapi"

    def ready(self):
        from ai_components.chat_model import ChatModel

        chat_model = ChatModel()
        setattr(self, "chat_model", chat_model)
