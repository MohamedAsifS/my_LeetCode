class Solution {
    public int minimumRecolors(String blocks, int k) {
        int white=0;
        for(int i=0;i<k;i++){
            if(blocks.charAt(i)=='W')
              white++;
            }
        int r=k;
        int res=white;
        for(int i=0;i<blocks.length()-k;i++){
            if(blocks.charAt(i)=='W'){
                white--;
            }

            if(blocks.charAt(r)=='W'){
                white++;
            }
            r++;

            res=Math.min(white,res);

            
        }
        return res;}
        
    }
