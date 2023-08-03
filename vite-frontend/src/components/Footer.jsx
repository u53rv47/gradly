/** @format */

import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import { FaFacebook, FaTwitter, FaInstagram, FaLinkedin } from 'react-icons/fa';
import { Link } from 'react-router-dom';

const Footer = () => {
  return (
    <footer className='bg-dark text-light py-5'>
      <Container>
        <Row>
          <Col md={4} className='mb-4'>
            <h5>gradly</h5>
            <p>Footer content goes here.</p>
            <div className='d-flex'>
              <a
                href='https://www.facebook.com'
                target='_blank'
                rel='noopener noreferrer'
                className='social-icon'>
                <FaFacebook />
              </a>
              <a
                href='https://www.twitter.com'
                target='_blank'
                rel='noopener noreferrer'
                className='social-icon'>
                <FaTwitter />
              </a>
              <a
                href='https://www.instagram.com'
                target='_blank'
                rel='noopener noreferrer'
                className='social-icon'>
                <FaInstagram />
              </a>
              <a
                href='https://www.linkedin.com'
                target='_blank'
                rel='noopener noreferrer'
                className='social-icon'>
                <FaLinkedin />
              </a>
            </div>
          </Col>
          <Col md={8}>
            <Row>
              <Col sm={4} className='mb-4'>
                <h5>Main Links</h5>
                <ul className='list-unstyled'>
                  <li>
                    <Link to='/'>Home</Link>
                  </li>
                  <li>
                    <Link to='/about'>About</Link>
                  </li>
                  <li>
                    <Link to='/communities'>Communities</Link>
                  </li>
                  <li>
                    <Link to='/resources'>Resources</Link>
                  </li>
                  <li>
                    <Link to='/events'>Events</Link>
                  </li>
                </ul>
              </Col>
              <Col sm={4} className='mb-4'>
                <h5>Menus</h5>
                <ul className='list-unstyled'>
                  <li>
                    <Link to='/cookie-consent'>Cookie Consent Tool</Link>
                  </li>
                  <li>
                    <Link to='/students'>Students</Link>
                  </li>
                  <li>
                    <Link to='/community-guidelines'>Community Guidelines</Link>
                  </li>
                  <li>
                    <Link to='/faq'>FAQ</Link>
                  </li>
                </ul>
              </Col>
              <Col sm={4} className='mb-4'>
                <h5>Contact</h5>
                <p>123 Street, City, Country</p>
                <p>Email: info@example.com</p>
                <p>Phone: +1 234 567 890</p>
              </Col>
            </Row>
          </Col>
        </Row>
      </Container>
    </footer>
  );
};

export default Footer;
