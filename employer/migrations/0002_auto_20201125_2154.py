# Generated by Django 3.1.3 on 2020-11-25 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='phone',
            new_name='company',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='field',
        ),
        migrations.RemoveField(
            model_name='detail',
            name='subfield',
        ),
        migrations.AddField(
            model_name='detail',
            name='job_title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='phone_number',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='detail',
            name='position',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detail',
            name='county',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='detail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
