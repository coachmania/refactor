<template>
	<CardTitle>Langues</CardTitle>
	<LangSummary 
		v-for="lang in items"
		:lang="lang"
		@changeContent="handleChangeContent"
		@deleteLang="fetchItems"
	/>
	<div class="flex justify-center">
		<AddItemButton @click="addLang">Ajouter une langue</AddItemButton>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
import LangSummary from './LangSummary.vue';
import AddItemButton from '../button/AddItemButton.vue';

const items = ref([]);

const fetchItems = async () => {
	try {
		const response = await apiClient.get('/cv_lang/items/');
        items.value = response.data;
	} catch (error) {
		console.error('Error fetching languages:', error);
	}
};

const addLang = async () => {
	try {
		await apiClient.post('/cv_lang/add/', {});
		await fetchItems();
	} catch (error) {
		console.error('Error adding language:', error);
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