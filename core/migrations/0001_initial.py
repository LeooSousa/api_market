# Generated by Django 3.0 on 2019-12-04 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_estabelecimento', models.CharField(max_length=50)),
                ('cnpj', models.CharField(blank=True, max_length=13, null=True)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=15, verbose_name='UF')),
                ('bairro', models.CharField(blank=True, max_length=50, null=True)),
                ('endereco', models.CharField(blank=True, max_length=60, null=True)),
                ('numero_residencia', models.CharField(blank=True, max_length=5, null=True)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, null=True, upload_to='Foto_produtos')),
                ('descricao', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Categoria')),
                ('estabelecimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Estabelecimento')),
            ],
        ),
    ]