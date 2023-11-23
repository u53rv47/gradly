/** @format */
import * as React from 'react';
import { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import queryString from 'query-string';
import axios from 'axios';
import {
  Button,
  // Card,
  Typography,
  Avatar,
  CssBaseline,
  TextField,
  FormControlLabel,
  Checkbox,
  Grid,
  Box,
  Container,
} from '@mui/material';
import { LockOpenOutlined } from '@mui/icons-material';
import { BsLinkedin } from 'react-icons/bs';
import { FcGoogle } from 'react-icons/fc';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link } from 'react-router-dom';

function Copyright(props) {
  return (
    <Typography
      variant='body2'
      color='text.secondary'
      align='center'
      {...props}>
      {'Copyright © '}
      <Link color='inherit' href='https://mui.com/'>
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const defaultTheme = createTheme();

export default function Login() {
  const navigate = useNavigate();
  const location = useLocation();

  async function authenticate(state, code) {
    const token = localStorage.getItem('refresh');

    if (token) {
      console.log('Token exists');
      navigate(-1);
    } else {
      const url = 'http://localhost:8000/api/auth/o/google-oauth2/';
      const data = queryString.stringify({
        code: code,
        state: state,
      });
      const res = await axios.post(url, data, {
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        },
        withCredentials: true,
      });
      if (res.status === 201) {
        console.log('Response: ' + res.data);
        localStorage.setItem('access', res.data.access);
        localStorage.setItem('refresh', res.data.refresh);
      } else console.log(res);
    }
  }

  useEffect(() => {
    const values = queryString.parse(location.search);
    const state = values.state ? values.state : null;
    const code = values.code ? values.code : null;
    console.log('State: ' + state);
    console.log('Code: ' + code);
    if (state && code) {
      authenticate(state, code);
    }
  }, [location]);

  async function signupWithGoogle() {
    try {
      const url =
        process.env.REACT_APP_AUTH_URL + '/o/google-oauth2/?redirect_uri=http://localhost:3000/';

      const res = await axios.get(url, {
        headers: {
          'Content-Type': 'application/json',
        },
        withCredentials: true,
      });

      console.log('Res: ' + res.data);
      window.location.href = res.data.authorization_url;
    } catch (err) {
      console.log('Error logging in');
    }
  }

  const handleSubmit = (event) => {
    event.preventDefault();
    const data = new FormData(event.currentTarget);
    const email = data.get('email');
    const password = data.get('password');
    console.log({
      email,
      password
    });
    const url = process.env.REACT_APP_AUTH_URL + "/jwt/create/";
    axios.post(url, { email, password }).then((res) => {
      console.log(res.data);
      localStorage.setItem("access", res.data.access);
      localStorage.setItem("refresh", res.data.refresh);
      navigate(-1);
    }).catch((err) => {
      if (err)
        console.log(err);
    });
  };
  const handleSocialLogin = (loginWith) => {
    if (loginWith === 'google') {
    }
  };
  return (
    <ThemeProvider theme={defaultTheme}>
      <Container component='main' maxWidth='xs'>
        <CssBaseline />
        <Box
          sx={{
            marginTop: 8,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
          }}>
          <Avatar sx={{ m: 1, bgcolor: 'secondary.main' }}>
            <LockOpenOutlined onClick={() => { navigate("/") }} />
          </Avatar>
          <Typography component='h1' variant='h5'>
            Sign in
          </Typography>
          <Box
            component='form'
            onSubmit={handleSubmit}
            noValidate
            sx={{ mt: 1 }}>
            <TextField
              margin='normal'
              required
              fullWidth
              id='email'
              label='Email Address'
              name='email'
              autoComplete='email'
              autoFocus
            />
            <TextField
              margin='normal'
              required
              fullWidth
              name='password'
              label='Password'
              type='password'
              id='password'
              autoComplete='current-password'
            />
            <FormControlLabel
              control={<Checkbox value='remember' color='primary' />}
              label='Remember me'
            />
            <Grid container spacing={2}>
              <Grid item xs={6}>
                <Button
                  variant='contained'
                  fullWidth
                  color='primary'
                  startIcon={<FcGoogle />}
                  onClick={() => handleSocialLogin('google')}
                // Add margin to the right for spacing
                >
                  Google
                </Button>
              </Grid>
              <Grid item xs={6}>
                <Button
                  variant='contained'
                  fullWidth
                  color='primary'
                  startIcon={<BsLinkedin />}
                  onClick={() => handleSocialLogin('linkedin')}>
                  LinkedIn
                </Button>
              </Grid>
            </Grid>

            <Button
              type='submit'
              fullWidth
              variant='contained'
              sx={{ mt: 3, mb: 2 }}>
              Sign In
            </Button>
            <Grid container>
              <Grid item xs>
                <Link to='/signup' variant='body2'>
                  Forgot password?
                </Link>
              </Grid>
              <Grid item>
                <Link to='/signup' variant='body2'>
                  {"Don't have an account? Sign Up"}
                </Link>
              </Grid>
            </Grid>
          </Box>
        </Box>
        <Copyright sx={{ mt: 8, mb: 4 }} />
      </Container>
    </ThemeProvider>
  );
}
