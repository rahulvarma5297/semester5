let promise = new Promise(function(resolve, reject){
    const x = 1;
    const y = "1";
    if(x == y){
        resolve()
    }else{
        reject()
    }
})

/*
promise.then(
    function(res){
        console.log("Both are Same " + res);
    },

    function(rej){
        console.log("Both are Not Same " + rej);
    }
)*/

promise.then(res =>{
    console.log("Both are Same ");
}).catch(rej => {
    console.log("Both are Not Same ");
})


// async function FSD2(){
//     const x = 1;
//     const y = "1";
//     if(x == y){
//         await console.log("Correct");
//     }else{
//         await console.log("Error");
//     }
// };

// console.log("MSG-2");
// console.log(FSD2());
// console.log("MSG-3");


async function FSD2(){
    const x = 1;
    const y = "1";
    if(x == y){
        await console.log("Correct");
    }else{
        await console.log("Error");
    }
};
console.log(FSD2());
