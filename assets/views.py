
# Create your views here.
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

from .forms import AssetForm
from .models import Asset

# Create your views here.

def asset_index(request):
    assets = Asset.objects.all()
    paginator = Paginator(assets,1)
    page = request.GET.get('page')
    paged_assets = paginator.get_page(page)  

    context = {
        'assets': paged_assets
    }

    return render(request,'assets/assets.html', context)

def asset_add(request):

    if request.method == 'POST':
        form = AssetForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse('assets'))
    else:

        form = AssetForm()

    return render(request,'assets/asset_add.html',{'form': form , 'title': 'Add New'}) 

def asset_edit(request,id):
    asset = get_object_or_404(Asset,pk=id)
    form =  AssetForm(request.POST or None, instance=asset)

    if form.is_valid():
        form.save()
        return redirect(reverse('assets'))
    
    return render(request,'assets/asset_add.html', {'form': form , 'title': 'Update'} ) 




        





       


