import uuid
from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel

from clinic.users.models import User


class Patient(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)

    name = models.CharField("Patient's name", max_length=255)
    birth_date = models.DateField(
        null=True,
        blank=True
    )
    slug = AutoSlugField(
        always_update=False,
        populate_from="name"
    )

    creator = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name="created"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("patients:PatientDetail", kwargs={"pk": self.id})
    