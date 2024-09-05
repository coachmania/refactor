import { defineStore } from 'pinia';
import apiClient from '@/services/api.js';

export const useAuthStore = defineStore('auth', {
	state: () => ({
		username: ''
	}),
	actions: {
        async login(username, password) {
            try {
                await apiClient.post('/accounts/login/', {
                    username,
                    password
                });
                this.username = username;
                console.log('Login successful');
            } catch (error) {
                console.error('Login failed:', error.response.data);
                throw error;
            }
        },
        async logout() {
            try {
                await apiClient.post('/accounts/logout/');
                this.username = '';
                console.log('Logout successful');
            } catch (error) {
                console.error('Logout failed:', error.response.data);
                throw error;
            }
        }
	},
    // getters: {
    //     isLogged: (state) => !!state.accessToken
    // }
});