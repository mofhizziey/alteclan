import { useState, useEffect } from "react"

const OurFeaturedBrands = (() => {
    return (
      <div>
        <section className="">
            <div className="container-fluid p-2 text-center">

                    <div className="col-lg-8 mx-auto p-3">
                        <h2>Our featured brands</h2>
                        <div className="row">
                          <div className='container-fluid col-lg-6'>
                              <div className="card mx-auto  col-10 mt-5"> <img className='mx-auto img-thumbnail' src="./resources/images/cd592433c6cb1720b7fbb3f263e913d7.jpg" width="auto" height="auto" />
                                  <div className="card-body text-center mx-auto">
                                      <div className='cvp'>
                                          <h5 className="card-title font-weight-bold">brand name</h5>
                                        <a href="#" className="btn btn-dark">VIEW BRAND</a>
                                      </div>
                                  </div>
                              </div>
                          </div>
                          <div className='container-fluid col-lg-6'>
                              <div className="card mx-auto  col-10 mt-5"> <img className='mx-auto img-thumbnail' src="./resources/images/cd592433c6cb1720b7fbb3f263e913d7.jpg" width="auto" height="auto" />
                                  <div className="card-body text-center mx-auto">
                                      <div className='cvp'>
                                          <h5 className="card-title font-weight-bold">brand name</h5>
                                        <a href="#" className="btn btn-dark">VIEW BRAND</a>
                                      </div>
                                  </div>
                              </div>
                          </div>
                            <div className='container-fluid col-lg-6'>
                                <div className="card mx-auto  col-10 mt-5"> <img className='mx-auto img-thumbnail' src="./resources/images/cd592433c6cb1720b7fbb3f263e913d7.jpg" width="auto" height="auto" />
                                    <div className="card-body text-center mx-auto">
                                        <div className='cvp'>
                                            <h5 className="card-title font-weight-bold">brand name</h5>
                                          <a href="#" className="btn btn-dark">VIEW BRAND</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className='container-fluid col-lg-6'>
                                <div className="card mx-auto col-10 mt-5"> <img className='mx-auto img-thumbnail' src="./resources/images/cd592433c6cb1720b7fbb3f263e913d7.jpg" width="auto" height="auto" />
                                    <div className="card-body text-center mx-auto">
                                        <div className='cvp'>
                                            <h5 className="card-title font-weight-bold">brand name</h5>
                                          <a href="#" className="btn btn-dark">VIEW BRAND</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <hr />
                        <p className="text-muted text-center lead">This is some of our brand partners, for more intensive information on their products click the view brand button.</p>
                    </div>
                </div>

        </section>
      </div>
    )
  })

  export default OurFeaturedBrands;
