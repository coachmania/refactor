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
                const response = await apiClient.post('/accounts/token/refresh/')

                const { access_token } = response.data;
                this.accessToken = access_token;
                localStorage.setItem('accessToken', access_token);
                
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
                console.log('Refresh successful');
            } catch (error) {
                console.error('Refresh failed:', error.response.data);
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
                console.log('Login successful');
            } catch (error) {
                console.error('Login failed:', error.response.data);
                throw error;
            }
        },
        // async logout() {
        //     try {
        //         await apiClient.post('/accounts/logout/');
        //         this.username = '';
        //         // this.isAuthenticated = false;
        //         console.log('Logout successful');
        //     } catch (error) {
        //         console.error('Logout failed:', error.response.data);
        //         throw error;
        //     }
        // },
        async profile() {
            try {
                console.log('Profile called');
                
                apiClient.defaults.headers.common['Authorization'] = `Bearer ${this.accessToken}`;
                const response = await apiClient.get('/accounts/profile/');
                console.log('Profile:', response.data);
            } catch (error) {
				console.error('Profile failed:', error.response.data);
				throw error;
			}
        },
    },
});