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
    public ListNode rotateRight(ListNode head, int k) {
        int len=1;

        if(head==null || head.next==null) return head;

        ListNode templast=head;

        while(templast!=null && templast.next!=null){
            len++;
            templast=templast.next;
        }

       
       
        
        int need=k%len;
         if (need==0)return head;
        
        len=len-need;
        ListNode temp=head;

        

       
       
        

        while(len>1){
            temp=temp.next;
            len--;

        }
       

        ListNode join= new ListNode();
        join.next=temp.next;
        join=temp.next;
        temp.next=null;

        templast.next=head;

        







        



        return join;
        
    }
}