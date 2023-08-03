/** @format */

import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Routes,
  useLocation,
} from 'react-router-dom';
import 'bootstrap/dist/css/bootstrap.min.css';
import About from './components/About';
import Home from './components/Home';
import Header from './components/Header';
import Footer from './components/Footer';
import Communities from './components/Communities';
import Resources from './components/Resources';
import Events from './components/Events';
import './App.css';
import './components/style.css';
import Login from './components/login/Login';

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
