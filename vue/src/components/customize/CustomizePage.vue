<<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<CardTitle>Apparence</CardTitle>
			<Templates/>
			<ExperienceFirst/>
			<FontSize/>
			<Colors/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { onMounted } from 'vue';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import Templates from './Templates.vue';
import ExperienceFirst from './ExperienceFirst.vue';
import FontSize from './FontSize.vue';
import Colors from './Colors.vue';

import { useCvCustomizeStore } from '@/store/cvCustomizeStore.js';

const store = useCvCustomizeStore();
onMounted(() => {
	store.fetchData();
});
</script>