# Generated by Django 4.1 on 2023-03-01 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_staff_user_name_alter_condition_check_up_patient_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nextappointment',
            name='doctor',
        ),
        migrations.AddField(
            model_name='nextappointment',
            name='staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staff', to='accounts.staff'),
        ),
        migrations.AlterField(
            model_name='condition_check_up',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nurse', to='accounts.staff'),
        ),
        migrations.AlterField(
            model_name='patienthasdiagnosis',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to='accounts.patient'),
        ),
    ]
