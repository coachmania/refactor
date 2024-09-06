import { defineStore } from 'pinia';
import apiClient from '@/services/api.js';

export const useAuthStore = defineStore('auth', {
	state: () => ({
		username: '',
        accessToken: localStorage.getItem('accessToken') || '',
	}),
	actions: {
        async tokenRefresh() {
            try {
                this.accessToken = '';
                const response = await apiClient.post('/accounts/token/refresh/')

                const { access_token } = response.data;
                this.accessToken = access_token;
                localStorage.setItem('accessToken', access_token);
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
            } catch (error) {
                throw error;
            }
        },
        async login(username, password) {
            try {
                const response = await apiClient.post('/accounts/login/', {
                    username,
                    password
                });

                const { access_token } = response.data;
                this.username = username;
                this.accessToken = access_token;
                localStorage.setItem('accessToken', access_token);
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
                console.log('Login:', response.data);
            } catch (error) {
                throw error;
            }
        },
        async profile() {
            try {
                const response = await apiClient.get('/accounts/profile/');
                console.log('Profile:', response.data);
            } catch (error) {
				throw error;
			}
        },
        async logout() {
            try {
                const response = await apiClient.post('/accounts/logout/');
                this.username = '';
                this.accessToken = '';
                localStorage.removeItem('accessToken');
                apiClient.defaults.headers.common['Authorization'] = '';
                console.log('Logout:', response.data);
            } catch (error) {
                throw error;
            }
        },  
    },
});