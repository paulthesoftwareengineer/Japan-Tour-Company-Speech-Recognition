import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I could not understand what you said")
except sr.RequestError as e:
    print("Error requesting results from Google Speech Recognition service; {0}".format(e))
