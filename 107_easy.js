


function TreeNode(val, left, right) {
      this.val = (val===undefined ? 0 : val)
      this.left = (left===undefined ? null : left)
      this.right = (right===undefined ? null : right)
 }
let fifteen = new TreeNode(15)
let seven = new TreeNode(7)
let left = new TreeNode(9)
let right = new TreeNode(20,fifteen,seven)
let root = new TreeNode(3, left, right)
var levelOrderBottom = function (root) {
    const result = [];
    let level = 0

    searchHelper(root, level, result)

    return result;
};

function searchHelper(root, level, result) {
    if (root === null) return result

    if(level === result.length) {
        result.unshift([])
        result[0].push(root.val)
        result[0].push(searchHelper(root.left, level + 1, result))
        result[0].push(searchHelper(root.right, level + 1, result))
    }

        return result;
}

let circular = levelOrderBottom(root);
l