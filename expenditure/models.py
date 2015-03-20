from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Expense(models.Model):
    expense_date = models.DateField(auto_now_add=True, verbose_name="Date Expense Incurred")
    particulars = models.TextField(verbose_name='Particulars')
    amount = models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Amount')
    incurred_by = models.ForeignKey('clinic.Employee', verbose_name='Employee Name')

    def __unicode__(self):

        return '%s - %d incurred by %s' % (self.particulars, self.amount, self.incurred_by)

    def get_absolute_url(self):
        return reverse('expense_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = 'Expenses'
