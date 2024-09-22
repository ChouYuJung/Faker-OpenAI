import random
from typing import Optional

from faker_openai._utils import fake

try:
    from openai.types.chat.chat_completion_assistant_message_param import (
        ChatCompletionAssistantMessageParam,
    )
    from openai.types.chat.chat_completion_function_message_param import (
        ChatCompletionFunctionMessageParam,
    )
    from openai.types.chat.chat_completion_system_message_param import (
        ChatCompletionSystemMessageParam,
    )
    from openai.types.chat.chat_completion_tool_message_param import (
        ChatCompletionToolMessageParam,
    )
    from openai.types.chat.chat_completion_user_message_param import (
        ChatCompletionUserMessageParam,
    )
except ImportError:
    pass


def gen_chat_system_message():
    return dict(
        content=fake.paragraph(),
        role="system",
        name=fake.name(),
    )  # type: ignore


def gen_chat_user_message():
    return dict(
        content=fake.paragraph(),
        role="user",
        name=fake.name(),
    )  # type: ignore


def get_chat_assistant_message(with_func: bool = False, with_tool: bool = False):
    if with_func:
        return dict(
            content=fake.paragraph(),
            role="assistant",
            function_call=dict(
                name="_".join(fake.words(random.randint(1, 3))),
                arguments=fake.words(random.randint(1, 3)),
            ),
        )  # type: ignore
    if with_tool:
        return dict(
            content=fake.paragraph(),
            role="assistant",
            tool_calls=[get_chat_tool_message()],
        )  # type: ignore
    return dict(
        content=fake.paragraph(),
        role="assistant",
    )  # type: ignore


def get_chat_tool_message(parts_num: Optional[int] = None):
    if parts_num is not None:
        return dict(
            content=[
                {"text": fake.paragraph(), "type": "text"} for _ in range(parts_num)
            ],
            role="tool",
            tool_call_id=f"call_{random.randint(1000, 9999)}",
        )  # type: ignore
    return dict(
        content=fake.paragraph(),
        role="tool",
        tool_call_id=f"call_{random.randint(1000, 9999)}",
    )  # type: ignore


class FakerOpenaiMessage:

    def chat_tool_message(
        self, parts_num: Optional[int] = None
    ) -> "ChatCompletionToolMessageParam":

        if parts_num is not None:
            return dict(
                content=[
                    {
                        "text": fake.paragraph(),
                        "type": "text",
                    }
                    for _ in range(parts_num)
                ],
                role="tool",
                tool_call_id=f"call_{random.randint(1000, 9999)}",
            )  # type: ignore
        return dict(
            content=fake.paragraph(),
            role="tool",
            tool_call_id=f"call_{random.randint(1000, 9999)}",
        )  # type: ignore

    def chat_user_message(
        self, parts_num: Optional[int] = None
    ) -> "ChatCompletionUserMessageParam":
        if parts_num is not None:
            return dict(
                content=[
                    {
                        "text": fake.paragraph(),
                        "type": "text",
                    }
                    for _ in range(parts_num)
                ],
                role="user",
                name=fake.name(),
            )  # type: ignore
        return dict(
            content=fake.paragraph(),
            role="user",
            name=fake.name(),
        )  # type: ignore

    def chat_system_message(
        self, parts_num: Optional[int] = None
    ) -> "ChatCompletionSystemMessageParam":
        if parts_num is not None:
            return dict(
                content=[
                    {
                        "text": fake.paragraph(),
                        "type": "text",
                    }
                    for _ in range(parts_num)
                ],
                role="system",
                name=fake.name(),
            )  # type: ignore
        return dict(
            content=fake.paragraph(),
            role="system",
            name=fake.name(),
        )  # type: ignore

    def chat_function_message(
        self, parts_num: Optional[int] = None
    ) -> "ChatCompletionFunctionMessageParam":
        if parts_num is not None:
            return dict(
                content=[
                    {
                        "text": fake.paragraph(),
                        "type": "text",
                    }
                    for _ in range(parts_num)
                ],
                role="function",
                name=f"function_{random.randint(1, 5)}",
            )  # type: ignore
        return dict(
            content=fake.paragraph(),
            role="function",
            name=f"function_{random.randint(1, 5)}",
        )  # type: ignore

    def chat_assistant_message(
        self, *, with_func: bool = False, with_tool: bool = False
    ) -> "ChatCompletionAssistantMessageParam":
        if with_func:
            return dict(
                content=fake.paragraph(),
                role="assistant",
                function_call=dict(
                    name="_".join(fake.words(random.randint(1, 3))),
                    arguments=fake.words(random.randint(1, 3)),
                ),
            )  # type: ignore
        if with_tool:
            return dict(
                content=fake.paragraph(),
                role="assistant",
                tool_calls=[self.chat_tool_message()],
            )  # type: ignore
        return dict(
            content=fake.paragraph(),
            role="assistant",
        )  # type: ignore
