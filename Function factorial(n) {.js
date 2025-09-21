Function factorial(n) {
    let n=5;

    if(n===0) {
        return 1;
    } 
     else {
        return n*factorial(n-1);
     }
    }

    console.log(factorial(n));