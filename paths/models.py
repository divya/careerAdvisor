# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Linkentries(models.Model):
    link_url = models.TextField()
    usr_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'LinkEntries'


class Milentries(models.Model):
    usr_id = models.IntegerField()
    mil_country = models.TextField(blank=True, null=True)
    mil_branch = models.TextField(blank=True, null=True)
    mil_rank = models.TextField(blank=True, null=True)
    mil_date = models.TextField(blank=True, null=True)
    mil_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MilEntries'


class Nodetypes(models.Model):
    node_type_id = models.AutoField(primary_key=True)
    node_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'NodeTypes'


class Nodes(models.Model):
    node_id = models.AutoField(primary_key=True)
    node_type_id = models.IntegerField()
    node_title = models.TextField()

    class Meta:
        managed = False
        db_table = 'Nodes'


class Patentries(models.Model):
    usr_id = models.IntegerField()
    pat_title = models.TextField(blank=True, null=True)
    pat_url = models.TextField(blank=True, null=True)
    pat_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PatEntries'


class Pubentries(models.Model):
    usr_id = models.IntegerField()
    pub_title = models.TextField(blank=True, null=True)
    pub_url = models.TextField(blank=True, null=True)
    pub_date = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PubEntries'


class Skillentries(models.Model):
    sk_id = models.IntegerField()
    usr_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'SkillEntries'


class Skillnames(models.Model):
    sk_id = models.AutoField(primary_key=True)
    sk_name = models.TextField()

    class Meta:
        managed = False
        db_table = 'SkillNames'


class Trajectoryentries(models.Model):
    usr_id = models.IntegerField()
    node_id = models.IntegerField()
    org_name = models.TextField(blank=True, null=True)
    org_location = models.TextField(blank=True, null=True)
    start_date_str = models.TextField(blank=True, null=True)
    end_date_str = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    start_date_month_int = models.IntegerField(blank=True, null=True)
    start_date_year_int = models.IntegerField(blank=True, null=True)
    start_date_year_month_int = models.IntegerField(blank=True, null=True)
    end_date_month_int = models.IntegerField(blank=True, null=True)
    end_date_year_int = models.IntegerField(blank=True, null=True)
    end_date_year_month_int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrajectoryEntries'


class Trajectorytemp(models.Model):
    usr_id = models.AutoField(primary_key=True)
    list_node_id = models.TextField()

    class Meta:
        managed = False
        db_table = 'TrajectoryTemp'


class Users(models.Model):
    usr_id = models.AutoField(primary_key=True)
    filename = models.TextField()
    usr_title = models.TextField(blank=True, null=True)
    usr_headline = models.TextField(blank=True, null=True)
    usr_contact = models.TextField(blank=True, null=True)
    usr_summary = models.TextField(blank=True, null=True)
    usr_eligibility = models.TextField(blank=True, null=True)
    usr_additional_info = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Users'
