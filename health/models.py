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
    classification_text =  models.CharField(max_length=28, choices=IMC,
                                    blank=True, verbose_name="Classificação IMC")
    imc = models.DecimalField(max_digits=5, decimal_places=2, null=True,
                                    blank=True, verbose_name="IMC")

    class Meta:
        verbose_name = "Indice de Massa Corporal"
        verbose_name_plural = "Indice de Massa Corporal"

    def __str__(self):
        return self.identifier.name

    def save(self, *args, **kwargs):
        self.imc = (self.weight / self.height**2)
        if self.imc < 16:
            self.classification_text = "Magreza grave"
        elif self.imc < 17:
            self.classification_text = "Magreza moderada"
        elif self.imc < 18.5:
            self.classification_text = "Magreza leve"
        elif self.imc < 25:
            self.classification_text = "Saudável"
        elif self.imc < 30:
            self.classification_text = "Sobrepeso"
        elif self.imc < 35:
            self.classification_text = "Obesidade Grau I"
        elif self.imc < 40:
            self.classification_text = "Obesidade Grau II (severa)"
        elif self.imc > 40:
            self.classification_text = "Obesidade Grau III (mórbida)"

        if self.systolic_blood_pressure <= 120 and self.diastolic_blood_pressure <= 80:
            self.classification = "Verde"
        elif self.systolic_blood_pressure <= 120 and self.diastolic_blood_pressure > 80:
            self.classification = "Amarelo"
        elif self.systolic_blood_pressure <= 139 and self.diastolic_blood_pressure <= 89:
            self.classification = "Amarelo"
        elif self.systolic_blood_pressure <= 139 and self.diastolic_blood_pressure > 89:
            self.classification = "Laranja"
        elif self.systolic_blood_pressure <= 159 and self.diastolic_blood_pressure <= 99:
            self.classification = "Laranja"
        elif self.systolic_blood_pressure <= 159 and self.diastolic_blood_pressure > 99:
            self.classification = "Vermelho"
        elif self.systolic_blood_pressure >= 160 and self.diastolic_blood_pressure >= 100:
            self.classification = "Vermelho"
        return super().save(*args, **kwargs) 