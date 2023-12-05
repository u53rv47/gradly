/** @format */

import axios from 'axios';
import * as React from 'react';
import { useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Button, CssBaseline, Grid, Box, Typography, Container } from '@mui/material';
import { setProfession } from '../../../store/user/userSlice';

const defaultTheme = createTheme();

export default function Profession() {
	const navigate = useNavigate();
	const [clicked, setClicked] = React.useState(false);

	const dispatch = useDispatch();

	const handleClicked = (event) => {
		console.log("Clicked:", clicked);
		setClicked(!clicked);

	};
	const handleSubmit = (event) => {
		event.preventDefault();
		const profession = clicked ? "Student" : "Professional";
		const access = localStorage.getItem("access");
		const url = process.env.REACT_APP_AUTH_URL + "/users/me/";
		axios.patch(url, { profession }, {
			headers: {
				'Authorization': `Bearer ${access}`
			}
		}).then((res) => {
			navigate("/signup/field");
			dispatch(setProfession({ profession: res.data.profession }));
		}).catch((err) => {
			if (err) {
				console.log(err);
				navigate("/login");
			}
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
					<Typography component='h1' variant='h5'>
						Let us know about you
					</Typography>
					<Box
						component='form'
						noValidate
						onSubmit={handleSubmit}
						sx={{ mt: 3 }}>
						<Grid container spacing={2}>
							<Grid item xs={12}>
								<Box sx={{
									background: clicked ? "white" : "lightblue",
									border: 1,
									borderRadius: "10px",
									display: 'flex',
									flexDirection: 'column',
									alignItems: 'center',
								}}
									onClick={handleClicked}>I'm a professional</Box>
							</Grid>

							<Grid item xs={12}>
								<Box sx={{
									background: clicked ? "lightblue" : "white",
									border: 1,
									borderRadius: "10px",
									display: 'flex',
									flexDirection: 'column',
									alignItems: 'center',
								}}
									onClick={handleClicked}>I'm a student</Box>
							</Grid>
						</Grid>
						<Button
							type='submit'
							fullWidth
							variant='contained'
							sx={{ mt: 3, mb: 2, textTransform: 'none' }}>
							Next
						</Button>
					</Box>
					<Copyright sx={{ mt: 5 }} />
				</Box>
			</Container>
		</ThemeProvider >
	);
}


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