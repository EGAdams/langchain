import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool
from python_repl import PythonREPL
from python_repl_tool import PythonREPLTool

from langchain.agents.agent_toolkits import create_python_agent
from langchain.tools.python.tool import PythonREPLTool
from langchain.python import PythonREPL
from langchain.llms.openai import OpenAI

key=""
import os
os.environ["OPENAI_API_KEY"] = key


class PythonCodeRunner:
    @staticmethod
    async def run_python_code():
        request_data = await request.get_json(force=True)
        print( "getting code from request_data... " )
        code = request_data.get("code")
        print( "code: ", code )
        print( "creating python agent..." )
        agent_executor = create_python_agent(
            llm=OpenAI(temperature=0.2, max_tokens=3000 ),
            tool=PythonREPLTool(),
            verbose=True
        )
        print( "done executing agent_executor." )
        print( "running agent_executor..." )
        result = agent_executor.run(code)
        print( "result: ", result )
        print ( "returning agent_executor result..." )
        
        return Response(response=result, status=200)