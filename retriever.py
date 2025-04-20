from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma


def get_retriever(file_path, embed_model_name):

    loader = JSONLoader(file_path=file_path, jq_schema='.[]', text_content=False) #Load the JSON file.
    docs = loader.load() #I do not split this any further, as the docs variable is already a list, loaded from JSON, and each item is not a big document.

    embeddings = HuggingFaceEmbeddings(model_name=embed_model_name)
    vectorstore = Chroma.from_documents(documents=docs, 
                                        embedding=embeddings)
    # we vectorise the documents and store them in a vector database for further retrieval.
    
    retriever = vectorstore.as_retriever()

    return retriever