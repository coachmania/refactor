<template>
	<div ref="editorContainer" class="quill-editor"></div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import Quill from 'quill';
import 'quill/dist/quill.snow.css'; // Importer les styles de Quill

const editorContainer = ref(null);

onMounted(() => {
  new Quill(editorContainer.value, {
    theme: 'snow', // Vous pouvez changer le thème ici
    modules: {
      toolbar: [
        [{ 'header': '1' }, { 'header': '2' }],
        ['bold', 'italic', 'underline'],
        [{ 'list': 'ordered'}, { 'list': 'bullet' }],
        ['link']
      ]
    }
  });
});
</script>

<style>
.quill-editor {
  height: 400px; /* Ajustez la hauteur selon vos besoins */
}
</style>
