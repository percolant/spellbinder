from django.db import models
from django.contrib.auth import get_user_model


COLORS = [
    ('W', 'White'),
    ('U', 'Blue'),
    ('B', 'Black'),
    ('R', 'Red'),
    ('G', 'Green')
]

FORMATS = [
    ('Standard', 'Standard'),
    ('Modern', 'Modern'),
    ('Legacy', 'Legacy'),
    ('Pauper', 'Pauper'),
    ('Vintage', 'Vintage'),
    ('EDH', 'EDH')
]

LANGUAGES = [
    ('EN', 'English'),
    ('ES', 'Spanish'),
    ('FR', 'French'),
    ('DE', 'German'),
    ('IT', 'Italian'),
    ('PT', 'Portuguese'),
    ('JA', 'Japanese'),
    ('KO', 'Korean'),
    ('RU', 'Russian'),
    ('CH', 'Chinese')
]

STATES = [
    ('NM', 'Nearly Mint'),
    ('EX', 'Excellent'),
    ('LP', 'Lightly Played'),
    ('PL', 'Played')
]


class Edition(models.Model):
    code = models.CharField(max_length=3, blank=False, unique=True)
    full_name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return '{} - {}'.format(self.code, self.full_name)


class Color(models.Model):
    color = models.CharField(
        max_length=1,
        blank=False,
        unique=True,
        choices=COLORS
    )

    def __str__(self):
        return self.get_color_display()


class Format(models.Model):
    format = models.CharField(
        max_length=10,
        blank=False,
        unique=True,
        choices=FORMATS
    )

    def __str__(self):
        return self.get_format_display()


class Artist(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    number = models.IntegerField(blank=False)
    edition = models.ForeignKey(
        Edition,
        related_name='cards',
        on_delete=models.PROTECT
    )
    name = models.CharField(max_length=50, blank=False)
    type_line = models.CharField(max_length=50, blank=False)
    colors = models.ManyToManyField(Color, blank=True)
    cmc = models.IntegerField(blank=False)
    mana_cost = models.CharField(max_length=15, blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    toughness = models.IntegerField(blank=True, null=True)
    loyalty = models.IntegerField(blank=True, null=True)
    formats = models.ManyToManyField(Format)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.PROTECT)
    oracle_text = models.TextField(blank=True, null=True)
    instances = models.ManyToManyField(
        get_user_model(),
        blank=True,
        through='CardInstance'
    )

    class Meta:
        unique_together = ('number', 'edition')
        ordering = ['edition', 'number']

    def __str__(self):
        return '{}/{} - {}'.format(self.edition.code, self.number, self.name)


class CardInstance(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=2,
        blank=False,
        choices=LANGUAGES
    )
    state = models.CharField(
        max_length=2,
        blank=False,
        choices=STATES
    )
    commentary = models.CharField(max_length=255, blank=True, null=True)

    # TODO an idea: implement functionality that will allow to follow card's
    # buy/sell history (reconsider on_delete)

    def __str__(self):
        return '{} | {} | {} | {}'.format(
            self.user.username,
            self.card.name,
            self.language,
            self.state
        )
