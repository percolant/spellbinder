from django.contrib import admin

from cards.models import (
    Edition,
    Color,
    Format,
    Artist,
    Rarity,
    Card,
    CardInstance
)


class CardAdmin(admin.ModelAdmin):
    list_display=('base', 'type_line', 'mana_cost', 'rarity', 'power_toughness', )
    list_filter=('edition', 'rarity', 'colors', 'formats', )

    def base(self, obj):
        return obj.__str__()

    def power_toughness(self, obj):
        if obj.power and obj.toughness:
            return '{}/{}'.format(obj.power, obj.toughness)
        return ''


admin.site.register(Edition)
admin.site.register(Color)
admin.site.register(Format)
admin.site.register(Artist)
admin.site.register(Rarity)
admin.site.register(Card, CardAdmin)
admin.site.register(CardInstance)
