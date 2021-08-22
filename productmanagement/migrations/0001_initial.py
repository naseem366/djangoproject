# Generated by Django 3.1.7 on 2021-06-11 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorymanagement', '0003_auto_20210611_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_Image', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('amount', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorymanagement.category')),
            ],
        ),
    ]
