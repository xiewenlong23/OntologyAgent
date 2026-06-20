from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any


@dataclass
class ToolResult:
    success: bool
    data: dict | None = None
    error: str | None = None
    execution_time_ms: int = 0


class Tool(ABC):
    name: str
    description: str
    params_schema: dict

    @abstractmethod
    async def execute(self, params: dict, context: dict) -> ToolResult:
        """Execute tool, return result or raise ToolExecutionError"""
        pass


class ToolExecutionError(Exception):
    pass
