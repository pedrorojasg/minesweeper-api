import uuid

from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


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
    """
    STATUS_CHOICES = (
        ('started', 'started'),
        ('lost', 'lost'),
        ('won', 'won'),
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
    status = models.CharField(
        _('status'), max_length=10,
        choices=STATUS_CHOICES,
        blank=True, null=False
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        related_name='games',
        blank=True, null=True
    )
    rows = models.IntegerField(
        _('rows'), validators=[MinValueValidator(2), MaxValueValidator(100)],
        blank=True, null=False
    )
    cols = models.IntegerField(
        _('cols'), validators=[MinValueValidator(2), MaxValueValidator(100)],
        blank=True, null=False
    )
    mines = models.IntegerField(
        _('mines'), validators=[MinValueValidator(1), MaxValueValidator(9900)],
        blank=True, null=False
    )
    field = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=True, null=False),
            size=100,
        ),
        size=100,
    )
    game_board = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=True, null=False),
            size=100,
        ),
        size=100,
    )

    class Meta:
        ordering = ('-created_time',)
