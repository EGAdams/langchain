import asyncio
import GenerateDirectories as generate_directories
import  GenerateHeaderFile as generate_header_file
import GenerateCppFile     as generate_cpp_file
import UpdateMakeFile as update_makefile 
import GenerateHtmlDocumentation as generate_html_documentation
import GenerateUnitTest as generate_unit_test
import ShellExecutor as shell_executor
import CodeGenAgent as codegen_agent
from CodeGenAgent import CodeGenAgent

# Create the tools
update_makefile = update_makefile.UpdateMakefile( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", shell_executor )
generate_directories = generate_directories.GenerateDirectories(
    name='Directory Generator',
    description='A tool for generating directories',
    base_directory=r"C:\Users\eg197\langchain\gpt_server\code_gen\\" )

generate_header_file = generate_header_file.GenerateHeaderFile(
    name='Header File Generator',
    description='A tool for generating headers',
    base_directory=r"C:\Users\eg197\langchain\gpt_server\code_gen\\",
    template_file=r"C:\Users\eg197\langchain\gpt_server\code_gen\header_template.txt" )


generate_cpp_file           = generate_cpp_file.GenerateCppFile(        r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\cpp_template.txt"    )
shell_executor              = shell_executor.ShellExecutor() # for the next tool..
generate_html_documentation = generate_html_documentation.GenerateHtmlDocumentation( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\html_template.txt" )
generate_unit_test          = generate_unit_test.GenerateUnitTest( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\unit_test_template.txt" )


# Create a list of tool instances
tools = [
    generate_directories,
    generate_header_file,
    generate_cpp_file,
    update_makefile,
    generate_html_documentation,
    generate_unit_test
]

# Create a CodeGenAgent instance
codegen_agent = CodeGenAgent(tools=tools)



# Test the plan method
print(codegen_agent.plan([]))

# Test the aplan method
print(asyncio.run(codegen_agent.aplan([])))