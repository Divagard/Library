# Generated by Django 4.2.6 on 2024-01-28 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud_det',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register_Number', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('Department', models.CharField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('college_Name', models.CharField(max_length=20)),
                ('College_Location', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='stud_fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register_Number', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('College_Fees', models.IntegerField()),
                ('Bus_Fees', models.IntegerField()),
                ('Exam_Fees', models.IntegerField()),
                ('Total_Fees', models.IntegerField()),
            ],
        ),
    ]
