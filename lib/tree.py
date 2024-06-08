class Tree:
    def __init__(self, root=None):
        self.root = root

  # ------------------------ USING DEPTH --------------------------
    # def get_element_by_id(self, id):
    #     if not self.root:
    #         return None  # Return None if the tree is empty

    #     nodes_to_visit = [self.root]

    #     while nodes_to_visit:
    #         current_node = nodes_to_visit.pop(0)  # Pop the first element (LIFO for DFS when combined with prepend operation)
    #         if current_node['id'] == id:
    #             return current_node  # Return the node if its id matches the given id
    #         nodes_to_visit = current_node.get('children', []) + nodes_to_visit  # Prepend children to the front of the list
        
    #     return None  # Return None if no node with the given id is found
    

    # # ----------------USING BREADTH ---------------------------
    def get_element_by_id(self, id):
        if not self.root:
            return None
        nodes_to_visit = [self.root]

        while nodes_to_visit:
            current_node = nodes_to_visit.pop(0)
            if current_node['id'] ==id:
                return current_node
            nodes_to_visit = nodes_to_visit + current_node.get('children', [])

        return None
