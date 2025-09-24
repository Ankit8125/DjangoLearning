from django.shortcuts import render
from .models import ChaiVariety, Store
from django.shortcuts import get_object_or_404
from .forms import ChaiVarietyForm

# Create your views here.
def all_chai(request):
  chais = ChaiVariety.objects.all() # ORM
  # We will get an array since we used 'all()', so we must know the type of data we are expecting
  return render(request, 'chai/all_chai.html', {'chais': chais}) # Sending data as well

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id) # pk = primay key
  return render(request, 'chai/chai_detail.html', {'chai': chai})

def chai_store_view(request):
  stores = None # Initializing
  if request.method == "POST": # Form validation
    form = ChaiVarietyForm(request.POST)
    if form.is_valid():
      chai_variety = form.cleaned_data['chai_variety'] # Name should be same as that of forms.py
      stores = Store.objects.filter(chai_varieties = chai_variety) # chai_varieties is a field in the model Store
  else:
    form = ChaiVarietyForm()
  return render(request, 'chai/chai_stores.html', {'stores': stores, 'form': form})