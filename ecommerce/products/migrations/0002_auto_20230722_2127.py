# Generated by Django 4.2.3 on 2023-07-22 16:27

from django.db import migrations

def create_default_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Category.objects.create(name='Category 1')
    Category.objects.create(name='Category 2')
    Category.objects.create(name='Category 3')
    
class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_categories),
    ]


