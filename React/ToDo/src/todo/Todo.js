import React from "react"
import { useState } from "react"

function Todo() {
  const [name, setName] = useState('')
  const [address, setAddress] = useState('')
  const [students, setStudents] = useState([])

  return (
  <>
    <h1>Students Name</h1>
      <input 
      value={name}
      onChange={e => setName(e.target.value)}
      type="text" />
    <h1>Students Address</h1>
      <input
      value={address}
      onChange={e => setAddress(e.target.value)}
      type="text" />

      <button onClick={() => {
        setStudents([
          ...students, 
          {name: name, address: address}
        ])
      }}>
        Add Student</button>
        
        <ul>
          {students.map(student => (
            <li>{student.name} {student.address}</li>
          ))}
        </ul>
    </>
)
}

export default Todo