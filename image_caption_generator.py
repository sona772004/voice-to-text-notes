import os
import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import InceptionV3
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications.inception_v3 import preprocess_input
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from tensorflow.keras.preprocessing.text import Tokenizer
from tqdm import tqdm
import matplotlib.pyplot as plt
import cv2
import nltk
from nltk.translate.bleu_score import corpus_bleu

class ImageCaptionGenerator:
    def __init__(self):
        self.image_model = None
        self.caption_model = None
        self.tokenizer = Tokenizer()
        self.max_length = 35
        self.vocab_size = 0
        
    def extract_features(self, img_path):
        """Extract features from image using InceptionV3"""
        img = tf.keras.preprocessing.image.load_img(img_path, target_size=(299, 299))
        x = tf.keras.preprocessing.image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x
    
    def encode_image(self, img_path):
        """Encode image using InceptionV3"""
        img = self.extract_features(img_path)
        return self.image_model.predict(img, verbose=0)
    
    def idx_to_word(self, integer, tokenizer):
        """Convert index to word"""
        for word, index in tokenizer.word_index.items():
            if index == integer:
                return word
        return None
    
    def predict_caption(self, model, image, tokenizer, max_length):
        """Generate caption for image"""
        in_text = 'startseq'
        for i in range(max_length):
            sequence = tokenizer.texts_to_sequences([in_text])[0]
            sequence = pad_sequences([sequence], maxlen=max_length)
            yhat = model.predict([image, sequence], verbose=0)
            yhat = np.argmax(yhat)
            word = self.idx_to_word(yhat, tokenizer)
            if word is None:
                break
            in_text += ' ' + word
            if word == 'endseq':
                break
        return in_text
    
    def generate_caption(self, image_path):
        """Generate caption for a given image"""
        if not os.path.exists(image_path):
            return "Error: Image not found"
            
        try:
            # Load models if not loaded
            if self.image_model is None:
                self.load_models()
                
            if self.caption_model is None:
                return "Error: Caption model not found. Please train the model first."
            
            # Encode the image
            image = self.encode_image(image_path).reshape((1, 2048))
            
            # Generate caption
            caption = self.predict_caption(self.caption_model, image, self.tokenizer, self.max_length)
            
            # Clean up the caption
            caption = caption.replace('startseq', '').replace('endseq', '').strip()
            return caption if caption else "Could not generate caption for this image."
            
        except Exception as e:
            return f"Error generating caption: {str(e)}"
    
    def load_models(self, model_path='models/'):
        """Load pre-trained models"""
        # Create models directory if it doesn't exist
        os.makedirs(model_path, exist_ok=True)
        
        # Load or create image model
        if not os.path.exists(os.path.join(model_path, 'image_model.h5')):
            print("Downloading and setting up image model...")
            base_model = InceptionV3(weights='imagenet')
            self.image_model = Model(base_model.input, base_model.layers[-2].output)
            self.image_model.save(os.path.join(model_path, 'image_model.h5'))
        else:
            print("Loading image model...")
            self.image_model = load_model(os.path.join(model_path, 'image_model.h5'))
        
        # Load tokenizer
        tokenizer_path = os.path.join(model_path, 'tokenizer.pkl')
        if os.path.exists(tokenizer_path):
            with open(tokenizer_path, 'rb') as f:
                self.tokenizer = pickle.load(f)
        
        # Load caption model
        caption_model_path = os.path.join(model_path, 'caption_model.h5')
        if os.path.exists(caption_model_path):
            print("Loading caption model...")
            self.caption_model = load_model(caption_model_path)
        else:
            print("Caption model not found. Please train the model first.")

def main():
    # Initialize the caption generator
    caption_generator = ImageCaptionGenerator()
    
    # Example usage
    image_path = input("Enter the path to your image: ")
    
    # Generate caption
    caption = caption_generator.generate_caption(image_path)
    print("\nGenerated Caption:", caption)
    
    # Display the image with caption
    if os.path.exists(image_path):
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        plt.figure(figsize=(10, 10))
        plt.imshow(img)
        plt.axis('off')
        plt.title(caption, wrap=True)
        plt.show()

if __name__ == "__main__":
    # Download required NLTK data
    nltk.download('punkt', quiet=True)
    main()
