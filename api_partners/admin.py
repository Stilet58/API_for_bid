from django.contrib import admin
from datetime import date
from django.utils.translation import ugettext_lazy as _
from .models import Form

#Фильтр по десятилетиям рождения
class DOBListFilter(admin.SimpleListFilter):
    title = _('Год рождения')#Название фильтра
    parameter_name = 'decade'

    def lookups(self, request, model_admin):

#Название десятилетий для фильтра
        return (
            ('30s', _('30-е')),
            ('40s', _('40-е')),
            ('50s', _('50-е')),
            ('60s', _('60-е')),
            ('70s', _('70-е')),
            ('80s', _('80-е')),
            ('90s', _('90-е')),
            ('00s', _('00-е')),
        )

#Возврат отфильтрованных данных
    def queryset(self, request, queryset):
        if self.value() == '30s':
            return queryset.filter(dob__gte=date(1930, 1, 1),
                                   dob__lte=date(1939, 12, 31))
        if self.value() == '40s':
            return queryset.filter(dob__gte=date(1940, 1, 1),
                                   dob__lte=date(1949, 12, 31))
        if self.value() == '50s':
            return queryset.filter(dob__gte=date(1950, 1, 1),
                                   dob__lte=date(1959, 12, 31))
        if self.value() == '60s':
            return queryset.filter(dob__gte=date(1960, 1, 1),
                                   dob__lte=date(1969, 12, 31))
        if self.value() == '70s':
            return queryset.filter(dob__gte=date(1970, 1, 1),
                                   dob__lte=date(1979, 12, 31))
        if self.value() == '80s':
            return queryset.filter(dob__gte=date(1980, 1, 1),
                                   dob__lte=date(1989, 12, 31))
        if self.value() == '90s':
            return queryset.filter(dob__gte=date(1990, 1, 1),
                                   dob__lte=date(1999, 12, 31))
        if self.value() == '00s':
            return queryset.filter(dob__gte=date(2000, 1, 1),
                                   dob__lte=date(2010, 12, 31))


#Фильтр по скоринговым баллам
class ScoringBallListFilter(admin.SimpleListFilter):
    title = _('Скоринговый балл')#Название фильтра
    parameter_name = 'hundreds'

    def lookups(self, request, model_admin):

#Название промежутков для фильтра
        return (
            ('before_100', _('0-100')),
            ('before_200', _('100-200')),
            ('before_300', _('200-300')),
            ('before_400', _('300-400')),
            ('before_500', _('400-500')),
            ('before_600', _('500-600')),
            ('before_700', _('600-700')),
            ('before_850', _('700-850')),
        )

#Возврат отфильтрованных данных
    def queryset(self, request, queryset):
        if self.value() == 'before_100':
            return queryset.filter(scoring_ball__gte=0,
                                   scoring_ball__lte=99)
        if self.value() == 'before_200':
            return queryset.filter(scoring_ball__gte=100,
                                   scoring_ball__lte=199)
        if self.value() == 'before_300':
            return queryset.filter(scoring_ball__gte=200,
                                   scoring_ball__lte=299)
        if self.value() == 'before_400':
            return queryset.filter(scoring_ball__gte=300,
                                   scoring_ball__lte=399)
        if self.value() == 'before_500':
            return queryset.filter(scoring_ball__gte=400,
                                   scoring_ball__lte=499)
        if self.value() == 'before_600':
            return queryset.filter(scoring_ball__gte=500,
                                   scoring_ball__lte=599)
        if self.value() == 'before_700':
            return queryset.filter(scoring_ball__gte=600,
                                   scoring_ball__lte=699)
        if self.value() == 'before_850':
            return queryset.filter(scoring_ball__gte=700,
                                   scoring_ball__lte=850)

class FormAdmin(admin.ModelAdmin):
    list_display = ('surname', 'first_name', 'last_name', 'dob',
                    'phone_number', 'phone_confirmation', 'passport', 'scoring_ball', 'date_of_change', 'date_of_creation') #Сортировка отображения на странице
    list_display_links = ('surname', 'first_name', 'last_name')
    list_filter = ['date_of_change', DOBListFilter, ScoringBallListFilter] #Фильтр по дате изменения, дате рождения и скоринговому баллу
    date_hierarchy = 'date_of_creation' #Иерархический фильтр по дате создания
    search_fields = ['surname', 'first_name', 'last_name', 'phone_number', 'scoring_ball'] #Текстовый поиск

admin.site.register(Form, FormAdmin)
