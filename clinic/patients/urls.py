from django.urls import path
from django.views.generic import TemplateView

from clinic.patients.views import (
    patient_detail_view,
)


app_name="patients"
urlpatterns = [
    path(
        route="",
        view=TemplateView.as_view(template_name="404.html")
    ),
    path(
        route="<uuid:pk>",
        view=patient_detail_view,
        name="PatientDetail"
    )
]
