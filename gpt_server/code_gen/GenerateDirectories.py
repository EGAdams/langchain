import os
import logging
from langchain.tools.base import BaseTool
from pydantic import BaseModel, Field

class GenerateDirectories(BaseTool):
    base_directory: str = Field(...)
    
    def __init__(self, name: str, description: str, base_directory: str):  
        super().__init__(name=name, description=description, base_directory=base_directory)
        logging.basicConfig(level=logging.INFO)  

    def validate_directory_name(self, directory_name):
        # Check if directory name is not empty
        if not directory_name:
            return False

        # Check if directory name contains invalid characters
        invalid_chars = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*']
        if any(char in directory_name for char in invalid_chars):
            return False

        # Check if directory already exists
        if os.path.exists(os.path.join(self.base_directory, directory_name)):
            print("directory already exists, nothing to do...")
            return True

        return True

    def create_directory(self, directory_name):
        if self.validate_directory_name(directory_name):
            try:
                os.makedirs(os.path.join(self.base_directory, directory_name), exist_ok=True)
                logging.info(f"Directory '{directory_name}' created successfully.")
                return True
            except Exception as e:
                logging.error(f"Failed to create directory '{directory_name}'. Error: {str(e)}")
                return False
        else:
            logging.error(f"Failed to create directory '{directory_name}'. Invalid directory name or directory already exists.")
            return False
        
    def _run(self, *args, **kwargs):
        # Implement the synchronous execution logic here
        print( "*** WARNING: GenerateDirectories._run() called, but not implemented. ***" )

    async def _arun(self, *args, **kwargs):
        # Implement the asynchronous execution logic here
        print( "*** WARNING: GenerateDirectories._arun() called, but not implemented. ***" )
    
# if main
if __name__ == "__main__":
    base_dir = 'code_gen'
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    gd = GenerateDirectories(base_dir)
    print(gd.create_directory('test_dir'))
    print(gd.list_directories())