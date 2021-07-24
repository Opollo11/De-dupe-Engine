import React from 'react';
import { NavLink } from 'react-router-dom';
import web from '../src/images/5576597.jpg';
const home=()=>{
    return (
        <>
         <section id="header" className="">
             <div className="container-fluid nav_bg">
               <div className="row">
                   <div className="col-10 mx-auto">
                       <div className="row">

                      
                       <div className="col-md-10 pt -5 pt-lg-0 order-2 order-lg-1  d-flex justify-content-center flex-column">
                          <h1>
                          "solve your duplication issues"

                            <strong className="brand-name">De-Dupe</strong>
                          </h1> 
                          <h2 className="my-3">
                              We are team of taleneted developers.

                          </h2>
                          <div className="mt-3">
                          {/* <button type="button" class="btn btn-info">Get started </button> */}
                          <NavLink to ="/service" className="btn-get-started" >
                              Get started
                          </NavLink>
                              
                              
                          </div>
                       </div>
                        <div className="col-lg-6 order-1 order-lg-2 header-img">
                            <img src={web} className="img-fluid animated" alt="home img" />

                        </div>
                        </div>
                   </div>

               </div>

             </div>






         </section>
        </>

    );
};
export default home;