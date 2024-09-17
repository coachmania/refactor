<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<SubSectionLayout>
				<template v-if="showItemDetail">
					<LangDetail :langId=selectedLangId @close="showItemDetail = false"/>
				</template>
				<template v-else>
					<LangItems @changeContent="handleChangeContent"/>
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
import LangItems from './LangItems.vue';
import LangDetail from './LangDetail.vue';

const selectedLangId = ref();
const showItemDetail = ref(false);

const handleChangeContent = (id) => {
	selectedLangId.value = id;
    showItemDetail.value = true;
};
</script>