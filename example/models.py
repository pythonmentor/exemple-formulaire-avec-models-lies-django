from django.db import models


class Parent(models.Model):
    name = models.CharField("parent name", max_length=150, unique=True)

    def __str__(self):
        return self.name


class Child(models.Model):
    parent = models.ForeignKey(
        "Parent", on_delete=models.CASCADE, related_name="children"
    )
    name = models.CharField("child name", max_length=150)

    class Meta:
        verbose_name_plural = "children"

    def __str__(self):
        return self.name
