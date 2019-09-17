def subset_sum(lst, k):
    """
    >>> subset_sum([], 0)
    True
    >>> subset_sum([], 4)
    False
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    if k == 0:
        return True
    elif k < 0 or len(lst) == 0:
        return False
    else:
        return subset_sum(lst[1:], k) or subset_sum(lst[1:], k - lst[0])

class Tree(object):
    def __init__(self, value, branches = []):
        self.value = value
        self.branches = branches

    def __str__(self):
        pass



    def __repr__(self):
        pass

null = 'null'

class Link(object):
    def __init__(self, value, next = null):
        self.value = value
        self.next = next

    def __str__(self):
        current_node = self
        result = '<' + str(current_node.value)
        while current_node.next != null:
            current_node = current_node.next
            result += ' ' + str(current_node.value)
        result += '>'
        return result     

    def __repr__(self):
        result = 'Link(' + str(self.value)
        if self.next != null:
            result += ', ' + self.next.__repr__() + ')'
        else:
            result += ')'
        return result


def long_paths(tree, n):
    """Return a list of all paths in tree with length at least n.
    >>> t = Tree(3, [Tree(4), Tree(4), Tree(5)])
    >>> left = Tree(1, [Tree(2), t])
    >>> mid = Tree(6, [Tree(7, [Tree(8)]), Tree(9)])
    >>> right = Tree(11, [Tree(12, [Tree(13, [Tree(14)])])])
    >>> whole = Tree(0, [left, Tree(13), mid, right])
    >>> for path in long_paths(whole, 2):
    ...     print(path)
    ...
    <0 1 2>
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 6 9>
    <0 11 12 13 14>
    >>> for path in long_paths(whole, 3):
    ...     print(path)
    ...
    <0 1 3 4>
    <0 1 3 4>
    <0 1 3 5>
    <0 6 7 8>
    <0 11 12 13 14>
    >>> long_paths(whole, 4)
    [Link(0, Link(11, Link(12, Link(13, Link(14)))))]
    """
    if len(tree.branches) > 0:
        paths_of_branches = map(lambda branch: long_paths(branch, n - 1) ,tree.branches)
        child_paths = []
        for item in paths_of_branches:
            child_paths += item
        return [Link(tree.value, item) for item in child_paths]
    else:
        if n <= 0:
            return [Link(tree.value)]
        else:
            return []
