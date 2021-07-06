import 'bootstrap/dist/css/bootstrap.min.css';
import NavComponent from "./components/homepage/NavBarComponent";
import SearchComponent from "./components/homepage/SearchBarComponent";
import Releases from "./components/homepage/ReleasesComponents"
import OurFeaturedBrands from './components/homepage/OurFeaturedBrandsComponents'
import PartOfClan from './components/homepage/PartOfClanComponent'
import DiscoverProducts from './components/homepage/DiscoverProductsComponents'
import WelcomeComponent from './components/homepage/WelcomeComponent'
import Footer from './components/homepage/FooterComponent'
import { useState, useEffect } from 'react'



function App() {
     // Create state using hooks
     const [state, setState] = useState([])

      return (
        <div className="">

          <NavComponent />
          <SearchComponent />
          <Releases />
          <OurFeaturedBrands />
          <DiscoverProducts />
          <PartOfClan />
          <Footer />
        </div>
      )
}

export default App;
