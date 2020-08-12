'''
Write methods to serialize and deserialize a binary tree

I need to come back to this to review it, but the basic approach is depth first
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # Top-down recursive approach
    def serialize(self, root):

        def dfs(root):
            # Base case
            if not root:
                res.append("None,")
                return

                # If we get here the node is not None and we add it's value
            res.append(str(root.val) + ",")

            # Recurse going left first
            dfs(root.left)
            dfs(root.right)

        res = []
        dfs(root)
        return "".join(res)

    def deserialize(self, data):

        def rdeserialize(l):
            if l[0] == 'None':
                l.pop(0)
                return None

            root = TreeNode(l[0])
            l.pop(0)
            root.left = rdeserialize(l)
            root.right = rdeserialize(l)
            return root

        data_list = data.split(',')
        root = rdeserialize(data_list)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))