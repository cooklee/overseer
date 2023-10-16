# Generated by Django 4.2.6 on 2023-10-16 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_task_done'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('amount', models.FloatField()),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tracker.task')),
            ],
        ),
    ]
