const mobileMenuButton = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuButton.addEventListener('click', function() {
    const isOpen = mobileMenu.getAttribute('aria-expanded') === 'true';
    mobileMenuButton.classList.toggle('bg-gray-700');
    mobileMenuButton.classList.toggle('text-white');
    mobileMenuButton.classList.toggle('hover:bg-gray-700');
    mobileMenuButton.classList.toggle('hover:text-white');
    mobileMenu.setAttribute('aria-expanded', !isOpen);
    mobileMenu.classList.toggle('hidden');
})
