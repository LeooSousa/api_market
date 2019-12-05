from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ESTADO_CHOICES = (

        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),

    )


class Categoria(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self):
        return f' {self.tipo}'

class Estabelecimento(models.Model):
    nome_estabelecimento = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=13, null=True, blank=True )
    uf = models.CharField(null=False,verbose_name="UF", choices=ESTADO_CHOICES, max_length=15)
    bairro = models.CharField(max_length=50, null=True, blank=True)
    endereco = models.CharField(max_length=60, blank=True, null=True)
    numero_residencia = models.CharField(max_length=5, null=True, blank=True)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    cep = models.CharField(max_length=50, null=True, blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.nome_estabelecimento}'

class Produto(models.Model):
    foto = models.ImageField(upload_to='Foto_produtos', null=True, blank=True)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estabelecimento = models.ForeignKey(Estabelecimento, on_delete=models.CASCADE)


    def __str__(self):
        return f' {self.descricao} - {self.preco}'
