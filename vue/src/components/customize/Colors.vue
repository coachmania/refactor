<template>
	<CardLayout>
		<CardTitle>Couleurs</CardTitle>
		<ColorSelector
			v-for="n in 3"
			:key="n"
		>
			{{ n }}
		</ColorSelector>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';
</script>