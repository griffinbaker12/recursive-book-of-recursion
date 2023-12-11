root  = {'data': 'A', 'children': []}
node2 = {'data': 'B', 'children': []}
node3 = {'data': 'C', 'children': []}
node4 = {'data': 'D', 'children': []}
node5 = {'data': 'E', 'children': []}
node6 = {'data': 'F', 'children': []}
node7 = {'data': 'G', 'children': []}
node8 = {'data': 'H', 'children': []}
root['children'] = [node2, node3]
node2['children'] = [node4]
node3['children'] = [node5, node6]
node5['children'] = [node7, node8]

# preorder access a node's data before traversing its child nodes
# can be useful to copy of a tree because you need to create the parent nodes before the children
def preorderTraversel(node):
    print(node['data'])  
    if len(node['children']) > 0:
        for child in node['children']:
            preorderTraversel(child)
     
# preorderTraversel(root)

# visit children before accessing the node's data
# used when deleting a tree and ensuring that no child nodes are "orphaned" by deleting their parents first
def postorderTraversal(node):
    for child in node['children']:
        postorderTraversal(child)
    print(node['data'])

postorderTraversal(root)

# in order refers to accessing the node's data after processing
# the node on the L and before the node on the R 

root2 = root = {'data': 'A', 'children': [{'data': 'B', 'children': 
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children': 
[{'data': 'E', 'children': [{'data': 'G', 'children': []}, 
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

# the depth of a node is the number of edges between a root node and the node in question
def getDepth(node):
    if len(node['children']) == 0:
        return 0
    childrenMaxDepth = 0
    for child in node['children']:
        depth = getDepth(child)
        if depth > childrenMaxDepth:
            childrenMaxDepth = depth
    return 1 + childrenMaxDepth

print(getDepth(root2))
