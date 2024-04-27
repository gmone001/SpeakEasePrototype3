import os
from dotenv import load_dotenv
import speech_recognition as sr
import openai
from gtts import gTTS
from playsound import playsound

# Load API key from .env file
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI
openai.api_key = api_key

# Initialize speech recognizer
recognizer = sr.Recognizer()

def listen_and_transcribe():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language="es-ES")  # Set to Spanish recognition
            print(f"Recognized text: {text}")
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

def ask_openai(question, history=[]):
    history.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=history
    )
    answer = response.choices[0].message['content']
    history.append({"role": "assistant", "content": answer})
    return answer

def synthesize_response(text):
    tts = gTTS(text=text, lang='es')  # Generate speech in Spanish
    tts.save("response.mp3")
    print("Response audio saved as response.mp3.")
    playsound("response.mp3")

def main():
    # Initial greeting in Spanish
    initial_greeting = "Hola, ¿cómo estás? Me llamo Andrea."
    print("Chatbot: " + initial_greeting)
    synthesize_response(initial_greeting)

    history = []

    while True:
        question = listen_and_transcribe()
        if question:
            response_text = ask_openai(question, history)
            print(f"OpenAI response: {response_text}")
            synthesize_response(response_text)

if __name__ == "__main__":
    main()
