import axios from 'axios';

const apiClient = axios.create({
    baseURL: '/api',
    withCredentials: true,
});

apiClient.interceptors.response.use(
    response => response,
    async error => {
        const { response } = error;
        if (response && response.status === 401) {
            if (response.config && !response.config.__isRetryRequest) {
                response.config.__isRetryRequest = true;
                try {
                    await apiClient.post('/accounts/token/refresh/', {
                        refresh: localStorage.getItem('refresh_token')
                    });
                    return apiClient(response.config);
                } catch (refreshError) {
                    console.error('Token refresh failed:');
                    return Promise.reject(refreshError);
                }
            }
        }
        return Promise.reject(error);
    }
);

export default apiClient;