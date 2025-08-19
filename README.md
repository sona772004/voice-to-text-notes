<<<<<<< HEAD
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
=======
# Voice-to-Text Note Taking App

A modern web application that allows users to record voice notes and have them automatically transcribed to text. Built with Python, Flask, and modern web technologies.

## Features

- 🎤 Record voice notes with your microphone
- ✍️ Type notes manually if preferred
- 🔄 Real-time speech-to-text conversion
- 💾 Save and manage your notes
- 🎨 Clean, responsive UI with Tailwind CSS
- 📱 Mobile-friendly design

## Tech Stack

- **Backend**: Python with Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Speech Recognition**: SpeechRecognition library with Google Web Speech API
- **Database**: SQLite with SQLAlchemy ORM
- **Styling**: Tailwind CSS
- **Icons**: Font Awesome

## Prerequisites

- Python 3.8+
- pip (Python package manager)
- Microphone access (for voice recording)

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/voice-notes-app.git
   cd voice-notes-app
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\\venv\\Scripts\\activate
   ```

3. **Install dependencies**
>>>>>>> origin/main
   ```bash
   pip install -r requirements.txt
   ```

<<<<<<< HEAD
4. Run the application:
=======
4. **Run the application**
>>>>>>> origin/main
   ```bash
   python app.py
   ```

<<<<<<< HEAD
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
=======
5. **Open your browser**
   Visit `http://localhost:5000` to use the application.

## Usage

1. Click the microphone button to start recording your voice note.
2. Click it again to stop recording.
3. The app will automatically transcribe your speech to text.
4. Click "Save Note" to store your note.
5. View, edit, or delete your notes from the dashboard.
>>>>>>> origin/main

## Project Structure

```
<<<<<<< HEAD
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
=======
voice-notes-app/
├── app.py                # Main Flask application
├── requirements.txt      # Python dependencies
├── instance/
│   └── notes.db         # SQLite database (created on first run)
└── templates/
    ├── base.html        # Base template
    └── index.html       # Main application page
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Styled with [Tailwind CSS](https://tailwindcss.com/)
- Icons by [Font Awesome](https://fontawesome.com/)
- Speech recognition powered by [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
>>>>>>> origin/main
