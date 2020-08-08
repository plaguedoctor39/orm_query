from django.views.generic import ListView
from django.shortcuts import render

from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'


    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'
    object_list = Article.objects.defer('genre__name', 'author__phone', 'author__name', 'author_id', 'genre_id', 'author', 'genre').order_by(ordering)
    print(object_list)
    context = {'object_list': object_list}

    return render(request, template_name, context)
