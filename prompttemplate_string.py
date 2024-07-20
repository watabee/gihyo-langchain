# PromptTemplate : 単一のメッセージ内の特定の文字列を変換する際に用いるクラス
from langchain_core.prompts import (PromptTemplate)

prompt_template = PromptTemplate.from_template("与えた単語を{language}に変換してください")
result = prompt_template.invoke({"language": "日本語"})
print(result)
