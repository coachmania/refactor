<template>
	<div class="col-span-full">
		<span class="label label-text">{{ label }}</span>
		<div id="toolbar" class="bg-base-200 border-b border-base-300 rounded-t-btn flex p-1 gap-1">
			<button 
				:class="{'btn-ghost': !isBoldActive, 'btn-primary': isBoldActive}" 
				class="ql-bold btn btn-sm btn-square"
			>
				<svg class="w-icon h-icon fill-current pointer-events-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M17.061 11.22A4.46 4.46 0 0 0 18 8.5C18 6.019 15.981 4 13.5 4H6v15h8c2.481 0 4.5-2.019 4.5-4.5a4.48 4.48 0 0 0-1.439-3.28zM13.5 7c.827 0 1.5.673 1.5 1.5s-.673 1.5-1.5 1.5H9V7h4.5zm.5 9H9v-3h5c.827 0 1.5.673 1.5 1.5S14.827 16 14 16z"></path></svg>
			</button>
			<button 
				:class="{'btn-ghost': !isItalicActive, 'btn-primary': isItalicActive}" 
				class="ql-italic btn btn-sm btn-square"
			>
				<svg class="w-icon h-icon fill-current pointer-events-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M19 7V4H9v3h2.868L9.012 17H5v3h10v-3h-2.868l2.856-10z"></path></svg>
			</button>
			<button 
				:class="{'btn-ghost': !isUnderlineActive, 'btn-primary': isUnderlineActive}" 
				class="ql-underline btn btn-sm btn-square"
			>
				<svg class="w-icon h-icon fill-current pointer-events-none" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M5 18h14v2H5zM6 4v6c0 3.309 2.691 6 6 6s6-2.691 6-6V4h-2v6c0 2.206-1.794 4-4 4s-4-1.794-4-4V4H6z"></path></svg>
			</button>
		</div>
		<div ref="editorContainer" class="rounded-b-btn shadow-sm">
		</div>
	</div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { handleInput } from './handleInput';
import Quill from 'quill';
import 'quill/dist/quill.snow.css';

const props = defineProps({
	label: String,
	name: String,
	value: String,
});

const emit = defineEmits(['update:value']);
const editorContainer = ref(null);
let quill;
const isBoldActive = ref(false);
const isItalicActive = ref(false);
const isUnderlineActive = ref(false);

const updateCurrentFormat = (quill) => {
	const range = quill.getSelection();
	if (range && range.length > 0) {
		const format = quill.getFormat();
		isBoldActive.value = !!format.bold;
		isItalicActive.value = !!format.italic;
		isUnderlineActive.value = !!format.underline;
	} else {
		isBoldActive.value = false;
		isItalicActive.value = false;
		isUnderlineActive.value = false;
	}
};

onMounted(() => {
	quill = new Quill(editorContainer.value, {
		modules: {
			toolbar: '#toolbar'
		}
	});

	quill.on('selection-change', () => {
		updateCurrentFormat(quill);
	});
	quill.on('text-change', () => {
		updateCurrentFormat(quill);
		handleInput(quill.root.innerHTML, emit, props.name);
	});

	quill.root.innerHTML = props.value || '';
});

watch(() => props.value, (newValue) => {
    if (quill && quill.root.innerHTML !== newValue) {
        quill.root.innerHTML = newValue || '';
    }
});
</script>

<style>
.ql-container {
	@apply static h-auto;
}

.ql-editor {
	@apply w-full p-4 input h-full bg-base-200 rounded-t-none;
}

.ql-tooltip {
	@apply hidden;
}
</style>
