class A{
    static field = 10;
}

let a = new A();
A.prototype.field = 20;
let b = new A();
// b.field = 30;

console.log(a.field);
console.log(b.field);
console.log(A.field);
