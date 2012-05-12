from warnings import warn

from dist import *
try:
    from local import *
except ImportError:
    warn('Using sample for local settings directly.')
    from local_sample import *
