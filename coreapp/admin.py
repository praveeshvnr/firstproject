from django.contrib import admin
#Register your models here.
from .models import HRtasks
admin.site.register(HRtasks)


from .models import Item
from .models import regdetails
# Register your models here.

admin.site.register(Item)
admin.site.register(regdetails)

from .models import admingivetask
admin.site.register(admingivetask)