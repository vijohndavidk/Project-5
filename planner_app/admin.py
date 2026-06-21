from django.contrib import admin
from .models import Subject
from .models import Timetable
from .models import Progress


admin.site.register(Subject)
admin.site.register(Timetable)
admin.site.register(Progress)