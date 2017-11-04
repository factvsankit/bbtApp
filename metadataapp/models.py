from decimal import Decimal
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class PlantData(models.Model):
    name = models.CharField(max_length=50, blank=True, default='')
    kg_per_bio_intensive_bed = models.TextField(blank=True, default='')
    cost_per_kg = models.TextField(blank=True, default='')
    nutrition = models.TextField(blank=True, default='')
    seed_availability = models.TextField(blank=True, default='')
    common_pest = models.TextField(blank=True, default='')
    jhol_mal_recipe = models.TextField(blank=True, default='')
    compost = models.TextField(blank=True, default='')
    planting_distance = models.TextField(blank=True, default='')
    planting_date = models.TextField(blank=True, default='')
    planting_depth = models.TextField(blank=True, default='')
    alternatives = models.TextField(blank=True, default='')
    soil_preparation = models.TextField(blank=True, default='')
    seed_rate = models.TextField(blank=True, default='')
    water_requirement = models.TextField(blank=True, default='')
    intercultural_operation = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


@python_2_unicode_compatible
class Event(models.Model):
    choices = [('Prepare Sunken Bed', 'Prepare Sunken Bed'),
               ('Prepare leaf pot bed', 'Prepare leaf pot bed'),
               ('Prepare raised bed', 'Prepare raised bed'),
               ('Nursery/Garden bed preparation', 'Nursery/Garden bed preparation'),
               ('Transplant From Nursery Into Garden Bed', 'Transplant From Nursery Into Garden Bed'),
               ('Sew Seeds Into Garden Bed', 'Sew Seeds Into Garden Bed'),
               ('Direct Seeding', 'Direct Seeding'),
               ('Mulch Plant', 'Mulch Plant'),
               ('Water with 5:1 Water to Urine', 'Water with 5:1 Water to Urine'),
               ('Water with 3:1 Water to Urine', 'Water with 3:1 Water to Urine'),
               ('Apply Bio-Pesticide', 'Apply Bio-Pesticide'),
               ('Apply Compost/FYM', 'Apply Compost/FYM'),
               ('Water Plant', 'Water Plant'),
               ('Build Staking For Plant', 'Build Staking For Plant'),
               ('Clear Out Old Plants', 'Clear Out Old Plants'),
               ('Water Seed Bed', 'Water Seed Bed'),
               ('Thin Direct Seeded Plants', 'Thin Direct Seeded Plants'),
               ('Water Vegetable Bed with 5:1 Water to Urine', 'Water Vegetable Bed with 5:1 Water to Urine'),
               ('Start Plastic Covered Nursery', 'Start Plastic Covered Nursery')]
    choices_weeks = [('Week 1', 'Week 1'),
                     ('Week 2', 'Week 2'),
                     ('Week 3', 'Week 3'),
                     ('Week 4', 'Week 4')]
    choices_months = [('Baisakh', 'Baisakh'),
                      ('Jestha', 'Jestha'),
                      ('Ashar', 'Ashar'),
                      ('Shrawan', 'Shrawan'),
                      ('Bhadra', 'Bhadra'),
                      ('Ashoj', 'Ashoj'),
                      ('Karthik', 'Karthik'),
                      ('Mangshir', 'Mangshir'),
                      ('Poush', 'Poush'),
                      ('Magh', 'Magh'),
                      ('Falgun', 'Falgun'),
                      ('Chaitra', 'Chaitra')]
    YEAR_CHOICES = [('2016', '2016'),
                    ('2017', '2017')]
    event_name = models.CharField(max_length=100, blank=True, default='', choices=choices)
    nepali_event_name = models.CharField(max_length=200, blank=True, default='')
    week = models.CharField(max_length=20, blank=True, default='', choices=choices_weeks)
    month = models.CharField(max_length=30, blank=True, default='', choices=choices_months)
    year = models.CharField(max_length=4, blank=True, choices=YEAR_CHOICES)
    remark = models.CharField(max_length=300, blank=True, default='')
    plant_events = models.ForeignKey("Plant", blank=True, null=True)

    def __str__(self):
        return self.event_name


@python_2_unicode_compatible
class Plant(models.Model):
    CHOICES_SEASON = [('summer', 'summer'),
                      ('rainy', 'rainy'),
                      ('winter', 'winter')]
    CHOICES_GROUP = [('1', '1'),
                     ('2', '2'),
                     ('3', '3'),
                     ('4', '4'),
                     ('5', '5'),
                     ('6', '6'),
                     ('7', '7'),
                     ('8', '8'),
                     ('9', '9')]
    name = models.CharField(max_length=60, blank=True, default='')
    unique_name = models.CharField(max_length=40, blank=True, default='')
    detailURL = models.CharField(max_length=100, blank=True, default='')
    season = models.CharField(max_length=20, blank=True, default='', choices=CHOICES_SEASON)
    image = models.CharField(max_length=30, blank=True, default='')
    group = models.CharField(max_length=2, blank=True, choices=CHOICES_GROUP)
    remark_about_plant = models.TextField(blank=True, default='')
    last_changed_by = models.CharField(max_length=30, blank=True, null=True)
    # events = models.ManyToManyField(Event, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


@python_2_unicode_compatible
class Fruit(models.Model):
    name = models.CharField(max_length=60, blank=True, default='')
    unique_name = models.CharField(max_length=40, blank=True, default='')
    detailURL = models.CharField(max_length=100, blank=True, default='')
    image = models.CharField(max_length=30, blank=True, default='')
    last_changed_by = models.CharField(max_length=30, blank=True, null=True)
    # events = models.ManyToManyField(Event, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


@python_2_unicode_compatible
class CropPricing(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default=Decimal('0.0000'))

    def __str__(self):
        return "{}: {}".format(self.name, self.price)
