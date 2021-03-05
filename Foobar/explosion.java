public class explosion {


    public static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;

        public TreeNode(int val) {
            this.val = val;
        }
    }

    public static void buildTrees(TreeNode tree1, TreeNode tree2, int depth) {
        if (depth == 0) {
            return;
        }

        TreeNode left1 = new TreeNode(tree1.val);
        TreeNode left2 = new TreeNode(tree1.val + tree2.val);
        TreeNode right1 = new TreeNode(tree1.val + tree2.val);
        TreeNode right2 = new TreeNode(tree2.val);

        buildTrees(left1, left2, depth - 1);
        buildTrees(right1, right2, depth - 1);
    }

    public static String solution(String x, String y) {
        TreeNode tree1 = new TreeNode(Integer.parseInt(x));
        TreeNode tree2 = new TreeNode(Integer.parseInt(y));

        buildTrees(tree1, tree2, 10);

        printTree(tree1);

        return "";
    }

    private static void printTree(TreeNode tree1) {

    }

    public static void main(String[] args) {

    }
}
