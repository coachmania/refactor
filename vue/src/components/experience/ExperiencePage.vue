<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<SubSectionLayout>
				<template v-if="showDetail">
					<ExperienceDetail :item_id="selectedId" @close="showDetail = false"/>
				</template>
				<template v-else>
					<ExperienceItems @changeContent="handleChangeContent"/>
				</template>
			</SubSectionLayout>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref } from 'vue';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import SubSectionLayout from '../layout/SubSectionLayout.vue';
import ExperienceDetail from './ExperienceDetail.vue';
import ExperienceItems from './ExperienceItems.vue';

const selectedId = ref();
const showDetail = ref(false);

const handleChangeContent = (id) => {
	selectedId.value = id;
    showDetail.value = true;
};
</script>