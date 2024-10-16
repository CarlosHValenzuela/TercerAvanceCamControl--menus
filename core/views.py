from django.shortcuts import render, redirect # type: ignore
from django.http import StreamingHttpResponse # type: ignore
from core.utils.videoReconocer import   generate_frames
from core.utils.videoCapturar import capture_plate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # type: ignore
from django.contrib.auth.models import User # type: ignore
from django.contrib.auth import login, logout, authenticate # type: ignore
from django.contrib.auth.decorators import login_required # type: ignore
from django.http import HttpResponse # type: ignore
from django.db import IntegrityError # type: ignore

# Vista para la página principal
def home(request):
    return render(request, 'home.html')

@login_required
def main(request):
    return render(request, 'main.html')

@login_required
def reconocedor(request):
    return render(request, 'reconocedor.html')

@login_required
def captura(request):
    return render(request, 'captura.html')

@login_required
def residentes(request):
    return render(request, 'residentes.html')

@login_required
def perfil(request):
    return render(request, 'perfil.html')


#Vista Iniciar Sesion
def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'login.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o password esta incorrecto'
        })
        else:
            login(request, user)
            return redirect('main')

# Vista Crear Usuario
def registro (request):

    if request.method == 'GET':
        return render(request, 'registro.html',{
            'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
           try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('main')
           except IntegrityError:
               return render(request, 'registro.html',{
                   'form': UserCreationForm,
                   'error':'Usuario ya existe'})
           
        return render(request, 'registro.html', {"form": UserCreationForm, "error": "Password no coincide."})
    
# Vista Cerrar Sesion    
def cerrarSesion(request):
    logout(request)
    return redirect('inicioSesion')
    
# Vista para el feed de video
def video_feed(request):
    return StreamingHttpResponse(generate_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def video_capture(request):
    return StreamingHttpResponse(capture_plate(), content_type='multipart/x-mixed-replace; boundary=frame')