from django.db import models
from codetributhon.behaviors import Timestampable


class Organization(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Organizations'

    name = models.CharField(
            verbose_name='Nom',
            max_length=255
    )

    enabled = models.BooleanField(
            verbose_name='Activer',
            null=False,
            blank=False,
            default=False
    )

    url = models.URLField(
            verbose_name='URL',
            max_length=255,
            blank=True
    )

    def __str__(self):
        return self.name


class Project(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Projets'

    name = models.CharField(
            verbose_name='Nom du projet',
            max_length=255,
            blank=False,
            null=False
    )

    description = models.TextField(
            verbose_name='Description du projet'
    )

    enabled = models.BooleanField(
        verbose_name='Activer',
        null=False,
        blank=False,
        default=False
    )

    logo = models.ImageField(
            upload_to="avatars_projects",
            verbose_name='Logo',
            blank=True
    )

    nb_contrib = 0

    organization = models.ForeignKey(
            Organization,
            verbose_name='Organization',
            related_name='projects'
    )

    def __str__(self):
        return self.name


class Contribution(Timestampable, models.Model):
    class Meta:
        verbose_name_plural = 'Contributions'

    username = models.CharField(
            verbose_name="Nom d'utilisateur",
            max_length=50,
    )

    email = models.EmailField(
            verbose_name='Courriel',
    )

    project = models.ForeignKey(
            Project,
            verbose_name='Project',
            related_name='contributions',
    )

    url = models.URLField(
            verbose_name='URL',
            max_length=255
    )

    description = models.TextField(
            verbose_name='Description du projet'
    )

    enabled = models.BooleanField(
        verbose_name='Valider',
        null=False,
        blank=False,
        default=False,

    )

    def __str__(self):
        return self.username

