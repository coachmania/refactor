<template>
	<div class="box-border overflow-hidden w-full h-full grid grid-cols-[80mm,1fr] bg-tpPrimary text-tpBody">
		<aside class="p-10 rayClass">
			<div class="bg-tpLight h-full">
				<Name splited/>
				<pre>{{ cvData }}</pre>
			</div>
		</aside>
	</div>
</template>

<script setup>
import Name from './elements/Name.vue';

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