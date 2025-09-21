
let fact = (n) =>
[...Array(n+1).keys()]
.filter(
    (i) =>n%i ===0

);

console.log(fact(12)));