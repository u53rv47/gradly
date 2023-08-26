/** @format */

import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import img3 from "../Assets/gradely images/Picture3.png";

const Communities = () => {
  return (
    <div className="home-page">
      <Container className="heightView">
        <Row className="align-items-center heightView">
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>FIND YOUR COMMUNITY</h3>
              <p>
                Build relationships with professionals who get you. It’s the
                natural way to network.
              </p>
              <Button
                as={Link}
                variant="primary"
                to="/communities"
                // onClick={navigate("/communities")}
              >
                Join Community
              </Button>
            </div>
          </Col>
          <Col md={8}>
            <img src={img3} alt="Dummy" className="img-fluid" />
          </Col>
        </Row>
       
      </Container>
      <Container>
      <Row className="align-items-center my-5">
          <Col md={4}>
            <div className="community-links">
              <h3> POPULAR COMMUNITIES</h3>
              <ul>
                <li>Leadership Community</li>
                <li>Florida state university </li>
                <li>Human resources </li>
                <li>Luxury watches </li>
                <li>Healthcare consulting </li>
              </ul>
            </div>
          </Col>
          <Col md={4}>
            <div className="community-links">
              <h3> TRENDING COMMUNITIES</h3>
              <ul>
                <li>Leadership Community</li>
                <li>Florida state university </li>
                <li>Human resources </li>
                <li>Luxury watches </li>
                <li>Healthcare consulting </li>
              </ul>
            </div>
          </Col>
          <Col md={4}>
            <div className="community-links">
              <h3> PREFERRED COMMUNITIES</h3>
              <ul>
                <li>Leadership Community</li>
                <li>Florida state university </li>
                <li>Human resources </li>
                <li>Luxury watches </li>
                <li>Healthcare consulting </li>
              </ul>
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Communities;
