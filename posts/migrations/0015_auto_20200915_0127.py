# Generated by Django 3.0.6 on 2020-09-15 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20200915_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('주점', '주점'), ('부스', '부스'), ('공연', '공연'), ('기타', '기타')], max_length=300, null=True),
        ),
    ]
