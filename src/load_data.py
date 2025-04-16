
import os

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

file_path = "docs\hc_articles.json"

loader = JSONLoader(file_path=file_path, jq_schema='.[]', text_content=False)
docs = loader.load()

model_name = "all-MiniLM-L6-v2"
embeddings = HuggingFaceEmbeddings(model_name=model_name)

vectorstore = Chroma.from_documents(documents=docs, 
                                    embedding=embeddings)

retriever = vectorstore.as_retriever()


query = "how do i install nodVPN?"

# Perform a similarity search
results = vectorstore.similarity_search(query, )

for result in results:
    print(result.page_content)
    print("--------------")