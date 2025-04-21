from connectivity import is_connectivity_issue, has_country, is_device, is_OS
from history import history_connection, save_history
from prompt import get_final_prompt
from history import return_history, save_history
from prompt import get_final_prompt

def generate_model_answer(prompt, retriever, tokenizer, llm, chat_history):# Function for returning final model answer string.
    conversation_history = return_history(chat_history) # Get recent conversation history in string format. 
    fp = get_final_prompt(prompt, retriever, tokenizer, llm, conversation_history) # Generate final prompt that will be fed into the reader llm.
    model_answer = llm(fp)[0]['generated_text'] # Get the model answer in a string format.
    save_history(chat_history = chat_history, model_answer=model_answer)
    return model_answer

def generate_model_answer_test(prompt, retriever, tokenizer, llm, chat_history):
    # Only used for testing.
    conversation_history = return_history(chat_history) 
    fp = get_final_prompt(prompt, retriever, tokenizer, llm, conversation_history)
    model_answer = llm(fp)[0]['generated_text']
    save_history(chat_history = chat_history, model_answer=model_answer)
    return fp, model_answer # Returns final prompt, which was fed into the model together with the model answer. 

def get_model_answer(prompt, chat_history, retriever, tokenizer, llm):
            
    try:
        if history_connection(chat_history) != False: # Check if previous question was related to connectivity issues.
            last_prompt = chat_history[-3]['content'] # Get previous user prompt from the history.
            prompt = last_prompt + ' ' + prompt # Join the previous and the new user prompts.
            # Its done because the new user prompt likely refers only to the country and/ or device without specifying the problem/ qestion itself again. 
            # This prompt has the information about the question and the clarifying information about the device and location.
            # Assumption: model will not care about the format of the prompt while searching for similar documents in the vector space.
            # Assumption: model will not care if the second half of the prompt has something along the lines of "i dont know".
                
            answer = generate_model_answer(prompt, retriever, tokenizer, llm, chat_history)
        else:      
                        
            if is_connectivity_issue(prompt) == True: # Checks if user is dealing with a connectivity issue.
                
                if not has_country(prompt) and not is_device(prompt) and not is_OS(prompt): # Checks if user mentioned their country/device/OS in the initial prompt.
                    # Meant to avoid asking for the information that was already provided.
                    answer = "Please provide information of Your country, device and operating system."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                elif not has_country(prompt):
                    answer = "Please provide the country."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                elif not is_device(prompt) and not is_OS(prompt):
                    answer = "Please provide the device type and operating system."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                else:
                    answer = generate_model_answer(prompt, retriever, tokenizer, llm, chat_history)            
            else: 
                answer = generate_model_answer(prompt, retriever, tokenizer, llm, chat_history)
    except Exception as e:
        answer = "Sorry, model couldnt provide the answer dur to this error: "+ e +", try again."

    return answer

def get_model_answer_test(prompt, chat_history, retriever, tokenizer, llm):#The function returns final prompt together with the answer.
    #Only used for testing.
    
    fp = 'No final Prompt'
    try:
        if history_connection(chat_history) != False: 
            last_prompt = chat_history[-3]['content']
            prompt = last_prompt + ' ' + prompt
            
            fp, answer = generate_model_answer_test(prompt, retriever, tokenizer, llm, chat_history)
        else:      
                    
            if is_connectivity_issue(prompt) == True:  
            
                if not has_country(prompt) and not is_device(prompt) and not is_OS(prompt):
                    answer = "Please provide information of Your country, device and operating system."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                elif not has_country(prompt):
                    answer = "Please provide the country."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                elif not is_device(prompt) and not is_OS(prompt):
                    answer = "Please provide the device type and operating system."
                    save_history(chat_history = chat_history, model_answer=answer, more_info_needed = True)
                else:
                    fp, answer = generate_model_answer_test(prompt, retriever, tokenizer, llm, chat_history)
                
            else: 
                fp, answer = generate_model_answer_test(prompt, retriever, tokenizer, llm, chat_history)
    except Exception as e:
        answer = "Sorry, model couldnt provide the answer dur to this error: "+ e +", try again."

    return fp, answer # returns final prompt, which was fed into the model together with the model answer. 
