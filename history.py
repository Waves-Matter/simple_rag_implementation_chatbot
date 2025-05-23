def save_history(chat_history, prompt = None, model_answer = None, more_info_needed = False): #Function for saving the chat history.
    
    if prompt!=None: # Checking if a prompt is given. 
        chat_history.append({"role": "user", "content": prompt, "more_info_needed": more_info_needed})
        
    if model_answer!=None: # Checking if a model_answer is given. 
        chat_history.append({"role": "assistant", "content": model_answer, "more_info_needed": more_info_needed})
    
    
    if len(chat_history) > 6: # Limit chat history size.
        chat_history.pop(0)
        

def return_history(chat_history):# Function for formating the chat history and returning it in a string format. 
    context = 'Conversation history:\n'
    context += "\n".join([f"{msg['role']}: \"{msg['content']}\"" for msg in chat_history])
        
    return context

def clear_history(chat_history): # Function for deleting the chat history.
    chat_history = []
    return chat_history

def history_connection(chat_history): # Function needed for checking if previous question was related to connectivity issue. Needed in the answer process.
    return chat_history[-2]['more_info_needed']

# In a more complicated case a better decision would be to code this as an object.