import os
import requests

# Create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# Model download links
models = {
    "cnn_model.h5": "https://drive.google.com/uc?export=download&id=1x-jUduEkdC5g2qPw7Hl3Sy5cERxzdjOq",
    "resnet_model.h5": "https://drive.google.com/uc?export=download&id=1XTBXVmuspWfBgOTLNef2yLEPPMLPucGc",
    "vgg_model.h5": "https://drive.google.com/uc?export=download&id=1bfbLMhIvHN6CsMrOLTZFv1ffc_5LahcW",
    "rf_model.joblib": "https://drive.google.com/uc?export=download&id=1VmJ2ZCUUQu6wrNbCRPLhhmPM8eNN01i9"
}

for name, url in models.items():
    print(f"Downloading {name}...")
    response = requests.get(url)
    with open(f"models/{name}", "wb") as f:
        f.write(response.content)
print("✅ All models downloaded!")
