# 1-mashq
def diameter_of_binary_tree(root):
    diameter = [0]
    def depth(node):
        if not node: return 0
        left = depth(node.left)
        right = depth(node.right)
        diameter[0] = max(diameter[0], left + right)
        return 1 + max(left, right)
    depth(root)
    return diameter[0]
# 2-mashq
def serialize(root):
    def helper(node):
        if not node: 
            result.append("null")
            return
        result.append(str(node.val))
        helper(node.left)
        helper(node.right)
    result = []
    helper(root)
    return ",".join(result)

def deserialize(data):
    def helper():
        val = next(vals)
        if val == "null": return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split(","))
    return helper()
