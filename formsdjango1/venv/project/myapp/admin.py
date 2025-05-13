from django.contrib import admin
from .models import Event
from .models import Birthday
from .models import Marriage
# Register your models here.
admin.site.register(Event)
admin.site.register(Birthday)
admin.site.register(Marriage)
