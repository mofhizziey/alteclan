import { useEffect, useState } from "react";
const WelcomeComponent = (() => {

const style={

  opacity: "0.9",
  backgroundSize: "cover",
  padding: "50px",

}

    return (
      <div >
      <div style={{backgroundImage: "url('./mainWelcome.jpg')"}}  className="container-fluid">
         <div className="container text-center">
             <h4>WELCOME TO OUR CLAN</h4>
             <p  className="lead text-center">EVERTHING ALTE</p>
         </div>

        </div>
      </div>
    )
  })

  export default WelcomeComponent;
