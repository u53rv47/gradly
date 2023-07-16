/** @format */

import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { Navbar, Nav, Button, Container, Offcanvas } from 'react-bootstrap';

const Header = () => {
  const [showOffcanvas, setShowOffcanvas] = useState(false);

  const handleCloseOffcanvas = () => setShowOffcanvas(false);
  const handleShowOffcanvas = () => setShowOffcanvas(true);

  return (
    <>
      <Navbar bg='dark' variant='dark' expand='lg'>
        <Container>
          <Navbar.Brand as={Link} to='/'>
            Gradly
          </Navbar.Brand>
          <Navbar.Toggle
            aria-controls='navbar-nav'
            onClick={handleShowOffcanvas}
          />
          <Navbar.Collapse id='navbar-nav' className='justify-content-between'>
            <Nav className='mr-auto'>
              <Nav.Link as={Link} to='/home'>
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
                style={{ maxWidth: '150px' }}>
                Login
              </Button>
              <Button
                variant='outline-light'
                as={Link}
                to='/signup'
                style={{ maxWidth: '150px' }}>
                SignUp
              </Button>
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>

      <Offcanvas
        show={showOffcanvas}
        onHide={handleCloseOffcanvas}
        placement='end'>
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>Menu</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <Nav className='flex-column'>
            <Nav.Link as={Link} to='/home'>
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
            <Button
              variant='outline-light'
              as={Link}
              to='/login'
              className='mt-3'
              style={{ width: '100%' }}>
              Login
            </Button>
            <Button
              variant='outline-light'
              as={Link}
              to='/signup'
              className='mt-2'
              style={{ width: '100%' }}>
              Signup
            </Button>
          </Nav>
        </Offcanvas.Body>
      </Offcanvas>
    </>
  );
};

export default Header;
