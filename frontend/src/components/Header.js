/** @format */

import React from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav, Button, Container } from 'react-bootstrap';

const Header = () => {
  return (
    <Navbar bg='dark' variant='dark' expand='lg' className='navSticky'>
      <Container>
        <Navbar.Brand as={Link} to='/' style={{fontSize:'30px'}}>
          Gradly
        </Navbar.Brand>
        <Navbar.Toggle aria-controls='navbar-nav' />
        <Navbar.Collapse id='navbar-nav' className='justify-content-between'>
          <Nav className='mr-auto'>
            <Nav.Link as={Link} to='/Home'>
              Home
            </Nav.Link>
            <Nav.Link as={Link} to='/about'>
              About
            </Nav.Link>
            <Nav.Link as={Link} to='/communities'>
              Communities
            </Nav.Link>
            <Nav.Link as={Link} to='/resources'>
              Resources
            </Nav.Link>
            <Nav.Link as={Link} to='/events'>
              Events
            </Nav.Link>
          </Nav>
          <Nav className='ml-auto gap-2'>
            <Button
              variant='outline-light'
              as={Link}
              to='/login'
              style={{ minWidth: '95px', maxWidth: '150px' }}>
              Login
            </Button>
            <Button
              variant='outline-light'
              as={Link}
              to='/signup'
              style={{ minWidth: '95px', maxWidth: '150px' }}>
              SignUp
            </Button>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Header;
