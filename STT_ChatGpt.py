__author__ = "Shay Stevens"
__Date__ = "June 2023"

# Importing required libraries
import openai
import speech_recognition as sr
from gtts import gTTS
import os

# Function to convert text to speech using gTTS
def speak(text):
    tts = gTTS(text=text, lang='en') # Convert text to speech
    tts.save("response.mp3") # Save speech as an mp3 file
    os.system("mpg123 response.mp3") # Play the mp3 file

# Function to convert speech to text using Google's Speech Recognition API
def listen():
    r = sr.Recognizer() # Initialize recognizer class (for recognizing the speech)

    with sr.Microphone() as source: # Use microphone as source of input
        print("Listening...") 
        audio = r.listen(source) # Listen to the audio via microphone
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-US') # Convert audio to text
            print(f'User said: {query}\n')
            return str(query)
        except Exception as e:
            print("Could not recognize your voice. Please say it again.")
            return None

# Function to get response from OpenAI's GPT-3 model
def answer(query):
    api_key = "YOUR_OPENAI_API_KEY" # OpenAI API key
    openai.api_key = api_key

    try:
        completion = openai.ChatCompletion.create(
        model =  "gpt-3.5-turbo", # OpenAI's GPT model
        messages = [{"role": "user", "content": query}] # User's query
        )

        reply = completion.choices[0].message.content
        print(reply.encode('ascii', errors='ignore').decode('ascii')) # Print model's reply

    except StopIteration:
        print("I am sorry, but I can't find the answer.")

# Main function
if __name__ == "__main__":
    query = listen() # Convert user's speech to text
    if query:
        answer(query) # Get response to user's query from GPT-3 model
