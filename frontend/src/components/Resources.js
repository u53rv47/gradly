/** @format */

import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import img4 from "../Assets/gradely images/Picture4.png";

const Resources = () => {
  return (
    <div className="home-page">
      <Container className="heightView">
        <Row className="align-items-center heightView">
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>CAREER INSIGHTS</h3>
              <p>
                Get up to speed on the latest workplace chatter. Discover new
                ways to level up at work.
              </p>
              <Button
                as={Link}
                variant="primary"
                to="/resources"
              >
                Explore Resource
              </Button>
            </div>
          </Col>
          <Col md={8}>
            <img src={img4} alt="Dummy" className="img-fluid" />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Resources;
