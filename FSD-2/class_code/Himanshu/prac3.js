console.log('a');

setTimeout(() => {
    Promise.resolve().then(() => console.log('b'), 100)
})

function c() {
    setTimeout(() => {
        console.log('c');
    }, 1000)
}

setTimeout(() => {
    console.log('d');
}, 1000)

c()