# Generated by Django 4.2.6 on 2023-10-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=50)),
                ('ifLogged', models.BooleanField(default=False)),
                ('user_id', models.CharField(blank=True, default='', max_length=500)),
                ('token', models.CharField(blank=True, default='', max_length=500, null=True)),
            ],
        ),
    ]
