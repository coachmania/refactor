<template>
	<div class="grid gap-md">
		<div class="grid grid-cols-[auto,1fr] gap-2 items-center">
			<ReorderButton/>
			<div 
				class="btn no-animation grid grid-cols-[1fr,auto] items-center pl-md p-2 bg-base-200 rounded-btn h-full"
				@click="handleClick(item.id)"
			>
				<ItemSummaryName
					:subtitle="item.title"
				>{{ item.company || 'Nouvelle experience' }}</ItemSummaryName>
				<DeleteButton @click.stop @click="showModal = true"/>
			</div>
		</div>
		<DeleteConfirmation 
			v-if="showModal"
			@confirm="deleteItem(item.id)"
			@cancel="showModal = false"
		>
			Êtes-vous sûr de vouloir supprimer cette expérience ?
		</DeleteConfirmation>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import apiClient from '@/services/api';
import DeleteConfirmation from '../global/DeleteConfirmation.vue';
import ReorderButton from '../button/ReorderButton.vue';
import DeleteButton from '../button/DeleteButton.vue';
import ItemSummaryName from '../global/ItemSummaryName.vue';

const showModal = ref(false);

const emit = defineEmits(['changeContent', 'deleteItem']);
const handleClick = (id) => {
    emit('changeContent', id);
};

const deleteItem = async (id) => {
	try {
		await apiClient.delete(`/cv_experience/delete/${id}/`);
		showModal.value = false;
		emit('deleteItem');
	} catch (error) {
		console.error('Error deleting language:', error);
	}
};

const props = defineProps({
	item: Object
});
</script>