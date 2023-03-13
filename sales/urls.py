from django.urls import path, include

from sales.views import HomeView, PlanStoreDetailView, SellCreate

app_name = 'sales'

urlpatterns = [
    path('plans/<int:pk>', PlanStoreDetailView.as_view(), name="plan_stores_list"),
    path('plans/<int:pk>/create', SellCreate.as_view(), name="sell_create"),
    path('', HomeView.as_view(), name="plans_list"),
]
