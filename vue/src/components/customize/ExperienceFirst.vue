<template>
	<CardLayout>
		<CardTitle>Afficher en premier</CardTitle>
		<MultiButton
			class="grid-cols-3"
			:items="data.type_choices"
			:selectedItem="data.type"
			@click="updateValue"
		/>
		<AlertBox class-color="alert-info">
			<p>Ici, vous pouvez changer l'ordre selon l'importance : placez en premier les expériences ou les formations, selon ce qui valorise le mieux votre profil.</p>
		</AlertBox>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import MultiButton from '../button/MultiButton.vue';

// TODO temp 
const data = {
	type_choices: ['Expérience', 'Formation'],
	type: 'Expérience',
};
</script>