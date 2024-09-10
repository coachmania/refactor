<template>
	<div class="w-full">
		<div id="toolbar" class="border border-base-300 rounded-t-btn flex p-1 gap-1">
			<button class="ql-bold btn btn-sm btn-square btn-primary">
				<svg class="w-icon h-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M17.061 11.22A4.46 4.46 0 0 0 18 8.5C18 6.019 15.981 4 13.5 4H6v15h8c2.481 0 4.5-2.019 4.5-4.5a4.48 4.48 0 0 0-1.439-3.28zM13.5 7c.827 0 1.5.673 1.5 1.5s-.673 1.5-1.5 1.5H9V7h4.5zm.5 9H9v-3h5c.827 0 1.5.673 1.5 1.5S14.827 16 14 16z"></path></svg>
			</button>
			<button class="ql-italic btn btn-sm btn-square btn-primary">
				<svg class="w-icon h-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 7V4H9v3h2.868L9.012 17H5v3h10v-3h-2.868l2.856-10z"></path></svg>
			</button>
			<button class="ql-underline btn btn-sm btn-square btn-primary">
				<svg class="w-icon h-icon fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 18h14v2H5zM6 4v6c0 3.309 2.691 6 6 6s6-2.691 6-6V4h-2v6c0 2.206-1.794 4-4 4s-4-1.794-4-4V4H6z"></path></svg>
			</button>
		</div>
		<div ref="editorContainer" class="rounded-b-btn border border-t-0 border-base-300 bg-base-100"></div>
	</div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Quill from 'quill';

const editorContainer = ref(null);

onMounted(() => {
	new Quill(editorContainer.value, {
		modules: {
			toolbar: '#toolbar'
		}
	});
});
</script>

<style>
.ql-editor {
	@apply min-w-full p-4 input h-full;
}

.ql-tooltip {
	@apply hidden;
}
</style>
