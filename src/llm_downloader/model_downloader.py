import os

MODEL_FILE_PATH = os.getenv("MODEL_FILE_PATH") #"../models/"
MODEL_NAME = os.getenv("MODEL_NAME") #"Llama-3.2-3B-Instruct-Q4_K_M.gguf"
REPO_NAME = os.getenv("REPO_NAME") #"unsloth/Llama-3.2-3B-Instruct-GGUF"

if os.path.exists(MODEL_FILE_PATH+REPO_NAME) and any(fname.endswith(".gguf") for fname in os.listdir(MODEL_FILE_PATH+REPO_NAME)):
    print("Model already exists, skipping the download.")
else:
    print(f"Downloading {MODEL_NAME} from {REPO_NAME}...")
    os.makedirs(MODEL_FILE_PATH+REPO_NAME)
    cmd = f"huggingface-cli download {REPO_NAME} {MODEL_NAME} --local-dir {MODEL_FILE_PATH+REPO_NAME}"
    os.system(cmd)
    print(f"Downloaded model in {MODEL_FILE_PATH+REPO_NAME}")