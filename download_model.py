from huggingface_hub import hf_hub_download

# Replace with the correct repo_id and filename if different
model_path = hf_hub_download(
    repo_id="TheBloke/llama-2-7b-chat-ggml",  # Replace with the actual model repository
    filename="llama-2-7b-chat.ggmlv3.q8_0.bin",
    use_auth_token=True
)

print(f"Model downloaded to: {model_path}")
