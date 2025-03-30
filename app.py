from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
Api_Key = os.getenv("API_KEY")

# Initialize Flask app
app = Flask(__name__)

# Configure Generative AI API
genai.configure(api_key=Api_Key)
model = genai.GenerativeModel('gemini-1.5-flash')

# Home route to render a basic template
@app.route('/')
def index():
    return render_template('index.html')

# API route to interact with the model
@app.route('/generate', methods=['POST'])
def generate():
    user_input = request.form['user_input']  # Get user input from form

    # Generate content from model
    response = model.generate_content(user_input)

    return jsonify({'response': response.text})  # Return the AI response as JSON

# Run the app
if __name__ == '__main__':
    app.run(debug=True)

