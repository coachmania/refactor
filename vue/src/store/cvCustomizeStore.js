import { ref } from 'vue';
import { defineStore } from 'pinia';
import apiClient from '@/services/api';

export const useCvCustomizeStore = defineStore('cvCustomize', () => {
	const cvCustomize = ref(null);
	const isLoading = ref(false);
	const cvSchemes = ref(null);

	const primary = ref('');
	const secondary = ref('');
	const third = ref('');
	const dark = ref('');
	const light = ref('');
	const head = ref('');
	const title = ref('');
	const subtitle = ref('');
	const body = ref('');

	const fetchData = async () => {
		isLoading.value = true;
		try {
			const responseFields = await apiClient.get('cv_settings/fields/');
			cvCustomize.value = responseFields.data;

			const responseSchemes = await apiClient.get('cv_settings/scheme/1/');
			cvSchemes.value = responseSchemes.data;
		} catch (error) {
			console.error("Error fetching API data", error);
		} finally {
			isLoading.value = false;
		}
	}

	const setProperty = (name, value) => {
		if (cvCustomize.value && cvCustomize.value[name] !== undefined) {
			cvCustomize.value[name] = value;
		} else {
			console.error(`Unknown property: ${name}`);
		}
	}

	return {
		cvCustomize,
		isLoading,
		cvSchemes,
		primary,
		secondary,
		third,
		dark,
		light,
		head,
		title,
		subtitle,
		body,
		fetchData,
		setProperty
	}
});
