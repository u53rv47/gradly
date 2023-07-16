/** @format */

import React from 'react';
import { Container, Row, Col, Button } from 'react-bootstrap';
import dummyImage from '../Assets/Picture1.png';

const Home = () => {
  return (
    <div className='home-page'>
      <Container className='h-100'>
        <Row className='align-items-center h-100'>
          <Col md={6}>
            <div className='text-start text-md-left my-3'>
              <h3>
                Become a member of the premier and most extensive professional
                community in your industry.
              </h3>
              <p>
                Engage with industry experts to gain insights, gather valuable
                advice and stay ahead in your career.
              </p>
              <Button variant='primary'>Join Community</Button>
            </div>
          </Col>
          <Col md={6}>
            <img src={dummyImage} alt='Dummy' className='img-fluid' />
          </Col>
        </Row>

      </Container>
    </div>
  );
};

export default Home;
