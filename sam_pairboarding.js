function findCommonAncestor(root, nodeA, nodeB) {
    let smaller;
    let larger;
    if (nodeA.val < nodeB.val) {
        smaller = nodeA
        larger = nodeB
    } else if (nodeB.val < nodeA.val) {
        smaller = nodeB.val
        larger = nodeA.val
    } else {
        //tbd

    }

    if (smaller.val <= root.val && root.val <= larger.val) {
        return root.val
    } else if (root.val < smaller) {
        root = root.right
    } else {
        root = root.left
    }
    return findCommonAncestor(root, nodeA, nodeB)
    
}