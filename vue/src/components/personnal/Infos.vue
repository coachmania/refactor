<template>
	<CardLayout>
		<CardTitle title="Informations personnelles"/>
		<div class="grid grid-cols-2 gap-md">
			<!-- TODO ADD text input -->
			<TextInput
				label="Prénom"
				placeholder="Jean"
				name="first_name"
				:value="firstName"
				@update:value="updateValue"
			/>
			<TextInput
				label="Nom"
				placeholder="Dupont"
				name="name"
				:value="name"
				@update:value="updateValue"
			/>
			<TextInput
				label="Téléphone"
				placeholder="06 12 34 56 78"
				name="phone"
				:value="phone"
				@update:value="updateValue"
			/>
			<TextInput
				label="Email"
				placeholder="jean@jobmania.fr"
				name="email"
				:value="email"
				@update:value="updateValue"
			/>
			<!-- TODO replace by numberInput -->
			<TextInput
				label="Âge"
				placeholder="20"
				name="age"
				:value="age"
				@update:value="updateValue"
			/>
			<!-- TODO replace by dateInput -->
			<TextInput
				label="Date de naissance"
				placeholder="01/01/2000"
				name="birthdate"
				:value="birthdate"
				@update:value="updateValue"
			/>
		</div>
	</CardLayout>
</template>

<script setup>
import CardLayout from '../layout/CardLayout.vue';
import CardTitle from '../global/CardTitle.vue';
import TextInput from '../input/TextInput.vue';
</script>