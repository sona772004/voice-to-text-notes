from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
from simple_caption_generator import SimpleImageCaptionGenerator

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Initialize the caption generator
caption_generator = SimpleImageCaptionGenerator()

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file part'}), 400
        
        file = request.files['file']
        
        if file.filename == '':
            return jsonify({'success': False, 'error': 'No selected file'}), 400
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            
            # Ensure upload directory exists
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            
            # Save the file
            file.save(filepath)
            
            # Generate caption
            caption = caption_generator.predict(filepath)
            
            # Check if caption generation failed
            if caption.startswith('Error:') or 'not found' in caption:
                return jsonify({
                    'success': False,
                    'error': caption,
                    'image_url': f'/static/uploads/{filename}'
                }), 200
            
            return jsonify({
                'success': True,
                'image_url': f'/static/uploads/{filename}',
                'caption': caption
            })
        
        return jsonify({'success': False, 'error': 'File type not allowed. Please upload an image file (PNG, JPG, JPEG, GIF).'}), 400
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
