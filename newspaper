import pyttsx3
import requests
import json
engine =pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)
# print(voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Hello! Welcome to ABC news!")

    url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=2d7c147e1e5f4f8dbd5362b7b9259cd2"

    news = requests.get(url).text
    news = json.loads(news)
    # print(news["totalResults"])
    arts = news['articles']
    for article in arts:
        print(article['author'])
        speak(article['author'])
        print(article['title'])
        speak(article['title'])
        print(article['description'])
        speak(article['description'])
        speak("Moving on to the next news.")

