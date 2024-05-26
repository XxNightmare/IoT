from .models import *
import pyttsx3

def getInformationUser(id_user):
    data = {}
    u = User.objects.get(id = id_user)
    data["name"] = u.name
    data["lastName_P"] = u.lastName_P
    data["lastName_M"] = u.lastName_M
    data["email"] = u.email
    data["password"] = u.password
    return data

def responseAudio(text: str):
    try:
        engine = pyttsx3.init()
        engine.say(str(text))
        engine.runAndWait()
    except Exception as ex:
        print(f"Error {ex}")
