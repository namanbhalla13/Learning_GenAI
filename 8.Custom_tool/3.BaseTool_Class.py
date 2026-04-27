from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type


class MultiplyInput(BaseModel):
    a: int = Field(..., description="First number")
    b: int = Field(..., description="Second number")


class MultiplyTool(BaseTool):
    name: str = "multiply"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput


    def _run(self, a: int, b: int) -> int:
        return a * b


multiply_tool = MultiplyTool()


print(multiply_tool.invoke({"a": 2, "b": 4}))
print(multiply_tool.name)
print(multiply_tool.description)
print(multiply_tool.args)
print(multiply_tool.args_schema.model_json_schema())
