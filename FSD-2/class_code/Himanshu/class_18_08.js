let a = 5;
let b = 5.0;
let c = 'Rahul Varma';
let d = true;
let e = null;
let f;
let g = 'a'

console.log(typeof(a));
console.log(typeof(b));
console.log(typeof(c));
console.log(typeof(d));
console.log("this is "+ typeof(e));
console.log(typeof(f+1));
console.log(typeof(g));

console.log(e+1);
console.log(f+1);
console.log(typeof(NaN));




setTimeout(function aa() {console.log('a')}, 1000);
setTimeout(function bb() {console.log('b')}, 500);
setTimeout(function cc() {console.log('c')}, 0);

function dd(){
    console.log('d');
}
dd();
