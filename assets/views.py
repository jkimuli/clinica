from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Asset

# Create your views here.

class AssetListView(LoginRequiredMixin,ListView):
    model = Asset
    context_object_name = 'assets'
    template_name = 'assets/asset_list.html'

class AssetCreateView(UserPassesTestMixin,CreateView):
     
    def test_func(self):
        return self.request.user.is_superuser

class AssetDeleteView(UserPassesTestMixin,DeleteView):

    def test_func(self):
        return self.request.user.is_superuser    

class AssetDetailView(LoginRequiredMixin,DetailView):
    pass

class AssetUpdateView(UserPassesTestMixin,UpdateView):
    pass  

class AssetListView(UserPassesTestMixin,CreateView):
    def test_func(self):
        return self.request.user.is_superuser

class AssetDeleteView(UserPassesTestMixin,DeleteView):
    def test_func(self):
        return self.request.user.is_superuser          


