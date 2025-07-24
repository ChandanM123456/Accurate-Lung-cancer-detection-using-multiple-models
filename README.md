# Accurate-Lung-cancer-detection-using-multiple-models
A deep learning model for lung cancer detection using CNN, Transfer learning, Resnet, Random forest .  .
# 🩺 Accurate Lung Cancer Detection Using Multiple Models

This project implements a deep learning pipeline for the accurate classification of lung cancer from medical imaging data. It compares and evaluates multiple models including CNN and transfer learning architectures such as VGG16 and ResNet50, along with a traditional machine learning classifier — Random Forest.  

---

## 📖 About the Project

Lung cancer is one of the leading causes of death globally. Early detection using medical imaging (such as CT scans or X-rays) can significantly improve survival rates. This project aims to automate the classification of lung cancer into:

- ✅ Malignant cases
- ✅ Benign cases
- ✅ Normal (healthy) cases

Using deep learning and machine learning techniques, this tool performs image preprocessing, model training, prediction, and evaluation on a custom dataset.

---

## 🧠 Models Used

The following four models are implemented and compared:

1. **Custom CNN**
   - Built from scratch using Keras.
   - Used as a baseline for performance comparison.

2. **VGG16 (Transfer Learning)**
   - Pre-trained on ImageNet.
   - Fine-tuned on the lung cancer dataset.

3. **ResNet50 (Transfer Learning)**
   - Deep residual learning framework.
   - Adapted for 3-class image classification.

4. **Random Forest Classifier**
   - Traditional machine learning model.
   - Trained on features extracted from images.

Each model's performance is evaluated using accuracy scores and visualized using confusion matrices and loss/accuracy plots.

---
