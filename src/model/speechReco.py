import speech_recognition as sr

fr = "fr-FR"

def getAudio():
    """
        Record audio from main microphone source of the computer.

    Returns:
        
        - AudioData: Audio data in the record.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        r.adjust_for_ambient_noise(source)
        print("Dites quelque chose")
        audio = r.listen(source)
        return audio

def getTextFromAudio(languageAudio):
    """
        Generate String from AudioData to be used in many functions.
        
    Args:
    
        - languageAudio (str): Language of the user.

    Returns:
        
        - str: Text from audio recorded by the microphone.
    """
    audio = getAudio()
    r = sr.Recognizer()
    try:
        text = r.recognize_google(audio, language=languageAudio)
        return text
    except sr.UnknownValueError:
        print("L'audio n'a pas été compris")
    except sr.RequestError as e:
        print("Le service Google Speech API ne fonctionne plus" + format(e))