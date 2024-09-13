<template>
	<CardLayout>
		<CardTitle>Taille de police</CardTitle>
		<div class="join grid grid-cols-4">
			<button 
				v-for="(item, index) in data.type_choices" 
				:key="index" 
				class="btn join-item no-animation"
				:class="item === data.type ? 'btn-primary' : 'bg-base-100 border-base-content/15'"
				@click="updateValue(item)"
			>
				{{ item }}
			</button>
		</div>

	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';

// TODO temp
const data = {
	type_choices: ['Petit', 'Moyen', 'Grand', 'Très grand'],
	type: 'Moyen',
};
</script>