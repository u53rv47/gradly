/** @format */

import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
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

const App = () => {
  return (
    <Router>
      <Header />
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/home' element={<Home />} />
        <Route path='/about' element={<About />} />
        <Route path='/communities' element={<Communities />} />
        <Route path='/resources' element={<Resources />} />
        <Route path='/events' element={<Events />} />
      </Routes>
      <Footer />
    </Router>
  );
};

export default App;
