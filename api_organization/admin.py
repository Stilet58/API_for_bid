from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import *


#Фильтр по минимальным скоринговым баллам
class MinScoringBallListFilter(admin.SimpleListFilter):
    title = _('Минимальный cкоринговый балл')#Название фильтра
    parameter_name = 'before850'

    def lookups(self, request, model_admin):

#Название промежутков для фильтра
        return (
            ('from_0', _('От 0 и выше')),
            ('from_100', _('От 100 и выше')),
            ('from_200', _('От 200 и выше')),
            ('from_300', _('От 300 и выше')),
            ('from_400', _('От 400 и выше')),
            ('from_500', _('От 500 и выше')),
            ('from_600', _('От 600 и выше')),
            ('from_700', _('От 700 и выше')),
        )

#Возврат отфильтрованных данных
    def queryset(self, request, queryset):
        if self.value() == 'from_0':
            return queryset.filter(min_scoring_ball__gte=0,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_100':
            return queryset.filter(min_scoring_ball__gte=100,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_200':
            return queryset.filter(min_scoring_ball__gte=200,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_300':
            return queryset.filter(min_scoring_ball__gte=300,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_400':
            return queryset.filter(min_scoring_ball__gte=400,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_500':
            return queryset.filter(min_scoring_ball__gte=500,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_600':
            return queryset.filter(min_scoring_ball__gte=600,
                                   min_scoring_ball__lte=850)
        if self.value() == 'from_700':
            return queryset.filter(min_scoring_ball__gte=700,
                                   min_scoring_ball__lte=850)


class CreditOrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone',  'date_of_change', 'date_of_creation') #Сортировка отображения на странице
    date_hierarchy = 'date_of_creation'  # Иерархический фильтр по дате создания
    list_filter = ['date_of_change'] #Фильтр по дате изменения
    search_fields = ['name', 'phone'] #Текстовый поиск


class ProposalAdmin(admin.ModelAdmin):
    list_display = ('name', 'type_of_a_proposal', 'start_date_of_rotation','end_date_of_rotation', 'min_scoring_ball',
                     'max_scoring_ball', 'credit_organization', 'date_of_change', 'date_of_creation') #Сортировка отображения на странице
    date_hierarchy = 'date_of_creation' #Иерархический фильтр по дате создания
    list_filter = ['date_of_change', 'credit_organization', MinScoringBallListFilter] #Фильтры по дате изменения и минимальному скоринговому баллу
    search_fields = ['name', 'type_of_a_proposal', 'credit_organization'] #Текстовый поиск


class BidAdmin(admin.ModelAdmin):
    list_display = ('form', 'proposal', 'status', 'date_of_dispatch', 'date_of_creation') #Сортировка отображения на странице
    date_hierarchy = 'date_of_creation' #Иерархический фильтр по дате создания
    list_filter = ['date_of_dispatch', 'status'] #Фильтры по дате отправки и статусу
    search_fields = ['form', 'proposal', 'credit_organization'] #Текстовый поиск


admin.site.register(Credit_organization, CreditOrganizationAdmin)
admin.site.register(Proposal, ProposalAdmin)
admin.site.register(Bid, BidAdmin)

