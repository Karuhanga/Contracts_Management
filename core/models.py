from django.db import models

# Create your models here.
# TODO Update Contracts model to clear Notification Statuses on create or update
from django.urls import reverse


class ContractManager(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('manager', kwargs={'pk': self.pk})


class Section(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    section_manager = models.CharField(max_length=100)
    section_manager_email = models.EmailField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section', kwargs={'pk': self.pk})


class Company(models.Model):
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    name = models.CharField(max_length=30)
    contact_person = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('company', kwargs={'pk': self.pk})

    def get_absolute_edit_url(self):
        return self.get_absolute_url() + "/update"


class Contract(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    section = models.ForeignKey('Section', on_delete=models.PROTECT)
    company = models.ForeignKey('Company', on_delete=models.PROTECT)
    start_date = models.DateField()
    expiry_date = models.DateField()
    contract_manager = models.ForeignKey('ContractManager', on_delete=models.PROTECT)
    comments = models.TextField(default="", blank=True)
    is_active = models.BooleanField(default=True)

    def summary(self):
        return "Name: {} \nDescription: {} \nSection: {} \nCompany: {} \nExpiry date: {} \nActive: {}".format(self.name,
                                                                                                              self.description,
                                                                                                              self.section,
                                                                                                              self.company,
                                                                                                              self.expiry_date,
                                                                                                              self.is_active)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contract', kwargs={'pk': self.pk})

    def get_absolute_edit_url(self):
        return self.get_absolute_url() + "/update"
