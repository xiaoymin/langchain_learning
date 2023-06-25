from langchain.chains.openai_functions.openapi import get_openapi_chain

chain = get_openapi_chain("https://doc.xiaominfo.com/demo/data/knife4j.json")

result=chain.run("单纯文件上传")
print(result)