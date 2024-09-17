<template>
	<CardLayout>
		<CardTitle>Taille de police</CardTitle>
		<MultiButton
			colsClass="grid-cols-4"
			:items="data.type_choices"
			:selectedItem="data.type"
			@click="updateValue"
		/>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

// TODO temp
const data = {
	type_choices: ['Petit', 'Moyen', 'Grand', 'Très grand'],
	type: 'Moyen',
};
</script>