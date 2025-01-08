from .models import *
from django.shortcuts import render

def home_view(request):
    soz = request.GET.get('soz' , "").lower()
    correct = None
    incorrects = None

    if soz is not "":
        if Correct.objects.filter(word=soz):
            correct = Correct.objects.get(word=soz)
            print(correct)
            incorrects = Incorrect.objects.filter(correct=correct)

        elif Incorrect.objects.filter(word=soz):
            incorrect = Incorrect.objects.get(word=soz)
            correct = incorrect.correct
            incorrects = Incorrect.objects.filter(correct=correct)

        elif 'h' not in soz and 'x' not in soz:
            correct = "Soz tarkibida 'Xx' yoki 'Hh' mavjud emas!"
            incorrects = "Soz tarkibida 'Xx' yoki 'Hh' mavjud emas!"
        else:
            correct = 'Omborda mavjud emas!'
            incorrects = 'Omborda mavjud emas!'
    context = {
        'correct': correct,
        'incorrects': incorrects,
        "soz": soz,
    }
    return render(request , 'index.html' , context)
