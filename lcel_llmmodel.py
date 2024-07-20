# LCEL (LangChain Expression Language): コンポーネント間の一連のフローを、Pipe(|)を使って構築するLangChain独自の構文
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()
prompt = ChatPromptTemplate.from_messages([
    ("system", "与えた単語を{language}に変換してください"),
    ("user", "hi")
])

chain = prompt | model | parser
result = chain.invoke({"language": "日本語"})
print(result)
# => こんにちは
