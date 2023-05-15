// alert("Welcome Rahul Varma to FSD-2 course");

function func() {
  var name = "Rahul Varma";
  alert(`Welcome ${name} to FSD-2 course`);
}

function confi_func() {
  var ans;
  if (confirm("Press a button!")) {
    ans = "You pressed OK!";
  } else {
    ans = "You pressed Cancel!";
  }
  document.getElementById("confi").innerHTML = ans;
}

function func1() {
  document.getElementById("t1").innerHTML = "Rahul Varma";
  document.getElementById("t2").innerHTML = "";
  document.getElementById("t3").innerHTML = "";
  document.getElementById("t4").innerHTML = "";
  document.getElementById("t5").innerHTML = "";
}

function func2() {
  document.getElementById("t1").innerHTML = "";
  document.getElementById("t2").innerHTML = "Charan Kumar";
  document.getElementById("t3").innerHTML = "";
  document.getElementById("t4").innerHTML = "";
  document.getElementById("t5").innerHTML = "";
}

function func3() {
  document.getElementById("t1").innerHTML = "";
  document.getElementById("t2").innerHTML = "";
  document.getElementById("t3").innerHTML = "Kamal";
  document.getElementById("t4").innerHTML = "";
  document.getElementById("t5").innerHTML = "";
}

function func4() {
  document.getElementById("t1").innerHTML = "";
  document.getElementById("t2").innerHTML = "";
  document.getElementById("t3").innerHTML = "";
  document.getElementById("t4").innerHTML = "Rohith";
  document.getElementById("t5").innerHTML = "";
}

function func5() {
  document.getElementById("t1").innerHTML = "";
  document.getElementById("t2").innerHTML = "";
  document.getElementById("t3").innerHTML = "";
  document.getElementById("t4").innerHTML = "";
  document.getElementById("t5").innerHTML = "Nikhil";
}

function del(x) {
  document.getElementById("deltab").deleteRow(x.parentNode.parentNode.rowIndex);
}

function add_data() {
  let temp = document.getElementById("deltab").getElementsByTagName("tbody")[0];

  let newRow = temp.insertRow();

  let new1 = newRow.insertCell();
  let newtxt1 = document.createTextNode("NA");
  new1.appendChild(newtxt1);

  let new2 = newRow.insertCell();
  let newtxt2 = document.createTextNode("NA");
  new2.appendChild(newtxt2);

  let new3 = newRow.insertCell();
  let newtxt3 = document.createTextNode("NA");
  new3.appendChild(newtxt3);

  let new4 = newRow.insertCell();
  let newtxt4 = document.createTextNode("NA");
  new4.appendChild(newtxt4);

  let new5 = newRow.insertCell();
  let newtxt5 = document.createTextNode("NA");
  new5.appendChild(newtxt5);

  let new6 = newRow.insertCell();
  let newtxt6 = document.createTextNode("NA");
  new6.appendChild(newtxt6);

  let new7 = newRow.insertCell();
  let newtxt7 = document.createTextNode("NA");
  new7.appendChild(newtxt7);
}

class subject {
  constructor(name, faculty) {
    this.name = name;
    this.faculty = faculty;
  }
  // Methods
  msg() {
    return `In this semester ${this.sub} is running`;
  }
}

class ssham extends subject {
  constructor(name, faculty) {
    super(name, faculty);
    this.type = type;
  }
}

function semester_subjects() {
  let sub1 = new subject("FSD-2 ->", "himangshu");
  let sub2 = new subject("GTA -> ", "odelu");
  let sub3 = new subject("DM -> ", "amit");
  let sub4 = new subject("ML -> ", "viswanath");
  let sub5 = new subject("CC -> ", "bhemappa");
  let sub6 = new subject("CCI -> ", "raji");
  /*
    let subjects = []
    subjects.push({ name: 'FSD-2 -> ', faculty: 'himangshu' })
    subjects.push({ name: 'GTA -> ', faculty: 'odelu' })
    subjects.push({ name: 'DM -> ', faculty: 'amit' })
    subjects.push({ name: 'ML -> ', faculty: 'viswanath' })
    subjects.push({ name: 'CC -> ' , faculty: 'bhemappa'})
    subjects.push({ name: 'CCI -> ', faculty: 'raji' })
    subjects.push({ name: 'QRA -> ', faculty: 'sabana' })
    */
  let txt = "";
  txt += sub1.name + sub1.faculty + "<br>";
  txt += sub2.name + sub2.faculty + "<br>";
  txt += sub3.name + sub3.faculty + "<br>";
  txt += sub4.name + sub4.faculty + "<br>";
  txt += sub5.name + sub5.faculty + "<br>";
  txt += sub6.name + sub6.faculty + "<br>";
/*
  let sub7 = new ssham("QRA -> ", "sabana", "ssham");
  txt += sub7.name + sub7.faculty + "<br>";
  txt += sub7.name + "is " + sub7.type + "course";*/

  document.getElementById("sub").innerHTML = txt;
}


function semester_subjects_array(){
    let subjects = []
    subjects.push({ name: 'FSD-2 -> ', faculty: 'himangshu' })
    subjects.push({ name: 'GTA -> ', faculty: 'odelu' })
    subjects.push({ name: 'DM -> ', faculty: 'amit' })
    subjects.push({ name: 'ML -> ', faculty: 'viswanath' })
    subjects.push({ name: 'CC -> ' , faculty: 'bhemappa'})
    subjects.push({ name: 'CCI -> ', faculty: 'raji' })
    subjects.push({ name: 'QRA -> ', faculty: 'sabana' })
    let txt = "";
    for (let index = 0; index < subjects.length; index++) {
        txt += subjects[index].name + subjects[index].faculty +'<br>';
    }
    document.getElementById("sub2").innerHTML = txt;
}