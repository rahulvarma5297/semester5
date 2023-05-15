console.log('a');

setTimeout(()=>{
    Promise.resolve()
    .then(
        ()=> console.log('b')
    )
}, 500)

function c (){
    setTimeout(()=>{
        console.log('c');
    }, 500)
}

setTimeout(()=>{
    console.log('d');
}, 1000)

c();