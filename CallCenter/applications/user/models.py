from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True, default="")
    lastName_P = models.CharField(max_length=100, blank=True, null=True, default="")
    lastName_M = models.CharField(max_length=100, blank=True, null=True, default="")
    email = models.EmailField(max_length=250, unique=True)
    password = models.CharField(max_length=150, blank=True, null=True, default="")
    class Meta:
        verbose_name = 'UsuariosInit'
        verbose_name_plural = 'UsuariosInit'
        ordering = ['id']
        db_table = "user"
        
class Conversations(models.Model):
    user        = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    created_at  = models.DateField(auto_now = False, null = True, blank = True)
    class Meta():
        verbose_name = 'Conversaciones'
        verbose_name_plural = 'Conversaciones'
        ordering = ['id']
        db_table = "conversations"

class Messages(models.Model):
    conversation    = models.ForeignKey(Conversations, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    senderUser      = models.ForeignKey(User, on_delete = models.CASCADE, default = 1)   # ID USUARIOS
    message         = models.CharField(max_length = 500, blank = True, null = True, default = "")
    class Meta():
        verbose_name = 'Mensajes'
        verbose_name_plural = 'Mensajes'
        ordering = ['id']
        db_table = "messages"

class Intents(models.Model): # Intenciones
    nameIntention = models.CharField(max_length = 100, blank = True, null = True, default = "") # NOMBRE INTENCION
    description   = models.CharField(max_length = 500, blank = True, null = True, default = "") # DESCRIPCION INTENCION
    class Meta():
        verbose_name = 'Intenciones'
        verbose_name_plural = 'Intenciones'
        ordering = ['id']
        db_table = "intents"

class Responses(models.Model): # Respuestas
    categoria           = models.CharField(max_length = 255, blank = True, null = True, default = "") # CATEGORIA
    subcategoria        = models.CharField(max_length = 255, blank = True, null = True, default = "") # SUBCATEGORIA
    texto_consulta      = models.TextField(blank = True, null = True, default = "") # TEXTO CONSULTA
    descripcion_problema    = models.TextField(blank = True, null = True, default = "") # DESCRIPCION PROBLEMA
    solucion_sugerida   = models.TextField(blank = True, null = True, default = "") # SOLUCION SUGERIDA
    class Meta():
        verbose_name = 'Respuestas'
        verbose_name_plural = 'Respuestas'
        ordering = ['id']
        db_table = "responses"

class TrainingPhrases(models.Model): # Frases de Entrenamiento
    intention    = models.ForeignKey(Intents, on_delete = models.CASCADE, default = 1)   # ID INTENCION
    phrase     = models.CharField(max_length = 500, blank = True, null = True, default = "") # Frase de Entrenamiento
    class Meta():
        verbose_name = 'FrasesDeEntrenamiento'
        verbose_name_plural = 'FrasesDeEntrenamiento'
        ordering = ['id']
        db_table = "trainingPhrases"
