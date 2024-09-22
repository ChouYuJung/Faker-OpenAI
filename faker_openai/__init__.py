from faker_openai._chat_message import FakerOpenaiMessage
from faker_openai._chat_request import FakerOpenaiChatRequest
from faker_openai._chat_response import FakerOpenaiChatResponse
from faker_openai._id import FakerOpenaiId


class FakerOpenAI(
    FakerOpenaiId, FakerOpenaiMessage, FakerOpenaiChatRequest, FakerOpenaiChatResponse
):
    pass
