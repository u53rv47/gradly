import { createSlice } from '@reduxjs/toolkit'

const initialState = { user: null };
export const userSlice = createSlice({
	name: 'user',
	initialState,
	reducers: {
		setUser: (state, action) => {
			state.user = action.payload;
		},
		resetUser: (state, action) => {
			return initialState;
		},
		setProfession: (state, action) => {
			state.user = {
				...state.user, ...action.payload
			};
		}
	},
})

// Action creators are generated for each case reducer function
export const { setUser, resetUser, setProfession } = userSlice.actions;

export default userSlice.reducer;