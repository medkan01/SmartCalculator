import speech_recognition as sr

fr = "fr-FR"

def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        r.adjust_for_ambient_noise(source)
        print("Dites quelque chose")
        audio = r.listen(source)
        return audio

def getTextFromAudio(audio, language_audio):
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio, language=language_audio)
        return text
    except sr.UnknownValueError:
        print("L'audio n'a pas été compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))