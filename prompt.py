from context import get_simple_context, get_Multi_Query_context

def get_final_prompt(prompt, retriever, tokenizer, llm = None, history = None, specify_question = None): # Function returns the final prompt which is given to the model.
    # prompt - original user input.
    # history - history of the previous conversation.
    # specify_question - case specific instruction that is given to the model //not used in this project.
    
    prompt_in_chat_format = [ # Prompt is constructed in a way to give model instructions on how to construct the answer. 
    # In this case the model is instructed to answer the question based on the context.
    
    {
        "role": "system",
        "content": """You are a customer support agent. Using the information contained in the context, give a comprehensive answer to the question. 
Respond only to the question asked, response should be concise and relevant to the question. 
Provide full rephrased context of the relevant documents in Your answer if needed. 
Take the chat history into account when creating the response. Execute case specific instructions if they are present. 
If the answer is not related to the context or cannot be deduced from the context, do not give an answer and ask for another question.""",
    },
    {
        "role": "user",
        "content": """Context: 
        {context}
         ---
        You need to provide an answer to this user prompt:
        {question}""",
    },
]
    
    RAG_PROMPT_TEMPLATE = tokenizer.apply_chat_template( # Template specifies how to convert conversations into a single tokenizable string in the expected model format.
        prompt_in_chat_format, tokenize=False, add_generation_prompt=True
    )
    
    try: 
        context = get_Multi_Query_context(prompt, retriever, tokenizer, llm) # Gets context based on the prompt and additional model generated questions which are relevant to the original prompt.
    except Exception as e:
        context = get_simple_context(prompt, retriever) # Gets context based on the prompt.
    
    if history != None: # Checks if the chat history is available.
        context =  history +"\n"+ "Useful information: \n" + context # Adds chat history to the context.
        
    if specify_question != None: # Checks for case specific instructions.
        prompt = prompt + "\n Case specific instruction:" + specify_question # Adds case specific instructions.
    
    final_prompt = RAG_PROMPT_TEMPLATE.format(question=prompt, context=context)

    return final_prompt # Returns the final prompt which will be given to the llm.

    