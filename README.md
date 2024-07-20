# gihyo-langchain

Software Design 2024年8月号のLLMアプリ開発入門のサンプルアプリ

## 環境構築

```shell
$ python -m venv venv
$ source venv/bin/activate
$ which python # venv 内であればOK

$ pip install langchain==0.2.3
$ pip install langchain-openai==0.1.8
$ pip install langchain-community==0.2.4
```

```shell
$ export OPENAI_API_KEY=sk-***
```

PyPDFLoader を使うための設定

```shell
$ pip install pypdf==4.2.0
$ mkdir -p data
$ curl https://raw.githubusercontent.com/langchain-ai/langchain/master/libs/community/tests/examples/layout-parser-paper.pdf > data/layout-parser-paper.pdf
```

RecursiveCharacterTextSplitter を使うための設定

```shell
$ pip install langchain-text-splitters==0.2.1
```

Chroma を使うための設定

```shell
$ pip install langchain-chroma==0.1.1
```
