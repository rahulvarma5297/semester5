import React from 'react'
import RegistrationForm from './RegistrationForm'

const Registration = (props) => {
  function func(x){
    props.data_fetch(x);
  }
  return (
    <div>
      <RegistrationForm data_fetch={func}/>
    </div>
  )
}

export default Registration