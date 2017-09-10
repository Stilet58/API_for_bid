from django.db import models
from api_partners.models import Form

#Модель кредитной организации
class Credit_organization(models.Model):
    name = models.CharField('Название', max_length=250)
    phone = models.CharField('Телефон', max_length=50)

    def __str__(self):
        return str(self.name)

#Модель для предложений
class Proposal(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_change = models.DateTimeField('Дата и время изменения', auto_now=True)
    start_date_of_rotation = models.DateTimeField('Дата и время начала ротации')
    end_date_of_rotation = models.DateTimeField('Дата и время окончания ротации')
    name = models.CharField('Название предложения', max_length=250)
    type_of_a_proposal = models.CharField('Тип', max_length=100)
    min_scoring_ball = models.IntegerField('Минимальный скоринговый балл')
    max_scoring_ball = models.IntegerField('Максимальный скоринговый балл')
    credit_organization = models.ForeignKey(Credit_organization, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)


# Модель для выпадающего списка статусов
class Status_bid(models.Model):
    name = models.CharField('Тип статуса заявки', max_length=50)

    def __str__(self):
        return str(self.name)


#Модель заявки в кредитную организацию
class Bid(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_dispatch = models.DateTimeField('Дата и время отправки')
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status_bid, null=True, verbose_name='Статус', on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.status)