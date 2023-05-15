console.log('a');



function c (){
    setTimeout(()=>{
        console.log('c');
    }, 100)
    
}

setTimeout(()=>{
    console.log('b');
}, 100)

setTimeout(()=>{
    console.log('d');
}, 100)

c();