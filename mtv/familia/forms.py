from django import forms


class PersonaForm(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=100)
    apellido = forms.CharField(label="Apellido", max_length=100)
    email = forms.EmailField(label="Email")
    fecha = forms.DateField(label='Fecha de nacimiento', widget=forms.TextInput(attrs={'type': 'date','class': 'form-control  datetimepicker'}), required=True)
 