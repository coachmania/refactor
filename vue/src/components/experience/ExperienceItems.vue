<template>
	<CardTitle>Expériences</CardTitle>
	<!-- <LangSummary 
		v-for="item in items"
		:item="item"
		@changeContent="handleChangeContent"
		@deleteLang="fetchItems"
	/> -->
	<div class="flex justify-center">
		<AddItemButton @click="addLang">Ajouter une expérience</AddItemButton>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import AddItemButton from '../button/AddItemButton.vue';
// import LangSummary from './LangSummary.vue';

const items = ref([]);

const fetchItems = async () => {
	try {
		const response = await apiClient.get('/cv_experience/items/');
        items.value = response.data;
	} catch (error) {
		console.error('Error fetching experience:', error);
	}
};

const addLang = async () => {
	try {
		await apiClient.post('/cv_experience/add/', {});
		await fetchItems();
	} catch (error) {
		console.error('Error adding experience:', error);
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