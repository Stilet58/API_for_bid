from django.db import models
from api_partners.models import Form


#Модель кредитной организации
class Credit_organization(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_change = models.DateTimeField('Дата и время изменения', auto_now=True)
    name = models.CharField('Название', max_length=250)
    phone = models.CharField('Телефон', max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = 'Кредитная организация'
        verbose_name_plural = 'Кредитные организации'

    def __str__(self):
        return str(self.name)


#Модель для предложений
class Proposal(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    date_of_change = models.DateTimeField('Дата и время изменения', auto_now=True)
    name = models.CharField('Название предложения', max_length=250)
    type_of_a_proposal = models.CharField('Тип', max_length=100)
    min_scoring_ball = models.IntegerField('Минимальный скоринговый балл')
    max_scoring_ball = models.IntegerField('Максимальный скоринговый балл')
    start_date_of_rotation = models.DateTimeField('Дата и время начала ротации', blank=True, null=True)
    end_date_of_rotation = models.DateTimeField('Дата и время окончания ротации', blank=True, null=True)
    credit_organization = models.ForeignKey(Credit_organization, verbose_name='Кредитная организация',
                                            on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'

    def __str__(self):
        return self.name


#Типы статуса для заявок
STATUS_CHOICES = (
    ('new', 'Новая'),
    ('sent', 'Отправлена'),
    ('recieved', 'Получена'),
)


#Модель заявки в кредитную организацию
class Bid(models.Model):
    date_of_creation = models.DateTimeField('Дата и время создания', auto_now_add=True)
    form = models.ForeignKey(Form, verbose_name='Анкета', on_delete=models.CASCADE)
    proposal = models.ForeignKey(Proposal, verbose_name='Предложение', on_delete=models.SET_NULL, null=True)
    status = models.CharField('Статус', max_length=50, choices=STATUS_CHOICES, default='Новая')
    date_of_dispatch = models.DateTimeField('Дата и время отправки', blank=True, null=True)


    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.status