<template>
	<CardLayout>
		<CardTitle>Adresse</CardTitle>
		<AlertBox classColor="alert-info">
			Dans un CV, on ne met pas l'adresse complète. Le complément d'adresse sert ici à indiquer un arrêt de bus, de métro, etc.
		</AlertBox>
		<div class="grid grid-cols-3 gap-md">
			<TextInput
				class="col-span-2"
				label="Complément d'adresse"
				placeholder="Arrêt de bus, étage, etc."
				name="additional"
				:value="additional"
				@update:value="updateValue"
			/>
			<!-- TODO change to number or postalCode input -->
			<TextInput
				class="col-span-1"
				label="Code postal"
				placeholder="69006"
				name="postal_code"
				:value="postalCode"
				@update:value="updateValue"
			/>
		</div>
		<div class="grid grid-cols-2 gap-md">
			<TextInput
				label="Ville"
				placeholder="Lyon"
				name="city"
				:value="city"
				@update:value="updateValue"
			/>
			<!-- TODO change to select country input champs hybrid libre ou parmis un liste (autocompletion) -->
			<TextInput
				label="Pays"
				placeholder="France"
				name="country"
				:value="country"
				@update:value="updateValue"
			/>
		</div>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import AlertBox from '../global/AlertBox.vue';
import TextInput from '../input/TextInput.vue';
</script>