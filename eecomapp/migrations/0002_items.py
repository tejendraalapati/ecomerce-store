# Generated by Django 4.1.2 on 2023-06-10 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eecomapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('images', models.ImageField(upload_to='products')),
            ],
        ),
    ]
