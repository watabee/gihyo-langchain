# Tool: LLMが特定のツールを呼び出すために使用されるコンポーネント
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


@tool
def weather(place: str) -> str:
    """与えられた都市の天気をお伝えします"""
    return "晴れです"


model = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = model.bind_tools([weather])

result = llm_with_tools.invoke("東京の天気を教えて")
print(result.tool_calls)
# => [{'name': 'weather', 'args': {'place': '東京'}, 'id': 'call_CFpZTL5CKlnWulRbp8VmP6DZ', 'type': 'tool_call'}]
