from django.db import models

# Create your models here.
class Me(models.Model):
    """Model definition for Me."""
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    date_naissance = models.DateField( auto_now=False, auto_now_add=False)
    biographie = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    freelance = models.CharField(max_length=50)
    lien_cv = models.CharField(max_length=50)
    photo = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    telephone1 = models.CharField(max_length=10)
    telephone2 = models.CharField(max_length=10)
    email1 = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)


    # TODO: Define fields here

    class Meta:
        """Meta definition for Me."""

        verbose_name = 'Me'
        verbose_name_plural = 'Mes'

    def __str__(self):
        """Unicode representation of Me."""
        return self.nom
        


    def get_absolute_url(self):
        """Return absolute url for Me."""
        return ('')

    # TODO: Define custom methods here

class Service(models.Model):
    """Model definition for Service."""
    image = models.CharField(max_length=50)
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Service."""

        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        """Unicode representation of Service."""
        return self.titre
        


    def get_absolute_url(self):
        """Return absolute url for Service."""
        return ('')

    # TODO: Define custom methods here


class Competence(models.Model):
    """Model definition for Competence."""
    activités = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Competence."""

        verbose_name = 'Competence'
        verbose_name_plural = 'Competences'

    def __str__(self):
        """Unicode representation of Competence."""
        return self.activités


    def get_absolute_url(self):
        """Return absolute url for Competence."""
        return ('')

    # TODO: Define custom methods here


class Education(models.Model):
    """Model definition for Education."""
    etablissement = models.CharField(max_length=50)
    debut_fin = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Education."""

        verbose_name = 'Education'
        verbose_name_plural = 'Educations'

    def __str__(self):
        """Unicode representation of Education."""
        return self.description

    def get_absolute_url(self):
        """Return absolute url for Education."""
        return ('')

    # TODO: Define custom methods here

class CategorieProjet(models.Model):
    """Model definition for CategorieProjet."""
    titre = models.CharField(max_length=50)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for CategorieProjet."""

        verbose_name = 'CategorieProjet'
        verbose_name_plural = 'CategorieProjets'

    def __str__(self):
        """Unicode representation of CategorieProjet."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for CategorieProjet."""
        return ('')

    # TODO: Define custom methods here


class Projet(models.Model):
    """Model definition for Projet."""
    titre = models.CharField(max_length=50)
    categorie = models.ForeignKey(CategorieProjet, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Projet."""

        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        """Unicode representation of Projet."""
        return self.titre

    def get_absolute_url(self):
        """Return absolute url for Projet."""
        return ('')

    # TODO: Define custom methods here
