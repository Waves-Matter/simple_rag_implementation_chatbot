from prompt import get_final_prompt, is_connectivity_issue, has_country, is_device, is_OS
from history import history_connection, return_history, save_history

def get_final_answer(prompt, chat_history, retriever, tokenizer, llm):
    fp = 'No final Prompt'
    answer = "Sorry, model couldnt provide the answer, try again."
    conversation_history = return_history(chat_history)
    
    if history_connection(chat_history) != False: 
        last_prompt = chat_history[-3]['content']
        prompt = last_prompt + ' ' + prompt
            
        fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
        model_answer = llm(fp)[0]['generated_text']
        answer = model_answer
        save_history(chat_history = chat_history, model_answer=answer)
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
                fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
                model_answer = llm(fp)[0]['generated_text']
                answer = model_answer
                save_history(chat_history = chat_history, model_answer=answer)
            
        else: 
            fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
            model_answer = llm(fp)[0]['generated_text']
            answer = model_answer
            save_history(chat_history = chat_history, model_answer=answer)
            
    return answer

def get_final_answer_test(prompt, chat_history, retriever, tokenizer, llm):#The function returns final prompt together with the answer.
    #Only used for testing.
    fp = 'No final Prompt'
    answer = "Sorry, model couldnt provide the answer, try again."
    conversation_history = return_history(chat_history)
    
    if history_connection(chat_history) != False: 
        last_prompt = chat_history[-3]['content']
        prompt = last_prompt + ' ' + prompt
            
        fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
        model_answer = llm(fp)[0]['generated_text']
        answer = model_answer
        save_history(chat_history = chat_history, model_answer=answer)
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
                fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
                model_answer = llm(fp)[0]['generated_text']
                answer = model_answer
                save_history(chat_history = chat_history, model_answer=answer)
            
        else: 
            fp = get_final_prompt(prompt, retriever, tokenizer, conversation_history)
            model_answer = llm(fp)[0]['generated_text']
            answer = model_answer
            save_history(chat_history = chat_history, model_answer=answer)

    return fp, answer