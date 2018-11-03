# Generated by Django 2.1.2 on 2018-11-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anotacao_Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('anotacao', models.TextField()),
                ('parteCorpo', models.CharField(blank=True, max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dados_Musculos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dadosMusculos', models.CharField(max_length=40)),
                ('dia', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Fisioterapeuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpfFisioterapeuta', models.CharField(max_length=20)),
                ('crefito', models.CharField(max_length=15)),
                ('especialidade', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpfPaciente', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('bairro', models.CharField(max_length=40)),
                ('cep', models.CharField(max_length=15)),
                ('cidade', models.CharField(max_length=40)),
                ('uf', models.CharField(blank=True, max_length=2, null=True)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('dataNascimento', models.DateField()),
                ('responsavel', models.CharField(blank=True, max_length=100, null=True)),
                ('cpfResponsavel', models.CharField(blank=True, max_length=20, null=True)),
                ('diagnostico', models.CharField(max_length=200)),
                ('descricaoDiagnostico', models.TextField()),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='paciente_fotos')),
            ],
        ),
    ]
