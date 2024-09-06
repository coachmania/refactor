import axios from 'axios';
import { useAuthStore } from '@/store/authStore';

const apiClient = axios.create({
    baseURL: '/api',
    withCredentials: true,
});

apiClient.interceptors.response.use(
    response => response,
    async error => {
        const authStore = useAuthStore();
        const originalRequest = error.config;

        if (error.response.status === 401 && !originalRequest._retry) {
            // console.error('OKKK 401 recu et pas de retry');
            originalRequest._retry = true;

            try {
                // Delete the current token
                apiClient.defaults.headers.common['Authorization'] = '';
                await authStore.tokenRefresh();
                // console.error('OK Token refresh successful');
                
                // return apiClient(originalRequest);
            } catch (refreshError) {
                // console.error('NK Token refresh failed:');
            }
        }

        // console.error('Erreur de la requête :', error.response || error.message);
        return Promise.reject(error);
    }
);

export default apiClient;