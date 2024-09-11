<template>
	<Header/>
	<EditorLayout>
		<template v-slot:editor>
			<SectionLayout>
				<template v-slot:cards>
					<Type
						@update:type="updateType"
					/>
					<Title :type="type"/>
				</template>
			</SectionLayout>
		</template>
	</EditorLayout>
</template>

<script setup>
import { ref } from 'vue';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';

const type = ref('');

const updateType = (selectedType) => {
	type.value = selectedType;
};
</script>