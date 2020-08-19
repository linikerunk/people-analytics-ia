from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

from django.utils.timezone import now

from users.models import Base, Employee

CLASSIFICATION = (("Verde", "Verde"), ("Amarelo", "Amarelo"),
                  ("Vermelho", "Vermelho"), ("Azul", "Azul"),)
IMC = (("Magreza grave", "Magreza grave"), 
        ("Magreza moderada", "Magreza moderada"),
        ("Magreza leve", "Magreza leve"), ("Saudável", "Saudável"),
        ("Sobrepeso", "Sobrepeso"), ("Obesidade Grau I", "Obesidade Grau I"),
        ("Obesidade Grau II (severa)", "Obesidade Grau II (severa)"),
        ("Obesidade Grau III (mórbida)", "Obesidade Grau III (mórbida)"),)


class BodyMassIndex(Base):
    identifier = models.ForeignKey(Employee, verbose_name="RE Funcionário", 
                                    unique=False, on_delete=models.PROTECT)
    weighing_date = models.DateTimeField(default=datetime.now, editable=False,
                                    verbose_name="Data de Pesagem")
    weight = models.DecimalField(max_digits=5, decimal_places=2,
                                    verbose_name="Peso")
    height = models.DecimalField(max_digits=5, decimal_places=2,
                                    verbose_name="Altura") 
    abdominal_circumference = models.DecimalField(max_digits=5,
                                    decimal_places=2, null=True, blank=True,
                                    verbose_name="Circunferência Abdominal(cm)")
    systolic_blood_pressure = models.DecimalField(max_digits=5,
                                    decimal_places=2, null=True, blank=True,
                                    verbose_name="Pressão Arterial Sistólica")
    diastolic_blood_pressure = models.DecimalField(max_digits=5,
                                    decimal_places=2, null=True, blank=True,
                                    verbose_name="Pressão Arterial Diastólica")   
    classification =  models.CharField(max_length=8, choices=CLASSIFICATION,
                                    null=True, blank=True,
                                    verbose_name=" Classificação ")
    imc =  models.CharField(max_length=28, choices=IMC, null=True,
                                    verbose_name=" Classificação IMC")

    def __str__(self):
        return self.identifier

    def save(self, *args, **kwargs):
        pass 