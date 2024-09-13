<template>
	<CardLayout>
		<CardTitle>Type de poste recherché</CardTitle>
		<MultiButton 
			class="grid-cols-3"
			:items="data.type_choices"
			:selectedItem="data.type"
			@click="updateValue"
		/>
	</CardLayout>
</template>

<script setup>
import apiClient from '@/services/api.js';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

const props = defineProps({
	data: Object,
});

const updateValue = async (selectedType) => {
	try {
		let sendData = {type: selectedType}
		await apiClient.put('/cv_title/fields/', sendData);
		props.data.type = selectedType;
	} catch (error) {
		console.error('Error updating title type:', error);
	}
};
</script>