let fsd = {
    sub1: "FSD-1",
    sub2: "FSD-2",
    coordi: "Academic",
    faculty: {
        sec1: "Dr. Subu",
        sec2: "him",
        sec3: "bhem"
    },
    printFSD: function(){
        return this.sub2 + " is teaching"
    }
}

// console.log(fsd);
// console.log(fsd.sub1);
// console.log(fsd.faculty.sec1);
console.log(fsd.printFSD());

let subjects = {
    1 : "FSD-1",
    2 : "ML",
    3 : "DATA MINING",
    4 : "GTA",
    5 : "CLOUD COMPUTING"
}

// console.log(subjects);
console.log(subjects[1]);

