"""
Module holding functions for a quantitative comparison of groupings
"""
from sklearn import metrics


def compare_groupings(membership_1, membership_2):
    """
    Compute similarity between membership lists.

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
    membership_1: list
      The group affiliation of each node in the (reference) grouping.
    membership_2: list
      The group affiliation of each node in the (reference grouping.



    Returns
    =======
    homogeneity, completeness, v-measure: tuple
      Homogeneity, completeness and v-measure as computed by the
      :func:`~.sklearn.metrics.homogeneity_completeness_v_measure`.
    """
    h, c, v = metrics.homogeneity_completeness_v_measure(
            membership_1, membership_2
    )
    return h, c, v
