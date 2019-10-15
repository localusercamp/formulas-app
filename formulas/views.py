from django.shortcuts import render
from .models import Formula
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def formulas_index(request):
    formulas = Formula.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'formulas/formulas_index.html', {'formulas':formulas})

def formula_detail(request, pk):
    formula = get_object_or_404(Formula, pk=pk)
    return render(request, 'formulas/formula_detail.html', {'formula': formula})
