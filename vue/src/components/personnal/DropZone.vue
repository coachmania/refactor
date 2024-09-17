<template>
	<div
        :class="[
			'btn no-animation bg-base-200 h-full flex items-center flex-col',
			{'bg-base-content/15': isDragging}
		]"
		@dragover.prevent="handleDragOver"
		@dragleave.prevent="handleDragLeave"
		@drop.prevent="handleDrop"
		@click="triggerFileInput"
	>
		<svg class="w-8 h-8 fill-current" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M4 5h13v7h2V5c0-1.103-.897-2-2-2H4c-1.103 0-2 .897-2 2v12c0 1.103.897 2 2 2h8v-2H4V5z"></path><path d="m8 11-3 4h11l-4-6-3 4z"></path><path d="M19 14h-2v3h-3v2h3v3h2v-3h3v-2h-3z"></path></svg>
		<h1 class="text-lg">Sélectionner une image</h1>
		<p class="font-thin">ou glisser-déposer ici</p>
        <input 
            class="hidden" 
            type="file" 
            ref="fileInput" 
			accept="image/*"
            @change="handleFileSelect"
        />
	</div>
</template>

<script setup>
import { ref } from 'vue';
import imageCompression from 'browser-image-compression';

const fileInput = ref(null);
const isDragging = ref(false);

const triggerFileInput = () => {
    fileInput.value.click();
};

const handleFileSelect = (event) => {
    const files = event.target.files;
    processFiles(files);
};

const handleDrop = (event) => {
    const files = event.dataTransfer.files;
    processFiles(files);
};

const handleDragOver = () => {
    isDragging.value = true;
};

const handleDragLeave = () => {
    isDragging.value = false;
};

const resizeAndCompressImage = async (file) => {
    const options = {
        maxSizeMB: 1,
        maxWidthOrHeight: 500,
        useWebWorker: true,
    };
    return await imageCompression(file, options);
};

const processFiles = async (files) => {
	if (files.length > 1) {
		console.error('Please select 1 file only');
		return;
	}
	const file = files[0];
	if (!file.type.startsWith('image/')) {
		console.error('Invalid file type:', file.type);
		return;
	}
	try {
        const compressedFile = await resizeAndCompressImage(file);
		// Call api
	} catch (error) {
		console.error('Erreur lors de la compression de l\'image:', error);
	}
};
</script>