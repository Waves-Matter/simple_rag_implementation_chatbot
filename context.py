import json
import re

def get_body_content(document): #Function is meant extract the content of the document from the retriever and return it in string form.
  
    string_text = document.page_content # Turn the document into a string
    dat = json.loads(string_text) # Turn it back to json because it's easier to extract the data this way as it is easily structured.
    # In this case we know that the original file that contained out documents is indeed in json file format.
    
    body_content = dat.get('body')
    body_title = dat.get('title')
    body_url = dat.get('url')
    
    return body_content, body_title, body_url # Return important parts.

def get_simple_context(prompt, retriever): #Function is meant to retrieve documents related to the prompt and format the document content.
    context_docs = retriever.get_relevant_documents(prompt) # Get documents relevant to the prompt.
    
    context = "\nExtracted documents:\n"
    context = "\n".join([
    f"Document {i + 1}:\nTitle: {get_body_content(doc)[1]}\n{get_body_content(doc)[0]}\nUrl: {get_body_content(doc)[2]}"
    for i, doc in enumerate(context_docs)
    ]) # Putting all the information into a nice string.
    
    return context

def get_context_from_retreiever(prompt, retriever): #Function is meant to retrieve documents related to the prompt and format the document content.
    context_docs = retriever.get_relevant_documents(prompt)
    
    context_set = {# Create a set to hold the formatted document strings
        f"Title: {get_body_content(doc)[1]}\n{get_body_content(doc)[0]}\nUrl: {get_body_content(doc)[2]}"
        for doc in context_docs
    }
    return context_set

def get_union(list_of_sets): # Returns all the unique items from the list of sets.
    return set.union(*list_of_sets)

def get_Multi_Query_context(prompt, retriever, tokenizer, llm): # Function meant to execute Multi Query RAG 
    
    questions_prompt = get_additional_questions(prompt, tokenizer, llm) # Generate the additional questions related to the original prompt.
    questions_prompt.append(prompt) # Adding original prompt to the list, so the retriever would return all the possible information related to the original prompt.
    # Generated questions might not capture all the nuances of the original prompt. 
    
    list_of_document_lists  = []
    
    for ques in questions_prompt: # loop through all the model generated questions and the original prompt.
        context_docs = get_context_from_retreiever(ques, retriever) # Get relevant documents for each question.
        list_of_document_lists.append(context_docs)
        
    union_of_docs = get_union(list_of_document_lists) # Get the union of all the unique documents.
    
    doc_list = []
    i = 1
    for thing in union_of_docs: # Put all the documents in a formated string.
        formatted_string = f"Document no. {i}\n{thing}"
        doc_list.append(formatted_string)
        i+=1
    return "\n\n".join(doc_list) # Return a single string of context documents

def generate_prompt_questions_prompt(prompt, tokenizer): # Function returns the prompt which is given to the model to generate further questions about the prompt.
    
    prompt_in_chat_format = [ # Prompt is constructed in a way to give model instructions on how to construct the answer. 
    # In this case the model is instructed to generate questions that would enrich the original user prompt.
    {
        "role": "system",
        "content": """You are an AI language model assistant. Your task is to generate five 
different versions of the given user query to retrieve relevant documents from a vector 
database. By generating multiple perspectives on the user query, your goal is to help
the user overcome some of the limitations of the distance-based similarity search. 
Provide five alternative questions separated by newlines. Original query: {question}""",
    },
]
    
    RAG_PROMPT_TEMPLATE = tokenizer.apply_chat_template(
        prompt_in_chat_format, tokenize=False, add_generation_prompt=True
    )
    
    final_prompt = RAG_PROMPT_TEMPLATE.format(question=prompt)

    return final_prompt # Return the final prompt that is going to be given to a model. 

def get_additional_questions(prompt, tokenizer, llm): # Function returns a list of model generated questions.
    questions_prompt = generate_prompt_questions_prompt(prompt, tokenizer)
    model_answer = llm(questions_prompt)[0]['generated_text']  # Generating new questions related to the prompt.
    questions = model_answer.split('\n') # Splitting the model answer by new line.
    cleaned_questions = [re.sub(r'^\d+\.\s*', '', question) for question in questions] # Removing numbers and '.' from the start of each question.
    return cleaned_questions
