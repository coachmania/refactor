<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<Type @updateType="updateType"/>
			<Title :type="sharedType"/>
			<Links/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref } from 'vue';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
import Links from './Links.vue';

const sharedType = ref('');
const updateType = (type) => {
	sharedType.value = type;
}
</script>