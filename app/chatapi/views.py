import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, ParseError, APIException
from rest_framework import status
from core.models import APIKey
import logging
from django.http import StreamingHttpResponse

# from .serializers import MessageSerializer
from .authentication import APIKeyAuthentication
from ai_components.chat_model import ChatModel
from rest_framework.exceptions import AuthenticationFailed


class APIKeyValidationView(APIView):
    """
    This view handles the validation of the API key and returns
    the associated model name and model ID.
    """

    def post(self, request):
        auth_header = request.META.get("HTTP_AUTHORIZATION", "")
        if auth_header.startswith("Bearer "):
            api_key = auth_header.split("Bearer ")[1]
        else:
            raise AuthenticationFailed("No API Key provided")
        try:
            api_key_obj = APIKey.objects.get(key=api_key)
            return Response(
                {
                    "data": [
                        {"model": api_key_obj.model_name, "id": api_key_obj.model_id}
                    ]
                },
                status=status.HTTP_200_OK,
            )
        except APIKey.DoesNotExist:
            raise AuthenticationFailed("Invalid API Key")


class ChatAPIView(APIView):
    # authentication_classes = [APIKeyAuthentication]

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

            print(f"messages: {messages}")

            chat_model = ChatModel()  # Create an instance of your ChatModel

            user_prompt = messages[-1]["content"] if messages else ""
            print(f"user_prompt: {user_prompt}")

            def stream_chat_responses():
                try:
                    for response_chunk in chat_model.predict(user_prompt):
                        print(f"response_chunk:{response_chunk}")
                        yield response_chunk
                except Exception as e:
                    raise RuntimeError(f"Error during prediction: {e}")

            return StreamingHttpResponse(
                stream_chat_responses(), content_type="text/plain"
            )
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
