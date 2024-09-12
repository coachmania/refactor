<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Picture/>
			<Infos v-model:data="pageData.data"/>
			<Address v-model:data="pageData.data"/>
			<Mobility v-model:data="pageData.data"/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Picture from './Picture.vue';
import Infos from './Infos.vue';
import Address from './Address.vue';
import Mobility from './Mobility.vue';

const pageData = reactive({
	data: {},
});

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/fields/');
		Object.assign(pageData.data, response.data);
	} catch (error) {
		console.error('Error fetching title types:');
	}
};

onMounted(() => {
	fetchData();
});
</script>