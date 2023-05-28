from langchain.agents.agent import BaseSingleActionAgent
from langchain.agents.agent_types import AgentType
from langchain.agents.tools import InvalidTool
from langchain.base_language import BaseLanguageModel
from langchain.callbacks.base import BaseCallbackManager
from langchain.callbacks.manager import Callbacks
from langchain.schema import ( AgentAction, AgentFinish )

from typing import Any, Dict, List, Sequence, Tuple, Union, Optional

from langchain.tools.base import BaseTool

class CodeGenAgent(BaseSingleActionAgent):
    tools: List[BaseTool]

    def __init__(self, tools: List[Dict[str, Any]]) -> None:
        tool_instances = [self._create_tool(tool) for tool in tools]
        super().__init__(tools=tool_instances)
        self.tools = tool_instances

    def _create_tool(self, tool: Dict[str, Any]) -> BaseTool:
        # Create a BaseTool instance from the dictionary
        # This is a simplified example, you might need to adjust it based on your actual tool classes
        tool_class = tool.pop('class')
        return tool_class(**tool)




    @property
    def return_values(self) -> List[str]:
        return ["output"]

    def get_allowed_tools(self) -> Optional[List[str]]:
        return [tool.name for tool in self.tools]

    def plan(
        self,
        intermediate_steps: List[Tuple[AgentAction, str]],
        callbacks: Callbacks = None,
        **kwargs: Any,
    ) -> Union[AgentAction, AgentFinish]:
        # Get the last action and its result
        last_action, last_result = intermediate_steps[-1] if intermediate_steps else (None, None)

        # If there are no intermediate steps, choose the first tool
        if last_action is None:
            return AgentAction(self.tools[0].name, kwargs)

        # If the last action was successful, choose the next tool
        if last_result == "success":
            next_tool_index = self.tools.index(last_action.tool) + 1
            if next_tool_index < len(self.tools):
                return AgentAction(self.tools[next_tool_index].name, kwargs)
            else:
                return AgentFinish("success")

        # If the last action was not successful, retry the same tool
        else:
            return AgentAction(last_action.tool, kwargs)

    async def aplan(
        self,
        intermediate_steps: List[Tuple[AgentAction, str]],
        callbacks: Callbacks = None,
        **kwargs: Any,
    ) -> Union[AgentAction, AgentFinish]:
        # This method can simply call the synchronous plan method
        return self.plan(intermediate_steps, callbacks, **kwargs)


    @property
    def input_keys(self) -> List[str]:
        return [ tool.name for tool in self.tools ]


    @property
    def _agent_type(self) -> str:
        return str(AgentType.CODE_GEN.value)

    @classmethod
    def from_llm_and_tools(
        cls,
        llm: BaseLanguageModel,
        tools: Sequence[BaseTool],
        callback_manager: Optional[BaseCallbackManager] = None,
        **kwargs: Any,
    ) -> BaseSingleActionAgent:
        return cls(tools)

