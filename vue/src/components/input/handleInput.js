let typingTimeout = null;

export function handleInput(event, emit, name) {
    clearTimeout(typingTimeout);
    typingTimeout = setTimeout(() => {
        emit('update:value', {name, value: event.target.value});
		console.log('emit');
    }, 500);
}