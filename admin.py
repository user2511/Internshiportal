from django.contrib import admin

from .models.candidate import Candidates
from .models.candidate import Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Candidates)


