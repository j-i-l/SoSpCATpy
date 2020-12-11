"""
This module defines the methods for social community detection.
"""


def get_groups(
        a_graph,
        method='component_infomap', return_form='membership'):
    """
    Return the grouping of the provided graph object using the specified
    method. The grouping is returned as a list of sets each holding all
    members of a group.

    Parameters
    ==========
    a_graph: :class:`igraph.Graph`
        The graph to partition
    method: str (default='component_infomap')
        String specifying which method to use. If two methods
        should be used one after the other they should be separated by `_`.
        Default: 'component_infomap' which will first consider all
        disconnected components as groups then apply infomap on all of
        those groups to optionally further split.
    return_form: str (default='membership')
        Determines the format of how the social group structure should be
        returned. Options are:

        * ``'membership'``: A list returning for each `index` node the group it
          belongs to.
        * ``'memberlists'``: Dictionary with a list of members `value` for each
          group `key`.

    Returns
    =======
    dict
      Depending on what was chosen for the `return_form` attribute, either the
      membership dict, i.e.::

          {
              node_id: group_id,
              ...
          }

      or the memberlist dict, i.e.::

          {
              group_id: [node1_id, node2_id, ...],
              ...
          }

      (value) is returned.

    """
    # methods = method.split('_')
    # For now only 'component_infomap' is allowed as procedure
    if method == 'component_infomap':
        # first the connected components
        a_graph.vs['component'] = a_graph.clusters(
                ).membership
        components = set(a_graph.vs['component'])
        # create for each component a graph and apply infomap to it
        node_membership = {}
        # print(
        #     'INFO: Found {0} disconnected components'.format(len(components))
        # )
        if components:
            # do the community detection on each component and create a
            # compound group id: component_group
            for component in components:
                _comp_graph = a_graph.subgraph(
                    [
                        node['name']
                        for node in a_graph.vs
                        if node['component'] == component
                        ]
                    )
                _infompa_comp_graph = _comp_graph.community_infomap('weight')
                _comp_graph.vs['_group'] = _infompa_comp_graph.membership
                for node in _comp_graph.vs:
                    node_membership[node['name']] = '{0}_{1}'.format(
                            node['component'], node['_group']
                            )
                del _infompa_comp_graph
        else:
            _infompa_comp_graph = a_graph.community_infomap('weight')
            a_graph.vs['group'] = _infompa_comp_graph.membership
            node_membership = {
                node['name']: node['group']
                for node in a_graph.vs
            }
        group_membership = {}
        for node in node_membership:
            try:
                group_membership[node_membership[node]].append(node)
            except KeyError:
                group_membership[node_membership[node]] = [node]
    if return_form == 'membership':
        # nbr_nodes = len(a_graph.vs['name'])
        # membership = [None]*nbr_nodes
        # for g, members in group_membership.items():
        #     for member in members:
        #         membership[member] = g
        # return membership
        return node_membership
    elif return_form == 'memberlists':
        # return [_group for _group in group_membership.values()]
        return group_membership
    else:
        return None
