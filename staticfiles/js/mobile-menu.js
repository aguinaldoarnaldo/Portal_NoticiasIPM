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
    
    // Set active menu item based on current URL
    const currentPath = window.location.pathname;
    const menuLinks = document.querySelectorAll('.main-nav a');
    
    menuLinks.forEach(link => {
        // Remove any existing active class
        link.classList.remove('active');
        
        const href = link.getAttribute('href');
        
        // Check for exact match or path starts with
        if (currentPath === href || 
            (href !== '/' && currentPath.startsWith(href)) ||
            (href.includes('/eventos') && currentPath.includes('/evento')) ||
            (href.includes('/notice') && currentPath.includes('/noticia'))) {
            link.classList.add('active');
        }
    });
});
