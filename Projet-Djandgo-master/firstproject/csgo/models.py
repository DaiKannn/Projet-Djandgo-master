from django.db import models


class CSGO(models.Model):
    Nom_du_Major = models.CharField(max_length=100)
    Lieu = models.CharField(max_length=100)
    date_debut = models.DateField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    nombres_equipes = models.IntegerField(blank=False)
    resultat = models.TextField(null=True, blank=True)

    def __str__(self):
        chaine = f" Voici le major{self.Nom_du_Major} qui a eu lieu {self.Lieu} entre le {self.date_debut} {self.date_fin} vec {self.nombres_equipes} et le resultat {self.resultat}"
        return chaine

    def dico(self):
        return {"Nom_du_Major": self.Nom_du_Major, "Lieu": self.Lieu, "date_debut": self.date_debut, "date_fin": self.date_fin,
                "nombres_equipes": self.nombres_equipes, "resultat": self.resultat}


class Major(models.Model):
    Horaire = models.CharField(max_length=100)
    Equipe = models.CharField(max_length=100)
    Score = models.IntegerField(blank=True, null=True)
    Stats = models.IntegerField(blank=False)

    def __str__(self):
        chaine = f"{self.Horaire} opposant {self.Equipe} le resultat {self.Score} voici les stats des joueurs {self.Stats}"
        return chaine

    def dico(self):
        return {"Horaire": self.Horaire, "Equipe": self.Equipe, "Score": self.Score,
                "Stats": self.Stats}