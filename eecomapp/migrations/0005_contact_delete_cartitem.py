# Generated by Django 4.1.2 on 2023-06-10 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eecomapp', '0004_remove_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone_number', models.CharField(max_length=10)),
                ('Email', models.EmailField(max_length=100)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='cartItem',
        ),
    ]
