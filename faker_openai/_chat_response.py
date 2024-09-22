from typing import Dict

from faker_openai._chat_message import get_chat_assistant_message
from faker_openai._id import rand_chat_completion_id
from faker_openai._utils import fake


class FakerOpenaiChatResponse:

    def chat_response(
        self,
        n: int = 1,
        with_function_call: bool = False,
        with_tool_calls: bool = False,
    ) -> Dict:
        choices = []
        for _ in range(n):
            choice = {
                "index": _,
                "message": get_chat_assistant_message(
                    with_func=with_function_call, with_tool=with_tool_calls
                ),
                "finish_reason": fake.random_element(
                    ["stop", "length", "content_filter", "function_call", "tool_calls"]
                ),
            }
            choices.append(choice)

        return {
            "id": rand_chat_completion_id(),
            "object": "chat.completion",
            "created": int(fake.unix_time()),
            "model": fake.random_element(["gpt-3.5-turbo", "gpt-4"]),
            "choices": choices,
            "usage": {
                "prompt_tokens": fake.random_int(1, 1000),
                "completion_tokens": fake.random_int(1, 1000),
                "total_tokens": fake.random_int(1, 2000),
            },
            "system_fingerprint": fake.sha256(),
        }
