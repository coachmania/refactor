<template>
	<CardLayout>
		<CardTitle>Type de poste recherché</CardTitle>
		<MultiButton 
			class="grid-cols-3"
			:items="data.type_choices"
			:selectedItem="data.type"
			@clicked="updateValue"
		/>
	</CardLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

const data = reactive({});

const updateValue = async (selectedType) => {
	try {
		let sendData = {type: selectedType}
		await apiClient.put('/cv_title/fields/', sendData);
		data.type = selectedType;
	} catch (error) {
		console.error('Error updating title type:', error);
	}
};

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_title/type/');
		Object.assign(data, response.data);
	} catch (error) {
		console.error('Error fetching title type:', error);
	}
};

onMounted(() => {
	fetchData();
})
</script>