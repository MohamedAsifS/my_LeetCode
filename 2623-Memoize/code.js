/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let last_val ={}
 
    console.log(fn)
    return function(...args) {
     const key=JSON.stringify(args)
    
       if(key in last_val){
         return last_val[key]}
      
       let res=fn.apply(this,args)
        last_val[key]=res
       
       return res
       
        

       }
       
      
      
        
    }
    



/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */