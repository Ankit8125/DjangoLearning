from django.shortcuts import render
from .models import ChaiVariety
from django.shortcuts import get_object_or_404

# Create your views here.
def all_chai(request):
  chais = ChaiVariety.objects.all() # ORM
  # We will get an array since we used 'all()', so we must know the type of data we are expecting
  return render(request, 'chai/all_chai.html', {'chais': chais}) # Sending data as well

def chai_detail(request, chai_id):
  chai = get_object_or_404(ChaiVariety, pk=chai_id) # pk = primay key
  return render(request, 'chai/chai_detail.html', {'chai': chai})