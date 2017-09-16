from django.db import models


# Подтверждение телефона
STATUS_CHOICES = (
    ('Yes', 'Да'),
    ('No', 'Нет'),
)


# Модель анкеты клиента
class Form(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_change = models.DateTimeField('Дата и время изменения', auto_now=True)
    surname = models.CharField('Фамилия', max_length=200, default='')
    first_name = models.CharField('Имя', max_length=200, default='')
    last_name = models.CharField('Отчество', max_length=200, default='')
    dob = models.DateField('Дата рождения')
    phone_number = models.CharField('Телефон', max_length=50)
    phone_confirmation = models.CharField('Телефон подтвержден', max_length=5, choices=STATUS_CHOICES, default='Нет')
    passport = models.CharField('Паспорт', max_length=100)
    scoring_ball = models.IntegerField('Скоринговый балл', blank=True, null=True)

    class Meta:
        verbose_name = 'Анкета клиента'
        verbose_name_plural = 'Анкеты клиента'

    def __str__(self):
        return self.surname + ' ' + self.first_name + ' ' + self.last_name
