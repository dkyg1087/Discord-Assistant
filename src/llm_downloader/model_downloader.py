import os

MODEL_FILE_PATH = os.getenv("MODEL_FILE_PATH") #"../models/"
MODEL_NAME = os.getenv("MODEL_NAME") #"Llama-3.2-3B-Instruct-Q4_K_M.gguf"
REPO_NAME = os.getenv("REPO_NAME") #"unsloth/Llama-3.2-3B-Instruct-GGUF"

print(f"MODEL_FILE_PATH: {MODEL_FILE_PATH}")
print(f"MODEL_NAME: {MODEL_NAME}")
print(f"REPO_NAME: {REPO_NAME}")

if os.path.exists(MODEL_FILE_PATH+REPO_NAME) and any(fname.endswith(".gguf") for fname in os.listdir(MODEL_FILE_PATH+REPO_NAME)):
    print("Model already exists, skipping the download.")
else:
    print(f"Downloading {MODEL_NAME} from {REPO_NAME}...")
    os.makedirs(MODEL_FILE_PATH+REPO_NAME)
    if not os.path.exists(MODEL_FILE_PATH+REPO_NAME):
        print(f"Failed to create directory: {MODEL_FILE_PATH+REPO_NAME}")
        exit(1)
    else:
        print(f"Directory created: {MODEL_FILE_PATH+REPO_NAME}")
    cmd = f"huggingface-cli download {REPO_NAME} {MODEL_NAME} --local-dir {MODEL_FILE_PATH+REPO_NAME}"
    print(f"Running command: {cmd}")
    os.system(cmd)
    if os.path.exists(MODEL_FILE_PATH+REPO_NAME) and any(fname.endswith(".gguf") for fname in os.listdir(MODEL_FILE_PATH+REPO_NAME)):
        print(f"Downloaded model in {MODEL_FILE_PATH+REPO_NAME}")
    else:
        print(f"Failed to download model from {REPO_NAME}")