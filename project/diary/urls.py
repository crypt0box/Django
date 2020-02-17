from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),    # /diary
    # path('add/', views.AddView.as_view(), name='add'),    # /diary/add
    # path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),  # /diary/update/n(ex:1,2,...)
    # path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),  # /diary/delete/n
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'),  # /diary/detail/n
]
