# Generated by Django 5.0.7 on 2024-11-16 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_addresschangeapplication_drivinglicenseapplication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresschangeapplication',
            name='additional_documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/supporting_docs'),
        ),
        migrations.AlterField(
            model_name='addresschangeapplication',
            name='address_proof',
            field=models.FileField(upload_to='documents/address_proofs/'),
        ),
        migrations.AlterField(
            model_name='deathcertificateapplication',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/supporting_docs/'),
        ),
        migrations.AlterField(
            model_name='drivinglicenseapplication',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/supporting_docs/'),
        ),
        migrations.AlterField(
            model_name='pancardapplication',
            name='address_proof',
            field=models.FileField(upload_to='documents/address_proofs/'),
        ),
        migrations.AlterField(
            model_name='pancardapplication',
            name='id_proof',
            field=models.FileField(upload_to='documents/id_proofs/'),
        ),
        migrations.AlterField(
            model_name='voterregistration',
            name='address_proof',
            field=models.FileField(upload_to='documents/address_proofs/'),
        ),
        migrations.AlterField(
            model_name='voterregistration',
            name='id_proof',
            field=models.FileField(upload_to='documents/id_proofs/'),
        ),
    ]
