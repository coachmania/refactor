<template>
	<div class="grid gap-md">
		<div class="grid grid-cols-[auto,1fr] gap-2 items-center">
			<ReorderButton/>
			<div 
				class="btn no-animation grid grid-cols-[1fr,auto] items-center pl-md p-2 bg-base-200 rounded-btn h-full"
				@click="handleClick(lang.id)"
			>
				<div class="h-full grid grid-rows-2">
					<h1 class="h-full flex items-center">
						{{ lang.name || 'Nouvelle langue' }}
					</h1>
					<p class="font-thin h-full flex items-center">{{ lang.level }}</p>
				</div>
				<DeleteButton @click.stop @click="showModal = true"/>
			</div>
		</div>
		<DeleteConfirmation 
			v-if="showModal"
			@confirm="deleteLang(lang.id)"
			@cancel="showModal = false"
		>
			Êtes-vous sûr de vouloir supprimer cette langue ?
		</DeleteConfirmation>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import apiClient from '@/services/api';
import DeleteConfirmation from '../global/DeleteConfirmation.vue';
import ReorderButton from '../button/ReorderButton.vue';
import DeleteButton from '../button/DeleteButton.vue';

const showModal = ref(false);

const emit = defineEmits(['changeContent', 'deleteLang']);
const handleClick = (id) => {
    emit('changeContent', id);
};

const deleteLang = async (id) => {
	try {
		await apiClient.delete(`/cv_lang/delete/${id}/`);
		showModal.value = false;
		emit('deleteLang');
	} catch (error) {
		console.error('Error deleting language:', error);
	}
};

const props = defineProps({
	lang: Object
});
</script>