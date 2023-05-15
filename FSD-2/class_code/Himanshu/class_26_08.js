/*
function fsd(subName, cName){
    this.name = subName
    this.cnam = cName
}
//If we keep obj.prototype then it will change to that particular object only
// other wise it will change to all other objects
fsd.prototype.chName = function(){
    return this.cnam;
}

let obj1 = new fsd("fsd", "d");
console.log(obj1);
console.log(obj1.chName());
*/

class dept {
  constructor(subject, coursecode, credit) {
    this.sub = subject;
    this.cour = coursecode;
    this.cr = credit;
  }
  // Methods
  msg() {
    return `In this semester ${this.sub} is running`;
  }

  // Static Method
  static add(a, b) {
    return a + b;
  }
}

let sub1 = new dept ("FSD-2", "CS001", 4)
console.log(sub1.msg());
console.log(dept.add(4,5));

//Inheritence
class CSE extends dept{
    constructor(subject, coursecode, credit, elective, track){
        super(subject, coursecode, credit);
        this.ele = elective;
        this.tr = track;
    }

    msg() {
        return `${this.sub}  ${this.tr}`;
      }
}

let sub2 = new CSE("FSD-3", "CS003", 4,"PE","fsd");
console.log(sub2.msg());
