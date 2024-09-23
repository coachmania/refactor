<template>
	<SubSectionLayout>
		<CardTitle>Couleurs</CardTitle>
		<ColorSelector 
			v-for="(colors, name) in schemes"
			:name="name"
			:colors="colors"
		/>
	</SubSectionLayout>
</template>

<script setup>
import { computed } from 'vue';
import { useCvCustomizeStore } from '@/store/cvCustomizeStore';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import ColorSelector from './ColorSelector.vue';

const cvCustomizeStore = useCvCustomizeStore();
const schemes = computed(() => cvCustomizeStore.cvSchemes);
</script>