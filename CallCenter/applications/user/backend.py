from datetime import date, timedelta
from email import message
from os import error, path, remove
from django.db import transaction
from django.conf import settings
from django.http.response import JsonResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template.loader import get_template         # Esta funcion se encarga de extraer el html al que editaremos.
import os, time, json
import json
from django.http import HttpResponse
import pyttsx3
from MySQLdb import Date

from applications.user.functions import *

import speech_recognition as sr

def give_response(request):
    data = {}
    respuesta = request.POST.get('response')
    try:
        responseAudio(respuesta)
        data["allOk"] = True
    except Exception as ex:
        print(f"Error {ex}")
        data["allOk"] = False
    return JsonResponse(data)

def get_conversacion(request):
    data = {}
    # OBTENER AUDIO DEL MICRÓFONO
    recog = sr.Recognizer()
 
    with sr.Microphone() as source:
        audio = recog.listen(source)
    try:
        text = recog.recognize_google(audio, language='es-ES')
        data["allOk"] = True
        data["conversation"] = text
    except sr.UnknownValueError:
        data["conversation"] = "Google Speech Recognition No pudo entender lo que comentas"
        data["allOk"] = False
    except sr.RequestError as e:
        data["allOk"] = False
        data["conversation"] = "Could not request results from Google Speech Recognition service; {0}".format(e)
    return JsonResponse(data)
