/** @format */

import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import About from './components/About.js';
import Home from './components/Home.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';
import Communities from './components/Communities.js';
import Resources from './components/Resources.js';
import Events from './components/Events.js';
import './App.css';
import './components/style.css';
import Login from './components/login/Login.js';

const App = () => {
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
};

const AppRoutes = () => {
  const location = useLocation();

  // Check if the current location is "/login"
  const isLoginRoute = location.pathname === '/login';

  return (
    <React.Fragment>
      {!isLoginRoute && <Header />}
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/home' element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route path='/communities' element={<Communities />} />
        <Route path='/resources' element={<Resources />} />
        <Route path='/events' element={<Events />} />
        <Route path='/login' element={<Login />} />
      </Routes>
      {!isLoginRoute && <Footer />}
    </React.Fragment>
  );
};

export default App;
