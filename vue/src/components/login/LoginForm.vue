<template>
	<div>
		<form @submit.prevent="handleSubmit">
			<div>
				<label for="username">Username:</label>
				<input type="text" id="username" v-model="username" required>
			</div>
			<div>
				<label for="password">Password:</label>
				<input type="password" id="password" v-model="password" required>
			</div>
			<button type="submit">Submit</button>
		</form>
	</div>
</template>

<script>
import apiClient from '@/services/api.js';

export default {
	name: 'LoginForm',
	data() {
		return {
			username: '',
			password: ''
		};
	},
	methods: {
		async handleSubmit() {
			try {
				const response = await apiClient.post('api/accounts/login/', {
					username: this.username,
					password: this.password
				});
				console.log('Login successful:', response.data);
				localStorage.setItem('access_token', response.data.access);
				localStorage.setItem('refresh_token', response.data.refresh);
			} catch (error) {
				console.error('Login failed:', error.response.data);
			}
		}
	}
};
</script>