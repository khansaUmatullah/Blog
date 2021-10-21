# Generated by Django 3.1.4 on 2021-10-21 18:42

from django.db import migrations, models
import froala_editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogmodel_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=froala_editor.fields.FroalaField(),
        ),
        migrations.AlterField(
            model_name='blogmodel',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
