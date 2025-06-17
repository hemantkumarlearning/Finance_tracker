from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet,TransactionViewSet,BudgetViewSet,MonthlyReportView
from django.urls import path

router = DefaultRouter()
router.register(r'categories', CategoryViewSet,basename='categories')
router.register(r'transactions', TransactionViewSet,basename='transactions')
router.register(r'budgets', BudgetViewSet,basename='budgets')

urlpatterns = router.urls + [
path("reports/monthly/", MonthlyReportView.as_view(), name="monthly-report"),
]