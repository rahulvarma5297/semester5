function check() {
    let phone = document.getElementById("phone").value;
    let email = document.getElementById("email").value;
    let roll = document.getElementById("roll").value;

    if(!email.includes('@') || !email.includes('.')){
        alert('invalid email');
        return false;
    }
    else if (phone.length != 10) {
        alert("Phone number is not of 10 Digits");
        return false;
    } else if (!roll.startsWith("S2020")) {
        alert("Please enter Roll number starting with S2020");
        return false;
    } else {
        alert("Registration Successfull");
        return true;
    }
}