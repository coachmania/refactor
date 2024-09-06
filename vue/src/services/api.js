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
            originalRequest._retry = true;
            try {
                // console.error(apiClient.defaults.headers.common['Authorization']);
                console.error(authStore.accessToken);
                apiClient.defaults.headers.common['Authorization'] = '';
                await authStore.tokenRefresh();
                
                // console.error(apiClient.defaults.headers.common['Authorization']);
                console.error(authStore.accessToken);
                // const newRequest = {
                //     ...originalRequest,
                //     headers: {
                //         ...originalRequest.headers,
                //         'Authorization': `Bearer ${authStore.accessToken}`
                //     }
                // };
                originalRequest.headers['Authorization'] = `Bearer ${authStore.accessToken}`;
                // return await apiClient(newRequest);
                return await apiClient(originalRequest);
            } catch (refreshError) {
                // rooter.push('/login');
                console.error('Refresh error:', refreshError);
                return Promise.reject(refreshError);
            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;