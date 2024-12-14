/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {

    

        

        ListNode temp=head;
        int count=0;   
      
        while(temp!=null){
            count++;
            temp=temp.next;
            
        }

        temp=head;
        int half=(count/2)-1;
        int[] box=new int[half+1];
       
       
        int sec=0,res=0;
        while(temp!=null){
            if (count <= 2){
                res+=temp.val;
                
            }
            else if (sec <= half){
                box[sec]=temp.val;
                sec++;
            }
            else{ 
                
                box[half]=(box[half]+temp.val);
                res=Math.max(box[half],res);
                half--;
            }
            temp=temp.next;
        }
         

        
        return res;
    }
}