document.addEventListener('DOMContentLoaded', () => {
    const menuBtn = document.getElementById('mobile-menu-btn');
    const nav = document.querySelector('.main-nav');
    
    if (menuBtn && nav) {
        const icon = menuBtn.querySelector('i');

        menuBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            
            const isOpen = nav.classList.toggle('active');
            icon.className = isOpen ? 'fas fa-times' : 'fas fa-bars';
            
            // Lock body scroll when menu is open
            document.body.style.overflow = isOpen ? 'hidden' : '';
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', (e) => {
            if (nav.classList.contains('active') && !nav.contains(e.target) && !menuBtn.contains(e.target)) {
                nav.classList.remove('active');
                icon.className = 'fas fa-bars';
                document.body.style.overflow = '';
            }
        });

        // Prevent menu clicks from closing the menu
        nav.addEventListener('click', (e) => {
            e.stopPropagation();
        });
    }
});
