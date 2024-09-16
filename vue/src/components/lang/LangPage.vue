<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<template v-if="showItemDetail">
				<LangItemDetail :langId=selectedLangId @close="showItemDetail = false"/>
			</template>
			<template v-else>
				<LangItems @changeContent="handleChangeContent"/>
			</template>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { ref } from 'vue';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import LangItems from './LangItems.vue';
import LangItemDetail from './LangItemDetail.vue';

const selectedLangId = ref();
const showItemDetail = ref(false);

const handleChangeContent = (id) => {
	selectedLangId.value = id;
    showItemDetail.value = true;
};
</script>