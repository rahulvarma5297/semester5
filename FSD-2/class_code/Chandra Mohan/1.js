/*
const myfunc = () => {
    console.log("Chandra Mohan");
}

myfunc();

const func = (name) => {
    console.log(name);
}

const f = () => "Rahul Varma";

func("Rahul Varma");
console.log(f());


const multiply = (num) => num * 2;
console.log(multiply(2));
*/

/*
const arr = [1,2,3]
const newarr = [...arr, 4];

console.log(newarr);

const person = {
    name : "Chandra"
}
const newPerson = {
    ...person,
    age : 29
}
console.log(newPerson);
*/

const f = (...args) => {
    return args.filter(x => x === 1);
}
console.log(f(1,2,3));

const {name, age}={name:'Chandra',age:35};

console.log(name);
console.log(age);

const arr = [1,2,3,4,5,6,7,8]

const temp = arr.filter((x) => {
    return x % 2 != 1;
})
console.log(temp);