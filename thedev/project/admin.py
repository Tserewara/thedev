from django.contrib import admin
from .models import Project, KanbanBoard, Task, Tag
# Register your models here.


admin.site.register(Project)
admin.site.register(KanbanBoard)
admin.site.register(Task)
