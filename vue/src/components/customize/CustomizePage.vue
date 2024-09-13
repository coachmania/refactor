<<template>
	<Header/>
	<EditorLayout>
		<SectionLayout>
			<CardTitle>Apparence</CardTitle>
			<Templates/>
			<ExperienceFirst/>
			<FontSize/>
		</SectionLayout>
	</EditorLayout>
</template>

<script setup>
import { reactive, onMounted } from 'vue';
import apiClient from '@/services/api';
import Header from '@/components/header/Header.vue';
import EditorLayout from '../layout/EditorLayout.vue';
import SectionLayout from '../layout/SectionLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import Templates from './Templates.vue';
import ExperienceFirst from './ExperienceFirst.vue';
import FontSize from './FontSize.vue';

// const pageData = reactive({
// 	data: {},
// });

// const fetchData = async () => {
// 	try {
// 		// const response = await apiClient.get('/cv_customize/fields/');
// 		Object.assign(pageData.data, response.data);
// 	} catch (error) {
// 		console.error('Error fetching title types:');
// 	}
// };

// onMounted(() => {
// 	// fetchData();
// });
</script>