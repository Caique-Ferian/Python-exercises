from django.shortcuts import render, get_object_or_404
from galery.models import Photography


# Cria Os Controllers da aplicação aqui, que neste caso está sendo usado para renderizar arquivos HTML
def index(request):
    photographys = Photography.objects.order_by("-published_date").filter(
        published=True
    )
    return render(request, "galery/index.html", {"cards": photographys})


def image(request, photo_id):
    photography = get_object_or_404(Photography, pk=photo_id)
    return render(request, "galery/image.html", {"photography": photography})
