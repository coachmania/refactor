<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Type :data="data"/>
			<Title :data="data"/>
			<Links :data="data"/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
import Links from './Links.vue';

const data = ref({
	type: '',
	typeChoices: [],
	title: '',
	details: '',
});

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_title/fields/');
		data.value = response.data;
	} catch (error) {
		console.error('Error fetching title types:', error);
	}
};

onMounted(() => {
	fetchData();
});
</script>