<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Picture/>
			<Infos :data="data"/>
			<Address :data="data"/>
			<Mobility/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Picture from './Picture.vue';
import Infos from './Infos.vue';
import Address from './Address.vue';
import Mobility from './Mobility.vue';

const data = ref({});

const fetchData = async () => {
	try {
		const response = await apiClient.get('/cv_personnal/fields/');
		data.value = response.data;
	} catch (error) {
		console.error('Error fetching title types:');
	}
};

onMounted(() => {
	fetchData();
});
</script>