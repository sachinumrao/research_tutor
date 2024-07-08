from huggingface_hub import hf_hub_download


def donwload_model():
    REPO_ID = "TheBloke/Mistral-7B-Instruct-v0.2-GGUF"
    FILENAME = "mistral-7b-instruct-v0.2.Q4_K_S.gguf"

    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir="./models/")
    
if __name__ == "__main__":
    donwload_model()