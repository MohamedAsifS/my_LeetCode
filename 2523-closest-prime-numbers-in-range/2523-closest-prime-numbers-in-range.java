class Solution {
    public int[] closestPrimes(int left, int right) {
    // same we use seive algorithim here

    int[] res=new int[2];

    res[0]=-1;
    res[1]=-1;

    if (right < 2){
        return res;
        
    }

    boolean[] prime=new boolean[right+1];
    Arrays.fill(prime,true);
    prime[0]=false;
    prime[1]=false;

    for(int i=2;i*i<=right;i++){
        if(prime[i]){
            for(int j=i*i;j<=right;j+=i){
                prime[j]=false;
            }
        }

    }
    ArrayList<Integer> arr=new ArrayList<>();
    for(int i=left;i<=right;i++){
        if(prime[i]){
            arr.add(i);
        }

    }
    if(arr.size()<2){
        return res;
    }
    int count=111111111;
    for(int i=1;i<arr.size();i++){
        int cal=arr.get(i)-arr.get(i-1);
     
        if(cal<count){
            count=cal;
            res[0]=arr.get(i-1);
            res[1]=arr.get(i);
        }
    }
        
    return res;}
}