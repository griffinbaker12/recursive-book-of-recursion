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

def extendTree(node, newNodes={'val': 0}):
    if len(node['children']) == 0:
        newNodes['val'] += 1
        node['children'].append({'data': "new_node" + str(newNodes['val']), 'children': []})
    else:
        for child in node['children']:
            extendTree(child, newNodes)
        
extendTree(root)

def inOrderTraversal(node):
    for child in node['children']:
        inOrderTraversal(child)
        print(child['data'])

inOrderTraversal(root)
