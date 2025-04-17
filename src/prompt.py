import json


def get_body_content(document):
  
    string_text = document.page_content
    dat = json.loads(string_text)
    body_content = dat.get('body')
    body_title = dat.get('title')
    body_url = dat.get('url')
    
    return body_content, body_title, body_url

def get_context(prompt, retriever):
    context_docs = retriever.get_relevant_documents(prompt)
    
    context = "\nExtracted documents:\n"
    context = "\n".join([
    f"Document {i + 1}:\nTitle: {get_body_content(doc)[0]}\n{get_body_content(doc)[1]}\nUrl: {get_body_content(doc)[2]}"
    for i, doc in enumerate(context_docs)
    ])
    
    return context

def get_final_prompt(prompt, retriever, tokenizer):
    prompt_in_chat_format = [
    {
        "role": "system",
        "content": """Using the information contained in the context, give a comprehensive answer to the question.
        Respond only to the question asked, response should be concise and relevant to the question.
        Provide the number of the source document when relevant.
        If the answer cannot be deduced from the context, do not give an answer.""",
    },
    {
        "role": "user",
        "content": """Context:
        {context}
    ---
    Now here is the question you need to answer.

    Question: {question}""",
    },
]
    
    RAG_PROMPT_TEMPLATE = tokenizer.apply_chat_template(
        prompt_in_chat_format, tokenize=False, add_generation_prompt=True
    )
    
    context = get_context(prompt, retriever)
    
    final_prompt = RAG_PROMPT_TEMPLATE.format(question=prompt, context=context)

    return final_prompt

    