from django.contrib import admin
from IceCreamVendingMachine.models import IceCream
from IceCreamVendingMachine.models import Stores
from IceCreamVendingMachine.models import WhereOffered
from IceCreamVendingMachine.models import Cart
from IceCreamVendingMachine.models import SnowCone

# Register your models here.
admin.site.register(IceCream)
admin.site.register(Stores)
admin.site.register(WhereOffered)
admin.site.register(Cart)
admin.site.register(SnowCone)
