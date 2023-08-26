import React from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
import { Link, useNavigate } from "react-router-dom";
import img1 from "../Assets/gradely images/Picture1.png";
import img2 from "../Assets/gradely images/Picture2.png";

import img4 from "../Assets/gradely images/Picture4.png";
import img5 from "../Assets/gradely images/Picture5.png";
import img6 from "../Assets/gradely images/Picture6.png";
import img7 from "../Assets/gradely images/Picture7.png";

import castrolLogo from "../Assets/logos/Castrol New 2023.png";
import herbalifeLogo from "../Assets/logos/Herbalife New 2023.png";
import jujutsuKaisenLogo from "../Assets/logos/Jujutsu Kaisen.png";
import laLigaLogo from "../Assets/logos/LaLiga 2023-2024 New.png";
// import levisLogo from '../Assets/logos/Levi's Original Store.png';
import pertaminaLogo from "../Assets/logos/Pertamina.png";
import toyotaFortunerLogo from "../Assets/logos/Toyota Fortuner.png";
import trustpilotLogo from "../Assets/logos/Trustpilot Stars.png";
import twitterLogo from "../Assets/logos/Twitter X Icon.png";
import yonexLogo from "../Assets/logos/Yonex.png";

const Home = () => {
  const navigate = useNavigate();
  const logos = [
    castrolLogo,
    herbalifeLogo,
    jujutsuKaisenLogo,
    laLigaLogo,
    // levisLogo,
    pertaminaLogo,
    toyotaFortunerLogo,
    trustpilotLogo,
    twitterLogo,
    yonexLogo,
  ];

  return (
    <div className="home-page">
      <Container className="heightView">
        <Row className="align-items-center heightView my-4">
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>
                Become a member of the premier and most extensive professional
                community in your industry.
              </h3>
              <p>
                Engage with industry experts to gain insights, gather valuable
                advice and stay ahead in your career.
              </p>
              <Button
                as={Link}
                variant="primary"
                to='/communities'
                
              >
                Join Community
              </Button>
            </div>
          </Col>
          <Col md={8}>
            <img src={img1} alt="Dummy" className="img-fluid" />
          </Col>
        </Row>
      </Container>
      <Container>
        <Container className="align-items-center text-center mt-4">
          <h4>Our Community Members Come From</h4>
          <div className="logo-container">
            {logos.map((logoImage, index) => (
              <img
                key={index}
                src={logoImage}
                alt={`Logo ${index}`}
                className="logo"
              />
            ))}
          </div>
        </Container>
        <Row className="align-items-center  my-4">
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>DISCOVER COMMUNITIES</h3>
              <p>
                where you can connect and form Relationships with like-minded
                individuals who have similar interests as you.
              </p>
              {/* <Button variant="primary">Join Community</Button> */}
            </div>
          </Col>
          <Col md={8} className="text-center">
            <img src={img2} alt="Dummy" className="img-fluid" />
          </Col>
        </Row>
        <Row className="align-items-center  my-4">
          <Col md={8}>
            <img src={img6} alt="Dummy" className="img-fluid" />
          </Col>
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>
                Engage in live discussions with industry leaders through Gradly
                Live.
              </h3>
              <p>
                where you can join events curated by industry professionals and
                gain valuable insights. Experience daily events that offer
                direct access to industry expertise and knowledge-sharing
                opportunities.
              </p>
              <Button as={Link} variant="primary" to="/events">
                Explore Events{" "}
              </Button>
            </div>
          </Col>
        </Row>
        <Row className="align-items-center  my-4">
          <Col md={4}>
            <div className="text-start text-md-left my-3">
              <h3>WEALTH OF RESOURCES</h3>
              <p>
                Discover valuable career growth resources curated by industry
                professionals to enhance your professional development
              </p>
              <p>
                Find a wealth of industry-driven content that can support your
                career advancement and provide valuable insights.
              </p>
              <Button
                as={Link} to='/resources'
                variant="primary"
              >
                Explore Resource
              </Button>
            </div>
          </Col>
          <Col md={8}>
            <img src={img7} alt="Dummy" className="img-fluid" />
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default Home;
