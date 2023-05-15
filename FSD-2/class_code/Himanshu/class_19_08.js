let fsd2 = {
    sub: "Fsd 2",
    faculty: "HS",
    section : {
        secA: 'SK',
        secB: 'BH'
    },
    printed: function(){
        return this.sub + ' taugh by ' + this.section.secA
    }
}

// console.log(fsd2.printed());
let check = 'printed'
console.log(fsd2[check]());