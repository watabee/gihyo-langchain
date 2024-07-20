# ChatPromptTemplate : 複数のメッセージ内の特定の文字列を変換する際に用いるクラス
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.prompts import SystemMessagePromptTemplate

# prompt_template = ChatPromptTemplate.from_messages([
#     ("system", "与えた単語を{langauge}に変換してください"),
#     ("user", "Hello")
# ])
prompt_template = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("与えた単語を{language}に変換してください"),
    HumanMessage(content="Hello")
])
result = prompt_template.invoke({"language": "日本語"})
print(result)
