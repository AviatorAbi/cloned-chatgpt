from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate

from langchain.memory import ConversationBufferMemory

def get_gpt_response(prompt,memory,openai_api_key):
    system_prompt=ChatPromptTemplate.from_messages([("system","你是一个语气亲切活泼，喜欢使用emoji的AI助手，与你的用户交流时要尽量显得像朋友一样，轻松自然。请使用俚语、表情符号（如：😊，😂）以及幽默感来让对话更有趣。避免过于书面化的语言。你可以在适当的时候用一些轻松的语气词，比如‘嘿，’‘对吧’。")])
    model = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key=openai_api_key, base_url="https://api.aigc369.com/v1",prompt=system_prompt)
    chain = ConversationChain(llm=model, memory=memory)
    response = chain.invoke({"input": prompt})
    return response["response"]

memory = ConversationBufferMemory(return_messages = True)

