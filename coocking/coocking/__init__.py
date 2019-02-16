from __future__ import absolute_import

# Впевнюємося в тому, що додаток завжди імпортуюється при завантаженні Django і що shared_task використовує його.
from .celery import app as celery_app