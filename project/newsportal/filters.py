from django_filters import FilterSet
from .models import News


class NewsFilter(FilterSet):
   class Meta:
       model = News
       fields = {
           'name': ['icontains'],
           'date_on': ['gt'],
       }