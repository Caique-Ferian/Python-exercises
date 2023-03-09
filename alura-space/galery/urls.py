from django.urls import path
from galery.views import index, image

# Toda aplicação por padrão é de boa pratica conter um arquivo urls.py, contendo suas rotas que devem ser apenas incluidas na URLS.PY central do app, igual router(armazena as rotas de cada controller) do express e app(utiliza as rotas de cada controller)
urlpatterns = [
    path("", index, name="index"),
    path("imagem/<int:photo_id>", image, name="image"),
]
