<template>
	<SubSectionLayout>
		<CardTitle>Taille de police</CardTitle>
		<MultiButton
			colsClass="grid-cols-4"
			:items="data.type_choices"
			:selectedItem="data.type"
			@click="updateValue"
		/>
	</SubSectionLayout>
</template>

<script setup>
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import MultiButton from '../button/MultiButton.vue';

// TODO temp
const data = {
	type_choices: ['Petit', 'Moyen', 'Grand', 'Très grand'],
	type: 'Moyen',
};
</script>