<template>
    <a
		class="btn btn-square grid place-items-center tooltip tooltip-right"
		:class="currentPage ? 'btn-primary' : 'btn-ghost'"
		:data-tip="name" 
		:href="currentPage ? null : url">
		<slot></slot>
    </a>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';

const props = defineProps({
	url: String,
	name: String,
});

const currentPage = ref(false);
const route = useRoute();

const checkCurrentPage = () => {
	currentPage.value = route.path.startsWith(props.url);
};

onMounted(checkCurrentPage);
</script>