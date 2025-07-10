import pyttsx3
from nltk.corpus import wordnet

class Speaking:
    def speak(self, audio):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.say(audio)
        engine.runAndWait()

class Meaning:
    def Dictionary(self):
        speak = Speaking()
        speak.speak("Which word do you want the meaning of, sir?")
        query = input("Enter word: ")

        synsets = wordnet.synsets(query)

        if not synsets:
            speak.speak("Sorry, I could not find the meaning.")
            print("Meaning not found.")
            return

        speak.speak(f"I found {len(synsets)} meanings. Here are some:")
        for syn in synsets[:3]:  # Limit to 3 meanings
            definition = syn.definition()
            print(f"Meaning: {definition}")
            speak.speak("Meaning is: " + definition)

if __name__ == '__main__':
    import nltk
    try:
        nltk.data.find('corpora/wordnet')
    except LookupError:
        nltk.download('wordnet')

    Meaning().Dictionary()
