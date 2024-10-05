# Detect-Melonoma-Cancer

How to Run locally? Please ensure that the following is being carried on in a new conda environment
```
git clone https://github.com/EternalBlissard/Detect-Melonoma-Cancer/
cd Detect-Melonoma-Cancer
cd Hugging-Face-Files
wget https://huggingface.co/spaces/eternalBlissard/DetectMelanomaCancer/resolve/main/ViTModel.pt?download=true
pip install -r requirements.txt
python3 app.py

```
## Inspiration
Every year, millions face the daunting diagnosis of melanoma, a life-threatening form of skin cancer that thrives on delayed detection. The emotional and physical toll on patients and their families is immeasurable, often compounded by the challenges of accessing timely and accurate screening. Inspired by the resilience of survivors and driven by the urgent need to save lives, our project harnesses cutting-edge artificial intelligence to revolutionize early detection. By making advanced, user-friendly skin cancer screening accessible to everyone, we aim to empower individuals with the knowledge to take proactive steps in their health journey. Our mission is not just to innovate but to create a future where melanoma is caught in its earliest, most treatable stages, significantly reducing mortality and bringing hope to countless lives worldwide. Together, we can transform the landscape of cancer care, turning the tide against melanoma through technology, compassion, and unwavering commitment.
## What it does
Its an advanced Computer Vision Based AI that inputs a zoomed in image of the human skin and then classifies it as 'benign' or 'malignant' in terms of Melonoma Cancer.
## How we built it
We built it by closely studying the concepts of Machine Learning, Deep Learning and Computer Vision. At first, we made our own architecture to do Computer Vision but as the accuracy was low. We apllied the concept of Transfer Learning on a Vision Transformer.<br><br>

The vision Transformer has been trained on a [kaggle dataset](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset) which has about 14k images all of which were used to train/test the model.
## Challenges we ran into
Limited GPU Availability<br>
Setting up gradio interface<br>
## Accomplishments that we're proud of
An accuracy of about 88% in training-test-validation showing there is no overfitting but definitely scope for development, which might happen if we just let the model train for a day.<br>
A deployed model free to use for all.<br>
Steps to replicate the entire procedure on local machines :)

## What we learned
A lot about cancer and Fine Tuning. Apparently, there are related concepts like Meta Learning and Multi Task Learning using the scope can be increased to multiple cancers
## What's next for Detect Melonoma Cancer
TO have an higher accuracy and more variety in this fight against cancer
