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
		<p v-if="message">{{ message }}</p>
	</div>
</template>

<script>
import { defineComponent } from 'vue';
import { useAuthStore } from '@/store/authStore';

export default defineComponent({
	name: 'LoginForm',
	data() {
		return {
			username: '',
			password: '',
			message: '',
		};
	},
	methods: {
		async handleSubmit() {
			const authStore = useAuthStore();
			try {
				await authStore.login(this.username, this.password);
				this.message = 'Login successful';
			} catch (error) {
				console.error('Login failed:', error.response.data);
				this.message = 'Login failed';
			}
		}
	}
});
</script>