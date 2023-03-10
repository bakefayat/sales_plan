from django.urls import path, include

from sales.views import HomeView

app_name = 'sales'

urlpatterns = [
    path('', HomeView.as_view(), name="plans_list"),
]