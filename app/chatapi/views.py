import json
import logging

from django.contrib.auth import get_user_model

from django.apps import apps
from django.http import StreamingHttpResponse

from .authentication import APIKeyAuthentication

# from .serializers import MessageSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed, ParseError, APIException


class APIKeyValidationView(APIView):
    """
    This view handles the validation of the API key and returns
    the associated model name and model ID.
    """

    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            ai_models = user.ai_models.all()
            data = [
                {"model": "gpt-3.5-turbo", "id": "gpt-3.5-turbo-16k"},
            ]
            data.extend(
                [
                    {"model": ai_model.model_name, "id": ai_model.model_id}
                    for ai_model in ai_models
                ]
            )
            print(data)
            return Response(
                {"data": data},
                status=status.HTTP_200_OK,
            )
        except get_user_model().DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")


class ChatAPIView(APIView):
    authentication_classes = [APIKeyAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            data = json.loads(request.body)
            print(f"data:{data}")
            model = data.get("model")
            messages = data.get("messages")
            key = data.get("key")
            prompt = data.get("prompt")
            temperature = data.get("temperature")

            # if not all([model, messages, key, prompt, temperature]):
            #     raise ParseError("Missing required fields")

            # print(f"messages: {messages}")

            chat_model = apps.get_app_config("chatapi").chat_model

            user_prompt = messages[-1]["content"] if messages else ""
            print(f"user_prompt: {user_prompt}")

            response = chat_model.predict(user_prompt)
            return StreamingHttpResponse(response, content_type="text/plain")

            # def stream_chat_responses():
            #     try:
            #         for response_chunk in chat_model.predict(user_prompt):
            #             print(f"response_chunk:{response_chunk}")
            #             yield response_chunk
            #     except Exception as e:
            #         raise RuntimeError(f"Error during prediction: {e}")

            # return StreamingHttpResponse(
            #     stream_chat_responses(), content_type="text/plain"
            # )
            # return Response({"response": model_response}, status=status.HTTP_200_OK)

        except json.JSONDecodeError:
            # JSON parsing error
            logging.error("Invalid JSON received", exc_info=True)
            raise ParseError("Invalid JSON")

        except IndexError:
            # Error accessing last message (if messages is empty)
            logging.error(
                "Error accessing last message in messages array", exc_info=True
            )
            raise ParseError("Error in processing messages")

        except KeyError:
            # Missing keys in the data dictionary
            logging.error("Missing keys in the data dictionary", exc_info=True)
            raise ParseError("Invalid data format")

        except Exception as e:
            # Generic exception handler for any other unforeseen errors
            logging.error(f"Unexpected error: {e}", exc_info=True)
            raise APIException("An unexpected error occurred")
