import fileinput

class UpdateMakefile:
    def __init__(self, makefile_path, shell_executor):
        self.makefile_path = makefile_path
        self.shell_executor = shell_executor

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
