from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Person
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


@method_decorator(login_required, name='dispatch')
class PersonList(ListView):
    model = Person
    paginate_by = 10


@method_decorator(login_required, name='dispatch')
class PersonDetail(DetailView):
    model = Person


@method_decorator(login_required, name='dispatch')
class PersonCreate(SuccessMessageMixin, CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list')
    success_message = "%(first_name)s cadastrado com sucesso"


@method_decorator(login_required, name='dispatch')
class PersonUpdate(SuccessMessageMixin, UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list')
    success_message = "%(first_name)s atualizado com sucesso"


@method_decorator(login_required, name='dispatch')
class PersonDelete(SuccessMessageMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('person_list')
    success_message = "Registro excluído com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(PersonDelete, self).delete(request, *args, **kwargs)
