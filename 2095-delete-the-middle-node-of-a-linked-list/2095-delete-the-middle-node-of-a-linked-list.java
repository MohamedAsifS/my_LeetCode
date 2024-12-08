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
    public ListNode deleteMiddle(ListNode head) {
        
        int len=0;
        ListNode temp =head;
        while(temp != null){
            len++;
            temp=temp.next;
        }
        if (len==1){
            return null;
        }
        if (len==2){
            head.next=null;
            return head;
        }
        int mid=len/2;
        temp=head;
        ListNode prev=null;
        int count=0;
        while(temp!=null){
            if (count==mid){

                break;
            }
            count++;
            prev=temp;
            temp=temp.next;
        }
        prev.next=temp.next;
        return head;
    }
}