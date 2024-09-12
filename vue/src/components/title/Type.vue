<template>
	<CardLayout>
		<CardTitle>Type de poste recherché</CardTitle>
		<div class="join grid grid-cols-3">
			<button 
				v-for="(item, index) in data.type_choices" 
				:key="index" 
				:class="['btn join-item no-animation', {
					'btn-primary': item === data.type,
					'bg-base-100 border-base-content/15': item !== data.type
				}]"
				@click="updateValue(item)"
			>
				{{ item }}
			</button>
		</div>
	</CardLayout>
</template>

<script setup>
import apiClient from '@/services/api.js';
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';

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