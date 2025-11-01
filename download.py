import gdown
import os

# Dataset
file_id = "1njSYctE9iF8ZHFvHur9aatFARZ6qc6oe"
folder = "input"
output = os.path.join(folder, "data.zip")

os.makedirs(folder, exist_ok=True)

url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, output, quiet=False)

# Model
file_id = "1hSOw9K9eZcFkeISOIO7wj7l3gcY1zi6v"
folder = os.path.join("output", "model")
output = os.path.join(folder, "checkpoints.zip")

os.makedirs(folder, exist_ok=True)

url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, output, quiet=False)
