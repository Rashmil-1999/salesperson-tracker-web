# Generated by Django 2.2.10 on 2020-02-27 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salespersonTrackerRest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='Assigned_Date',
        ),
        migrations.RemoveField(
            model_name='inventory',
            name='Assigned_Time',
        ),
        migrations.CreateModel(
            name='DailyTarget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Assigned_Date', models.DateField()),
                ('Assigned_Time', models.TimeField()),
                ('Quantity', models.IntegerField()),
                ('Completed', models.BooleanField()),
                ('Notes', models.TextField()),
                ('Assigned_By', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salespersonTrackerRest.Manager')),
                ('Assigned_To', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salespersonTrackerRest.Salesperson')),
                ('Item_Ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salespersonTrackerRest.ItemAssign')),
            ],
        ),
    ]