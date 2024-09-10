<template>
	<div class="grid grid-rows-[auto,1fr] h-screen">
		<Header/>
		<EditorLayout>
			<template v-slot:editor>
				<SectionLayout>
					<template v-slot:cards>
						<Type/>
						<Title/>
					</template>
				</SectionLayout>
			</template>
		</EditorLayout>
	</div>
</template>

<script setup>
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import Type from './Type.vue';
import Title from './Title.vue';
</script>