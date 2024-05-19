from django.db import models

class Users(models.Model):
    name        = models.CharField(max_length = 100, blank = True, null = True, default = "")
    email       = models.CharField(max_length = 250, blank = True, null = True, default = "")
    password    = models.CharField(max_length = 150, blank = True, null = True, default = "")
    phone       = models.CharField(max_length = 12, blank = True, null = True, default = "")
    created_at  = models.DateField(auto_now = False, null = True, blank = True)

class Conversations(models.Model):
    user        = models.ForeignKey(Users, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    created_at  = models.DateField(auto_now = False, null = True, blank = True)
    
class Messages(models.Model):
    conversation    = models.ForeignKey(Conversations, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    senderUser      = models.ForeignKey(Users, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    message         = models.CharField(max_length = 500, blank = True, null = True, default = "")

class Intents(models.Model): # Intenciones
    nameIntention = models.CharField(max_length = 100, blank = True, null = True, default = "") # NOMBRE INTENCION
    description   = models.CharField(max_length = 500, blank = True, null = True, default = "") # DESCRIPCION INTENCION

class Responses(models.Model): # Respuestas
    intention    = models.ForeignKey(Intents, on_delete = models.CASCADE, default = 1)   # ID INTENCION
    response     = models.CharField(max_length = 500, blank = True, null = True, default = "") # RESPUESTA

class TrainingPhrases(models.Model): # Frases de Entrenamiento
    intention    = models.ForeignKey(Intents, on_delete = models.CASCADE, default = 1)   # ID INTENCION
    phrase     = models.CharField(max_length = 500, blank = True, null = True, default = "") # Frase de Entrenamiento
 