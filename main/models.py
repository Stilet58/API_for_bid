from django.db import models

#Модель кредитной организации
class Credit_organization(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Название', max_length=250)
    phone = models.CharField('Телефон', max_length=50)



#Модель для предложений
class Proposal(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_creation = models.DateTimeField('Дата и время создания')
    date_of_change = models.DateTimeField('Дата и время изменения')
    start_date_of_rotation = models.DateTimeField('Дата и время начала ротации')
    end_date_of_rotation = models.DateTimeField('Дата и время окончания ротации')
    name = models.CharField('Название предложения', max_length=250)
    type_of_a_proposal = models.CharField('Тип', max_length=100)
    min_scoring_ball = models.IntegerField('Минимальный скоринговый балл')
    max_scoring_ball = models.IntegerField('Максимальный скоринговый балл')
    credit_organization = models.ForeignKey(Credit_organization)


#Модель анкеты клиента
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_creation = models.DateTimeField('Дата и время создания')
    date_of_change = models.DateTimeField('Дата и время изменения')
    full_name = models.CharField('ФИО', max_length=250)
    dob = models.DateField('Дата рождения')
    phone_number = models.CharField('Телефон', max_length=50)
    passport = models.CharField('Паспорт', max_length=100)
    scoring_ball = models.IntegerField('Скоринговый балл')


#Модель заявки в кредитную организацию
class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    date_of_creation = models.DateTimeField('Дата и время создания')
    date_of_dispatch = models.DateTimeField('Дата и время отправки')
    form = models.ForeignKey(Form)
    proposal = models.ForeignKey(Proposal)
    status = models.CharField('Статус', max_length=100)
