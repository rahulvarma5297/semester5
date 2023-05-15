let numbers = [1, 2, 3, 4];

const ans = numbers.reduce((acc, x) => {
    return acc + x;
}, 10)
console.log(ans);