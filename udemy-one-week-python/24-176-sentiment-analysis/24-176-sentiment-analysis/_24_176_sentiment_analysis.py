from textblob import TextBlob
import pyttsx3
import art

print(art.text2art("Ministry of Work"))

engine = pyttsx3.init()
engine.say("Hello employee number 99. We hope you had a great day at work. It's time to submit your employee wellness statement")
engine.runAndWait()

entry = input("Enter your employee wellness statement:\n")
blob = TextBlob(entry)

while blob.sentiment.polarity < 0.5:
    print("I don't like your attitude. You to be more positive. Try again!")
    engine.say("I don't like your attitude. You need to be more positive. Try again!")
    engine.runAndWait()
    print("-" * 100)
    entry = input("Enter your employee wellness statement:\n")
    blob = TextBlob(entry)

print("Great to hear you love it here. You can go home now. Thanks for being a part of our Ministry of Work family. See you tomorrow.")
engine.say("Great to hear you love it here. You can go home now. Thanks for being a part of our Ministry of Work family. See you tomorrow.")
engine.runAndWait()