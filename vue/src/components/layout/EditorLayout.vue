<template>
    <main class="grid grid-cols-[5rem,4fr,5fr] overflow-hidden">
        <Sidebar/>
        <slot></slot>
        <div 
            ref="container" 
            class="flex items-center justify-center bg-base-100 relative overflow-hidden select-none"
            @wheel="handleMouseWheel"
            @mousedown="handleMouseDown"
        >
            <div ref="page" class="shadow-sm">
                <CurrentTemplate/>
            </div>
        </div>
    </main>
</template>

<script setup>
import { onMounted, ref, onBeforeUnmount } from 'vue';
import Sidebar from '@/components/sidebar/Sidebar.vue';
import CurrentTemplate from '@/components/template/CurrentTemplate.vue';

const container = ref(null);
const page = ref(null);
const scaleStep = 0.1;

let currentScale;
let translateX = 0;
let translateY = 0;
let isDragging = false;
let lastPosX = 0;
let lastPosY = 0;

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
        currentScale = Math.min(3.0, Math.max(0.3, currentScale + delta * scaleStep));
    } else {
        translateY += delta * 50;
    }
    updateTransform();
};

const handleMouseDown = (event) => {
    isDragging = true;
    lastPosX = event.clientX;
    lastPosY = event.clientY;
};

const handleMouseUp = () => {
    isDragging = false;
};

const handleMouseMove = (event) => {
    if (isDragging) {
        const dx = event.clientX - lastPosX;
        const dy = event.clientY - lastPosY;
        translateX += dx;
        translateY += dy;
        updateTransform();
        lastPosX = event.clientX;
        lastPosY = event.clientY;
    }
};

onMounted(() => {
    adjustZoom();
    window.addEventListener('resize', adjustZoom);
    window.addEventListener('mouseup', handleMouseUp);
    window.addEventListener('mousemove', handleMouseMove);
});

onBeforeUnmount(() => {
    window.removeEventListener('resize', adjustZoom);
    window.removeEventListener('mouseup', handleMouseUp);
    window.removeEventListener('mousemove', handleMouseMove);
});
</script>