# Generated by Django 3.2.12 on 2022-03-11 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field', models.TextField(help_text='<ul><li>info a</li><li>info b</li></ul>')),
            ],
        ),
    ]