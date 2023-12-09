import React from "react"
import ".//Header.css"

function Header () {
  return (
    <div className="header">
      <ul className="header-list">
        <li className="header-list_item"><a className="header_link" href="/">Home</a></li>
        <li className="header-list_item"><a className="header_link" href="/School">School</a></li>
        <li className="header-list_item"><a className="header_link" href="/About">About-me</a></li>
      </ul>
    </div>
  );

}


export default Header