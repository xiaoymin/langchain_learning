from langchain.llms import OpenAI

# Before executing the following code, make sure to have
# your OpenAI key saved in the “OPENAI_API_KEY” environment variable.
llm = OpenAI(model="text-davinci-003", temperature=0.9)

text = "我想学习Python，你能否给我一些建议呢?"

print('query:',text)

print(llm(text))


