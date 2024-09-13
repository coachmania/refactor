<template>
	<CardLayout>
		<CardTitle>Afficher en premier</CardTitle>
		<div class="join grid grid-cols-3">
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
		<AlertBox class-color="alert-info">
			<p>Ici, vous pouvez changer l'ordre selon l'importance : placez en premier les expériences ou les formations, selon ce qui valorise le mieux votre profil.</p>
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';

// TODO temp 
const data = {
	type_choices: ['Expérience', 'Formation'],
	type: 'Expérience',
};
</script>