import chainlit as cl
from history import save_history
from model_loader import load_reader_tokenizer_model, load_retriever
from answer import get_model_answer

from text import token, file_path, embed_model_name, llm_model_name

my_retriever = load_retriever(file_path, embed_model_name)
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
    
    answer = get_model_answer(user_answer, chat_history, my_retriever, my_tokenizer, my_reader_llm)    
    
    await cl.Message(content=answer).send()
