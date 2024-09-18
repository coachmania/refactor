<template>
	<CardLayout>
		<CardTitle>Liens</CardTitle>
		<UrlInput
			label="LinkedIn"
			placeholder="https://linkedin.com/in/coachmania"
			name="linkedin_url"
			:value="data.linkedin_url"
			@update:value="updateValue"
		/>
		<div class="grid grid-cols-2 gap-md">
			<UrlInput
				label="Autre site"
				placeholder="https://github.com/"
				name="other_url"
				:value="data.other_url"
				@update:value="updateValue"
			/>
			<UrlInput
				label="Trimoji"
				placeholder="https://trimoji.fr/"
				name="trimoji_url"
				:value="data.trimoji_url"
				@update:value="updateValue"
			/>
		</div>
	</CardLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import UrlInput from '../input/UrlInput.vue';

const data = reactive({});

const updateValue = async ({name, value}) => {
	try {
		let sendData = {[name]: value,}
		await apiClient.put('/cv_title/update/', sendData);
	} catch (error) {
		console.error('Erreur lors de la mise à jour des liens :', error);
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_title/links/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Erreur lors de la récupération des liens :', error);
	}
};

onMounted(() => {
	fetchData();
});
</script>