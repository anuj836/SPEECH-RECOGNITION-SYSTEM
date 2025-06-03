#  SPEECH-RECOGNITION-SYSTEM

*COMPANY* : CODETECH IT SOLUTIONS

*NAME* : ANUJ DESHMUKH

*INTERN ID* : CT04DL900

*DURATION* : 4 weeks

*MENTOR* : NEELA SANTOSH

# Description

This Python script is designed to convert spoken audio into written text using the speech_recognition library. It is a basic implementation of automatic speech recognition (ASR), where the program takes an audio file as input and produces its corresponding text through Google's Web Speech API. This solution is particularly useful for applications like voice assistants, subtitle generation, dictation tools, or any system where audio-to-text conversion is needed.

The script starts by importing the speech_recognition module under the alias sr. This library provides a unified interface to multiple speech recognition engines and APIs, making it convenient for developers to use high-level methods for audio transcription.

The core of the program lies within the transcribe_audio function, which takes a single argument: the path to the audio file that needs to be transcribed. Inside this function, the first step is to initialize the speech recognizer using sr.Recognizer(). This object acts as a controller that provides methods to process and convert audio signals into text.

Next, the script opens the specified audio file using the context manager with sr.AudioFile(file_path) as source:. This ensures that the file is opened and then closed properly after its contents are read. The audio file is read into memory using the recognizer.record(source) method, which captures the entire audio stream from the file. The resulting `audio_data` object contains the waveform information needed for speech recognition.

Once the audio data is ready, the script attempts to transcribe it using Google's free Web Speech API through the method recognizer.recognize_google(audio_data). This method sends the audio data over the internet to Google's servers, where advanced machine learning models process the audio and return a string containing the recognized speech.

If the recognition is successful, the resulting text is printed to the console under the label "Transcription:". However, speech recognition is not always perfect. If the model cannot understand the spoken words—due to noise, accents, unclear pronunciation, or other issues—the recognize_google() method will raise an sr.UnknownValueError. In this case, the script catches the exception and informs the user that the audio could not be understood.

Alternatively, if the request to Google's servers fails—perhaps due to a network issue or incorrect API usage—the method will raise an sr.RequestError. The script handles this by printing a detailed error message, showing why the request could not be completed.

The main entry point of the script is guarded by the if __name__ == "__main__": clause. This ensures that the script runs only when executed directly, and not when imported as a module in another program. Inside this block, the variable audio_file is set to the path "male.wav", representing the audio file that the user wants to transcribe. The transcribe_audio(audio_file) function is then called with this file as input.

This script is a straightforward yet effective way to perform speech recognition in Python. It uses a high-level API that abstracts away the complexity of machine learning models, signal processing, and acoustic modeling. Developers can modify it to handle microphone input, transcribe longer audio files in chunks, or switch to offline recognizers for local processing. However, since it uses an online API, a stable internet connection is required, and the amount of free usage may be limited depending on Google's policies.

In summary, the script demonstrates how to use the speech_recognition library to transcribe audio from a file using Google’s Web Speech API. It includes error handling for both recognition failures and network issues, making it robust for basic usage. Its simplicity makes it ideal for beginners exploring audio processing or speech-enabled applications.



# OUTPUT

![Image](https://github.com/user-attachments/assets/00f9a35f-4b3f-4e2a-89e2-201055842715)
