from email.mime import image
from http.client import PRECONDITION_FAILED
from django.db import models
from autoslug import AutoSlugField

# Create your models here.


class CategorieArticle(models.Model):
    """Model definition for CategorieArticle."""
    titre = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for CategorieArticle."""

        verbose_name = 'CategorieArticle'
        verbose_name_plural = 'CategorieArticles'

    def __str__(self):
        """Unicode representation of CategorieArticle."""
        return self.titre
    


    def get_absolute_url(self):
        """Return absolute url for CategorieArticle."""
        return ('')

    @property
    def categoriearticles(self):
        return self.news.all().count()

    # TODO: Define custom methods here

class Article(models.Model):
    categorie = models.ForeignKey(CategorieArticle, on_delete=models.CASCADE, related_name="news")
    titre = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    section1 = models.CharField(max_length=300)
    image2 = models.CharField(max_length=50)
    section2 = models.CharField(max_length=300)
    section3 = models.CharField(max_length=300)
    accroche = models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    slug = AutoSlugField(populate_from='titre')
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        return self.titre


    def get_absolute_url(self):
        """Return absolute url for Article."""
        return ('')
    @property
    def commentaire(self):
        return self.cmts.all().count()

    @property
    def commentaires(self):
        return self.cmts.order_by("-created")

    # TODO: Define custom methods here

class Commentaire(models.Model):
    """Model definition for Commentaire."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='cmts')
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    commentaire = models.CharField(max_length=50)
    FIELDNAME = models.DateField()
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.nom
        pass


    def get_absolute_url(self):
        """Return absolute url for Commentaire."""
        return ('')

    # TODO: Define custom methods here

