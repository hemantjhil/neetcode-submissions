from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Initially, every node is its own parent.
        # Therefore, there are n separate components.
        parent = [i for i in range(n)]

        # Stores the size of each component.
        # Initially, every component contains one node.
        size = [1] * n

        def find(node):
            """
            Finds the root parent of a node.
            Path compression makes future lookups faster.
            """
            root = node

            # Find the root of the component
            while root != parent[root]:
                root = parent[root]

            # Compress the path by directly connecting nodes
            # to the root parent.
            while node != root:
                next_node = parent[node]
                parent[node] = root
                node = next_node

            return root

        def union(node1, node2):
            """
            Combines the components containing node1 and node2.
            Returns 1 if two components were merged,
            otherwise returns 0 if they were already connected.
            """
            root1 = find(node1)
            root2 = find(node2)

            # Both nodes already belong to the same component
            if root1 == root2:
                return 0

            # Attach the smaller component under the larger one
            if size[root2] > size[root1]:
                parent[root1] = root2
                size[root2] += size[root1]
            else:
                parent[root2] = root1
                size[root1] += size[root2]

            # Two components became one
            return 1

        # Initially, every node is a separate component
        components = n

        # Each successful union reduces the component count by one
        for node1, node2 in edges:
            components -= union(node1, node2)

        return components
