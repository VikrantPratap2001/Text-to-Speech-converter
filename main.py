import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("Enter what you want to hear: ")
    if text == "quit":
        speak.Speak("It was nice talking to you.")
        break
    speak.Speak(text)
