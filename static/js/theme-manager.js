/**
 * IPM Notícias - Gerenciador de Tema Manual (V2)
 * Corrigido para funcionar corretamente no Chrome/Edge independente da posição do script.
 */

(function() {
    'use strict';

    const STORAGE_KEY = 'ipm-theme';
    const THEMES = {
        LIGHT: 'light',
        DARK: 'dark'
    };

    /**
     * Obtém o tema salvo ou o padrão
     */
    function getSavedTheme() {
        try {
            const saved = localStorage.getItem(STORAGE_KEY);
            return (saved === THEMES.DARK) ? THEMES.DARK : THEMES.LIGHT;
        } catch (e) {
            return THEMES.LIGHT;
        }
    }

    /**
     * Aplica o tema ao elemento raiz (HTML) para evitar erros no Chrome
     */
    function applyTheme(theme) {
        // Usar documentElement (html) é mais seguro que o body para scripts no head
        document.documentElement.setAttribute('data-theme', theme);
        // Também aplicar ao body se já existir
        if (document.body) {
            document.body.setAttribute('data-theme', theme);
        }
        
        try {
            localStorage.setItem(STORAGE_KEY, theme);
        } catch (e) {}

        // Atualizar ícone do botão se o DOM já estiver pronto
        const updateIcon = () => {
            const toggleBtn = document.getElementById('theme-toggle');
            if (toggleBtn) {
                const icon = toggleBtn.querySelector('i');
                if (icon) {
                    icon.className = theme === THEMES.DARK ? 'fas fa-sun' : 'fas fa-moon';
                }
            }
        };

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', updateIcon);
        } else {
            updateIcon();
        }
    }

    /**
     * Alterna entre os temas
     */
    function toggleTheme(e) {
        if (e) e.preventDefault();
        const currentTheme = document.documentElement.getAttribute('data-theme') || THEMES.LIGHT;
        const newTheme = currentTheme === THEMES.DARK ? THEMES.LIGHT : THEMES.DARK;
        applyTheme(newTheme);
    }

    /**
     * Inicialização robusta
     */
    function init() {
        const initialTheme = getSavedTheme();
        applyTheme(initialTheme);
        
        const setupListener = () => {
            const toggleBtn = document.getElementById('theme-toggle');
            if (toggleBtn) {
                // Remover se já existir para evitar duplicados
                toggleBtn.removeEventListener('click', toggleTheme);
                toggleBtn.addEventListener('click', toggleTheme);
                console.log("[IPM Tema] Listener configurado.");
            }
        };

        // Ouvir mudanças no localStorage vindas de outras abas
        window.addEventListener('storage', (e) => {
            if (e.key === STORAGE_KEY) {
                applyTheme(e.newValue || THEMES.LIGHT);
            }
        });

        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', setupListener);
        } else {
            setupListener();
        }
    }

    // Execução imediata
    init();
})();
