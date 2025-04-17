import os

from retriever import get_retriever

file_path = "docs\hc_articles.json"
embed_model_name = "thenlper/gte-small" 
#other possible models:: "all-MiniLM-L6-v2"; "thenlper/gte-large"

my_retriever = get_retriever(file_path, embed_model_name)

query = "how to install NORDVPN?"
results = my_retriever.get_relevant_documents(query)
for result in results:
    print(result)
    print("---------------------")

#llm_model_name = "HuggingFaceH4/zephyr-7b-beta"

