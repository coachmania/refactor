<template>
    <div class="currentTemplate w-[210mm] aspect-a4 bg-white">

        <div v-if="!isLoading && cvData" class="box-border overflow-hidden w-full h-full grid grid-cols-[80mm,1fr] bg-tpPrimary text-tpBody">
            <TemplateAlice :cvData="cvData"/>
        </div>
        <div v-else-if="isLoading">
            <p>Chargement des données du CV...</p>
        </div>
        <div v-else>
            <p>Erreur lors du chargement des données du CV</p>
        </div>
	</div>
</template>

<script setup>
import { computed, onMounted } from 'vue';
import { useTemplateStore } from '@/store/templateStore';
import { useCvDataStore } from '@/store/cvDataStore';
import TemplateAlice from './TemplateAlice.vue';

const templateStore = useTemplateStore();

const primaryColor = computed(() => templateStore.primary);
const secondaryColor = computed(() => templateStore.secondary);
const thirdColor = computed(() => templateStore.third);
const darkColor = computed(() => templateStore.dark);
const lightColor = computed(() => templateStore.light);

const headSize = computed(() => templateStore.head);
const titleSize = computed(() => templateStore.title);
const subtitleSize = computed(() => templateStore.subtitle);
const bodySize = computed(() => templateStore.body);

const cvDataStore = useCvDataStore();
const cvData = computed(() => cvDataStore.cvData);
const isLoading = computed(() => cvDataStore.isLoading);

onMounted(() => {
    cvDataStore.fetchCvData();
});

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