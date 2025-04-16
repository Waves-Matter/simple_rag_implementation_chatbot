from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma

def get_retriever(file_path, embed_model_name):

    loader = JSONLoader(file_path=file_path, jq_schema='.[]', text_content=False) #Load the JSON file

    docs = loader.load() #We do not split this, as the doc variable is already a list, loaded from JSON
    
    embeddings = HuggingFaceEmbeddings(model_name=embed_model_name)

    vectorstore = Chroma.from_documents(documents=docs, 
                                        embedding=embeddings) #we vectorise the document

    retriever = vectorstore.as_retriever()
    return retriever
