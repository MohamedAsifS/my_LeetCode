/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode searchBST(TreeNode root, int val) {

        TreeNode temp=root;

        while(temp.right != null && temp.val != val && temp.left!=null){
             System.out.println(temp.val);
            if (temp.val == val){
                System.out.println(temp.val);
               
                return temp;
            
            }
            else if(val < temp.val){
                  
                temp=temp.left;
                System.out.println(temp.val);
              

            }
            else{
                temp=temp.right;
            }
        }
         if (temp.val ==val){
            return temp;
         }
              
        
        return null;
        
    }
}