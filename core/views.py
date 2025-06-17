from rest_framework import viewsets,permissions
from .models import Category,Transaction,Budget
from .serializers import CategorySerializer,TransactionSerializer,BudgetSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Sum

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionViewSet(viewsets.ModelViewSet):
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MonthlyReportView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request):
    # Parse query param: ?month=YYYY-MM
        month_str = request.query_params.get("month")
        if not month_str:
            return Response({"error": "month parameter is required (e.g. ?month=2025-06)"}, status=400)

        try:
            year, month = map(int, month_str.split("-"))
        except ValueError:
            return Response({"error": "Invalid month format. Use YYYY-MM"}, status=400)

        user = request.user
        start_date = datetime(year, month, 1).date()
        if month == 12:
            end_date = datetime(year + 1, 1, 1).date()
        else:
            end_date = datetime(year, month + 1, 1).date()

        transactions = Transaction.objects.filter(user=user, date__gte=start_date, date__lt=end_date)
        income = transactions.filter(category__type='income').aggregate(total=Sum("amount"))["total"] or 0
        expense = transactions.filter(category__type='expense').aggregate(total=Sum("amount"))["total"] or 0
        net = income - expense

    # Category-wise breakdown
        category_data = (
            transactions.filter(category__type='expense')
            .values("category__name")
            .annotate(total=Sum("amount"))
        )

    # Budget comparison
        budgets = Budget.objects.filter(user=user, month__year=year, month__month=month)
        budget_summary = []
        for budget in budgets:
            spent = transactions.filter(category=budget.category).aggregate(total=Sum("amount"))["total"] or 0
            status = "under" if spent <= budget.monthly_limit else "over"
            budget_summary.append({
                "category": budget.category.name,
                "limit": float(budget.monthly_limit),
                "spent": float(spent),
                "status": status
            })

        return Response({
            "month": month_str,
            "total_income": income,
            "total_expense": expense,
            "net_savings": net,
            "category_breakdown": category_data,
            "budget_status": budget_summary,
        })