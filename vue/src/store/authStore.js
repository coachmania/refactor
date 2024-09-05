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
		// logout() {
		// 	this.accessToken = '';
		// 	this.refreshToken = '';
		// 	this.username = '';
		// 	localStorage.removeItem('access_token');
		// 	localStorage.removeItem('refresh_token');
		// },
        // async profile() {
        //     try {
        //         const response = await apiClient.get('accounts/profile/', {
        //             headers: {
        //                 'Authorization': `Bearer ${this.accessToken}`
        //             }
        //         });
        //         return response.data;
        //     } catch (error) {
        //         throw error;
        //     }
        // }
	},
    // getters: {
    //     isLogged: (state) => !!state.accessToken
    // }
});