<template>
	<CardTitle>Expériences</CardTitle>
	<LangSummary 
		v-for="lang in items"
		:lang="lang"
		@changeContent="handleChangeContent"
		@deleteLang="fetchItems"
	/>
	<div class="flex justify-center">
		<button class="btn btn-primary no-animation" @click="addLang">
			<svg class="w-icon h-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 11h-6V5h-2v6H5v2h6v6h2v-6h6z"></path></svg>
			<p>Ajouter une langue</p>
		</button>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import CardTitle from '../global/CardTitle.vue';
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