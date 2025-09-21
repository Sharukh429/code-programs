function insertElements() {
    let arr=[1,2,3,4,5]
    let indesx = 2;
    let element=-99;

    arr.splice(indexedDB,0,element);

    console.log(arr);
}

insertElement();