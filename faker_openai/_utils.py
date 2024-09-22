import random
import string
from typing import Text

from faker import Faker

fake = Faker()


def rand_str(
    length: int = 10, chars: Text = string.ascii_letters + string.digits
) -> Text:
    """Generate a random string of fixed length."""

    return "".join(random.choice(chars) for _ in range(length))
