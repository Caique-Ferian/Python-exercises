from django.shortcuts import render


# Cria Os Controllers da aplicação aqui, que neste caso está sendo usado para renderizar arquivos HTML
def index(request):
    return render(request, "galery/index.html")


def image(request):
    return render(request, "galery/image.html")
