from llama_cpp import Llama
from llama_cpp.llama_speculative import LlamaPromptLookupDecoding
from fastapi import FastAPI
from pydantic import BaseModel
import os

MODEL_FILE_PATH = os.getenv("MODEL_FILE_PATH") #"/models/"
MODEL_NAME = os.getenv("MODEL_NAME") #"Llama-3.2-3B-Instruct-Q4_K_M.gguf"
REPO_NAME = os.getenv("REPO_NAME") #"unsloth/Llama-3.2-3B-Instruct-GGUF"

llm = Llama(
	model_path = MODEL_FILE_PATH+REPO_NAME+"/"+MODEL_NAME,
	flash_attn = True,
 	draft_model=LlamaPromptLookupDecoding(num_pred_tokens=3),
    n_ctx = 8192,
    n_batch = 8192,
    n_ubatch = 8192
)

app = FastAPI()

@app.get('/')
def root():
    return "Hello_world!"

class RequestItem(BaseModel):
    system:str
    user:str
@app.post('/complete/')

def return_response(requestItem:RequestItem):
    result = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": requestItem.system},
            {"role": "user", "content": requestItem.user}
        ]
        
    )
    return {"result": result["choices"][0]["message"]["content"],"usage":result["usage"]}
