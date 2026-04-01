// Close dropdown on outside click
document.addEventListener('click', (e) => {
    document.querySelectorAll('.dropdown').forEach(d => {
        if (!d.contains(e.target)) d.classList.remove('open');
    });
});

document.querySelectorAll('.dropdown > a').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
        e.preventDefault();
        trigger.parentElement.classList.toggle('open');
    });
});

// Dropdown — toggle on click, close on outside click
document.addEventListener('click', (e) => {
    document.querySelectorAll('.dropdown').forEach(d => {
        if (!d.contains(e.target)) d.classList.remove('open');
    });
});

document.querySelectorAll('.dropdown > a').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
        e.preventDefault();
        trigger.parentElement.classList.toggle('open');
    });
});