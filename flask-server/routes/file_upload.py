from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import PyPDF2
import extract_msg

file_upload_bp = Blueprint('file_upload', __name__)

# Define the upload folder path
UPLOAD_FOLDER = './uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@file_upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    # Save the file to the server
    filename = secure_filename(file.filename)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)

    # Check if the file is a PDF or MSG and extract text
    if filename.endswith('.pdf'):
        extracted_text = extract_text_from_pdf(filepath)
        return jsonify({"message": "File uploaded and text extracted", "text": extracted_text}), 200
    elif filename.endswith('.msg'):
        extracted_text = extract_text_from_msg(filepath)
        return jsonify({"message": "File uploaded and text extracted", "text": extracted_text}), 200
    
    return jsonify({"message": "File uploaded, but no extraction performed"}), 200

def extract_text_from_pdf(filepath):
    text = ""
    with open(filepath, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
    return text

def extract_text_from_msg(filepath):
    msg = extract_msg.Message(filepath)
    return msg.body