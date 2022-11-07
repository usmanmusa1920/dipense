from django.contrib.auth import get_user_model
User = get_user_model()

from .find import ICHECKP
from .track import STRACK
from .trigger import WH


class GEO(ICHECKP):
  pass


class SMTK(STRACK):
  pass


class HW(WH):
  pass
