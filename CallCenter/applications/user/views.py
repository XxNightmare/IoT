from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from .models import *
from .functions import *
from django.http import FileResponse

def home(request):
    data = {}
    # ---------- LOGIN USUARIO ---------------------------------------------------------------------------------------------------------------------------------------
    if request.method == "POST" and 'Login_button' in request.POST:
        email = request.POST['login_email']
        password = request.POST['login_password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('principal')
        else:
            return HttpResponse('Correo electrónico o contraseña incorrectos')
    # ---------- REGISTRAR USUARIO -----------------------------------------------------------------------------------------------------------------------------------
    if request.method == "POST" and 'Register_button' in request.POST:
        name = request.POST.get('register_name') # NOMBRE
        lastNameF = request.POST.get('register_lastNameF') # APELLIDO P
        lastNameM = request.POST.get('register_lastNameM') # APELLIDO M
        email = request.POST.get('register_email') # EMAIL
        password = request.POST.get('register_password') # CONTRASEÑA
        try:
            u = User(
                username=email,  # Usar el correo como nombre de usuario
                name=name,
                lastName_P=lastNameF,
                lastName_M=lastNameM,
                email=email,
                password=make_password(password),  # Encriptar la contraseña
            )
            u.save()
        except Exception as ex:
            print(f"Hubo un error en Register_button. Error {ex}")
    # -----------------------------------------------------------------------------------------------------------------------------------------------------------------
    return render(request, 'user/home.html', data)

def principal(request):
    if not request.user.is_authenticated:
        return redirect('../')
    data = {}
    data = getInformationUser(request.user.id)
    responseAudio(f"Bienvenido, {data['name']} {data['lastName_P']} {data['lastName_M']}")
    # ------------------------------------------------------------------------------------------------------------------------------------------
    if request.method == "POST" and 'btnDownload' in request.POST:
        image_path = os.path.join(r'C:\Users\rafa-\Documents\GitHub\IoT\CallCenter\applications\user\media', 'probabilidad_exito.png')
        response = FileResponse(open(image_path, 'rb'), as_attachment=True, filename='probabilidad_exito.png')
        return response
    # ------------------------------------------------------------------------------------------------------------------------------------------
    return render(request, 'user/principal.html', data)

def logout_user(request):
    logout(request)
    return redirect('home')
