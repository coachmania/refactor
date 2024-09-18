<template>
    <main class="grid grid-cols-[5rem,4fr,5fr] overflow-hidden">
        <Sidebar/>
        <slot></slot>
        <div 
            ref="container" 
            class="flex items-center justify-center bg-base-100 relative overflow-hidden select-none"
            @wheel="handleMouseWheel"
        >
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
const scaleStep = 0.1;

var currentScale;
var translateX = 0;
var translateY = 0;

const updateTransform = () => {
    page.value.style.transform = `translate(${translateX}px, ${translateY}px) scale(${currentScale})`;
};

const adjustZoom = () => {
    currentScale = Math.min(
        (container.value.clientWidth - 100) / page.value.clientWidth,
        (container.value.clientHeight - 100) / page.value.clientHeight
    );
    updateTransform();
};

const handleMouseWheel = (event) => {
    event.preventDefault();
    const delta = event.deltaY < 0 ? 1 : -1;

    if (event.ctrlKey) {
        currentScale = Math.min(3.0, Math.max(0.5, currentScale + delta * scaleStep));
    } else {
        translateY += delta * 50;
    }
    updateTransform();
};

onMounted(() => {
    adjustZoom();
    window.addEventListener('resize', adjustZoom);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', adjustZoom);
});
</script>