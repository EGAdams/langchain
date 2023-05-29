import fileinput
from tools import BaseTool

class UpdateMakefile(BaseTool):
    def __init__(self, name: str, description: str, base_directory: str, makefile_path: str, shell_executor):
        super().__init__(name=name, description=description, base_directory=base_directory)
        self.makefile_path = makefile_path
        self.shell_executor = shell_executor

    def run(self, file_path: str):
        self.add_file(file_path)

    def add_file(self, file_path):
        command = f"echo '{file_path}: ' >> {self.makefile_path}"
        return self.shell_executor.execute(command)

    def remove_file(self, file_path):
        for line in fileinput.input(self.makefile_path, inplace=True):
            if line.strip() != f"{file_path}: ":
                print(line, end='')

    def update_all_files(self, file_paths):
        for file_path in file_paths:
            self.add_file(file_path)

    def validate_makefile(self):
        command = f"make -n -f {self.makefile_path}"
        return self.shell_executor.execute(command)
    
    def _run(self, *args, **kwargs):
        # Implement the synchronous execution logic here
        print( "*** WARNING: GenerateDirectories._run() called, but not implemented. ***" )
        
    async def _arun(self, *args, **kwargs):
        # Implement the asynchronous execution logic here
        print( "*** WARNING: GenerateDirectories._arun() called, but not implemented. ***" )
