<template>
	<CardTitle>Centres d'intérêt</CardTitle>
	<HobbieSummary
		v-for="item in items"
		:item="item"
		@changeContent="handleChangeContent"
		@deleteItem="fetchItems"
	/>
	<div class="flex justify-center">
		<AddItemButton @click="addLang">Ajouter un centre d'intérêt</AddItemButton>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import AddItemButton from '../button/AddItemButton.vue';
import HobbieSummary from './HobbieSummary.vue';

const items = ref([]);

const fetchItems = async () => {
	try {
		const response = await apiClient.get('/cv_hobbie/items/');
        items.value = response.data;
	} catch (error) {
		console.error('Error fetching formation:', error);
	}
};

const addLang = async () => {
	try {
		await apiClient.post('/cv_hobbie/add/', {});
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