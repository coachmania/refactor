<template>
    <main class="grid grid-cols-[5rem,4fr,5fr] overflow-hidden">
        <Sidebar/>
        <slot></slot>
        <div ref="container" class="flex items-center justify-center bg-base-100 relative overflow-hidden select-none">
            <div ref="page" class="bg-white w-[210mm] h-[297mm] origin-center pointer-events-none select-none aspect-a4 shadow-sm">
                ok
            </div>
        </div>
    </main>
</template>

<script setup>
import { onMounted, ref, onBeforeUnmount } from 'vue';
import Sidebar from '@/components/sidebar/Sidebar.vue';

const container = ref(null);
const page = ref(null);

const adjustZoom = () => {
    const containerWidth = container.value.clientWidth;
    const containerHeight = container.value.clientHeight;
    const divWidth = page.value.clientWidth;
    const divHeight = page.value.clientHeight;

    const scaleX = (containerWidth - 100) / divWidth;
    const scaleY = (containerHeight - 100) / divHeight;
    const scale = Math.min(scaleX, scaleY);

    page.value.style.transform = `scale(${scale})`;
};

onMounted(() => {
    adjustZoom();
    window.addEventListener('resize', adjustZoom);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', adjustZoom);
});
</script>