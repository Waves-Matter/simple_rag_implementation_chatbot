### Project for a customer service chatbot

This is my (Ugnė) submission for ***AI Developer Homework Assignment***. :) <br />
Ths **chatbot** is able to take user's query and provide relevant answer using **RAG**. 
It takes recent chat history with the user into account and is able to answer follow-up questions.

## Build with

I used _Hugging Face_ for accessing LLM and embedding model. <br />
For generating the text I _[Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)_ LLM was used. 
I chose this model because it is relatively lightweight (has 1.5B parameters), thus doesn't take too much time to download. 
It is also finetuned on instruction following and has Long-context Support which is important for implementing RAG.
This model generates relatively reasonable answer, takes context into account and does that in a relatively short time (up to 10s)
(compared to the other models that I have tried, such as _BitNet b1.58 2B4T_ - would take up to 1 min to generate the answer, or _SmolLM2_ which would often output unreasonable answers )

For embedding I used _[small General Text Embeddings (GTE)](https://huggingface.co/thenlper/gte-small)_ model.
This model is suitable for text embedding tasks, such as  information retrieval or semantic textual similarity.

Vectorised documents were stored in _[Chroma](https://www.trychroma.com/)_ database.
It was chosen due to it being open source and its easy integration via _langchain_community_. 
(As well as it was one of the recommended databases mentioned in the task)

For user interface an open-source Python package _[Chainlit](https://docs.chainlit.io/get-started/overview)_ was used.
It is easily implementable and has a relatively pleasant UI.
(It was also included in the task recommendations)

## Running the Application

For easy instalation You can clone the repository. This can be done by:
```
git clone https://github.com/Waves-Matter/ChatBot.git
```

For easier management of dependencies it is recommended to create a virtual environment. 
I personally used Conda. 
```
conda create --name <my-env>
```

Install required libraries.
```
pip install -r requirements.txt
```

_BitsAndBytesConfig_ library needs cuda support, make sure to set it up.
```
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
```

For _PyTorch_ gpu support, make sure to follow installation instructions on [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)

Don't forget to insert Your own _HuggingFace_ API key in the 'text.txt' file :)

Finally, run to start the ✨Chatbot✨ 
```
chainlit run run_chainlit.py -w     
```
I personally used Python 3.9.21 for this project.

## Project structure

- `answer.py` Logic behind generating model's answer and checking for connectivity issues. 
- `connectivity.py` Methods used for the connectivity check.
- `context.py` Methods for retrieving relevant documents from user prompt. Implementation of Multi Query RAG.
- `history.py` Methods for maintaining short-term conversation history. History size is limited to avoid irrelevant information.
- `model_loader.py` Loads LLM and embedding model. Stores vectorised documents in the vector database.
- `prompt.py` Generating instructions and promps for the model.
- `run_chainlit.py` Final application that runs the **Chatbot** and its UI.
- `tester.ipynb` Jupyter notebook file for testing different cases of user prompts.
- `text.py` Holds the API token and model paths which are needed for the model retrieval from _Hugging Face_. 

Further explanation is provided in the comments of the code itself. :)

## Limitations of the Chatbot

- Doesn't have multi-language support;
- Sometimes references context documents which cannot be seen to the user;
- Will answer to random questions (such as what is the best dog breed) which are not related to context document and customer support role;
- Sometimes would advice the user to contact company's customer support, even though it itself is the customer support.

## Credentials
Ugnė Šilingaitė
[https://www.linkedin.com/in/ugnė-šilingaitė0616](https://www.linkedin.com/in/ugn%C4%97-%C5%A1ilingait%C4%970616/)
ugnsili@gmail.com






