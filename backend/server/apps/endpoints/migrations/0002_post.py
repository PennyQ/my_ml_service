# Generated by Django 2.2.4 on 2020-07-20 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('endpoints', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('cover', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
