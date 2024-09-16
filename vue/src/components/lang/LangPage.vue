<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<CardTitle>Langues</CardTitle>
			<AlertBox classColor="alert-info">
				<p>La justification peut être une expérience à l'étranger ou une certification (ex : TOEIC).</p>
			</AlertBox>
            <div class="grid gap-md" v-if="items.length">
                <LangItem v-for="lang in items" :key="lang.id" :lang="lang"/>
            </div>
			<AddSectionButton/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import AddSectionButton from '../global/AddSectionButton.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import LangItem from './LangItem.vue';

const items = ref([]);

const fetchItems = async () => {
	try {
		const response = await apiClient.get('/cv_lang/items/');
        items.value = response.data;
	} catch (error) {
		console.error('Error fetching languages:', error);
	}
};

onMounted(() => {
	fetchItems();
})
</script>