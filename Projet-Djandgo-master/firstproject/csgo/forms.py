from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class CSGOForm(ModelForm):
    class Meta:
        model = models.CSGO
        fields = ('Nom_du_Major', 'Lieu', 'date_debut', 'date_fin', 'nombres_equipes','resultat')
        labels = {
            'Nom_du_Major' : _('Major'),
            'Lieu' : _('Lieu') ,
            'date_debut' : _('date_debut'),
            'date_fin': _('date_fin'),
            'nombres_equipes' : _('nombres␣equipes'),
            'resultat' : _('Resultat'),
        }

class MajorForm(ModelForm):
    class Meta:
        model = models.Major
        fields = ('Horaire', 'Equipe','Score', 'Stats')
        labels = {
            'Horaire': _('Horaire'),
            'Equipe': _('Equipe'),
            'Score': _('Score'),
            'Stats': _('Stats'),
        }
class CSGOInstantForm(ModelForm):
    class Meta:
        model = models.CSGO
        fields = ('Nom_du_Major', 'Lieu', 'date_debut', 'date_fin', 'nombres_equipes', 'resultat')
        labels = {
            'Nom_du_Major': _('Major'),
            'Lieu': _('Lieu'),
            'date_debut': _('Date_debut'),
            'date_fin': _('Date_fin'),
            'nombres_equipes': _('Nombres␣equipes'),
            'resultat': _('Resultat'),
        }
