from django.urls import path

from clinic.patients.views import (
    patient_detail_view,
)


app_name="patients"
urlpatterns = [
    path(
        route="<uuid:pk>",
        view=patient_detail_view,
        name="PatientDetail"
    )
]
