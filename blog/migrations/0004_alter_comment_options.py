# Generated by Django 3.2.5 on 2021-08-26 22:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('created',)},
        ),
    ]
