# Generated by Django 4.2.11 on 2024-05-01 01:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fileUpload', '0005_datfile_hdrfile_alter_spectraldata_dat_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='datfile',
            name='file_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Original File Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='datfile',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Uploaded At'),
        ),
        migrations.AddField(
            model_name='hdrfile',
            name='file_name',
            field=models.CharField(default=1, max_length=255, verbose_name='Original File Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hdrfile',
            name='uploaded_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Uploaded At'),
        ),
        migrations.DeleteModel(
            name='SpectralData',
        ),
    ]
