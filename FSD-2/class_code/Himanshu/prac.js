// class A{
//     #field = 10;
//     set field(val){
//         this.#field = val;
//     }

//     get field(){
        // return this.#field;
//     }
// }

// let a = new A();
// console.log(a.field);

// a.field = 20;
// console.log(a.field);


class A{
    static filed = 10;
}

let a = new A();
// a.filed = 20;
let b = new A();
// b.filed = 30;
// A.filed = 40;
console.log(a.filed);
console.log(b.filed);
console.log(A.filed);