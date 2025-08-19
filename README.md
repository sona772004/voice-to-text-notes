# DesiCaption - Indian English Image Caption Generator

An AI-powered image caption generator that creates engaging, Indian-English social media captions for your photos. This project uses a pre-trained InceptionV3 model for image recognition and generates culturally relevant captions with a desi twist!

## Features

- 🎭 Generate Indian English/Hinglish captions for your images
- 📱 Clean and responsive web interface
- 🖼️ Drag and drop image upload
- 📋 One-click copy captions to clipboard
- 🔥 Indian social media style captions with emojis and hashtags
- 🎯 Culturally relevant phrases and expressions
- ⚡ Fast and lightweight
- 🎨 Built with TensorFlow, Flask, and Tailwind CSS

## Prerequisites

- Python 3.7+
- pip (Python package manager)
- Git (for cloning the repository)
- Web browser (Chrome, Firefox, or Edge recommended)

## 🚀 Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/desi-caption-generator.git
   cd desi-caption-generator
   ```

2. Create and activate a virtual environment:
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage

### Web Application

1. Start the Flask development server:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Upload an image using the drag and drop interface or by clicking to browse files

### Command Line

You can also use the caption generator from the command line:

```bash
python image_caption_generator.py
```

When prompted, enter the path to your image file.

## Example Captions

Here are some examples of the Indian English captions you can expect:

- "Kya baat hai! This beach is just wow! 😍 #DesiVibes #beach #vacation"
- "Aaj ka perfect shot! Sunset looking too good! ✨ #DesiPhotography #sunset"
- "Mast hai yeh food! ❤️ #DesiLife #foodie"
- "Dekho yeh dog aur cat ka kamaal! ✨ #DesiMagic #dog #cat"

## 🤝 Contributing

Contributions are welcome! Feel free to submit issues and enhancement requests.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built with ❤️ for the Indian social media community
- Uses TensorFlow and InceptionV3 for image recognition
- Inspired by the vibrant Indian social media culture

## Project Structure

```
desi-caption-generator/
├── app.py                     # Flask web application
├── simple_caption_generator.py # Main caption generation logic
├── requirements.txt            # Python dependencies
├── static/                    # Static files (CSS, JS, uploaded images)
│   └── uploads/               # Directory for uploaded images
│       └── .gitkeep           # Keep empty uploads directory
├── templates/                 # HTML templates
│   └── index.html             # Web interface
└── README.md                  # Project documentation
```

## Tech Stack

- **Backend**: Python, Flask, TensorFlow
- **Frontend**: HTML, Vanilla JavaScript, Tailwind CSS
- **Machine Learning**: InceptionV3 (pre-trained on ImageNet)
- **Deployment**: Can be deployed on any Python-compatible hosting service

## 🌟 Features Coming Soon

- More Indian language support (Hindi, Tamil, etc.)
- Custom caption styles
- Hashtag suggestions
- Mobile app version
- Social media sharing options
