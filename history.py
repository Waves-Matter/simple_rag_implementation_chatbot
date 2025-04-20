def save_history(chat_history, prompt = None, model_answer = None, is_connection = False): #Function for saving the chat history.
    
    if prompt!=None:
        chat_history.append({"role": "user", "content": prompt, "is_connection": is_connection})
        
    if model_answer!=None:
        chat_history.append({"role": "assistant", "content": model_answer, "is_connection": is_connection})
    
    
    if len(chat_history) > 6: # Limit chat history size.
        chat_history = chat_history[-6:]
        

def return_history(chat_history):#function for formating the chat history and returning it in a string format. 
    context = 'Conversation history:\n'
    context += "\n".join([f"{msg['role']}: \"{msg['content']}\"" for msg in chat_history])
        
    return context

def clear_history(chat_history):
    chat_history = []
    return chat_history

def history_connection(chat_history):
    return chat_history[-2]['is_connection']