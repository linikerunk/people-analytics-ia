from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


PHOTOS_FOLDER = "FotosFuncionarios/"
DEFAULT = '0000.jpg'


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Employee(Base):
    GENDER_CHOICES = (
        ('F', 'Feminino'),
        ('G', 'Masculino'))
    identifier = models.IntegerField("Registro", primary_key=True,
                                     validators=[MaxValueValidator(999999999),
                                                 MinValueValidator(1)])
    name = models.CharField("Nome Funcionário", max_length=130, null=False)
    admission = models.DateTimeField("Admissão")
    resignation = models.DateTimeField("Demissão", null=True)
    birth_date = models.DateTimeField("Data de Aniversário", null=True)
    zip_code = models.CharField('CEP', max_length=10, blank=True)
    email = models.EmailField('Email', max_length=70, blank=True, null=True,
                              error_messages={
                              'required': 'Porfavor digite seu e-mail.',
                              'unique': 'Já existe esse e-mail cadastrado.'})
    phone = models.CharField('Telefone', max_length=15, null=True)
    cpf = models.CharField('CPF', max_length=12, blank=False)
    role = models.CharField('Cargo', max_length=60, blank=False)
    cost_center = models.PositiveIntegerField('CDC', default=0, validators=[
                                              MaxValueValidator(99999),
                                              MinValueValidator(11111)],
                                              blank=False)
    gender = models.CharField('Gênero', max_length=12, choices=GENDER_CHOICES)
    photo = models.ImageField('Fotos Funcionários', max_length=200,
                            upload_to="FotosFuncionarios",  default="0000.jpg")

    def get_photo_url(self):
        path = f'{PHOTOS_FOLDER}/{self.identifier}'

        if default_storage.exists(path):
            return default_storage.open(path).name

        return default_storage.open(f'{PHOTOS_FOLDER}/{DEFAULT}').name

    class Meta:
        verbose_name_plural = "Employees"

    def __str__(self):
        return self.name


class CostCenter(Base):
    number = models.CharField('Centro de Custo', primary_key=True,
                              max_length=50, blank=False)
    name_department = models.CharField('Departamento', max_length=60)
    responsible = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "CostCenter"

    def __str__(self):
        return  self.number
