import os
import logging_code

from quart import request, Response


class FileReader:
    @staticmethod
    async def read_file():
        request_data = await request.get_json(force=True)
        filepath = request_data.get("filepath")

        if not filepath:
            return Response(response='No filepath provided', status=400)

        if not os.path.exists(filepath):
            return Response(response=f'File {filepath} does not exist', status=404)

        with open(filepath, 'r') as file:
            content = file.read()

        logging_code.logger.warning('read_file executed')
        logging_code.logger.error('read_file executed')
        return Response(response=content, status=200)