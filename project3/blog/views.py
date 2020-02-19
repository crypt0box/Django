from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.views import generic
from .models import Post, Category


class IndexView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        queryset = Post.objects.order_by('-created_at') # 昇順の場合-を付けない
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(text__icontains=keyword)
            )
        return queryset


class CategoryView(generic.ListView):
    model = Post
    paginate_by = 10

    def get_queryset(self):
        """
        category = get_object_or_404(Category, pk=self.kwargs['pk'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        """
        category_pk = self.kwargs['pk']
        queryset = Post.objects.order_by('-created_at').filter(category__pk=category_pk)
        return queryset
