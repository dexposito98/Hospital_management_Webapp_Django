# Generated by Django 4.1 on 2023-02-05 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_dignosis_patienthasdiagnosis_diagnosis'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patienthasdiagnosis',
            name='check_up_id',
        ),
        migrations.AddField(
            model_name='patienthasdiagnosis',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.patient'),
        ),
    ]
