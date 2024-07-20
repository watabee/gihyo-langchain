# StrOutputParser : ChatModelの出力から単一の文字列を出力したい場合に使うクラス
from langchain_core.messages import AIMessage
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
message = AIMessage(content="こんにちは！元気ですか？何かお手伝いできることはありますか？")
result = parser.invoke(message)
print(result)
