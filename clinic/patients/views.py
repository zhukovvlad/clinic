from django.views.generic import DetailView

from clinic.patients.models import Patient

# Create your views here.
class PatientDetailView(DetailView):
    model = Patient

patient_detail_view = PatientDetailView.as_view()
