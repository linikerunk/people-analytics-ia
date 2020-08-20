from datetime import datetime
from django.db import models
from django.core import validators
from users.models import Base, Employee

def current_year():
    return datetime.now().year


class Skill(Base):
    name = models.CharField('Nome', max_length=50, unique=True)
    description = models.TextField('Descrição', blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return self.name


class Evaluation(Base):
    valuator = models.ForeignKey(
        Employee,
        verbose_name='Avaliador',
        related_name='valuator_evaluations',
        on_delete=models.PROTECT
    )
    rated = models.ForeignKey(
        Employee,
        verbose_name='Avaliado',
        related_name='rated_evaluations',
        on_delete=models.PROTECT
    )
    year = models.PositiveIntegerField('Ano', default=current_year)
    skills = models.ManyToManyField(
        Skill, through='EvaluationSKill', related_name='evaluations'
    )

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-created']
        unique_together = ['rated', 'year']

    def __str__(self):
        return f'Avaliação de {self.rated} referente ao ano de {self.year}'

    def average(self):
        avg = self.evaluation_skills.aggregate(models.Avg('grade'))
        return avg['grade__avg']
    average.short_description = 'Média'


class EvaluationSkill(Base):
    evaluation = models.ForeignKey(
        Evaluation,
        verbose_name='Avaliação',
        related_name='evaluation_skills',
        on_delete=models.CASCADE
    )
    skill = models.ForeignKey(
        Skill,
        verbose_name='Habilidade',
        related_name='evaluation_skills',
        on_delete=models.CASCADE,
    )
    grade = models.PositiveIntegerField(
        'Nota',
        validators=[
            validators.MinValueValidator(0),
            validators.MaxValueValidator(5)
        ]
    )

    class Meta:
        verbose_name = 'Habilidade'
        verbose_name_plural = 'Habilidades'
        ordering = ['-skill__name']
        unique_together = ['evaluation', 'skill']

    def __str__(self):
        return f'{self.evaluation} | Habildade: {self.skill}, Nota: {self.grade}'
