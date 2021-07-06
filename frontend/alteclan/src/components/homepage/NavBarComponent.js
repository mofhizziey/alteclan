import { useEffect, useState } from "react";
import './navbarcomponent.css';



const NavComponent = (() => {
  // Create state using hooks
  // Set state to empty array.
const [state, setstate] = useState([])
const style = {
  fontSize: "16px",
  textAlign : "right"
}
  // Update and Fetch state using hooks
 useEffect (()=> {
   console.log("useEffect")
 })

 // Render the html value
    return (
       <header className="header sticky-top">
      <nav className="navbar navbar-expand-lg navbar-light bg-white py-3 shadow-sm">
        <div className="container"><a className="navbar-brand" href="#">
            <strong className="h6 mb-0 font-weight-bold text-uppercase">alteclan</strong></a>
            
        </div>
    </nav>
</header>
      )
})

export default NavComponent;
