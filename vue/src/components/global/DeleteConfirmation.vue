<template>
	<div class="fixed inset-0 z-50 bg-black bg-opacity-50 flex items-center justify-center" @click.self="$emit('cancel')">
		<div class="modal-box bg-base-100">
			<h3 class="text-lg font-bold">
				<slot>Êtes-vous sûr de vouloir supprimer cet élément ?</slot>
			</h3>
			<div class="modal-action grid grid-cols-2 gap-md">
				<button
					class="btn btn-block bg-base-200 shadow-sm"
					@click="$emit('cancel')"
				>Annuler</button>
				<button 
					class="btn btn-block btn-error"
					@click="$emit('confirm')"
				>Supprimer</button>
			</div>
		</div>
	</div>
</template>

<script setup>
import { onMounted, onUnmounted } from 'vue';

const emit = defineEmits(['cancel', 'confirm']);
const handleKeydown = (event) => {
    if (event.key === 'Escape') {
        emit('cancel');
    }
};

onMounted(() => {
    window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
    window.removeEventListener('keydown', handleKeydown);
});
</script>