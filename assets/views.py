from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Asset

# Create your views here.

class AssetListView(LoginRequiredMixin,ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = 'assets/asset_list.html'

class AssetCreateView(UserPassesTestMixin,CreateView):
    model = Asset
    fields = '__all__'
    template_name = 'assets/asset_add.html'
    success_url = reverse_lazy('assets:asset_list')
     
    def test_func(self):
        return self.request.user.is_superuser

class AssetDeleteView(UserPassesTestMixin,DeleteView):

    def test_func(self):
        return self.request.user.is_superuser    

class AssetDetailView(LoginRequiredMixin,DetailView):
    pass

class AssetUpdateView(UserPassesTestMixin,UpdateView):
    model = Asset
    fields = '__all__'
    template_name = 'assets/asset_add.html'
    success_url = reverse_lazy('assets:asset_list')


    def test_func(self):
        return self.request.user.is_superuser 

       


