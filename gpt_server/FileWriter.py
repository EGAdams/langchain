import os
import tempfile
import random
import logging_code

from quart import request, Response

from base_tool import BaseTool


class FileWriter:
    @staticmethod
    async def write_file():
        request_data = await request.get_json(force=True)
        file = request_data.get("file")
        directory = request_data.get("directory")
        filename = request_data.get("filename", "file.py")

        if not file:
            return Response(response='No file provided', status=400)

        if not directory:
            directory = os.path.join(tempfile.gettempdir(), str(random.randint(1000, 9999)))

        if not os.path.exists(directory):
            os.makedirs(directory)

        file_path = os.path.join(directory, filename)

        with open(file_path, 'w') as file:
            file.write(file)

        logging_code.logger.warning('write_file executed')
        logging_code.logger.error('write_file executed')
        return Response(response=f'Code written to {file_path}', status=200)