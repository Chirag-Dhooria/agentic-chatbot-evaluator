from typing import Protocol, TypeVar

from pydantic import BaseModel


T = TypeVar("T", bound=BaseModel)


class LLMProvider(Protocol):
    def structured_output(
        self,
        schema: type[T],
    ):
        ...