import React from "react";
import { useState } from "react";

const RegistrationForm = (props) => {
  const [firstname, setFirstname] = useState("");
  const [middlename, setMiddlename] = useState("");
  const [lastname, setLastname] = useState("");
  const [course, setCourse] = useState("fsd1");
  const [gender, setGender] = useState("");
  const [std, setStd] = useState("+91");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [pass, setPass] = useState("");
  const [passre, setPassre] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    
    const data = {
        firstname : firstname,
        middlename : middlename,
        lastname : lastname,
        course : course,
        gender : gender,
        std : std,
        phone : phone,
        address : address,
        email : email,
        pass : pass,
        passre : passre
    }

    props.data_fetch(data);

    alert("Please Open the Console for data");

    setFirstname("");
    setMiddlename("");
    setLastname("");
    setCourse("fsd1");
    setGender("");
    setStd("+91");
    setPhone("");
    setAddress("");
    setEmail("");
    setPass("");
    setPassre("");
  };



  return (
    <form onSubmit={handleSubmit}>
      <label>
        Firstname:
        <input
          type="text"
          value={firstname}
          onChange={(x) => setFirstname(x.target.value)}
        />
      </label>
      <br />
      <label>
        Middlename:
        <input
          type="text"
          value={middlename}
          onChange={(x) => setMiddlename(x.target.value)}
        />
      </label>
      <br />
      <label>
        Lastname:
        <input
          type="text"
          value={lastname}
          onChange={(x) => setLastname(x.target.value)}
        />
      </label>
      <br />

      <label>
        Course:
        <select value={course} onChange={(x) => setCourse(x.target.value)}>
          <option value="fsd1">fsd1</option>
          <option value="fsd2">fsd2</option>
          <option value="fsd3">fsd3</option>
        </select>
      </label>
      <br />

      <label value={gender} onChange={(x) => setGender(x.target.value)}>
        Gender:
        <br />
        <input type="radio" value="Male" name="gender" /> Male <br />
        <input type="radio" value="Female" name="gender" /> Female <br />
        <input type="radio" value="Other" name="gender" /> Other <br />
      </label>

      <br />

      
      <label>
        Phone:
        <input
          type="text"
          value="+91"
          onChange={(x) => setStd(x.target.value)}
          style = {{width : "40px"}}
        />
        <input
          type="text"
          value={phone}
          onChange={(x) => setPhone(x.target.value)}
        />
      </label>

      <br />

      <label>
        Address: <br />
        <textarea
          name=""
          id=""
          cols="50"
          rows="4"
          value={address}
          onChange={(x) => setAddress(x.target.value)}
        ></textarea>
      </label>

      <br />

      <label>
        Email:
        <input
          type="text"
          value={email}
          onChange={(x) => setEmail(x.target.value)}
        />
      </label>

      <br />

      <label>
        Password:
        <input
          type="password"
          value={pass}
          onChange={(x) => setPass(x.target.value)}
        />
      </label>

      <br />

      <label>
        Re-type Password:
        <input
          type="password"
          value={passre}
          onChange={(x) => setPassre(x.target.value)}
        />
      </label>

      <br />

      <input type="submit" value="Submit" />
    </form>
  );
};

export default RegistrationForm;
