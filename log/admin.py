from django.contrib import admin

from .models import Library
from .models import CC
from .models import Gymkhana
from .models import Csedept
from .models import Umiamhostel
from .models import Subhansrihostel
from .models import Dhansarihostel

admin.site.register(Library)
admin.site.register(CC)
admin.site.register(Gymkhana)
admin.site.register(Csedept)
admin.site.register(Umiamhostel)
admin.site.register(Subhansrihostel)
admin.site.register(Dhansarihostel)


# Register your models here.
