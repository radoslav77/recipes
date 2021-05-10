# Generated by Django 3.1 on 2021-05-06 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0007_delete_sub_recipe'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sub_recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_recipe', models.TextField(max_length=2000)),
                ('method', models.TextField(max_length=2000)),
                ('sub_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipe')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
