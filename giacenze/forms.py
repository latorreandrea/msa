from django import forms
from django.forms import ModelForm, Textarea #creare form da modello
# per validare from
from django.core import validators
from django.core.exceptions import ValidationError

# modelli utilizzati
from .models import Pc , Telefono, Periferiche


# Create  widget in forms.py file per implementare un datapiker
class DateInput(forms.DateInput):
    input_type = 'date'


TIPOLOGIA = (
    ("fisso", "fisso"),
    ("portatile", "portalile"),
    ("dismesso", "dismesso"),
)


class FormGiacenzaPC(forms.Form):
    """Form aggiunta pc"""
    seriale = forms.CharField(max_length=50)
    codice_interno = forms.CharField(max_length=50, validators=[validators.MinLengthValidator(3)])
    modello = forms.CharField(max_length=254)
    installazione = forms.DateTimeField(
        input_formats=['%d/%m/%Y'],
        widget=DateInput
    )
    tipologia = forms.ChoiceField(
        required=False,
        widget=forms.Select,
        choices=TIPOLOGIA,
    )

    def clean_contenuto(self):
        """
        convalidiamo il contenuto del form
        controllando che il codice interno del pc non sia gia presente nel database
        """
        codice_interno_registrato = self.cleaned_data['codice_interno']
        seriale_registrato = self.cleaned_data['seriale']
        if seriale_registrato in Pc.objects.filter(seriale=seriale_registrato):
            raise ValidationError("Questo codice seriale è stato già registrato")
        if codice_interno_registrato in Pc.objects.filter(codice_interno=codice_interno_registrato):
            raise ValidationError("Questo codice interno è stato già registrato")
        return codice_interno_registrato


class FormGiacenzaTelefono(ModelForm):
    """form aggiunta telefono"""
    class Meta:
        model = Telefono
        fields = '__all__'
        widgets = {
            'note': Textarea(attrs={'cols': 20, 'rows': 1}),
        }
        def clean_contenuto(self):
            """
            convalidiamo il contenuto del form
            controllando che il codice interno del pc non sia gia presente nel database
            """
            codice_interno_registrato = self.cleaned_data['codice_interno']
            seriale_registrato = self.cleaned_data['seriale']
            if seriale_registrato in Pc.objects.filter(seriale=seriale_registrato):
                raise ValidationError("Questo codice seriale è stato già registrato")
            if codice_interno_registrato in Pc.objects.filter(codice_interno=codice_interno_registrato):
                raise ValidationError("Questo codice interno è stato già registrato")
            return codice_interno_registrato


class FormGiacenzaPeriferiche(ModelForm):
    """form aggiunta telefono"""
    class Meta:
        model = Periferiche
        fields = '__all__'
        