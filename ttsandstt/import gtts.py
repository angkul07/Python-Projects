import gtts  
from playsound import playsound  



text = input("enter your text: ")
t1 = gtts.gTTS(text, lang='hr', tld='co.in')  

t1.save("welcome.mp3")  
playsound("welcome.mp3")  