

const DiscoverProducts = (() => {
const divStyle={
  backgroundColor:"white"
}

    return (
      <div>
      <div className="py-5" style={divStyle} id="venue">
          <div className="container">
              <div className="row bg-success text-light animate-in-down">
                  <div className="p-4 col-md-6 align-self-center text-color">
                      <p className="m-0">Feel comfortable, and purchase items</p>
                      <h2>Discover the products</h2>
                      <p className="my-4">The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here</p>
                  </div>
                  <div className="p-0 col-md-6">
                      <div className="carousel slide" data-ride="carousel" id="carousel1">
                          <div className="carousel-inner" role="listbox">
                              <div className="carousel-item"> <img className="d-block img-fluid w-100" src="./resources/images/54bc7bba47ae8d7fd478023a801a6481.jpg" alt="first slide" />>
                                  <div className="carousel-caption">
                                      <h3>Simura Hotels</h3>
                                      <p>Good architecture, services</p>
                                  </div>
                              </div>
                              <div className="carousel-item active"> <img className="d-block img-fluid w-100" src="./resources/images/b41ddacb79c68517c0904bb8a7e5c1d7.jpg" data-holder-rendered="true" />
                                  <div className="carousel-caption">
                                      <h3>Hauzkhas Village Bar</h3>
                                      <p>Enjoy our long drink</p>
                                  </div>
                              </div>
                              <div className="carousel-item"> <img className="d-block img-fluid w-100" src="./resources/images/61dc1a9c9497672befce333d943c59ca.jpg" data-holder-rendered="true" />
                                  <div className="carousel-caption">
                                      <h3>Cooking Hemorto</h3>
                                      <p>Tastes it better</p>
                                  </div>
                              </div>
                          </div> <a className="carousel-control-prev" href="#carousel1" role="button" data-slide="prev"> <span className="carousel-control-prev-icon" aria-hidden="true"></span> <span className="sr-only">Previous</span> </a> <a className="carousel-control-next" href="#carousel1" role="button" data-slide="next"> <span className="carousel-control-next-icon" aria-hidden="true"></span> <span className="sr-only">Next</span> </a>
                      </div>
                  </div>
              </div>
          </div>
      </div>
      </div>
    )
  })

  export default DiscoverProducts;
