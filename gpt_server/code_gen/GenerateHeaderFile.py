import logging
import os

from pydantic import Field
from langchain.tools.base import BaseTool

class GenerateHeaderFile( BaseTool ):
    base_directory: str = Field(...)
    template_file:  str = Field(...)
    
    def __init__(self, name: str, description: str, base_directory: str, template_file: str ):  
        super().__init__(name=name, description=description, base_directory=base_directory )
        self.template_file=template_file
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
    tool = GenerateHeaderFile( r"C:\Users\eg197\gpt_write_python\code_gen\\", r"C:\Users\eg197\gpt_write_python\code_gen\header_template.txt" )
    print(tool.create_header_file( "TestClassDeleteMe" ))