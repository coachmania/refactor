<template>
	<Header/>
	<EditorLayout>
		<template v-slot:editor>
			<SectionLayout>
				<template v-slot:cards>
					<Picture/>


				</template>
			</SectionLayout>
		</template>
	</EditorLayout>
</template>

<script setup>
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Picture from './Picture.vue';
</script>