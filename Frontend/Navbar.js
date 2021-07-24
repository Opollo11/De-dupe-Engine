import React from 'react';
import {NavLink} from 'react-router-dom'

const Navbar =() =>{
    return (
        <>
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
  <div className="container-fluid">
    <NavLink className="navbar-brand" to="/">De-Dupe </NavLink>
    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span className="navbar-toggler-icon"></span>
    </button>
    <div className="collapse navbar-collapse" id="navbarSupportedContent">
      <ul className="navbar-nav ms-auto mb-2 mb-lg-0">
        <li className="nav-item">
          <NavLink 
          exact
          activeClassName='menu_active'
          className="nav-link active" 
          aria-current="page" to="/">
            Home
            </NavLink>
        </li>
        <li className="nav-item">
          <NavLink 
          activeClassName='menu_active'
          className="nav-link" 
          to="/service">
            Services
            </NavLink>
        </li>
        <li className="nav-item">
          <NavLink 
          activeClassName='menu_active'
          className="nav-link" to="/about">About</NavLink>
        </li>
        <li className="nav-item">
          <NavLink 
          activeClassName='menu_active'
          className="nav-link" to="/contact">Contact</NavLink>
        </li>
      
      </ul>
      {/* <form className="d-flex">
        <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button className="btn btn-outline-success" type="submit">Search</button>
      </form> */}
    </div>
  </div>
</nav>
        </>
    );
};
export default Navbar;