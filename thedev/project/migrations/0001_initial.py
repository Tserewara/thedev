# Generated by Django 5.1.7 on 2025-03-23 18:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KanbanBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('details', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('kanban_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.kanbanboard')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('details', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('column', models.CharField(choices=[('backlog', 'Backlog'), ('ready_to_do', 'Ready To Do'), ('active', 'Active'), ('testing', 'Testing'), ('production', 'Production')], default='backlog', max_length=20)),
                ('kanban_board_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.kanbanboard')),
            ],
        ),
    ]
