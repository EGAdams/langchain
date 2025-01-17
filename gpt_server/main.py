import os
import subprocess
import tempfile
import random
import logging_code

from quart import request, Response, Quart, jsonify
import quart_cors
import quart

from PythonCodeRunner import PythonCodeRunner
from PythonAstCodeRunner import PythonAstCodeRunner
from langchain.gpt_server.Fileriter import CodeWriter
from FileReader import FileReader

app = quart_cors.cors(quart.Quart(__name__), allow_origin="https://chat.openai.com")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.post("/run_python_code")
async def run_python_code():
    return await PythonCodeRunner.run_python_code()

@app.post("/run_python_ast_code")
async def run_python_ast_code():
    return await PythonAstCodeRunner.run_python_ast_code()

# @app.post("/write_code")
# async def write_code():
#     return await CodeWriter.write_code()

# @app.post("/read_file")
# async def read_file():
#     return await FileReader.read_file()

@app.get("/logo.png")
async def plugin_logo():
    logo_path = os.path.join(BASE_DIR, 'logo.png')
    return await quart.send_file(logo_path, mimetype='image/png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest():
    host = request.headers['Host']
    manifest_path = os.path.join(BASE_DIR, ".well-known", "ai-plugin.json")
    with open(manifest_path) as f:
        text = f.read()
        return quart.Response(text, mimetype="text/json")

@app.get("/openapi.yaml")
async def openapi_spec():
    host = request.headers['Host']
    openapi_path = os.path.join(BASE_DIR, "openapi.yaml")
    with open(openapi_path) as f:
        text = f.read()
        return quart.Response(text, mimetype="text/yaml")

def main():
    app.run(debug=True, host="0.0.0.0", port=5003)

if __name__ == "__main__":
    main()
