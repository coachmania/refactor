<template>
	<CardTitle>Photo</CardTitle>
	<div class="grid gap-md grid-cols-[auto,1fr]">
		<div class="h-full flex flex-col items-center gap-md">
			<PictureDisplay :isHidden="isHidden"/>
			<HideButton
				:isHidden="isHidden"
				@click="updateValue"
			/>
		</div>
		<DropZone/>
	</div>
</template>

<script setup>
import { ref } from 'vue';
import CardTitle from '../global/CardTitle.vue';
import PictureDisplay from './PictureDisplay.vue';
import HideButton from './HideButton.vue';
import DropZone from './DropZone.vue';

const isHidden = ref(true);

// TODO voir ici quand on fetch je pense que le mieux cest de fetch une seule fois dans le parent et de passer la valeur en props

function updateValue(value) {
	// TODO : call API
	isHidden.value = !isHidden.value;
}
</script>