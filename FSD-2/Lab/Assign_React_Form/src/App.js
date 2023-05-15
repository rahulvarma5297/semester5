import React from "react";
import Registration from "./Components/Registration";

const App = () => {
  function func(x) {
    console.log(x);
    console.log(`The firstname Entered is: ${x.firstname}`);
    console.log(`The middlename Entered is: ${x.middlename}`);
    console.log(`The lastname Entered is: ${x.lastname}`);
    console.log(`The Course Selected is: ${x.course}`);
    console.log(`The Gender Selected is: ${x.gender}`);
    console.log(`The Phone Entered is: ${x.std} ${x.phone}`);
    console.log(`The Address Entered is: ${x.address}`);
    console.log(`The Email Entered is: ${x.email}`);
    console.log(`The Password Entered is: ${x.pass}`);
    console.log(`The Password2 Entered is: ${x.passre}`);
  }
  return (
    <div>
      <Registration data_fetch={func} />
    </div>
  );
};

export default App;
