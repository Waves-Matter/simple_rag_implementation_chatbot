import json

#Function needed to determine if user prompt suggests an issue related with connectivity.
def is_connectivity_issue(prompt):
    keywords = ['disconnect', 'can\'t connect', 'connection lost', 'network issue', 'connectivity', 'connect', 'connection']
    #The assumption is made that users will use cartain dictionary to decribe the problem
    #If these keywords are used, there is a high chance that user has a connectivity issue.
    #The keywords might be altered.
    
    return any((keyword in prompt.lower() for keyword in keywords))

def is_device(prompt):#Function checks if the user specified their device in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    keywords = ['phone', 'android', 'iphone', 'computer', 'laptop', 'kindle', 'nintendo', 'switch', 'playstation', 'xbox', 'rasberry', 'chromebook', 'tv']
    #In this function only the most popular itemsare listed thus it does not cover all of the possible cases. 
    
    return any((keyword in prompt.lower() for keyword in keywords))

def has_country(prompt):#Function checks if the user specified their location in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    countries = [
    "Afghanistan", "Albania", "Algeria", "Andorra", "Angola", 
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", 
    "Austria", "Azerbaijan", "The Bahamas", "Bahrain", "Bangladesh", 
    "Barbados", "Belarus", "Belgium", "Belize", "Benin", 
    "Bhutan", "Bolivia", "Bosnia and Herzegovina", "Botswana", 
    "Brazil", "Brunei", "Bulgaria", "Burkina Faso", "Burundi", 
    "Cabo Verde", "Cambodia", "Cameroon", "Canada", 
    "Central African Republic", "Chad", "Chile", "China", 
    "Colombia", "Comoros", "Congo, Democratic Republic of the", 
    "Congo, Republic of the", "Costa Rica", 
    "Croatia", "Cuba", "Cyprus", "Czech", "Denmark", 
    "Djibouti", "Dominica", "Dominican Republic", 
    "Timor", "Ecuador", "Egypt", 
    "Salvador", "Eritrea", "Estonia", 
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", 
    "Gabon", "The Gambia", "Georgia", "Germany", "Ghana", 
    "Greece", "Grenada", "Guatemala", "Guinea", 
    "Guyana", "Haiti", "Honduras", "Hungary", "Iceland", 
    "India", "Indonesia", "Iran", "Iraq", "Ireland", 
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", 
    "Kazakhstan", "Kenya", "Kiribati", "Korea, North", 
    "Korea, South", "Kosovo", "Kuwait", "Kyrgyzstan", 
    "Laos", "Latvia", "Lebanon", "Lesotho", "Liberia", 
    "Libya", "Liechtenstein", "Lithuania", "Luxembourg", 
    "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", 
    "Malta", "Marshall", "Mauritania", "Mauritius", 
    "Mexico", "Micronesia, Federated States of", "Moldova", 
    "Monaco", "Mongolia", "Montenegro", "Morocco", 
    "Mozambique", "Myanmar", "Burma", "Namibia", "Nauru", 
    "Nepal", "Netherlands", "New Zealand", "Nicaragua", 
    "Niger", "Nigeria", "North Macedonia", "Norway", "Oman", 
    "Pakistan", "Palau", "Panama", "Papua New Guinea", 
    "Paraguay", "Peru", "Philippines", "Poland", "Portugal", 
    "Qatar", "Romania", "Russia", "Rwanda", 
    "Saint Kitts and Nevis", "Saint Lucia", 
    "Saint Vincent and the Grenadines", "Samoa", "San Marino", 
    "Sao Tome and Principe", "Saudi Arabia", "Senegal", 
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", 
    "Slovakia", "Slovenia", "Solomon Islands", "Somalia", 
    "South Africa", "Spain", "Sri Lanka", "Sudan", 
    "Sudan, South", "Suriname", "Sweden", "Switzerland", 
    "Syria", "Taiwan", "Tajikistan", "Tanzania", 
    "Thailand", "Togo", "Tonga", "Trinidad and Tobago", 
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", 
    "Uganda", "Ukraine", "United Arab Emirates", 
    "United Kingdom", "United States", "Uruguay", "England",
    "Uzbekistan", "Vanuatu", "Vatican", "Venezuela", 
    "Vietnam", "Yemen", "Zambia", "Zimbabwe"
    ]
    #This function only checks for the country, thus if the user provides a city it will not work.

    return any((keyword.lower() in prompt.lower() for keyword in countries))

def is_OS(prompt):#Function checks if the user specified their OS in the initial prompt to avoid the chatbot asking for the information the user already provided. 
    keywords = [' Microsoft', 'Windows', 'Mac', 'Android', 'Linux', 'Ubuntu', 'Fedora']
    #In this function only the most popular OS are listed thus it does not cover all of the possible cases. 
    
    return any((keyword in prompt.lower() for keyword in keywords))

def get_body_content(document): #Function is meant extract the content of the document from the retriever and return it in string form.
  
    string_text = document.page_content
    dat = json.loads(string_text)
    body_content = dat.get('body')
    body_title = dat.get('title')
    body_url = dat.get('url')
    
    return body_content, body_title, body_url

def get_context(prompt, retriever): #Function is meant to format the document content.
    context_docs = retriever.get_relevant_documents(prompt)
    
    context = "\nExtracted documents:\n"
    context = "\n".join([
    f"Document {i + 1}:\nTitle: {get_body_content(doc)[0]}\n{get_body_content(doc)[1]}\nUrl: {get_body_content(doc)[2]}"
    for i, doc in enumerate(context_docs)
    ])
    
    return context

def get_final_prompt(prompt, retriever, tokenizer, history = None, specify_question = None): #Function returns the final prompt which is given to the model.
    #prompt - original user input.
    #history - history of the previous conversation.
    #specify_question - case specific instruction that is given to the model //not used in this project.
    
    prompt_in_chat_format = [
    {
        "role": "system",
        "content": """Using the information contained in the context, give a comprehensive answer to the question.
        Respond only to the question asked, response should be concise and relevant to the question.
        Provide url of the source document when relevant.
        Take the chat history into account when creating the response.
        Execute case specific instructions if they are present.
        If the answer cannot be deduced from the context, do not give an answer and ask for another question.""",
    },
    {
        "role": "user",
        "content": """Context: 
        {context}
         ---
        You need to provide answer to this user prompt:
        {question}""",
    },
]
    
    RAG_PROMPT_TEMPLATE = tokenizer.apply_chat_template(
        prompt_in_chat_format, tokenize=False, add_generation_prompt=True
    )
    
    context = get_context(prompt, retriever)
    
    if history != None:
        context =  history +"\n"+ "Useful information: \n" + context
        
    if specify_question != None:
        prompt = prompt + "\n Case specific instruction:" + specify_question
    
    final_prompt = RAG_PROMPT_TEMPLATE.format(question=prompt, context=context)

    return final_prompt


    