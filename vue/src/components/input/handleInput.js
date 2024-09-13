let typingTimeout = null;

export function handleInput(value, emit, name) {
    clearTimeout(typingTimeout);
    typingTimeout = setTimeout(() => {
        emit('update:value', {name, value: value});
    }, 500);
}