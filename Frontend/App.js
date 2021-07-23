import React from 'react';
import home from './home';
import About from './About';
import Contact from './Contact';
import Services from './Services';
import "../node_modules/bootstrap/dist/css/bootstrap.min.css";
import "../node_modules/bootstrap/dist/js/bootstrap.bundle";
import Navbar from "./Navbar";
import { Redirect, Route, Switch } from 'react-router';
const App=()=>{
    return (
        <>
        <Navbar />
         <Switch>
             <Route  exact path="/" component={home}/>
             <Route  exact path="/about" component={About}/>
             <Route  exact path="/contact" component={Contact}/>
             <Route   exact path="/service" component={Services}/>
             <Redirect to="/" />
             <home/>

         </Switch>
        </>
    );
};
export default App;