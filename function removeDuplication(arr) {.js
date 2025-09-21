function removeDuplication(arr) {

    let arr=["A","B","C","D"];
    return[...new Set(arr)];
}

console.log(removeDuplication(arr));