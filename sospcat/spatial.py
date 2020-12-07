"""
Module to define the spatial based partitioning
"""
from sklearn.cluster import KMeans


def get_groups(
        node_locations, nbr_clusters,
        return_form='membership', random_state=None,
        **kwargs
        ):
    """
    Perform k-means clustering on the provided node locations.

    Parameters
    ==========
    node_locations: dict
      Specify for each node `key` its position `value` in the form of a (x, y)
      tuple.
    nbr_clusters: int
      The number of clusters to find.
    return_form: str (default='membership')
        Determines the format of how the social group structure should be
        returned. Options are:

        * ``'membership'``: A list returning for each `index` node the group it
          belongs to.
        * ``'memberlists'``: Dictionary with a list of members `value` for each
          group `key`.
    random_state : int, RandomState instance, default=None
        Determines random number generation for centroid initialization. Use
        an int to make the randomness deterministic.

    Returns
    =======
    members: dict
      Depending on what was chosen for the `return_form` attribute, either the
      membership dict, i.e. for each node (key) the group affiliation (value,
      or the memberlist dict, i.e. for each group (key) a list of nodes
      (value) is returned.

    """
    nodes = sorted(node_locations.keys())
    positions = [node_locations[n] for n in nodes]
    membership_predict = KMeans(
        n_clusters=nbr_clusters,
        random_state=random_state,
        **kwargs
    ).fit_predict(positions)
    group_membership = {
            node: membership_predict[i]
            for i, node in enumerate(nodes)
        }
    # note: could use default dict here
    kmeans_grouping = {i: [] for i in range(nbr_clusters)}
    for i, memb in enumerate(membership_predict):
        kmeans_grouping[memb].append(nodes[i])
    if return_form == 'membership':
        membership = [None]*len(nodes)
        for g, members in kmeans_grouping.items():
            for member in members:
                membership[member] = g
        return membership
        return group_membership
    elif return_form == 'memberlists':
        return kmeans_grouping
    else:
        return None
