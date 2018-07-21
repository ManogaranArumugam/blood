from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy, resolve

from django.http import HttpResponse

from django.views.generic import TemplateView, CreateView
# from django.http import HttpResponseForbidden

from blood.donor.forms import DonorInformationForm
from blood.donor.models import DonorInformation
    


class DonorRegistrationView(CreateView):
    """"""
    template_name = 'donor/index.html'
    form_class = DonorInformationForm
    model = DonorInformation
    success_url = reverse_lazy('donor/success')


    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            form.save()
            return render(request, 'donor/success.html',)
        else:
            return self.form_invalid(form, **kwargs)
