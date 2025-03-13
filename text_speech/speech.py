import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('correction-sir-i-lost-both-legs-i-did-not-die.wav') as source:
    audio_text = r.listen(source)

    try:
        text = r.recognize_google(audio_text)
        print("Converting audio to text...")
        print(text)
    except:
        print('Sorry....run again')