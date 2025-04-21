import torch._dynamo
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import Chroma


def load_retriever(file_path, embed_model_name):

    loader = JSONLoader(file_path=file_path, jq_schema='.[]', text_content=False) # Load the JSON file.
    docs = loader.load() # I do not split this any further, as the docs variable is already a list, loaded from JSON, and each item is not a big document.

    embeddings = HuggingFaceEmbeddings(model_name=embed_model_name)
    vectorstore = Chroma.from_documents(documents=docs, 
                                        embedding=embeddings)
    # Vectorise the documents and store them in a vector database for further retrieval.
    
    retriever = vectorstore.as_retriever()

    return retriever


def load_reader_tokenizer_model(model_path, api_token): #Function that loads the reader and tokenizer models. 
    torch._dynamo.config.suppress_errors = True

    bnb_config = BitsAndBytesConfig( # Needed for model quantization.
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16, # Helps saving memory.
        device_map="auto",
    )
    
    my_tokenizer = AutoTokenizer.from_pretrained(model_path)
    my_model =AutoModelForCausalLM .from_pretrained(model_path, quantization_config=bnb_config, token = api_token)
    
    READER_LLM = pipeline(
    model=my_model,
    tokenizer=my_tokenizer,
    task="text-generation",
    do_sample=True,
    temperature=0.1, # In this case there is no need for the model to be creative.
    return_full_text=False,
    max_new_tokens=1024,
    )
    
    return READER_LLM, my_tokenizer

def get_tokenizer(model_path): #Function that loads the tokenizer.
    torch._dynamo.config.suppress_errors = True
    my_tokenizer = AutoTokenizer.from_pretrained(model_path)
    return my_tokenizer

def get_llm(model_path, api_token): #Function that loads the reader model. 
    torch._dynamo.config.suppress_errors = True

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_use_double_quant=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
    )

    llm = AutoModelForCausalLM .from_pretrained(model_path, quantization_config=bnb_config, token = api_token)
    
    return llm