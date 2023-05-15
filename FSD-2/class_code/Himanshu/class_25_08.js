
let cars = ["Tata", 34, "Volvo", "BMW"];
// We can also keep it blank (undefined).
// we can keep a list
// let cars = [,[1,2,3,4]]
let ncar = [...cars]
ncar[0] = "Mahindra";

console.log(cars);
console.log(cars[0]);


// Constructor
/*
function subjectDetails(track, subname, type, credit) {
  this.tr = track;
  this.sun = subname;
  this.ty = type;
  this.cr = credit;

  this.msg = function () {
    console.log(`${this.sun} is in 4th semester and with credits ${this.cr}`);
  };
}

sub1 = new subjectDetails("FSD", "fsd1", "PC", 4)
sub2 = new subjectDetails("special", "nlp", "PE", 3)
console.log(sub1);
console.log(sub1.msg());
*/

// Prototype

function fsd(){
    this.cname = 'fsd-1',
    this.dept = 'cse'
}

let fsd1 = new fsd();
fsd1.cre = 4;
// alert(fsd1.cre);

let fsd2 = new fsd();
// alert(fsd2.cre);