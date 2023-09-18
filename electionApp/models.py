from django.db import models


class PartyData(models.Model):
    party_id = models.AutoField(primary_key=True)
    party_name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    # password = models.CharField(
    #     max_length=255, null=True, blank=True, default='')
    founder_1 = models.CharField(
        max_length=255, null=True, blank=True, default='')
    founded_year = models.CharField(
        max_length=255, null=True, blank=True, default='')
    current_mps = models.CharField(
        max_length=255, null=True, blank=True, default='')
    no_of_electorate_held = models.CharField(
        max_length=255, null=True, blank=True, default='')
    polling_average = models.CharField(
        max_length=255, null=True, blank=True, default='')
    donations = models.CharField(
        max_length=255, null=True, blank=True, default='')
    party_contact_details = models.TextField(null=True, blank=True, default='')
    party_logo = models.FileField(upload_to='media/', blank=True, default='') 
    about_party = models.TextField(null=True, blank=True, default='')

    party_q_performance = models.TextField(null=True, blank=True, default='')
    party_q_productivity= models.TextField(null=True, blank=True, default='')
    party_q_religious = models.TextField(null=True, blank=True, default='')
    party_q_terrorism = models.TextField(null=True, blank=True, default='')
    party_q_internation_relation = models.TextField(null=True, blank=True, default='')
    party_q_introduce = models.TextField(null=True, blank=True, default='')
    party_address = models.TextField(null=True, blank=True, default='')
    founder_2 =  models.TextField(null=True, blank=True, default='')
    founder_3 = models.TextField(null=True, blank=True, default='')
    founder_4 = models.TextField(null=True, blank=True, default='')
    time_in_gov = models.TextField(null=True, blank=True, default='')
    # poling_avg = models.TextField(null=True, blank=True, default='')



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
    password = models.CharField(
        max_length=255, null=True, blank=True, default='')
    address = models.TextField(null=True, blank=True, default='')
    contact_details = models.TextField(null=True, blank=True, default='')
    electorate = models.CharField(
        max_length=255, null=True, blank=True, default='')
    age = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.CharField(max_length=255, null=True, blank=True, default='')
    social_media_contact = models.CharField(
        max_length=255, null=True, blank=True, default='')
    about_me = models.TextField(null=True, blank=True, default='')
    unique_strg = models.TextField(null=True, blank=True, default='')
    why_running = models.TextField(null=True, blank=True, default='')
    issues_facing = models.TextField(null=True, blank=True, default='')
    why_vote = models.TextField(null=True, blank=True, default='')
    cand_priority = models.TextField(null=True, blank=True, default='')
    cand_presslink = models.TextField(null=True, blank=True, default='')
    cand_img = models.FileField(upload_to='candidates/', blank=True, default='')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class meta:
        db_table = 'condidate_data'

    def __str__(self):
        return str(self.name)
