"""
Module holding functions for a quantitative comparison of groupings
"""
from sklearn import metrics

from .spatial import get_groups as get_spatial_groups


def social_vs_spatial(node_locations, soc_membership, **kwargs):
    r"""

    This method relies on the
    :func:`~.sklearn.metrics.homogeneity_completeness_v_measure` method form
    the :obj:`.sklearn.metrics` package.

    .. seealso::

      | V-Measure:
      | A conditional entropy-based external cluster evaluation measure
      | Andrew Rosenberg and Julia Hirschberg, 2007
      | http://acl.ldc.upenn.edu/D/D07/D07-1043.pdf

    Parameters
    ==========
    node_locations: dict(int, tuple)
      Specify for each node `key` its position `value` in the form of a (x, y)
      tuple.
    soc_membership: dict
      Holds for each node (key) the social group affiliation (value).

    Returns
    =======
    homogeneity, completeness, v-measure: tuple
      Homogeneity, completeness and v-measure as computed by the
      :func:`~.sklearn.metrics.homogeneity_completeness_v_measure`.
    """
    nbr_clusters = len(set(soc_membership.values()))
    spatial_membership = get_spatial_groups(
            node_locations, nbr_clusters, **kwargs
        )
    nodes = sorted(soc_membership.keys())
    # create lists for both memberships with the same ordering
    _soc_membership = [soc_membership[node] for node in nodes]
    _spat_membership = [spatial_membership[node] for node in nodes]
    h, c, v = metrics.homogeneity_completeness_v_measure(
            _soc_membership, _spat_membership
    )
    return h, c, v
