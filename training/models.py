from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Base(models.Model):
    created = models.DateField('Criação', auto_now_add=True)
    modified = models.DateField('Atualização', auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Training(Base):
    training_name = models.CharField('Nome Treinamento', max_length=100)
    category = models.CharField('Categoria', max_length=25)
    content = models.TextField('Conteúdo')
    required = models.CharField('Requisito', max_length=50)
    resource = models.CharField('Recursos', max_length=50)
    training_type = models.CharField('Tipo de Treinamento', max_length=50)
    local = models.CharField('Local', max_length=50)
    workload = models.IntegerField('Carga Horária')

    def __str__(self):
        return self.training_name


class Entity(Base):
    entity_name = models.CharField('Nome da Entidade', max_length=100)
    social_reason = models.CharField('Razão Social', max_length=100)
    cnpj = models.CharField('CNPJ', max_length=100)
    sap_code = models.CharField('Código SAP', max_length=100)
    contact_person = models.CharField('Pessoa Responsável', max_length=30)
    phone = models.PositiveIntegerField('Telefone', null=True, blank=True)
    zip_code = models.CharField('CEP', max_length=10)
    address = models.CharField('Endereço', max_length=60)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField('Estado', default="XX", max_length=2)
    email = models.EmailField(max_length=70, blank=False, unique=True,
                              verbose_name=u'Email', error_messages={
                              'required': 'Porfavor digite seu e-mail.',
                              'unique': 'Já existe esse e-mail cadastrado.'},)

    def __str__(self):
        return ' %s ' % f"Nome Entidade : {self.entity_name}   | \
        CNPJ : {self.cnpj}"


class Instructor(Base):
    registro_instrutor = models.IntegerField('Registro Instrutor',
                                             primary_key=True, validators=[
                                             MaxValueValidator(9999999999),
                                             MinValueValidator(0000000000)])
    instructor_name = models.CharField('Nome Instrutor', max_length=100)
    instructor_photo = models.ImageField(upload_to='photos_instructor',
                                         null=True, blank=True,
                                         verbose_name=u'Foto do Instrutor')
    # training = models.ManyToManyField(Training, 'Treinamento Habilitado')

    def __str__(self):
        return ' %s ' % f"Registro : {self.registro_instrutor} "


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_name = models.CharField('Nome do Evento', max_length=80)
    value = models.DecimalField('Valor', max_digits=8, decimal_places=2,
                                default=0)
    event_date = models.DateTimeField('Data Consulta', blank=True)
    present_list = models.FileField('Lista de Presença',
                                    upload_to="present_list", default="")
    # training = models.ForeignKey(
    #    Training, 'Treinamento', blank=True, on_delete=models.CASCADE)
    # entity = models.ForeignKey(
    #    Entity, 'Entidade', blank=True, on_delete=models.CASCADE)
    # instructor = models.ForeignKey(
    #    Instructor, 'Instrutor', blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return  ' %s ' % f"{self.event_name}"
