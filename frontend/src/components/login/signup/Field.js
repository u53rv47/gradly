/** @format */

import axios from 'axios';
import * as React from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { Button, CssBaseline, Grid, Box, Typography, Container, Select, MenuItem, TextField } from '@mui/material';
import { setUser } from '../../../store/user/userSlice';

const defaultTheme = createTheme();

export default function Field() {
	const navigate = useNavigate();
	const user = useSelector(state => state.user).user;

	let isStudent = !!user && user.profession === "Student";
	React.useEffect(() => {
		if ((isStudent && !!user.institute && !!user.major) || (!isStudent && !!user.industry))
			navigate("/signup/suggest/");
	}, []);
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
					<Box sx={{
						width: "350px"
					}}>
						<Typography component="h1" align='center'>
							We are on the way to find best Communities for you to join
						</Typography>
					</Box>
					{isStudent && <Institute />}
					{!isStudent && <Industry />}
					<Copyright sx={{ mt: 5 }} />
				</Box>
			</Container>
		</ThemeProvider >
	);
}
async function fetchList(name, route) {
	const newList = [`Please select your ${name}`,];
	const access = localStorage.getItem("access");
	const url = process.env.REACT_APP_BASE_URL + `/api/account/${route}/`;
	return axios.get(url, {
		headers: { 'Authorization': `Bearer ${access}` }
	}).then((res) => {
		res.data.forEach(val => {
			newList.push(val.name);
		});
		return newList;
	}).catch((err) => {
		if (err)
			console.log(err);
		return newList;
	});
}

function Institute(props) {
	const navigate = useNavigate();
	const dispatch = useDispatch();
	const [institute, setInstitute] = React.useState(0);
	const [major, setMajor] = React.useState(0);
	const [other, setOther] = React.useState("");

	const [instituteList, setInstituteList] = React.useState(["Please select your Institute",]);
	const [majorList, setMajorList] = React.useState(["Please select your Major",]);

	React.useEffect(() => {
		fetchList("Institute", "institutes").then((list) => {
			list.push("Other")
			setInstituteList(list);
		});
	}, []);
	React.useEffect(() => {
		fetchList("Major", "majors").then((list) => {
			setMajorList(list);
		});
	}, []);
	const handleSubmit = (event) => {
		event.preventDefault();

		const data = { major: major === 0 ? null : majorList[major], institute: institute === 0 ? null : instituteList[institute] };
		if (!!other && other !== "Please enter your institute")
			// console.log(other)
			data["institute"] = other;

		if (!!data.institute && !!data.major) {
			console.log(data)
			const url = process.env.REACT_APP_AUTH_URL + "/users/me/";
			const access = localStorage.getItem("access");
			console.log(`Bearer ${access}`);
			axios.patch(url, data, {
				headers: {
					'Authorization': `Bearer ${access}`
				}
			}).then((res) => {
				console.log("Field Response:", res.data);
				navigate("/signup/suggest");
				dispatch(setUser(res.data));
			}).catch((err) => {
				if (err) {
					console.log(err);
					navigate("/login");
				}
			});
		}

	};
	return (
		<Box
			component='form'
			noValidate
			onSubmit={handleSubmit}
			sx={{ mt: 1 }}>
			<Grid container spacing={2}>
				<Grid item xs={12}>
					<Typography variant='h6' align='center' marginTop={2}>What's your institute</Typography>
				</Grid>
				<Grid item xs={12} sx={{
					display: "flex",
					flexDirection: "column",
					alignItems: "center"
				}}>
					<Box sx={{ width: "250px" }}>
						<Select
							fullWidth
							size='small'
							value={institute}
							defaultValue="Please select your Institute"
							onChange={(event) => {
								const value = event.target.value;
								if (instituteList[value] === "Other") {
									setOther("Please enter your institute");
									setInstitute(0);
								} else {
									setOther("");
									setInstitute(value);
								}
							}}
						>
							{instituteList.map((institute, index, arr) => < MenuItem key={"institute " + index} value={index}>{institute}</MenuItem>)}
						</Select>

						{!!other && <TextField fullWidth size='small' margin="normal" placeholder={other} onChange={(e) => { setOther(e.target.value) }} />}
					</Box>
				</Grid >
				<Grid item xs={12}>
					<Typography variant='h6' align='center' marginTop={2}>What's your major</Typography>
				</Grid>
				<Grid item xs={12} sx={{
					display: "flex",
					flexDirection: "column",
					alignItems: "center"
				}}>
					<Box sx={{ width: "250px" }}>
						<Select
							fullWidth
							size='small'
							value={major}
							onChange={(event) => {
								setMajor(event.target.value);
							}}
						>
							{majorList.map((major, index, arr) => < MenuItem key={"major " + index} value={index}>{major}</MenuItem>)}
						</Select>
					</Box>
				</Grid >
			</Grid >
			<Button
				type='submit'
				fullWidth
				variant='contained'
				sx={{ mt: 3, mb: 2, textTransform: 'none' }}>
				Next
			</Button>
		</Box >
	);
}

function Industry(props) {
	const [industry, setIndustry] = React.useState('select');
	let industryList = ["Please select your Industry", "Some Industry 1", "Some Industry 2", "Some Industry 3", "Some Industry 4", "Some Industry 5"]
	// useEffect(() => {
	// Make request to get the industry
	// }, []);
	const handleSubmit = (event) => {
		event.preventDefault();
		// Make reuest to set the industry
	};
	return (
		<Box
			component='form'
			noValidate
			onSubmit={handleSubmit}
			sx={{ mt: 3 }}>
			<Grid container spacing={2}>
				<Grid item xs={12}>
					<Typography variant='h6' align='center' marginTop={2}>What's your industry</Typography>
				</Grid>
				<Grid item xs={12} sx={{
					display: "flex",
					flexDirection: "column",
					alignItems: "center"
				}}>
					<Box sx={{ width: "250px" }}>
						<Select
							fullWidth
							size='small'
							value={industry}
							onChange={(event) => {
								setIndustry(event.target.value);
							}}
						>
							{industryList.map((industry, index, arr) => < MenuItem key={"industry " + index} value={index}>{industry}</MenuItem>)}
						</Select>
					</Box>
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