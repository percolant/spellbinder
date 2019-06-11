from django.contrib import admin

from cards.models import (
    Edition,
    Color,
    Format,
    Artist,
    Card,
    CardInstance
)


admin.site.register(Edition)
admin.site.register(Color)
admin.site.register(Format)
admin.site.register(Artist)
admin.site.register(Card)
admin.site.register(CardInstance)
