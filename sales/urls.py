from django.urls import path, include

from sales.views import HomeView, PlanStoreListView

app_name = 'sales'

urlpatterns = [
    path('plans/<int:pk>', PlanStoreListView.as_view(), name="plan_stores_list"),
    path('', HomeView.as_view(), name="plans_list"),
]
