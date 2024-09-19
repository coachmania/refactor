<template>
	<SubSectionLayout>
		<CardTitle>Couleurs</CardTitle>
		<ColorSelector 
			v-for="(colors, name) in schemes"
			:name="name"
			:colors="colors"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';

const schemes = ref([]);

const fetchSchemes = async () => {
	try {
		const response = await apiClient.get('/templates/scheme/0/');
		schemes.value = response.data;
	} catch (error) {
		console.error(error);
	}
};

onMounted(() => {
	fetchSchemes();
})
</script>