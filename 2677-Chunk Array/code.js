/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    if(arr.length==0){
        return []
    }
    else if(arr.length < size){
        return [[...arr]]
    }
    let res=[]
    let current=size;
    for(let i=0;i<arr.length;i+=size){
        res.push(arr.slice(i,current))
        current+=size

        
    }
    return res
    
};
