import logging
import os

from pydantic import Field
from langchain.tools.base import BaseTool

class GenerateHeaderFile( BaseTool ):
    base_directory: str = Field(...)
    template_file: str
    
    def __init__(self, name_arg: str, description_arg: str, base_directory_arg: str, template_file_arg: str ):  
        super().__init__(name=name_arg, description=description_arg, base_directory=base_directory_arg )
        self.template_file=template_file_arg
        logging.basicConfig( level=logging.INFO )  

    def validate_class_name(self, class_name):
        # Check if class name is not empty
        if not class_name:
            return False
        # Check if class name contains invalid characters
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        if any(char in class_name for char in invalid_chars):
            return False
        return True

    def create_header_file(self, class_name):
        if self.validate_class_name(class_name):
            file_path = os.path.join(self.base_directory, f"{class_name}.h")
            with open(self.template_file, 'r') as template:
                content = template.read()
            content = content.replace("{CLASS_NAME}", class_name)
            with open(file_path, 'w') as file:
                file.write(content)
            return f"Header file '{class_name}.h' created successfully."
        else:
            return f"Failed to create header file '{class_name}.h'. Invalid class name."
        
    def _run(self, *args, **kwargs):
        # Implement the synchronous execution logic here
        print( "*** WARNING: GenerateDirectories._run() called, but not implemented. ***" )

    async def _arun(self, *args, **kwargs):
        # Implement the asynchronous execution logic here
        print( "*** WARNING: GenerateDirectories._arun() called, but not implemented. ***" )

# if main
if __name__ == "__main__":
    tool = GenerateHeaderFile(
    name_arg='Header File Generator',
    description_arg='A tool for generating headers',
    base_directory_arg=r"C:\Users\eg197\langchain\gpt_server\code_gen\\",
    template_file_arg=r"C:\Users\eg197\langchain\gpt_server\code_gen\header_template.txt" )
    print(tool.create_header_file( "TestClassDeleteMe" ))