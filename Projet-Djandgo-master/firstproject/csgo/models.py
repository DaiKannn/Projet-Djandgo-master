from django.db import models


class CSGO(models.Model):
    Nom_du_Major = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    bibliotheque = models.ForeignKey("Major", on_delete=models.CASCADE, null=True)
    nombres_pages = models.IntegerField(blank=False)
    resume = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f"{self.Nom_du_Major} écrit par {self.auteur} édité le {self.date_parution}"
        return chaine

    def dico(self):
        return {"Nom_du_Major": self.Nom_du_Major, "auteur": self.auteur, "date_parution": self.date_parution,
                "nombres_pages": self.nombres_pages, "resume": self.resume}


class Major(models.Model):
    Universite = models.CharField(max_length=100)
    Region = models.CharField(max_length=100)
    Departement = models.IntegerField(blank=True, null=True)
    nombres_de_livres = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.Universite} Dans l'université de {self.Region} Dans la région  {self.Departement}"
        return chaine

    def dico(self):
        return {"Universite": self.Universite, "Region": self.Region, "Departement": self.Departement,
                "nombres_de_livres": self.nombres_de_livres}