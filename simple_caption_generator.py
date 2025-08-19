import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import cv2

class SimpleImageCaptionGenerator:
    def __init__(self):
        self.model = self._load_model()
    
    def _load_model(self):
        """Load pre-trained InceptionV3 model"""
        print("Loading image recognition model...")
        model = InceptionV3(weights='imagenet')
        print("Model loaded successfully!")
        return model
    
    def preprocess_image(self, img_path):
        """Preprocess image for the model"""
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x
    
    def _get_hashtags(self, objects):
        """Generate relevant hashtags from detected objects"""
        # Filter out generic terms and create hashtags
        filtered = [obj for obj in objects if len(obj) > 3]  # Remove short words
        hashtags = ['#' + word.replace(' ', '') for word in filtered]
        return ' '.join(hashtags[:3])  # Return max 3 hashtags
    
    def _generate_style(self):
        """Randomly select an Indian English caption style"""
        styles = [
            "✨ {content} {hashtags}",
            "{content} 💫 {hashtags}",
            "{content} \n\n{hashtags}",
            "{content} \n\n📸✨ {hashtags}",
            "{content} \n\n#DesiVibes #IncredibleIndia {hashtags}",
            "{content} \n\n#AtmaNirbharBharat #MakeInIndia {hashtags}",
            "{content} \n\n#Swadesh #DesiDilSe {hashtags}",
            "{content} \n\n#IndianMoments #DesiLife {hashtags}"
        ]
        return np.random.choice(styles)
    
    def predict(self, img_path):
        """Generate a social media style caption for the image"""
        try:
            # Preprocess the image
            processed_img = self.preprocess_image(img_path)
            
            # Make prediction
            predictions = self.model.predict(processed_img, verbose=0)
            
            # Get top predicted classes in English
            decoded_predictions = decode_predictions(predictions, top=3)[0]
            
            # Extract class labels and format them naturally
            objects = [pred[1].replace('_', ' ') for pred in decoded_predictions]
            
            # Desi/Indian English phrases and expressions
            content_phrases = [
                f"Kya baat hai! This {objects[0]} is just wow! 😍 #DesiVibes",
                f"Aaj ka perfect shot! {objects[0]} looking too good! ✨ #DesiPhotography",
                f"Mast hai yeh {objects[0]}! ❤️ #DesiLife",
                f"Kya scene hai! {objects[0]} on point! 👌 #DesiStyle",
                f"Yeh {objects[0]} dekh kar dil khush ho gaya! 😊 #DesiFeels",
                f"Bohot hard! {objects[0]} at its best! 🔥 #DesiPride",
                f"Aisi hi raho {objects[0]}! ❤️ #DesiLove",
                f"Kya baat hai yaar! {objects[0]} is ❤️ #DesiMoments"
            ]
            
            # Add more context if multiple objects are detected
            if len(objects) > 1:
                if len(objects) == 2:
                    content_phrases += [
                        f"{objects[0]} aur {objects[1]} - ekdum jhakaas combo! 🤩 #DesiJodi",
                        f"Dekho yeh {objects[0]} aur {objects[1]} ka kamaal! ✨ #DesiMagic",
                        f"{objects[0]} ke saath {objects[1]} - kya baat hai! ❤️ #DesiVibes"
                    ]
                else:
                    content_phrases += [
                        f"{objects[0]}, {objects[1]} aur {objects[2]} - teeno ek saath! 😍 #DesiTrio",
                        f"{objects[0]} ke saath {objects[1]} aur {objects[2]} - full masti! 🤩 #DesiFun"
                    ]
            
            # Add some common Indian English phrases
            indian_phrases = [
                "What say? Looking good na?",
                "Timepass ho gaya! 😄",
                "Kya lagta hai?",
                "Puri tarah se paisa vasool! 💯",
                "Bas kar pagle, ab rulayega kya? 😍",
                "Aisi ki taisi! 🔥",
                "Dil jeet liya! ❤️",
                "Jhakaas! 👌"
            ]
            
            # Add Indian English phrases to some captions
            if np.random.random() > 0.5:  # 50% chance to add an Indian English phrase
                content_phrases = [f"{p} {np.random.choice(indian_phrases)}" for p in content_phrases]
            
            # Select random content phrase
            content = np.random.choice(content_phrases)
            
            # Generate hashtags
            hashtags = self._get_hashtags(objects)
            
            # Format final caption
            style = self._generate_style()
            caption = style.format(content=content, hashtags=hashtags)
            
            return caption
            
        except Exception as e:
            return f"Error generating caption: {str(e)}"

def main():
    # Initialize the generator
    generator = SimpleImageCaptionGenerator()
    
    # Get image path from user
    img_path = input("Enter the path to your image: ")
    
    if not os.path.exists(img_path):
        print("Error: Image not found!")
        return
    
    # Generate and display caption
    caption = generator.predict(img_path)
    print("\nGenerated Caption:", caption)
    
    # Display the image
    img = cv2.imread(img_path)
    if img is not None:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        import matplotlib.pyplot as plt
        plt.figure(figsize=(10, 10))
        plt.imshow(img)
        plt.axis('off')
        plt.title(caption, wrap=True)
        plt.show()

if __name__ == "__main__":
    main()
