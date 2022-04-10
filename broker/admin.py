from django.contrib import admin
from .models import Transaction


# Register your models here.
@admin.register(Transaction)
class AdminTransaction(admin.ModelAdmin):
    list_display = ["national_id", "branch", "transaction_value", "created"]

