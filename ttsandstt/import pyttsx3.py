import pyttsx3

hello = pyttsx3.init()

hello.setProperty('rate', 100)
voices = hello.getProperty('voices')
hello.setProperty('voice', voices[0].id)
text = input("Enter your text: ")

hello.say(text)
hello.runAndWait()