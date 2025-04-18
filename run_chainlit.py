import chainlit as cl
from retriever import get_retriever
from prompt import get_final_prompt, is_connectivity_issue, has_country, is_device, is_OS
from model_loader import load_reader_tokenizer_model

token = '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'
file_path = "C:\Cods\ChatBot\docs\hc_articles.json"
embed_model_name = "thenlper/gte-small" 
#llm_model_name = "HuggingFaceTB/SmolLM2-135M-Instruct" #small other model
llm_model_name = "microsoft/bitnet-b1.58-2B-4T"

def generate_history(chat_history, prompt = None, model_answer = None):
    
    if prompt!=None:
        chat_history.append({"role": "user", "content": prompt})
        
    if model_answer!=None:
        chat_history.append({"role": "assistant", "content": model_answer})
    
    
    if len(chat_history) > 6: # Limit chat history size
        chat_history = chat_history[-6:]
        
    context = 'Conversation history:\n'
    context += "\n".join([f"{msg['role']}: \"{msg['content']}\"" for msg in chat_history])
        
    return context


my_retriever = get_retriever(file_path, embed_model_name)
READER_LLM, my_tokenizer = load_reader_tokenizer_model(llm_model_name, token)
chat_history = []
temp_user_q = None

@cl.on_chat_start
async def main():
    
    starting_string = "Hi, how can I help You?"
    generate_history(chat_history = chat_history, model_answer = starting_string)
    
    await cl.Message(content = starting_string).send()

@cl.on_message
async def main(message: cl.Message):
    global temp_user_q
    user_answer = message.content
    convo_history = generate_history(chat_history = chat_history, prompt=user_answer)
    
    if temp_user_q != None: 
        user_answer = temp_user_q + ' ' + user_answer
        temp_user_q = None
            
        fp = get_final_prompt(user_answer, my_retriever, my_tokenizer, convo_history)
        model_answer = READER_LLM(fp)[0]['generated_text']
        answer = model_answer
    else:
                
        if is_connectivity_issue(user_answer) == True:            
                
            # instruction = "Solve the connectivity issue with the country and device provided."
            # if not has_country(user_answer) and not is_device(user_answer):
            #     instruction = "Don't answer the question right away. Ask the user to specify the country and th edevice. if this sentence is in the chat history, solve the problem using all the information availiable."
            # elif not has_country(user_answer):
            #     instruction = "Don't answer the question right away. Ask the user to specify the country. if this sentence is in the chat history, solve the problem using all the information availiable."
            # elif not is_device(user_answer):
            #     instruction = "Don't answer the question right away. Ask the user to specify the device. if this sentence is in the chat history, solve the problem using all the information availiable."
            
            if not has_country(user_answer) and not is_device(user_answer) and not is_OS(user_answer):
                answer = "Please provide information of Your country, device and operating system."
                temp_user_q = user_answer
            elif not has_country(user_answer):
                answer = "Please provide the country."
                temp_user_q = user_answer
            elif not is_device(user_answer) and not is_OS(user_answer):
                answer = "Please provide the device type and operating system."
                temp_user_q = user_answer
                
        else: 
            fp = get_final_prompt(user_answer, my_retriever, my_tokenizer, convo_history)
            model_answer = READER_LLM(fp)[0]['generated_text']
            answer = model_answer
    
    generate_history(chat_history = chat_history, model_answer=answer)

    await cl.Message(content=answer).send()