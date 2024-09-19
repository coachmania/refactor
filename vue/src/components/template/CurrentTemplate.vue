<template>
    <div class="currentTemplate w-[210mm] aspect-a4 bg-white">
		<TemplateAlice/>
	</div>
</template>

<script setup>
import { computed } from 'vue';
import { useTemplateStore } from '@/store/templateStore';
import TemplateAlice from './TemplateAlice.vue';

const store = useTemplateStore();

const primaryColor = computed(() => store.primary);
const secondaryColor = computed(() => store.secondary);
const thirdColor = computed(() => store.third);
const darkColor = computed(() => store.dark);
const lightColor = computed(() => store.light);

const headSize = computed(() => store.head);
const titleSize = computed(() => store.title);
const subtitleSize = computed(() => store.subtitle);
const bodySize = computed(() => store.body);
</script>

<style scoped>
    .currentTemplate {
        /* Colors */
        --tp-primary: v-bind(primaryColor);
        --tp-secondary: v-bind(secondaryColor);
        --tp-third: v-bind(thirdColor);
        --tp-dark: v-bind(darkColor);
        --tp-light: v-bind(lightColor);
        /* Font size */
        --tp-head: v-bind(headSize);
        --tp-title: v-bind(titleSize);
        --tp-subtitle: v-bind(subtitleSize);
        --tp-body: v-bind(bodySize);
    }
</style>