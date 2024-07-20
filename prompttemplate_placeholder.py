# MessagesPlaceholder : メッセージのリストをそのまま渡したい場合に便利なクラス
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "与えた単語を{language}に変換してください"),
    MessagesPlaceholder("messages")
])
result = prompt_template.invoke({
    "language": "日本語",
    "messages": [
        HumanMessage(content="Hello"),
        AIMessage(content="こんにちは"),
        HumanMessage(content="Good Morning")
    ]
})
print(result)
