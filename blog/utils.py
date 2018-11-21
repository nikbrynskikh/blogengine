from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *

class ObjectDetailMixin:
    """Класс-миксин, для связывания моделей по их слагам с отображением"""
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})

class ObjectCreateMixin:
    """Класс-миксин"""
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form':form})

    def post(self, request):
        bound_form = self.model_form(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)

        return render(request, self.template, context={'form':bound_form})