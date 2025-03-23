from django.db import models

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    # description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    kanban_board = models.ForeignKey('KanbanBoard', on_delete=models.CASCADE)


class KanbanBoard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Task(models.Model):
    COLUMN_CHOICES = [
        ('backlog', 'Backlog'),
        ('ready_to_do', 'Ready To Do'),
        ('active', 'Active'),
        ('testing', 'Testing'),
        ('production', 'Production'),
    ]
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    details = models.TextField()
    kanban_board_id = models.ForeignKey('KanbanBoard', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    column = models.CharField(max_length=20, choices=COLUMN_CHOICES, default='backlog')

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
