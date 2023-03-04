from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import New, Category
from .forms import ContactForm


def news_list(request):
    # news_list = New.objects.all()
    # news_list = New.objects.filter(status=New.Status.Published)
    news_list = New.published.all()

    context = {
        "news_list": news_list
    }
    return render(request, 'news/news_list.html', context)


def news_detail(request, news):
    news = get_object_or_404(New, slug=news, status=New.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news/news_detail.html', context)


def homePageView(request):
    news_list = New.published.all().order_by('-publish_time')[:5]
    categories = Category.objects.all()
    local_one = New.published.filter(category__name='mahalliy').order_by('-publish_time')[:1]
    local_news = New.published.filter(category__name='mahalliy').order_by('-publish_time')[1:6]
    context = {
        'news_list': news_list,
        'categories': categories,
        'local_news': local_news,
        'local_one': local_one
    }
    return render(request, 'news/home.html', context)

class HomePageView(ListView):
    model = New
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = New.published.all().order_by('-publish_time')[:5]
        context['local_news'] = New.published.filter(category__name='mahalliy').order_by('-publish_time')[:5]
        context['sport_news'] = New.published.filter(category__name='sport').order_by('-publish_time')[:5]
        context['technology_news'] = New.published.filter(category__name='texnologiya').order_by('-publish_time')[:5]
        context['foreign_news'] = New.published.filter(category__name='xorij').order_by('-publish_time')[:5]

        return context
# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningiz uchun tashakkur")
#     context = {
#         'form': form
#     }
#
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactPageView()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>biz bilan bog\'langaningiz tashakkur')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)


def error404PageView(request):
    context = {

    }
    return render(request, 'news/404.html', context)


def aboutPageView(request):
    context = {

    }
    return render(request, 'news/about.html', context)
