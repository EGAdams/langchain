import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool
from python_ast_repl_tool import PythonAstREPLTool


class PythonAstCodeRunner:
    @staticmethod
    async def run_python_ast_code():
        request_data = await request.get_json(force=True)
        code = request_data.get("code")
        tool = PythonAstREPLTool()
        result = tool._run(code)
        logging_code.logger.warning('run_python_ast_code executed')
        logging_code.logger.error('run_python_ast_code executed')
        return Response(response=result, status=200)