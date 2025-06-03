import speech_recognition as sr

def transcribe_audio(file_path):
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Load the audio file
    with sr.AudioFile(file_path) as source:
        audio_data = recognizer.record(source)

    # Recognize using Google Web Speech API
    try:
        text = recognizer.recognize_google(audio_data)
        print("Transcription:") 
        print(text)
    except sr.UnknownValueError:
        print("Could not understand the audio")
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {e}")

if __name__ == "__main__":
    audio_file = "male.wav"  # Path to your audio file
    transcribe_audio(audio_file)
