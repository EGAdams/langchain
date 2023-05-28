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
generate_directories        = generate_directories.GenerateDirectories( r"C:\Users\eg197\langchain\gpt_server\code_gen\\" )
generate_header_file        = generate_header_file.GenerateHeaderFile(  r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\header_template.txt" )
generate_cpp_file           = generate_cpp_file.GenerateCppFile(        r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\cpp_template.txt"    )
shell_executor              = shell_executor.ShellExecutor() # for the next tool..
update_makefile             = update_makefile.UpdateMakefile(           r"C:\Users\eg197\langchain\gpt_server\code_gen\\", shell_executor )
generate_html_documentation = generate_html_documentation.GenerateHtmlDocumentation( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\html_template.txt" )
generate_unit_test          = generate_unit_test.GenerateUnitTest( r"C:\Users\eg197\langchain\gpt_server\code_gen\\", r"C:\Users\eg197\langchain\gpt_server\code_gen\unit_test_template.txt" )


# Create the CodeGenAgent
codegen_agent = CodeGenAgent(tools=[
    {'class': generate_directories, 'other_arg': 'value'},
    {'class': generate_header_file, 'other_arg': 'value'},
    {'class': generate_cpp_file, 'other_arg': 'value'},
    {'class': update_makefile, 'other_arg': 'value'},
    {'class': generate_html_documentation, 'other_arg': 'value'},
    {'class': generate_unit_test, 'other_arg': 'value'},
])



# Test the plan method
print(codegen_agent.plan([]))

# Test the aplan method
print(asyncio.run(codegen_agent.aplan([])))