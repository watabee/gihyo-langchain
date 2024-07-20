from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o-mini")
messages = [("user", "こんにちは")]
result = model.invoke(messages)
print(result)
