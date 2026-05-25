import sys
import json

data = json.load(sys.stdin)
file_path = data.get('tool_input', {}).get('file_path', '')

bad_exts = (
    '.png', '.jpg', '.jpeg', '.webp', '.gif',
    '.mp4', '.mov', '.avi', '.webm',
    '.safetensors', '.ckpt', '.pt', '.pth', '.bin', '.onnx'
)

if file_path.endswith(bad_exts):
    print(f"Blocked: '{file_path}' belongs on Google Drive, not the repo.")
    print("Upload to: Generated Images/ or Models/ in the shared Drive folder.")
    sys.exit(1)
