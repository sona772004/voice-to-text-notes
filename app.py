from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import speech_recognition as sr
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Note {self.id}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes)

@app.route('/save_note', methods=['POST'])
def save_note():
    content = request.json.get('content', '').strip()
    if content:
        note = Note(content=content)
        db.session.add(note)
        db.session.commit()
        return jsonify({'success': True, 'id': note.id, 'created_at': note.created_at.strftime('%Y-%m-%d %H:%M:%S')})
    return jsonify({'success': False, 'error': 'Empty content'}), 400

@app.route('/delete_note/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'success': True})

import tempfile
import os
import wave
import audioop
import struct

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    print("\n=== New Transcription Request ===")
    print(f"Request files: {request.files}")
    
    if 'audio' not in request.files:
        print("Error: No audio file in request")
        return jsonify({'error': 'No audio file provided'}), 400
    
    audio_file = request.files['audio']
    print(f"Received audio file: {audio_file.filename}, Content-Type: {audio_file.content_type}")
    
    recognizer = sr.Recognizer()
    temp_audio_path = None
    
    try:
        # Save the uploaded file to a temporary file
        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
            audio_file.save(temp_audio.name)
            temp_audio_path = temp_audio.name
            print(f"Saved temporary audio to: {temp_audio_path}")
            
            # Verify the file is not empty
            if os.path.getsize(temp_audio_path) == 0:
                raise ValueError("Uploaded file is empty")
        
        print("Starting speech recognition...")
        try:
            # Process the WAV file
            with sr.AudioFile(temp_audio_path) as source:
                # Adjust for ambient noise
                print("Adjusting for ambient noise...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                
                print("Recording audio...")
                # Record the audio with a maximum duration of 10 seconds
                audio_data = recognizer.record(source, duration=10)
                
                print("Sending to Google Speech Recognition...")
                # Try with show_all=False to get a simple string response
                text = recognizer.recognize_google(audio_data, language='en-US')
                
                print(f"Recognition complete. Text: {text[:100]}..." if len(text) > 100 else f"Recognition complete. Text: {text}")
                
                if not text or text.strip() == '':
                    raise sr.UnknownValueError("No speech detected in the audio")
                
        except sr.UnknownValueError as e:
            print(f"Google Speech Recognition could not understand the audio: {str(e)}")
            return jsonify({'error': 'Could not understand the audio. Please speak clearly and try again.'}), 400
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return jsonify({'error': f'Speech recognition service error: {e}'}), 500
        except Exception as e:
            print(f"Error during speech recognition: {str(e)}")
            return jsonify({'error': f'Error processing audio: {str(e)}'}), 500
            
        return jsonify({'text': text})
        
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({'error': f'Error processing audio: {str(e)}'}), 500
        
    finally:
        # Clean up temporary file if it was created
        if temp_audio_path and os.path.exists(temp_audio_path):
            try:
                os.unlink(temp_audio_path)
                print("Cleaned up temporary file")
            except Exception as e:
                print(f"Warning: Could not clean up temporary file: {e}")
        # Clean up WAV file if it exists
        if 'wav_path' in locals() and os.path.exists(wav_path):
            try:
                os.unlink(wav_path)
                print("Cleaned up WAV file")
            except Exception as e:
                print(f"Warning: Could not clean up WAV file: {e}")

if __name__ == '__main__':
    os.makedirs('instance', exist_ok=True)
    app.run(debug=True)
