<template>
	<div class="grid grid-rows-[auto,1fr] h-screen">
		<Header/>
		<EditorLayout>
			<template v-slot:editor>
				<SectionLayout>
					<template v-slot:cards>
						<p>EDITOR</p>
					</template>
				</SectionLayout>
			</template>
		</EditorLayout>
	</div>
</template>

<script>
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';

export default {
	name: 'TitlePage',
	components: {
		Header,
		EditorLayout,
		SectionLayout,
	},
};
</script>