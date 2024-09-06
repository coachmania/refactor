import axios from 'axios';
import { useAuthStore } from '@/store/authStore';

const apiClient = axios.create({
    baseURL: '/api',
    withCredentials: true,
});

apiClient.interceptors.request.use(
    config => {
        const authStore = useAuthStore();
        if (authStore.accessToken) {
            config.headers['Authorization'] = `Bearer ${authStore.accessToken}`;
        }
        return config;
    },
    error => Promise.reject(error)
);

apiClient.interceptors.response.use(
    response => response,
    async error => {
        const authStore = useAuthStore();
        const originalRequest = error.config;
        if (error.response.status === 401 && !originalRequest._retry) {
            originalRequest._retry = true;
            try {
                await authStore.tokenRefresh();
                originalRequest.headers['Authorization'] = `Bearer ${authStore.accessToken}`;
                return await apiClient(originalRequest);
            } catch (refreshError) {
                // rooter.push('/login');
                console.error('Refresh Token error:', refreshError);
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;