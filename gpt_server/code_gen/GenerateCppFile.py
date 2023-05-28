import os

class GenerateCppFile:
    def __init__(self, base_directory, template_file):
        self.base_directory = base_directory
        self.template_file = template_file

    def validate_class_name(self, class_name):
        # Check if class name is not empty
        if not class_name:
            return False
        # Check if class name contains invalid characters
        invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
        if any(char in class_name for char in invalid_chars):
            return False
        return True

    def create_cpp_file(self, class_name):
        if self.validate_class_name(class_name):
            file_path = os.path.join(self.base_directory, f"{class_name}.cpp")
            with open(self.template_file, 'r') as template:
                content = template.read()
            content = content.replace("{CLASS_NAME}", class_name)
            with open(file_path, 'w') as file:
                file.write(content)
            return f"Cpp file '{class_name}.cpp' created successfully."
        else:
            return f"Failed to create cpp file '{class_name}.cpp'. Invalid class name."

# if main
if __name__ == "__main__":
    tool = GenerateCppFile( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\cpp_template.txt" )
    print(tool.create_cpp_file("NewClass"))