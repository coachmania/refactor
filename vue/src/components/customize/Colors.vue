<template>
	<SubSectionLayout>
		<CardTitle>Couleurs</CardTitle>
		<ColorSelector
			v-for="n in 3"
			:key="n"
		>
			{{ n }}
		</ColorSelector>
	</SubSectionLayout>
</template>

<script setup>
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';
</script>