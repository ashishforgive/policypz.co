from django.db import models

class PartyData(models.Model):
    party_id = models.AutoField(primary_key=True)
    party_name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True, default='')
    founder = models.CharField(max_length=255, null=True, blank=True, default='')
    founded_year = models.CharField(max_length=255, null=True, blank=True, default='')
    current_mps = models.CharField(max_length=255, null=True, blank=True, default='')
    no_of_electorate_held = models.CharField(max_length=255, null=True, blank=True, default='')
    polling_average = models.CharField(max_length=255, null=True, blank=True, default='')
    donations = models.CharField(max_length=255, null=True, blank=True, default='')
    contact_details = models.TextField(null=True, blank=True, default='')
    party_logo = models.CharField(max_length=255, null=True, blank=True, default='')
    about_me = models.TextField(null=True, blank=True, default='')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'party_data'

    def __str__(self):
        return str(self.party_name)
    

class CondidateData(models.Model):
    condidate_id = models.AutoField(primary_key=True) 
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, null=True, blank=True, default='')
    address = models.TextField(null=True, blank=True, default='')
    contact_details = models.TextField(null=True, blank=True, default='')
    electorate = models.CharField(max_length=255, null=True, blank=True, default='')
    age = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.CharField(max_length=255, null=True, blank=True, default='')
    social_media_contact = models.CharField(max_length=255, null=True, blank=True, default='')
    about_me = models.TextField(null=True, blank=True, default='')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'condidate_data'

    def __str__(self):
        return str(self.name)
    