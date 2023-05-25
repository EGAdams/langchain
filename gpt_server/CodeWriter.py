import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool


class CodeWriter:
    @staticmethod
    async def write_code():
        request_data = await request.get_json(force=True)
        code = request_data.get("code")
        directory = request_data.get("directory")
        filename = request_data.get("filename", "code.py")

        if not code:
            return Response(response='No code provided', status=400)

        if not directory:
            directory = os.path.join(tempfile.gettempdir(), str(random.randint(1000, 9999)))

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, filename)

        with open(file_path, 'w') as file:
            file.write(code)

        logging_code.logger.warning('write_code executed')
        logging_code.logger.error('write_code executed')
        return Response(response=f'Code written to {file_path}', status=200)