async function f() {
    let result = "first";
    let promise = new Promise((resolve, reject) => {
    setTimeout(() => resolve("second"), 1000)
    }
    );
    result = await promise;
    console.log(result);
    }
    f();