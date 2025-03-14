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

        ListNode templast=head;

        while(templast!=null && templast.next!=null){
            len++;
            templast=templast.next;
        }

         if(len==0){
            return null;
        }
         if(k==0 || k>=1 && len==1){
            return head;
        
}
       
        
        int need=k%len;
         if (k==len || need==0){
            return head;
        }
        len=len-need;
        ListNode temp=head;

        

       
       
        System.out.println(len);

        while(len>1){
            temp=temp.next;
            len--;

        }
        System.out.println(need+" "+len+" "+temp.val);

        ListNode join= new ListNode();
        join.next=temp.next;
        join=temp.next;
        temp.next=null;

        templast.next=head;

        







        System.out.println(len);



        return join;
        
    }
}