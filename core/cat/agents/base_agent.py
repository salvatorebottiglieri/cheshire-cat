from typing import List
from abc import ABC, abstractmethod

from langchain_core.utils import get_colored_text

from cat.utils import BaseModelDict

class AgentOutput(BaseModelDict):
    output: str | None = None
    intermediate_steps: List = []
    return_direct: bool = False


class BaseAgent(ABC):

    @abstractmethod
    async def execute(*args, **kwargs) -> AgentOutput:
        pass