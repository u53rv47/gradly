/** @format */

import * as React from 'react';
import Avatar from '@mui/material/Avatar';
import Button from '@mui/material/Button';
import CssBaseline from '@mui/material/CssBaseline';
import TextField from '@mui/material/TextField';
import FormControlLabel from '@mui/material/FormControlLabel';
import Checkbox from '@mui/material/Checkbox';
import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import Container from '@mui/material/Container';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link } from 'react-router-dom';
import IconButton from '@mui/material/IconButton';
import Visibility from '@mui/icons-material/Visibility';
import VisibilityOff from '@mui/icons-material/VisibilityOff';
import { FormControl, FormLabel, Radio, RadioGroup } from '@mui/material';

function Copyright(props) {
  return (
    <Typography
      variant='body2'
      color='text.secondary'
      align='center'
      {...props}>
      {'Copyright © '}
      <Link color='inherit' href='https://Gradly.com/'>
        Gradly
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}

const defaultTheme = createTheme();

export default function SignUp() {
  const [showPassword, setShowPassword] = React.useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = React.useState(false);

  // State variables for field errors and messages
  const [firstNameError, setFirstNameError] = React.useState('');
  const [lastNameError, setLastNameError] = React.useState('');
  const [emailError, setEmailError] = React.useState('');
  const [dateOfBirthError, setDateOfBirthError] = React.useState('');
  const [phoneNumberError, setPhoneNumberError] = React.useState('');
  const [passwordError, setPasswordError] = React.useState('');
  const [confirmPasswordError, setConfirmPasswordError] = React.useState('');

  const handleShowPasswordToggle = () => {
    setShowPassword(!showPassword);
  };

  const handleShowConfirmPasswordToggle = () => {
    setShowConfirmPassword(!showConfirmPassword);
  };

  const handleSubmit = (event) => {
    event.preventDefault();

    // Resetting error messages on each submission attempt
    setFirstNameError('');
    setLastNameError('');
    setEmailError('');
    setDateOfBirthError('');
    setPasswordError('');
    setConfirmPasswordError('');
    setPhoneNumberError('');

    const data = new FormData(event.currentTarget);
    console.log(data);

    // Validation checks
    const isValidDate = (dateString) => {
      // const pattern = /^\d{2}\/\d{2}\/\d{4}$/;
      const pattern = /(((0|1)[0-9]|2[0-9]|3[0-1])\/(0[1-9]|1[0-2])\/((19|20)\d\d))$/;
      return pattern.test(dateString);
    };

    const isPasswordValid = (password) => {
      return password.length >= 8; // Example: Minimum length of 8 characters
    };

    const isValidPhoneNumber = (phoneNumber) => {
      const pattern = /^[0-9]{10}$/; // Assuming 10-digit phone number
      return pattern.test(phoneNumber);
    };

    const dateOfBirth = data.get('dateOfBirth');
    if (!isValidDate(dateOfBirth)) {
      setDateOfBirthError('Invalid date format');
      return;
    }

    const password = data.get('password');
    if (!isPasswordValid(password)) {
      setPasswordError('Password must be at least 8 characters long');
      console.log(password);
      return;
    }

    const confirmPassword = data.get('confirmPassword');
    if (password !== confirmPassword) {
      setConfirmPasswordError('Passwords do not match');
      return;
    }

    const phoneNumber = data.get('phoneNumber');
    if (!isValidPhoneNumber(phoneNumber)) {
      setPhoneNumberError('Invalid phone number');
      return;
    }

    console.log({
      firstName: data.get('firstName'),
      lastName: data.get('lastName'),
      gender: data.get('gender'),
      dateOfBirth,
      email: data.get('email'),
      password,
      confirmPassword,
      phoneNumber,
    });
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
            <LockOutlinedIcon />
          </Avatar>
          <Typography component='h1' variant='h5'>
            Sign up
          </Typography>
          <Box
            component='form'
            noValidate
            onSubmit={handleSubmit}
            sx={{ mt: 3 }}>
            <Grid container spacing={2}>
              <Grid item xs={12} sm={6}>
                <TextField
                  autoComplete='given-name'
                  name='firstName'
                  required
                  fullWidth
                  id='firstName'
                  label='First Name'
                  autoFocus
                  error={!!firstNameError}
                  helperText={firstNameError}
                  onChange={(event) => {
                    setFirstNameError('');
                  }}
                />
              </Grid>
              <Grid item xs={12} sm={6}>
                <TextField
                  required
                  fullWidth
                  id='lastName'
                  label='Last Name'
                  name='lastName'
                  autoComplete='family-name'
                  error={!!lastNameError}
                  helperText={lastNameError}
                  onChange={(event) => {
                    setLastNameError('');
                  }}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  id='email'
                  label='Email Address'
                  name='email'
                  autoComplete='email'
                  error={!!emailError}
                  helperText={emailError}
                  onChange={(event) => {
                    setEmailError('');
                  }}
                />
              </Grid>
              <Grid item xs={12} container alignItems='center' justify='center'>
                <Grid item xs={6}>
                  <FormControl component='fieldset'>
                    <FormLabel component='legend'>Gender</FormLabel>
                  </FormControl>
                </Grid>
                <Grid item xs={6}>
                  <Grid>
                    <RadioGroup name='gender' row>
                      <FormControlLabel
                        value='male'
                        control={<Radio />}
                        label='Male'
                      />
                      <FormControlLabel
                        value='female'
                        control={<Radio />}
                        label='Female'
                      />
                    </RadioGroup>

                    <RadioGroup name='gender' row>
                      <FormControlLabel
                        value='not-specified'
                        control={<Radio />}
                        label='Prefer Not to Say'
                      />
                    </RadioGroup>
                  </Grid>
                </Grid>
              </Grid>
              <Grid item xs={6}>
                <TextField
                  required
                  fullWidth
                  type='date'
                  id='dateOfBirth'
                  name='dateOfBirth'
                  autoComplete='bday'
                  error={!!dateOfBirthError}
                  helperText={dateOfBirthError}
                  onChange={(event) => {
                    setDateOfBirthError('');
                  }}
                />
              </Grid>
              <Grid item xs={6}>
                <TextField
                  // required
                  fullWidth
                  id='phoneNumber'
                  label='Phone Number'
                  name='phoneNumber'
                  autoComplete='tel'
                  error={!!phoneNumberError}
                  helperText={phoneNumberError}
                  onChange={(event) => {
                    setPhoneNumberError('');
                  }}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name='password'
                  label='Password'
                  type={showPassword ? 'text' : 'password'}
                  id='password'
                  autoComplete='new-password'
                  InputProps={{
                    endAdornment: (
                      <IconButton onClick={handleShowPasswordToggle} edge='end'>
                        {showPassword ? <VisibilityOff /> : <Visibility />}
                      </IconButton>
                    ),
                  }}
                  error={!!passwordError}
                  helperText={passwordError}
                  onChange={(event) => {
                    setPasswordError('');
                  }}
                />
              </Grid>
              <Grid item xs={12}>
                <TextField
                  required
                  fullWidth
                  name='confirmPassword'
                  label='Confirm Password'
                  type={showConfirmPassword ? 'text' : 'password'}
                  id='confirmPassword'
                  autoComplete='new-password'
                  InputProps={{
                    endAdornment: (
                      <IconButton
                        onClick={handleShowConfirmPasswordToggle}
                        edge='end'>
                        {showConfirmPassword ? (
                          <VisibilityOff />
                        ) : (
                          <Visibility />
                        )}
                      </IconButton>
                    ),
                  }}
                  error={!!confirmPasswordError}
                  helperText={confirmPasswordError}
                  onChange={(event) => {
                    setConfirmPasswordError('');
                  }}
                />
              </Grid>
            </Grid>
            <Button
              type='submit'
              fullWidth
              variant='contained'
              sx={{ mt: 3, mb: 2 }}>
              Sign Up
            </Button>
            <Grid container justifyContent='flex-end'>
              <Grid item>
                <Link to='/login' variant='body2'>
                  Already have an account? Sign in
                </Link>
              </Grid>
            </Grid>
          </Box>
          <Copyright sx={{ mt: 5 }} />
        </Box>
      </Container>
    </ThemeProvider>
  );
}
