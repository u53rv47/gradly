/** @format */

import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './components/Header.js';
import Home from './components/Home.js';
import Feed from './components/Feed.js';
import Communities from './components/Communities.js';
import Resources from './components/Resources.js';
import Events from './components/Events.js';
import About from './components/About.js';
import Footer from './components/Footer.js';
import './App.css';
import './components/style.css';
import Login from './components/login/Login.js';
import SignUp from './components/login/signup/SignUp.js';
import Profession from './components/login/signup/Profession.js';
import Field from './components/login/signup/Field.js';
import Suggestion from './components/login/signup/Suggestion.js';


const App = () => {
  console.log("Home:", process.env.REACT_APP_BASE_URL)
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
};

const AppRoutes = () => {
  const location = useLocation();

  // Check if the current location is "/login"
  const isLoginRoute =
    location.pathname === '/login' || location.pathname === '/signup';

  return (
    <React.Fragment>
      {!isLoginRoute && <Header />}
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/home' element={<Home />} />
        <Route path='/feed' element={<Feed />} />
        <Route path='/communities' element={<Communities />} />
        <Route path='/resources' element={<Resources />} />
        <Route path='/events' element={<Events />} />
        <Route path='/about' element={<About />} />
        <Route path='/login' element={<Login />} />
        <Route path='/signup' element={<SignUp />} />
        <Route path='/signup/profession' element={<Profession />} />
        <Route path='/signup/field' element={<Field />} />
        <Route path='/signup/suggest' element={<Suggestion />} />
      </Routes>
      {!isLoginRoute && <Footer />}
    </React.Fragment>
  );
};

export default App;
