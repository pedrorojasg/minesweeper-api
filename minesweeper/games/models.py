import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


MIN_ROWS = 2
MAX_ROWS = 25
MIN_MINES = 1
MAX_MINES = int((MAX_ROWS**2)*0.5)


def get_secret() -> str:
    """
    Retorna an hexadecimal Secret, 12 chars length.
    """
    base = uuid.uuid4()
    s = str(base).replace('-', '')
    secret = s[:12]
    return secret.upper()


class Game(models.Model):
    """
    Game Model, stores id, times, secret, owner and the Game data.
    field_board is a rectangular matrix field that stores the structure of the field,
    it indicates if a cell has a mine 'm' or not ''.
    game_board is a rectangular matrix field that stores the current status of the
    game board, it indicates the status of each cell and user's plays.
    Possible state:
    '' => 'non played cell'
    '?' => 'user's question mark'
    'f' => 'user's flag'
    'x' => 'user's clicked cell'
    """
    STATUS_CHOICES = (
        ('started', 'started'),
        ('lost', 'lost'),
        ('won', 'won'),
    )
    FIELD_CELL_CHOICES = (
        ('', ''),
        ('m', 'm'),
    )
    PLAY_CELL_CHOICES = (
        ('', ''), # 'non played cell'
        ('?', '?'), # 'user's question mark'
        ('f', 'f'), # 'user's flag'
        ('x', 'x'), # 'user's clicked cell'
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(_('created time'), default=timezone.now)
    last_update_time = models.DateTimeField(_('last update'), auto_now=True)
    finished_time = models.DateTimeField(('finished time'), blank=True, null=True)
    secret = models.CharField(
        max_length=12,
        null=False, unique=True,
        default=get_secret
    )
    name = models.CharField(
        max_length=25,
        blank=True, null=False,
    )
    status = models.CharField(
        _('status'), max_length=10,
        choices=STATUS_CHOICES,
        default='started',
        blank=True, null=False
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='games',
        blank=True, null=True
    )
    rows = models.IntegerField(
        _('rows'), validators=[MinValueValidator(MIN_ROWS), MaxValueValidator(MAX_ROWS)],
        blank=True, null=False
    )
    cols = models.IntegerField(
        _('cols'), validators=[MinValueValidator(MIN_ROWS), MaxValueValidator(MAX_ROWS)],
        blank=True, null=False
    )
    mines = models.IntegerField(
        _('mines'), validators=[MinValueValidator(MIN_MINES), MaxValueValidator(MAX_MINES)],
        blank=True, null=False
    )
    field_board = ArrayField(
        ArrayField(
            models.CharField(
                choices=FIELD_CELL_CHOICES, max_length=1, blank=True, null=False),
            size=MAX_ROWS,
        ),
        size=MAX_ROWS,
    )
    game_board = ArrayField(
        ArrayField(
            models.CharField(
                choices=PLAY_CELL_CHOICES, max_length=1, blank=True, null=False),
            size=MAX_ROWS,
        ),
        size=MAX_ROWS,
    )

    class Meta:
        ordering = ('-created_time',)
