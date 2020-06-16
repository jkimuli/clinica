from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.forms import  inlineformset_factory

from .forms import SupplierForm,ProductForm,PurchaseForm,InvoiceLineItemForm,InvoiceForm
from .models import Supplier,Product,Purchase,Invoice,InvoiceLineItem

# Create your views here.

def supplier_index(request):
    suppliers = Supplier.objects.all()
    paginator = Paginator(suppliers,1)
    page = request.GET.get('page')
    paged_suppliers = paginator.get_page(page) 

    context = {
        'suppliers': paged_suppliers
    }

    return render(request,'pharmacy/suppliers.html', context)

def supplier_add(request):

    if request.method == 'POST':
        form = SupplierForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('suppliers'))
    else:

        form = SupplierForm()

    return render(request,'pharmacy/supplier_add.html',{'form': form})     

def product_index(request):
    products = Product.objects.all()
    paginator = Paginator(products,1)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page) 
    context = {
        'products': paged_products
    }

    return render(request,'pharmacy/products.html', context)

def product_add(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('products'))
    else:

        form = ProductForm()

    return render(request,'pharmacy/product_add.html',{'form': form , 'title': 'Add New Product'})  

def purchase_index(request):
    purchases = Purchase.objects.all()
    paginator = Paginator(purchases,1)
    page = request.GET.get('page')
    paged_purchases = paginator.get_page(page) 

    context = {
        'purchases': paged_purchases
    }

    return render(request,'pharmacy/purchases.html', context)

def purchase_add(request):

    if request.method == 'POST':
        form = PurchaseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('purchases'))
    else:

        form = PurchaseForm()

    return render(request,'pharmacy/purchase_add.html',{'form': form, 'title': 'Add New Purchase'})  

def supplier_edit(request,id):
    supplier = get_object_or_404(Supplier,pk=id)
    form = SupplierForm(request.POST or None, instance=supplier)

    if form.is_valid():
        form.save()
        return redirect('suppliers')

    return render(request,'pharmacy/supplier_add.html', {'form': form, 'title':'Update Supplier'})

def purchase_edit(request,id):
    purchase = get_object_or_404(Purchase,pk=id)
    form = PurchaseForm(request.POST or None, instance=purchase)

    if form.is_valid():
        form.save()
        return redirect('purchases')

    return render(request,'pharmacy/purchase_add.html', {'form': form, 'title':'Update Purchase'})

def product_edit(request,id):
    product = get_object_or_404(Product,pk=id)
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid():
        form.save()
        return redirect('products')

    return render(request,'pharmacy/product_add.html', {'form': form, 'title':'Update Product'}) 

def invoice_index(request):
    invoices = Invoice.objects.all()
    paginator = Paginator(invoices,1)
    page = request.GET.get('page')
    paged_invoices = paginator.get_page(page) 
    context = {
        'invoices': paged_invoices
    }

    return render(request,'pharmacy/invoices.html', context)

def invoice_add(request):
    InvoiceLineFormset = inlineformset_factory(Invoice,InvoiceLineItem,form=InvoiceLineItemForm,extra=2, max_num=6,can_delete=True)
    form = InvoiceForm(request.POST or None)
    formset = InvoiceLineFormset(request.POST or None)

    if form.is_valid() and formset.is_valid():
            invoice = form.save()
            line_items = formset.save(commit=False)
            for item in line_items:
                item.invoice = invoice                
                item.save()                   

            return redirect('invoices')  

    return render(request,'pharmacy/invoice_add.html',{'form':form, 'formset': formset})

def invoice_detail(request,id):
    invoice = get_object_or_404(Invoice,pk=id)
    context = {
        
    }

    return render(request,'pharmacy/invoice.html',context)    



        
