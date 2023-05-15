let a = ["a", "a", "b", "b", "c", "c"];
b = a.filter((x) => x == "a" || x == "b");
console.log(a);
console.log(b);

c = b.reduce ((acc, x) => {
    return acc + x;
}, 0)
console.log(c);