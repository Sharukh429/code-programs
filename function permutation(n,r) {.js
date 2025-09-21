function permutation(n,r) {
    if(n<r) return 0;
    
    let result = n;
    for(let i=1; i<r; i++) 
     result *= n-1;
    
    return result;
}

console.log("4P 1:",permutation(4,1));
console.log("4p 2:",permutation(4,2));