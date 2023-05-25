import os
from typing import Dict,Optional
from base_tool import BaseTool
from python_repl import PythonREPL
import logging_code

class PythonREPLTool(BaseTool):
    """A tool for running python code in a REPL."""

    name = "Python REPL"
    description = (
        "A Python shell. Use this to execute python commands. "
        "Input should be a valid python command. "
        "If you want to see the output of a value, you should print it out "
        "with `print(...)`."
    )
    python_repl: PythonREPL = PythonREPL()
    sanitize_input: bool = True

    def _run(self, query: str) -> str:
        """Use the tool."""
        if self.sanitize_input:
            query = query.strip().strip("```")
        result = self.python_repl.run(query)
        logging_code.logger.warning(f'PythonREPLTool._run executed with query: {query}')
        logging_code.logger.error(f'PythonREPLTool._run executed with result: {result}')
        return result

    async def _arun(self, query: str) -> str:
        """Use the tool asynchronously."""
        raise NotImplementedError("PythonReplTool does not support async")