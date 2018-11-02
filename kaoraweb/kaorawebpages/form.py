from django.forms import ModelForm, CharField, PasswordInput, DateInput, widgets, TextInput, Textarea, ImageField   
from .models import Login, Fisioterapeuta, Paciente, Anotacao_Paciente, Dados_Musculos

class LoginForm(ModelForm):
    senha = CharField(widget=PasswordInput())
    class Meta:
        model = Login
        fields = ('email', 'senha')
    
    def save(self, commit=True):
        user = super(LoginForm, self).save(commit=False)
        user.set_password(self.cleaned_data['senha'])
        if commit:
            user.save()

        return user

class FisioterapeutaForm(ModelForm):
    senha = CharField(widget=PasswordInput())
    class Meta:
        model = Fisioterapeuta
        fields = ('nome', 'cpfFisioterapeuta', 'crefito', 'especialidade', 'email', 'senha')
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Escreva seu nome'}),
            'cpfFisioterapeuta': TextInput(attrs={'class':'cpf','placeholder': 'XXX.XXX.XXX-XX'}),
            'crefito': TextInput(attrs={'class':'crefito','placeholder':'XXXXX-F'}),
            'especialidade': TextInput(attrs={'placeholder':'Sua especialidade'}),
            'email': TextInput(attrs={'placeholder':'fisioterapeuta@email.com'}),
            'senha': PasswordInput(attrs={'placeholder': 'Escolha uma senha'})
        }

class PacienteForm(ModelForm):

    class Meta:
        model = Paciente
        fields = ('nome', 'cpfPaciente', 'endereco', 'bairro', 'cep', 'cidade', 'uf', 'telefone', 'celular', 'email', 'dataNascimento', 'responsavel', 'cpfResponsavel', 'diagnostico', 'descricaoDiagnostico', 'fotos')
        widgets = {
            'nome': TextInput(attrs={'placeholder': 'Escreva o nome do seu paciente'}),
            'cpfPaciente': TextInput(attrs={'class':'cpf','placeholder': 'XXX.XXX.XXX-XX'}),
            'endereco': TextInput(attrs={'placeholder': 'Escreva o endereço de seu paciente'}),
            'bairro': TextInput(attrs={'placeholder': 'Escreva o bairro do seu paciente'}),
            'cep': TextInput(attrs={'class':'cep','placeholder': 'xxxxx-xxx'}),
            'cidade': TextInput(attrs={'placeholder': 'Escreva a cidade do seu paciente'}),
            'telefone': TextInput(attrs={'class':'telefone','placeholder':'(xx) xxxx-xxxx'}),
            'celular': TextInput(attrs={'class':'celular','placeholder':'(xx) xxxxx-xxxx'}),
            'email': TextInput(attrs={'placeholder':'paciente@email.com'}),
            'responsavel': TextInput(attrs={'placeholder':'Responsável pelo paciente'}),
            'cpfResponsavel': TextInput(attrs={'class':'cpf','placeholder': 'XXX.XXX.XXX-XX'}),
            'diagnostico': TextInput(attrs={'placeholder': 'Escreva diagnóstico do paciente'}),
            'descricaoDiagnostico': Textarea(attrs={'placeholder': 'Escreva a descrição do diagnóstico'}),
            'dataNascimento': DateInput(attrs={'type': 'date'}),
        }


class AnotacaoForm(ModelForm):
    class Meta:
        model = Anotacao_Paciente
        fields = ('data', 'anotacao', 'parteCorpo')
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
            'anotacao': Textarea(attrs={'placeholder': 'Escreva aqui sua anotação sobre o paciente'}),
            'parteCorpo': TextInput(attrs={'placeholder': 'Digite a parte analisada, ex: Pescoço'}),
        }

class DadosMusculosForm(ModelForm):
    class Meta:
        model = Dados_Musculos
        fields = ('dados_musculos','data','parteAnalisada')
        widgets = {
            'data': DateInput(attrs={'type': 'date'}),
        }