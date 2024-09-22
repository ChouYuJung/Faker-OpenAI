from typing import Dict, List, Optional, Union

from faker_openai._chat_message import gen_chat_system_message, gen_chat_user_message
from faker_openai._utils import fake


class FakerOpenaiChatRequest:

    def chat_request(
        self,
        messages_num: int = 3,
        frequency_penalty: Optional[float] = None,
        logit_bias: Optional[Dict[str, int]] = None,
        max_tokens: Optional[int] = None,
        n: Optional[int] = None,
        presence_penalty: Optional[float] = None,
        stop: Optional[Union[str, List[str]]] = None,
        temperature: Optional[float] = None,
        top_p: Optional[float] = None,
        user: Optional[str] = None,
    ) -> Dict:
        messages = [
            gen_chat_system_message(),
            *[gen_chat_user_message() for _ in range(messages_num - 1)],
        ]

        return {
            "model": fake.random_element(elements=("gpt-3.5-turbo", "gpt-4")),
            "messages": messages,
            "frequency_penalty": (
                frequency_penalty
                if frequency_penalty is not None
                else fake.pyfloat(min_value=-2.0, max_value=2.0)
            ),
            "logit_bias": (
                logit_bias
                if logit_bias is not None
                else {
                    str(fake.random_int(0, 100)): fake.random_int(-100, 100)
                    for _ in range(3)
                }
            ),
            "max_tokens": (
                max_tokens if max_tokens is not None else fake.random_int(1, 4096)
            ),
            "n": n if n is not None else fake.random_int(1, 5),
            "presence_penalty": (
                presence_penalty
                if presence_penalty is not None
                else fake.pyfloat(min_value=-2.0, max_value=2.0)
            ),
            "stop": (
                stop
                if stop is not None
                else fake.random_element(
                    elements=(None, fake.word(), [fake.word() for _ in range(2)])
                )
            ),
            "temperature": (
                temperature
                if temperature is not None
                else fake.pyfloat(min_value=0, max_value=2)
            ),
            "top_p": (
                top_p if top_p is not None else fake.pyfloat(min_value=0, max_value=1)
            ),
            "user": user if user is not None else fake.uuid4(),
        }
