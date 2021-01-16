# Generated by Django 3.1.4 on 2021-01-06 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created_at'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='is_publoshed',
            new_name='is_published',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='phoyo',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='udpated_at',
            new_name='updated_at',
        ),
    ]