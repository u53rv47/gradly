/** @format */

import React, { useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faLinkedin, faGoogle } from '@fortawesome/free-brands-svg-icons';

// import './Login.css';

const Login = () => {
  const googleClientId =
    '192577503971-iuehjh6pm3ka82f1i3f62iuaicl8jgom.apps.googleusercontent.com';

  useEffect(() => {
    // Load Google Platform API library
    const initGoogleAPI = () => {
      const script = document.createElement('script');
      script.src = 'https://apis.google.com/js/platform.js';
      script.async = true;
      script.onload = () => {
        // Initialize Google Platform API
        window.gapi.load('auth2', () => {
          window.gapi.auth2.init({
            client_id: googleClientId,
          });
        });
      };
      document.body.appendChild(script);
    };

    initGoogleAPI();

    return () => {
      // Clean up the added script when the component is unmounted
      const script = document.querySelector(
        'script[src="https://apis.google.com/js/platform.js"]'
      );
      if (script) {
        document.body.removeChild(script);
      }
    };
  }, []);

  const handleLogin = (provider) => {
    if (provider === 'LinkedIn') {
    } else if (provider === 'Google') {
      window.gapi.auth2
        .getAuthInstance()
        .signIn()
        .then(
          (googleUser) => {
            const profile = googleUser.getBasicProfile();
            console.log('Google login successful!');
            console.log('ID: ' + profile.getId());
            console.log('Name: ' + profile.getName());
            console.log('Email: ' + profile.getEmail());
            // You can perform additional actions with the retrieved user information here
          },
          (error) => {
            console.error('Google login failed:', error);
          }
        );
    }
  };

  return (
    <div className='login-container'>
      <h2>Login</h2>
      <form>
        <div className='form-group'>
          <label htmlFor='emailOrPhone'>
            please enter you credential to log in:
          </label>
          <input
            type='text'
            id='emailOrPhone'
            name='emailOrPhone'
            placeholder='Enter your email'
            // Add necessary event handlers to handle user input
          />
        </div>
        <div className='form-group'>
          <button type='submit'>Login</button>
        </div>
      </form>
      <div className='separator'>
        <span>OR</span>
      </div>
      <div className='social-buttons'>
        <button onClick={() => handleLogin('LinkedIn')}>
          <FontAwesomeIcon icon={faLinkedin} className='social-icon' />
          Continue with LinkedIn
        </button>
        <button onClick={() => handleLogin('Google')}>
          <FontAwesomeIcon icon={faGoogle} className='social-icon' />
          Continue with Google
        </button>
      </div>
    </div>
  );
};

export default Login;
