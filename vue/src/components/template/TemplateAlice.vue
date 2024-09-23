<template>
	<div class="box-border overflow-hidden w-full h-full grid grid-cols-[80mm,1fr] bg-tpPrimary text-tpBody">
		<aside class="p-10 rayClass">
			<div class="bg-tpLight h-full px-4 py-6 grid gap-md">
				<Name splited/>
				<Age/>
				<Contact>Contact</Contact>
				<Mobility/>
				<Lang>Langues</Lang>
				<pre>{{ cvData.langs }}</pre>
			</div>
		</aside>
	</div>
</template>

<script setup>
import Age from './elements/Age.vue';
import Name from './elements/Name.vue';
import Contact from './elements/Contact.vue';
import Mobility from './elements/Mobility.vue';
import Lang from './elements/Lang.vue';

const props = defineProps({
    cvData: {
        type: Object,
        required: true
    }
});
</script>

<style scoped>
.rayClass {
	background: linear-gradient(-45deg, transparent 22.5%, #ffffff55 22.5%, #ffffff55 27.5%, transparent 27.5%, transparent 72.5%, #ffffff55 72.5%, #ffffff55 77.5%, transparent 77.5%);
	background-size: 20px 20px;
}
</style>