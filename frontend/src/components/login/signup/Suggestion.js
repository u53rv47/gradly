/** @format */

import * as React from 'react';
import { Button, CssBaseline, Grid, Box, Typography, Container } from '@mui/material';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Link, useNavigate } from 'react-router-dom';
import { generate } from "random-words";

const defaultTheme = createTheme();

export default function Suggestion() {
	const navigate = useNavigate();
	const [communities, setCommunities] = React.useState([]);
	const [checked, setChecked] = React.useState([]);

	function getCommunity(n) {
		return generate({
			exactly: n,
			join: " "
		});
	}
	React.useEffect(() => {
		const newCommunities = [];
		for (let i = 0; i < 30; i++) {
			newCommunities.push(getCommunity(Math.ceil(Math.random() * 3)));
		}
		setCommunities(newCommunities);

		const temp = [];
		for (let i = 0; i < 30; i++)
			temp.push(false);
		setChecked(temp);
	}, []);

	const handleSubmit = (event) => {
		event.preventDefault();
		const selectedCommunities = communities.filter((community, i) => checked[i]);
		console.log(selectedCommunities);
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

					<Typography component="h1" align='center'>
						We have found the right Communities for you
					</Typography>
					<Typography variant='body2' align='center'>
						Please select atleast three
					</Typography>
					<Box
						component='form'
						noValidate
						onSubmit={handleSubmit}
						sx={{ mt: 3 }}>
						<Grid
							container
							direction="row"
							justifyContent="space-between"
							alignItems="flex-start"
						>
							{communities.map((community, index) => (
								<Box key={"community " + index} sx={{
									background: checked[index] ? "#70AD47" : "#4472C4",
									border: 1,
									borderRadius: "10px",
									display: "flex",
									justifyContent: "center",
									alignItems: 'center',
									margin: "5px",
									padding: "0px 5px 0px 5px",
								}}
									onClick={() => {
										const newChecked = [...checked];
										newChecked[index] = !newChecked[index];
										setChecked(newChecked);
									}}>{community}</Box>
							))}
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