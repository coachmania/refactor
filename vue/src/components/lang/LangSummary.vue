<template>
	<div class="grid grid-cols-[auto,1fr] gap-2 items-center">
		<button class="h-full btn btn-ghost btn-square">
			<svg class="w-icon h-icon fill-current pointer-events-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" ><path d="M6.227 11h11.547c.862 0 1.32-1.02.747-1.665L12.748 2.84a.998.998 0 0 0-1.494 0L5.479 9.335C4.906 9.98 5.364 11 6.227 11zm5.026 10.159a.998.998 0 0 0 1.494 0l5.773-6.495c.574-.644.116-1.664-.747-1.664H6.227c-.862 0-1.32 1.02-.747 1.665l5.773 6.494z"></path></svg>
		</button>
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
			<button class="btn btn-ghost btn-square" @click.stop @click="showModal = true">
				<svg class="w-icon h-icon fill-error pointer-events-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 20a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8h2V6h-4V4a2 2 0 0 0-2-2H9a2 2 0 0 0-2 2v2H3v2h2zM9 4h6v2H9zM8 8h9v12H7V8z"></path><path d="M9 10h2v8H9zm4 0h2v8h-2z"></path></svg>
			</button>
		</div>
	</div>
	<template v-if="showModal">
		<DeleteConfirmation 
			@confirm="deleteLang(lang.id)"
			@cancel="showModal = false"
		>
			Êtes-vous sûr de vouloir supprimer cette langue ?
		</DeleteConfirmation>
	</template>
</template>

<script setup>
import { ref } from 'vue';
import apiClient from '@/services/api';
import DeleteConfirmation from '../global/DeleteConfirmation.vue';

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