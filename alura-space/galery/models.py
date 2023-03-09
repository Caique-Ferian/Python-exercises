from django.db import models


class Photography(models.Model):
    CATEGORY_OPTIONS = [
        ("Nebulosa", "Nebulosa"),
        ("Estrela", "Estrela"),
        ("Galáxia", "Galáxia"),
        ("Planeta", "Planeta"),
    ]
    name = models.CharField(max_length=100, null=False, blank=False)
    subtitle = models.CharField(max_length=150, null=False, blank=False)
    category = models.CharField(
        max_length=100, choices=CATEGORY_OPTIONS, default=""
    )
    description = models.TextField(null=False, blank=False)
    photo = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Photography [name={self.name}]"
