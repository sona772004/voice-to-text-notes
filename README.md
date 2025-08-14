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
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Visit `http://localhost:5000` to use the application.

## Usage

1. Click the microphone button to start recording your voice note.
2. Click it again to stop recording.
3. The app will automatically transcribe your speech to text.
4. Click "Save Note" to store your note.
5. View, edit, or delete your notes from the dashboard.

## Project Structure

```
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
