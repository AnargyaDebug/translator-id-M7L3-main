import speech_recognition

def speech():
    mic = speech_recognition.Microphone()
    recognition = speech_recognition.Recognizer()

    with mic as audio_file:
        recognition.adjust_for_ambient_noise(audio_file)
        audio = recognition.listen(audio_file)
        
        return recognition.recognize_google(audio, language="en-EN")
