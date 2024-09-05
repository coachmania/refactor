import { defineStore } from 'pinia';
import apiClient from '@/services/api.js';

export const useAuthStore = defineStore('auth', {
	state: () => ({
		accessToken: localStorage.getItem('access_token') || '',
		refreshToken: localStorage.getItem('refresh_token') || '',
		username: ''
	}),
	actions: {
		async login(username, password) {
			try {
				const response = await apiClient.post('api/accounts/login/', {
					username,
					password
				});
				this.accessToken = response.data.access;
				this.refreshToken = response.data.refresh;
				this.username = username;
				localStorage.setItem('access_token', response.data.access);
				localStorage.setItem('refresh_token', response.data.refresh);
			} catch (error) {
				throw error;
			}
		},
		logout() {
			this.accessToken = '';
			this.refreshToken = '';
			this.username = '';
			localStorage.removeItem('access_token');
			localStorage.removeItem('refresh_token');
		}
	},
    getters: {
        isLogged: (state) => !!state.accessToken
    }
});