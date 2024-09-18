<template>
	<SubSectionLayout>
		<CardTitle>Type de poste recherché</CardTitle>
		<MultiButton 
			colsClass="grid-cols-4"
			:items="data.type_choices"
			:selectedItem="data.type"
			@clicked="updateValue"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api.js';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

const data = reactive({});

const updateValue = async (selectedType) => {
	try {
		let sendData = {type: selectedType}
		await apiClient.put('/cv_title/update/', sendData);
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