import ast
import sys
from io import StringIO
from typing import Dict, Optional

from pydantic import Field, root_validator


class BaseTool:
    """A base class for tools."""

    name: str
    description: str

    def _run(self, query: str) -> str:
        raise NotImplementedError

    async def _arun(self, query: str) -> str:
        raise NotImplementedError
