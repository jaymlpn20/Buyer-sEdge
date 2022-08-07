# Generated by Django 4.0.5 on 2022-07-20 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=0)),
                ('description', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
