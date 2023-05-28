import asyncio
from typing import List, Optional, Type, Union
from pydantic import BaseModel, Field

from langchain.tools.base import BaseTool
from langchain.tools.shell.tool import ShellTool, _get_platform
from langchain.utilities.bash import BashProcess
from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)


class ShellInput(BaseModel):
    """Commands for the ShellExecutor tool."""
    commands: Union[str, List[str]] = Field(
        ..., description="List of shell commands to run. Deserialized using json.loads"
    )


def _get_default_bash_process() -> BashProcess:
    return BashProcess()

class ShellExecutor(ShellTool):
    """Tool to run shell commands."""
    process: BashProcess = Field(default_factory=_get_default_bash_process)
    name: str = "shell_executor"
    description: str = f"Run shell commands on this {_get_platform()} machine."
    args_schema: Type[BaseModel] = ShellInput

    def _run(
        self,
        commands: Union[str, List[str]],
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Run commands and return final output."""
        return self.process.run(commands)

    async def _arun(
        self,
        commands: Union[str, List[str]],
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> str:
        """Run commands asynchronously and return final output."""
        return await asyncio.get_event_loop().run_in_executor(
            None, self.process.run, commands
        )


