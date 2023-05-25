import os
import subprocess


class PythonFileExecutor:
    # @command("execute_python_file", "Execute Python File", '"filename": "<filename>"')
    def execute_python_file(self, filename: str) -> str:
        """Execute a Python file in a Docker container and return the output

        Args:
            filename (str): The name of the file to execute

        Returns:
            str: The output of the file
        """
        # # logger.info(f"Executing file '{filename}'")

        if not filename.endswith(".py"):
            return "Error: Invalid file type. Only .py files are allowed."

        if not os.path.isfile(filename):
            return f"Error: File '{filename}' does not exist."

        if self.we_are_running_in_a_docker_container():
            result = subprocess.run(
                f"python {filename}", capture_output=True, encoding="utf8", shell=True
            )
            if result.returncode == 0:
                return result.stdout
            else:
                return f"Error: {result.stderr}"

        try:
            client = docker.from_env()
            image_name = "python:3-alpine"
            try:
                client.images.get(image_name)
                ## logger.warn(f"Image '{image_name}' found locally")
            except ImageNotFound:
                # # logger.info(
                #     f"Image '{image_name}' not found locally, pulling from Docker Hub"
                # )
                low_level_client = docker.APIClient()
                for line in low_level_client.pull(image_name, stream=True, decode=True):
                    status = line.get("status")
                    progress = line.get("progress")
                    if status and progress:
                        # logger.info(f"{status}: {progress}")
                        print( f"{status}: {progress}" )
                    elif status:
                        # logger.info(status)
                        print( status )
            container = client.containers.run(
                image_name,
                f"python {Path(filename).relative_to(CFG.workspace_path)}",
                volumes={
                    CFG.workspace_path: {
                        "bind": "/workspace",
                        "mode": "ro",
                    }
                },
                working_dir="/workspace",
                stderr=True,
                stdout=True,
                detach=True,
            )

            container.wait()
            logs = container.logs().decode("utf-8")
            container.remove()

            return logs

        except docker.errors.DockerException as e:
            # logger.warn(
            #     "Could not run the script in a container. If you haven't already, please install Docker https://docs.docker.com/get-docker/"
            # )
            return f"Error: {str(e)}"

        except Exception as e:
            return f"Error: {str(e)}"

    def we_are_running_in_a_docker_container(self) -> bool:
        """Check if we are running in a Docker container

        Returns:
            bool: True if we are running in a Docker container, False otherwise
        """
        return os.path.exists("/.dockerenv")