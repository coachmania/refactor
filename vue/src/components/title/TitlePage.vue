<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Type/>
			<Title/>
			<Links v-model:data="pageData.data"/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
import Links from './Links.vue';

const pageData = reactive({
	data: {},
});

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_title/fields/');
		Object.assign(pageData.data, response.data);
	} catch (error) {
		console.error('Error fetching title types:', error);
	}
};

onMounted(() => {
	fetchData();
});
</script>