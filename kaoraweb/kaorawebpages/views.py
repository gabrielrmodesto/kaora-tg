import json
import datetime
import time
from django.shortcuts import render,redirect
from .models import Login, Fisioterapeuta, Paciente, Anotacao_Paciente, Dados_Musculos
from .form import LoginForm, FisioterapeutaForm, PacienteForm, AnotacaoForm, DadosMusculosForm
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
    paciente = Paciente.objects.get(pk=pk)

    #leitura das anotações
    anotacoes = Anotacao_Paciente.objects.all()
    
    #leitura das avaliacoes do paciente
    queryMuscle = Dados_Musculos.objects.all()
    dadosMusculos = [int(obj.dadosMusculos) for obj in queryMuscle]
    dia = [obj.dia for obj in queryMuscle]
    context = {
        'dadosMusculos': json.dumps(dadosMusculos),
        'dia': json.dumps(dia, default=myconverter),
        'paciente': paciente,
        'anotacoes': anotacoes,
    }

    return render(request, 'kaorawebpages/paciente.html', context)

def Anotacao(request, pk):
    dados = {}
    paciente = Paciente.objects.get(pk=pk)
    formAnotacao = AnotacaoForm(request.POST or None)
    if formAnotacao.is_valid():
        data = formAnotacao.cleaned_data['data']
        parteCorpo = formAnotacao.cleaned_data['parteCorpo']
        anotacao = formAnotacao.cleaned_data['anotacao']
        formAnotacao.save()
        return redirect('consulta_paciente')

    dados['formAnotacao'] = formAnotacao
    dados['paciente'] = paciente
    return render(request, 'kaorawebpages/anotacao.html', dados)

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

def items():
    queryMuscle = Dados_Musculos.objects.all()
    items = {'charts': {'dadosMusculos': [], 'dia': []}}
    for item in queryMuscle:
        dia = int(time.mktime(item.dia.timetuple())*1000)
        items['charts']['dadosMusculos'].append([dia, item.dadosMusculos])
    return json.dumps(items)

def Avaliacao(request):
    # queryMuscle = Dados_Musculos.objects.all()
    # dadosMusculos = [int(obj.dadosMusculos) for obj in queryMuscle]
    #dia = [obj.dia for obj in queryMuscle]
    #paciente = Paciente.objects.get(pk=pk)
    # context = {
    #     'dadosMusculos': json.dumps(dadosMusculos),
    #     'dia': json.dumps(dia, default=myconverter),
    # }

    return render(request, 'kaorawebpages/avaliacao.html', {'queryMuscle': items()})

def Atualiza_Paciente(request, pk):
    data = {}
    paciente = Paciente.objects.get(pk=pk)
    formPaciente = PacienteForm(request.POST or None, instance=paciente)

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
        return redirect('consulta_paciente')

    data['formPaciente'] = formPaciente
    data['paciente'] = paciente
    return render(request, 'kaorawebpages/cadastroPaciente.html', data)

def Remover_Paciente(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    paciente.delete()
    return redirect('consulta_paciente')

def Atualizar_Anotacao(request, pk):
    dados = {}
    anotacoes = Anotacao_Paciente.objects.get(pk=pk)
    formAnotacao = AnotacaoForm(request.POST or None, instance=anotacoes)
    if formAnotacao.is_valid():
        data = formAnotacao.cleaned_data['data']
        parteCorpo = formAnotacao.cleaned_data['parteCorpo']
        anotacao = formAnotacao.cleaned_data['anotacao']
        formAnotacao.save()
        return redirect('consulta_paciente')

    dados['formAnotacao'] = formAnotacao
    dados['anotacoes'] = anotacoes
    return render(request, 'kaorawebpages/atualiza_anotacao.html', dados)

def Remover_Anotacao(request, pk):
    anotacao = Anotacao_Paciente.objects.get(pk=pk)
    anotacao.delete()
    return redirect('consulta_paciente')

def Termos(request):
    return render(request, 'kaorawebpages/termos.html')

def Como_Funciona(request):
    return render(request, 'kaorawebpages/funciona.html')

def sair(request):
    logout(request)
    return redirect('login')
