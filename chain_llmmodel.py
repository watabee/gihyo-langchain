# LLMChain: LLMを呼び出しテキストとして出力できるチェーン
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain


model = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_messages([
    ("system", "与えた単語を{language}に変換してください"),
    ("user", "hi")
])

chain = LLMChain(llm=model, prompt=prompt)
result = chain.run({"language": "日本語"})
print(result)
# => こんにちは
