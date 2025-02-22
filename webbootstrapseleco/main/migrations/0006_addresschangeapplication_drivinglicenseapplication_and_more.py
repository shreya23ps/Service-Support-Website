# Generated by Django 5.0.7 on 2024-11-14 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_deathcertificateapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressChangeApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('applicant_dob', models.DateField()),
                ('applicant_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=20)),
                ('applicant_aadhaar', models.CharField(max_length=12)),
                ('old_address', models.TextField()),
                ('new_address', models.TextField()),
                ('address_proof', models.FileField(upload_to='address_proof/')),
                ('additional_documents', models.FileField(blank=True, null=True, upload_to='additional_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DrivingLicenseApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=200)),
                ('applicant_father_name', models.CharField(max_length=200)),
                ('applicant_dob', models.DateField()),
                ('applicant_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=20)),
                ('applicant_aadhaar', models.CharField(max_length=12)),
                ('applicant_address', models.TextField()),
                ('license_type', models.CharField(choices=[('learner', "Learner's License"), ('permanent', 'Permanent License')], max_length=20)),
                ('vehicle_class', models.CharField(choices=[('mcwog', 'Motorcycle Without Gear'), ('mcwg', 'Motorcycle With Gear'), ('lmv', 'Light Motor Vehicle'), ('hmv', 'Heavy Motor Vehicle')], max_length=20)),
                ('applicant_contact', models.CharField(max_length=15)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('documents', models.FileField(blank=True, null=True, upload_to='driving_license_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RationCardApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('applicant_father_name', models.CharField(max_length=255)),
                ('applicant_dob', models.DateField()),
                ('applicant_gender', models.CharField(max_length=10)),
                ('applicant_aadhaar', models.CharField(max_length=12)),
                ('applicant_address', models.TextField()),
                ('applicant_state', models.CharField(max_length=100)),
                ('applicant_district', models.CharField(max_length=100)),
                ('applicant_city', models.CharField(max_length=100)),
                ('applicant_pincode', models.CharField(max_length=6)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('applicant_contact', models.CharField(max_length=15)),
                ('id_proof', models.FileField(upload_to='documents/id_proofs/')),
                ('address_proof', models.FileField(upload_to='documents/address_proofs/')),
                ('photo', models.ImageField(upload_to='documents/photos/')),
                ('family_members', models.IntegerField()),
                ('ration_card_type', models.CharField(choices=[('APL', 'Above Poverty Line'), ('BPL', 'Below Poverty Line')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='VoterRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_name', models.CharField(max_length=255)),
                ('applicant_dob', models.DateField()),
                ('applicant_gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('applicant_aadhaar', models.CharField(max_length=12, unique=True)),
                ('applicant_address', models.TextField()),
                ('applicant_pincode', models.CharField(max_length=6)),
                ('applicant_email', models.EmailField(max_length=254)),
                ('applicant_contact', models.CharField(max_length=15)),
                ('id_proof', models.FileField(upload_to='voter_registration/id_proof/')),
                ('address_proof', models.FileField(upload_to='voter_registration/address_proof/')),
            ],
        ),
    ]
