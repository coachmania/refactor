<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<CardTitle>Langues</CardTitle>
			<AlertBox classColor="alert-info">
				<p>La justification peut être une expérience à l'étranger ou une certification (ex : TOEIC).</p>
			</AlertBox>
			<AddSectionButton/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import AddSectionButton from '../global/AddSectionButton.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
</script>