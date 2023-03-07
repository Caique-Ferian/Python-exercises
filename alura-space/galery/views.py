from django.shortcuts import render
from galery.models import Photography


# Cria Os Controllers da aplicação aqui, que neste caso está sendo usado para renderizar arquivos HTML
def index(request):
    photographys = Photography.objects.all()
    return render(request, "galery/index.html", {"cards": photographys})


def image(request):
    return render(request, "galery/image.html")
