import json
from django.shortcuts import render,redirect
from .models import Login, Fisioterapeuta, Paciente, Anotacao_Paciente, Dados_Musculos
from .form import LoginForm, FisioterapeutaForm, PacienteForm, AnotacaoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def Cadastro_Fisioterapeuta(request):
    formFisioterapeuta = FisioterapeutaForm(request.POST or None)

    if formFisioterapeuta.is_valid():
        nome = formFisioterapeuta.cleaned_data['nome']
        cpfFisioterapeuta = formFisioterapeuta.cleaned_data['cpfFisioterapeuta']
        crefito = formFisioterapeuta.cleaned_data['crefito']
        especialidade = formFisioterapeuta.cleaned_data['especialidade']
        email = formFisioterapeuta.cleaned_data['email']
        senha = formFisioterapeuta.cleaned_data['senha']
        formFisioterapeuta.save()
        return redirect('login')

    return render(request, 'kaorawebpages/cadastro.html', {'formFisioterapeuta': formFisioterapeuta})

def Cadastro_Paciente(request):
    formPaciente = PacienteForm(request.POST or None)

    if formPaciente.is_valid():
        nome = formPaciente.cleaned_data['nome']
        cpfPaciente = formPaciente.cleaned_data['cpfPaciente']
        endereco = formPaciente.cleaned_data['endereco']
        bairro = formPaciente.cleaned_data['bairro']
        cep = formPaciente.cleaned_data['cep']
        cidade = formPaciente.cleaned_data['cidade']
        telefone = formPaciente.cleaned_data['telefone']
        celular = formPaciente.cleaned_data['celular']
        email = formPaciente.cleaned_data['email']
        dataNascimento = formPaciente.cleaned_data['dataNascimento']
        responsavel = formPaciente.cleaned_data['responsavel']
        cpfResponsavel = formPaciente.cleaned_data['cpfResponsavel']
        diagnostico = formPaciente.cleaned_data['diagnostico']
        descricaoDiagnostico = formPaciente.cleaned_data['descricaoDiagnostico']
        fotos = formPaciente.cleaned_data['fotos']
        formPaciente.save()
        return redirect('pagina_inicial')

    return render(request, 'kaorawebpages/cadastroPaciente.html', {'formPaciente': formPaciente})

def logar(request):
    formLogin = LoginForm(request.POST or None)
    if formLogin.is_valid():
        email = formLogin.cleaned_data['email']
        senha = formLogin.cleaned_data['senha']
        user = authenticate(username=email, password=senha)
        if user is not None:
            login(request, user)
            formLogin.save()
            return redirect('pagina_inicial')

    return render(request, 'kaorawebpages/login.html', {'formLogin': formLogin})

def home(request):
    return render(request, 'kaorawebpages/home.html')

def Consulta_Paciente(request):
    data = {}
    data['pacientes'] = Paciente.objects.all()
    return render(request, 'kaorawebpages/consultaPaciente.html', data)

def Perfil_Paciente(request, pk):
    #leitura da ficha do paciente
    data = {}
    paciente = Paciente.objects.get(pk=pk)
    formPacientes = PacienteForm(request.POST or None, instance=paciente)
    if formPacientes.is_valid():
        formPacientes.save()
        return redirect('perfil_paciente')

    data['formPacientes'] = formPacientes
    data['paciente'] = paciente

    #leitura das anotacoes do paciente


    #leitura das avaliacoes do paciente
    return render(request, 'kaorawebpages/paciente.html', data)

def Anotacao(request, pk):
    formAnotacao = AnotacaoForm(request.POST or None)
    if formAnotacao.is_valid():
        data = formAnotacao.cleaned_data['data']
        parteCorpo = formAnotacao.cleaned_data['parteCorpo']
        anotacao = formAnotacao.cleaned_data['anotacao']
        formAnotacao.save()
        return redirect('perfil_paciente')

    return render(request, 'kaorawebpages/anotacao.html', {'formAnotacao': formAnotacao})

def Avaliacao(request, pk):
    queryMuscle = Dados_Musculos.objects.all()
    dados_musculos = [obj.dados_musculos for obj in queryMuscle]
    data = [int(obj.data) for obj in queryMuscle]

    context = {
        'dados_musculos': json.dumps(dados_musculos),
        'data': json.dumps(data),
    }

    return render(request, 'kaorawebpages/avaliacao.html', context)

def sair(request):
    logout(request)
    return redirect('login')
