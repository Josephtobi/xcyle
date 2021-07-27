# Generated by Django 3.2.5 on 2021-07-27 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wasteprod', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bids', to='wasteprod.waste'),
        ),
        migrations.AlterField(
            model_name='waste',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
