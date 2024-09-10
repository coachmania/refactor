<template>
    <div class="grid grid-cols-[5rem,4fr,5fr]">
        <Sidebar/>
        <div>
            <slot name="editor"></slot>
        </div>
        <div>
            <!-- <slot name="content"></slot> -->
            <p>EDITOR</p>
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/sidebar/Sidebar.vue';

export default {
    name: 'EditorLayout',
    components: {
        Sidebar,
    }
};
</script>