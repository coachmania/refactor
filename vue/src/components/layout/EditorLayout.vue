<template>
    <main class="grid grid-cols-[5rem,4fr,5fr] overflow-hidden">
        <Sidebar/>
        <slot name="editor"></slot>
        <div>
            <!-- <slot name="content"></slot> -->
            <p>EDITOR</p>
        </div>
    </main>
</template>

<script setup>
import Sidebar from '@/components/sidebar/Sidebar.vue';
</script>