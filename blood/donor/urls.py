from django.conf.urls import url
 
from blood.donor.views import DonorRegistrationView

urlpatterns = [
	url(r'^$', DonorRegistrationView.as_view(), name='home'),
]