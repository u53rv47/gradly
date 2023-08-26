/** @format */

import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import img5 from "../Assets/gradely images/Picture5.png";

const Events = () => {
  return (
    <div className="home-page">
      <Container className="heightView">
        <Row className="align-items-center heightView">
          <Col md={8}>
            <img src={img5} alt="Dummy" className="img-fluid" />
          </Col>
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>LIVE EVENTS</h3>
              <p>
                Get access to free LIVE events that help you explore your
                favorite fields and grow to the next level.
              </p>
              <p>
                They’re taken by industry experts having vast knowledge about
                their subject.
              </p>
              <Button as={Link} variant="primary" to="/events">
              Explore Events 
              </Button>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Events;
