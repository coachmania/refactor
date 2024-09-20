import { ref } from 'vue';
import { defineStore } from 'pinia';
import apiClient from '@/services/api';

export const useCvDataStore = defineStore('cvData', () => {
	const cvData = ref(null);
	const isLoading = ref(false);

	const fetchCvData = async () => {
		isLoading.value = true;
		try {
			const response = await apiClient.get('/cv/content/');
			cvData.value = response.data
		} catch (error) {
			console.error("Error fecthing CV data", error);
		} finally {
			isLoading.value = false;
		}
	}

	return {
		cvData,
		isLoading,
		fetchCvData
	}
});