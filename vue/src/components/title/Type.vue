<template>
	<div class="card bg-base-200 border border-base-300">
		<div class="grid p-card gap-md">
			<h1 class="card-title">Type de poste recherché</h1>
	
			<div class="join grid grid-cols-3">
				<button 
					v-for="(item, index) in typeChoices" 
					:key="index" 
                    :class="['btn join-item no-animation', {
						'btn-primary': item === type,
						'bg-base-100 border-base-content/15': item !== type
					}]"
					@click="updateType(item)"
				>
					{{ item }}
				</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';

const emit = defineEmits(['update:type']);

const typeChoices = ref([]);
const type = ref('');

const fetchTitleTypes = async () => {
	try {
		const response = await apiClient.get('/cv_title/type/');
		typeChoices.value = response.data.type_choices;
		type.value = response.data.type;
		emit('update:type', type.value);
	} catch (error) {
		console.error('Error fetching title types:', error);
	}
};

const updateType = async (selectedType) => {
	type.value = selectedType;
	try {
		await apiClient.put('/cv_title/type/', {type: type.value});
		emit('update:type', selectedType);
	} catch (error) {
		console.error('Error updating title type:', error);
	}
};

onMounted(() => {
	fetchTitleTypes();
});
</script>