from django.shortcuts import render,redirect
from django.http import HttpResponse


# crear forms
from django.contrib.auth.forms import UserCreationForm
# registrar ususario
from django.contrib.auth.models import User
#crear session o cookie para el login
from django.contrib.auth import login
#manejar errores de la db
from django.db import IntegrityError

# Create your views here.

def Home(request):
    return render(request, 'home.html')


def SignUp(request):

    if request.method == 'GET':
        return render(request, 'signup.html',
                      {
                          'formulario': UserCreationForm,

                      })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # registrar usp_LoginUsuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request,user)
                print(request.POST)
                return redirect('task')
            except IntegrityError:
                return render(request, 'signup.html',
                              {
                                  'formulario': UserCreationForm,
                                  'error': 'Username alredy exits'
                              })
        else:
            return render(request, 'signup.html',
                              {
                                  'formulario': UserCreationForm,
                                  'error': 'password incorrect'
                              })

def Task(request):
  return render(request, 'task.html')


def Estudiante(request):
    return render(request, '_estudiante.html')
