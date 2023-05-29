import logging
from typing import Dict
from pydantic import Field
from langchain.tools.base import BaseTool
import os

class GenerateCppFile( BaseTool ):
    
    base_directory: str = Field(...)
    template_file: str  = ""         # !!! this cost me hours!
    
    def __init__(self, name_arg: str, description_arg: str, base_directory_arg: str, template_file_arg: str ):  
        super().__init__(name=name_arg, description=description_arg, base_directory=base_directory_arg )
        self.template_file=template_file_arg
        logging.basicConfig( level=logging.INFO )  

    def validate_class_name(self, class_name: str) -> bool:
        # Check if class name is not empty
        if not class_name:
            return False

        # Check if class name contains invalid characters
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        if any(char in class_name for char in invalid_chars):
            return False

        return True

    def run(self, class_name: str) -> Dict[str, str]:
        if self.validate_class_name(class_name):
            file_path = os.path.join(self.base_directory, f"{class_name}.cpp")
            with open(self.template_file, 'r') as template:
                content = template.read()
            content = content.replace("{CLASS_NAME}", class_name)
            with open(file_path, 'w') as file:
                file.write(content)
            return {"message": f"Cpp file '{class_name}.cpp' created successfully."}
        else:
            return {"message": f"Failed to create cpp file '{class_name}.cpp'. Invalid class name."}

    def _run(self, *args, **kwargs):
        # Implement the synchronous execution logic here
        print( "*** WARNING: GenerateDirectories._run() called, but not implemented. ***" )
        
    async def _arun(self, *args, **kwargs):
        # Implement the asynchronous execution logic here
        print( "*** WARNING: GenerateDirectories._arun() called, but not implemented. ***" )

# if main
if __name__ == "__main__":
    tool = GenerateCppFile(  
    name_arg='Header File Generator',  
    description_arg='A tool for generating headers',  
    base_directory_arg=r"C:\Users\eg197\langchain\gpt_server\code_gen\\",  
    template_file_arg=r"C:\Users\eg197\langchain\gpt_server\code_gen\cpp_template.txt" )  
    print( tool.run( "TestClassDeleteMe" ))
