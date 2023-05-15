// Fulfilled
// pending
// reject

// resolve, reject

// let promise = new Promise(function(a, b) {
//     const x = 1;
//     const y = "1";
//     console.log("first");
//     if(x == y) {
//     a();
//     } else {
//     b();
//     } });
//     console.log("second");
    
// promise.then(function(){
// console.log('Both grades are same');}).catch(function () {
// console.log('Both grades are not same');});

async function FSD2() {
    const x = 1;
    const y = "1";
    if(x == y) {
    await console.log("Correct");
    } else {
    await console.log("Error");
    } };
    
    console.log("MSG 2");
    console.log(FSD2());
    console.log("MSG 3");

// setTimeout(myFunction, 3000);
// function myFunction() {
// console.log("FSD 2 is running");
// }

// class CLASS {
//     constructor(arg1, arg2) {
//     this.a = arg1;
//     this.b = arg2;
//     }
    
//     // Methods
//     msg(){
//     return `Text running`;
//     }
//     // Static method
//     static add(a, b){
//     return a + b;
//     }
//     }

// obj1 = new CLASS(100,200);
// console.log(obj1.msg());
// // console.log(obj1.add(10,20));
// console.log(CLASS.add(34, 5))


// function fsd(subName, cName){
//     this.name = subName
//     this.cnam = cName
// }
    
// //include new prototype
// // fsd.prototype.chName = function nfs(){
// //     return this.cnam;
// // }
    
// let c1 = new fsd("FSD1", "CSE")
// console.log(c1)
// fsd.prototype.fac = "Raj";
// console.log(c1.fac)
// let c2 = new fsd("FSD2", "CSE")
// console.log(c2.fac);

// function fsd() {
//     this.cname = 'FSD-1';
//     this.dept = 'CSE';
//     }
    
//     fsd.prototype.cre = 4;
    
//     let fsdObj1 = new fsd();
//     console.log(fsdObj1.cre);
    
//     let fsdObj2 = new fsd();
//     console.log(fsdObj2.cre);


let cars = ["Saab", "Volvo", "BMW"];
let ncar = cars
ncar[0] = "Mahindra"

console.log(cars)
