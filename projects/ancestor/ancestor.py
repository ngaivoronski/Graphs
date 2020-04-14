
def earliest_ancestor(ancestors, starting_node):
    # set up the generation count
    count=0

    def ancestor_recursion(ancestors, current_node, count):
        # set up a list for the parents
        parents = []
        # iterate through the list of anscestors and find the parents
        for k,v in ancestors:
            if v == current_node:
                parents.append(k)
        
        # if there are no parents left, return a tuple with the final node and generation count
        if len(parents) == 0:
            return (current_node, count)
        # if there is one parent, add one to the generation count and rerun the function for that parent
        elif len(parents) == 1:
            return ancestor_recursion(ancestors, parents[0], count + 1)
        # if there are two parents, run the function for both parents
        elif len(parents) == 2:
            first_tree = ancestor_recursion(ancestors, parents[0], count + 1)
            second_tree = ancestor_recursion(ancestors, parents[1], count + 1)
            # take the result with the greater generation count
            if first_tree[1] > second_tree[1]:
                return first_tree
            elif second_tree[1] > first_tree[1]:
                return second_tree
            # if generation count is equal, use the branch with the lowest numeric ID
            else:
                if first_tree[0] > second_tree[0]:
                    return second_tree
                else:
                    return first_tree
    
    result = ancestor_recursion(ancestors, starting_node, count)

    if result[1] == 0:
        return -1
    else:
        return result[0]