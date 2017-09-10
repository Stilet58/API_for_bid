from django.db import models

#Модель анкеты клиента
class Form(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_change = models.DateTimeField('Дата и время изменения', auto_now=True)
    full_name = models.CharField('ФИО', max_length=250)
    dob = models.DateField('Дата рождения')
    phone_number = models.CharField('Телефон', max_length=50)
    passport = models.CharField('Паспорт', max_length=100)
    scoring_ball = models.IntegerField('Скоринговый балл')

    def __str__(self):
        return str(self.full_name)
