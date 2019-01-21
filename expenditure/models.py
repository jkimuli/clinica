from django.db import models
from django.urls import reverse

# Create your models here.

'''
    The expense model is used to model all expenses other than salary that are
    incurred by the clinic employees
'''    

class Expense(models.Model):
    expense_date = models.DateField(auto_now_add=True, verbose_name="Date Expense Incurred")
    particulars = models.TextField(verbose_name='Particulars')
    amount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')
    incurred_by = models.ForeignKey('clinic.Employee', on_delete=models.CASCADE, verbose_name='Employee Name')

    def __str__(self):

        return "{} - {} incurred by {}".format(self.particulars, self.amount, self.incurred_by)

    def get_absolute_url(self):
        return reverse('expense_detail', args=[self.pk])

    class Meta:
        verbose_name_plural = 'Expenses'
