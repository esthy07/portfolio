from tkinter import ACTIVE
from django.shortcuts import render
from .models import *
from Blog.models import Article

# Create your views here.
def index(request):
    context =  {
        "me":Me.objects.last(),
        "services":Service.objects.all(),
        "competences":Competence.objects.all(),
        "educations":Education.objects.all(),
        "catégoriesprojets":CategorieProjet.objects.all(),
        "projets":Projet.objects.all(),
        "articles":Article.objects.filter(status=True).order_by("-created")[:2]


    }
    return render(request, 'index.html', context)