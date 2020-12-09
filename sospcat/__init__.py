"""
The module exposes the functions :func:`get_social_groups` and
:func:`compare_soc_spat`.

:func:`get_social_groups` is defined in :mod:`.sospcat.social` as
:func:`.spspcat.social.get_groups`.

:func:`compare_soc_spat` is defined in :mod:`.sospcat.compare` as
:func:`.spspcat.social.social_vs_spatial`.

.. moduleauthor:: J. I. Liechti
"""

from ._version import __version__  # noqa: F401

from .social import get_groups as get_social_groups  # noqa: F401
from .compare import social_vs_spatial as compare_soc_spat  # noqa: F401

__all__ = ['get_social_groups', 'compare_soc_spat']
