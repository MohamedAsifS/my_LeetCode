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
    public ListNode oddEvenList(ListNode head) {

        ListNode odd=new ListNode(2),even=new ListNode(2),temp=head;
        int count=1;
        ListNode First_even=even,First_odd=odd;
        
         
        while(temp!=null){
            if(count%2!=0){
                odd.next=temp;
                odd=odd.next;
            }
            else{
                even.next=temp;
                even=even.next;
            }
            temp=temp.next;
            count++;
        }
        
        even.next=null;
        odd.next=First_even.next;
   

         return First_odd.next ;
    }
}