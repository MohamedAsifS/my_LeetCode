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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode seq=new ListNode();
        ListNode start=seq;
        int carry=0;
        int adder=0;
        int val=0;
        while(l1!=null || l2!=null || carry !=0){
            val=carry;

            if(l1!=null){
                val+=l1.val;
                l1=l1.next;
            }
            if(l2!=null){
                val+=l2.val;
                l2=l2.next;
            }
           int finalone=val%10;
           carry=val/10;
           ListNode node=new ListNode(finalone);
           seq.next=node;
           seq=node;

           
        }


       return start.next; 
    }
}