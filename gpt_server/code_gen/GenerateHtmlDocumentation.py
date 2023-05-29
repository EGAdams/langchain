import os
import logging

from pydantic import Field
from langchain.tools.base import BaseTool

class GenerateHtmlDocumentation(BaseTool):
    
    base_directory: str = Field(...)
    template_file: str  = ""         # !!! this cost me hours!
    
    def __init__(self, name_arg: str, description_arg: str, base_directory_arg: str, template_file_arg: str ):  
        super().__init__(name=name_arg, description=description_arg, base_directory=base_directory_arg )
        self.template_file=template_file_arg
        logging.basicConfig( level=logging.INFO )

    def validate_class_name(self, class_name):
        # Check if class name is not empty
        if not class_name:
            return False
        # Check if class name contains invalid characters
        invalid_chars = ['<', '>', ':', '\"', '/', '\\', '|', '?', '*']
        if any(char in class_name for char in invalid_chars):
            return False
        return True

    def create_html_file(self, class_name):
        if self.validate_class_name(class_name):
            file_path = os.path.join(self.base_directory, f"{class_name}.html")
            with open(self.template_file, 'r') as template:
                content = template.read()
            content = content.replace("{CLASS_NAME}", class_name)
            with open(file_path, 'w') as file:
                file.write(content)
            return f"HTML file '{class_name}.html' created successfully."
        else:
            return f"Failed to create HTML file '{class_name}.html'. Invalid class name."

    def update_html_file(self, class_name):
        # This method can be implemented based on your specific requirements
        pass

    def remove_html_file(self, class_name):
        if self.validate_class_name(class_name):
            file_path = os.path.join(self.base_directory, f"{class_name}.html")
            if os.path.exists(file_path):
                os.remove(file_path)
                return f"HTML file '{class_name}.html' removed successfully."
            else:
                return f"HTML file '{class_name}.html' does not exist."
        else:
            return f"Failed to remove HTML file '{class_name}.html'. Invalid class name."
    
    
    def _run(self, *args, **kwargs):
        # Implement the synchronous execution logic here
        print( "*** WARNING: GenerateDirectories._run() called, but not implemented. ***" )
        
    async def _arun(self, *args, **kwargs):
        # Implement the asynchronous execution logic here
        print( "*** WARNING: GenerateDirectories._arun() called, but not implemented. ***" )

# if main
if __name__ == "__main__":
    tool = GenerateHtmlDocumentation( "GenerateHtmlDocumentation", "This tool generates HTML documentation for a given class", r"C:\\Users\\eg197\\gpt_write_python\\code_gen\\\\", r"C:\\Users\\eg197\\gpt_write_python\\code_gen\\html_template.txt" )
    print(tool.create_html_file( "NewClass" ))
