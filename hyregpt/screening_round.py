# all utilities required to conduct the interview come here
# Requirements from the chatbot
# Should remember context
# Should take into account the current state of the conversation
# Should know when to end the conversation
# Should ask questions that help in judging the candidate as objectively as possible and subsequently simplify the decision of passing for the next round

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationEntityMemory
from langchain.memory.prompt import ENTITY_MEMORY_CONVERSATION_TEMPLATE
from decouple import config



chat_llm = ChatOpenAI(temperature=0.2, openai_api_key=config("OPENAI_API_KEY"))

entity_memory = ConversationEntityMemory(llm=chat_llm)


conversation_chain = ConversationChain(
                                    llm=chat_llm,
                                    verbose=True,
                                    prompt=ENTITY_MEMORY_CONVERSATION_TEMPLATE,
                                    memory=entity_memory
                    )

# print (f"input variables: {conversation_chain.prompt.input_variables}")


# print (f"template:\n {conversation_chain.prompt.template}")


'''

user_input = input("HUMAN: ")

while user_input.lower() != "end":
    ai_response = conversation_chain.predict(input=user_input)
    entities = conversation_chain.memory.entity_store.store
    # print (f"Chat History: {chat_history}\n")

    print (f"Entities: {entities}\n")

    print (f"AI : {ai_response}\n")

    user_input = input("HUMAN: ")
'''
# TODO:
# 1. Test the chain
# 2. What we will have to customize in terms of prompt, output parser


