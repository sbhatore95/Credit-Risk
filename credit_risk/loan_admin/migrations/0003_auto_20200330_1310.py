# Generated by Django 3.0.4 on 2020-03-30 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_admin', '0002_auto_20200329_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='credit_risk/dataset/train_dataset.csv')),
                ('columns', models.CharField(max_length=1000000)),
                ('nominal_features', models.CharField(max_length=1000000)),
            ],
        ),
        migrations.DeleteModel(
            name='CSV',
        ),
    ]
