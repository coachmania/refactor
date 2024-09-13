<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Type/>
			<Title/>
			<Links/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
import Links from './Links.vue';
</script>