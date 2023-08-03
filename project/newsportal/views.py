from django.views.generic import ListView, DetailView
from .models import News
from .filters import NewsFilter
from .forms import NewsForm
from django.http import HttpResponse
from django.shortcuts import render


class NewsList(ListView):
    model = News
    ordering = '-date_on'
    template_name = 'default.html'
    context_object_name = 'text'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = NewsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsDetail(DetailView):
    model = News
    template_name = 'onenew.html'
    context_object_name = 'new'


def multiply(request):
   number = request.GET.get('number')
   multiplier = request.GET.get('multiplier')

   try:
       result = int(number) * int(multiplier)
       html = f"<html><body>{number}*{multiplier}={result}</body></html>"
   except (ValueError, TypeError):
       html = f"<html><body>Invalid input.</body></html>"

   return HttpResponse(html)

def create_news(request):
    form = NewsForm()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/news/')

    return render(request, 'news_edit.html', {'form': form})