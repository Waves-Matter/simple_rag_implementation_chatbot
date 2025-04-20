import chainlit as cl
from retriever import get_retriever
from history import save_history, return_history
from model_loader import load_reader_tokenizer_model
from answer import get_final_answer

token = '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'
file_path = "C:\Cods\ChatBot\docs\hc_articles.json"
embed_model_name = "thenlper/gte-small" 
llm_model_name = "HuggingFaceTB/SmolLM2-135M-Instruct" #small other model
#llm_model_name = "microsoft/bitnet-b1.58-2B-4T"

my_retriever = get_retriever(file_path, embed_model_name)
my_reader_llm, my_tokenizer = load_reader_tokenizer_model(llm_model_name, token)
chat_history = []

@cl.on_chat_start
async def main():
    
    starting_string = "Hi, how can I help You?"
    save_history(chat_history = chat_history, model_answer = starting_string)
    
    await cl.Message(content = starting_string).send()

@cl.on_message
async def main(message: cl.Message):
    
    user_answer = message.content
    
    save_history(chat_history = chat_history, prompt=user_answer)
    
    answer = get_final_answer(user_answer, chat_history, my_retriever, my_tokenizer, my_reader_llm)    
    
    await cl.Message(content=answer).send()
