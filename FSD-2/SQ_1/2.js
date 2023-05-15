class fsd {
    constructor(arg1, arg2) {
        this.a = arg1;
        this.b = arg2;
        this.display = function () {
            console.log("Running");
        };
    }
}

let obj1 = new fsd(20, 40);
let obj2 = new fsd(2, 2);
fsd.prototype.cre = 4;
console.log(obj1.cre);
console.log(obj2.cre);

