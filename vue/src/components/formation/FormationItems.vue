<template>
	<CardTitle>Formations</CardTitle>
	<FormationSummary
		v-for="item in items"
		:item="item"
		@changeContent="handleChangeContent"
		@deleteItem="fetchItems"
	/>
	<div class="flex justify-center">
		<AddItemButton @click="addLang">Ajouter une formation</AddItemButton>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import AddItemButton from '../button/AddItemButton.vue';
import FormationSummary from './FormationSummary.vue';

const items = ref([]);

const fetchItems = async () => {
	try {
		const response = await apiClient.get('/cv_formation/items/');
        items.value = response.data;
	} catch (error) {
		console.error('Error fetching formation:', error);
	}
};

const addLang = async () => {
	try {
		await apiClient.post('/cv_formation/add/', {});
		await fetchItems();
	} catch (error) {
		console.error('Error adding formation:', error);
	}
};

const emit = defineEmits(['changeContent']);
const handleChangeContent = (id) => {
    emit('changeContent', id);
};

onMounted(() => {
	fetchItems();
})
</script>