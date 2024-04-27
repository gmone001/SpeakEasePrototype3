The Conversational Assistant is an advanced application designed to enhance user engagement through voice-driven interactions. It combines speech recognition, AI-powered conversation, and speech synthesis to provide a seamless interaction experience in Spanish. This application is perfect for users looking to practice their Spanish speaking and comprehension skills or for those who need an interactive guide that responds audibly.

Features

Speech Recognition: Converts spoken Spanish into text using Google's speech recognition service.
AI Conversation: Leverages OpenAI's GPT-4 to generate intelligent and context-aware responses.
Text-to-Speech: Utilizes Google's Text-to-Speech (gTTS) to convert the response text into audible speech, providing a hands-free experience.


Technologies Used

Python 3.8+: The primary programming language.
Speech Recognition: speech_recognition library to handle voice input.
OpenAI API: For generating conversational responses.
gTTS (Google Text-to-Speech): For synthesizing speech from text.
dotenv: For managing environmental variables securely.
playsound: For playing audio files.

Prerequisites
Python 3.8 or higher
Pip for Python package installation
Microphone for voice input

pip install python-dotenv speech_recognition openai gtts playsound


inside the .env OPENAI_API_KEY='your_openai_api_key_here'

Usage

The application will start by greeting you in Spanish. Respond in Spanish, and it will continue the conversation.
The assistant listens to your speech, converts it to text, sends it to OpenAI for processing, and speaks the response back to you.


Contact-
Graciella Monetti
gmone001@gold.ac.uk
