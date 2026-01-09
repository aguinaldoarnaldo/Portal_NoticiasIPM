/**
 * IPM Notícias - Sistema de Tema Automático
 * Regras:
 * - 6h às 18h: Tema Light (padrão)
 * - 18h às 6h: Tema Dark
 */

(function() {
    'use strict';

    const LIGHT_START = 6;  // 6:00
    const DARK_START = 18;  // 18:00

    /**
     * Determina o tema baseado na hora atual
     * @returns {string} 'light' ou 'dark'
     */
    function getThemeByTime() {
        const hour = new Date().getHours();
        // Das 6h às 17h59 = Light, das 18h às 5h59 = Dark
        if (hour >= LIGHT_START && hour < DARK_START) {
            return 'light';
        }
        return 'dark';
    }

    /**
     * Aplica o tema ao body
     * @param {string} theme - 'light' ou 'dark'
     */
    function applyTheme(theme) {
        document.body.setAttribute('data-theme', theme);
        console.log(`[IPM Tema] Tema ${theme} aplicado às ${new Date().toLocaleTimeString()}`);
    }

    /**
     * Calcula milissegundos até a próxima mudança de tema
     * @returns {number} milissegundos
     */
    function getMillisecondsUntilNextChange() {
        const now = new Date();
        const hour = now.getHours();
        
        let targetHour;
        if (hour >= DARK_START || hour < LIGHT_START) {
            // Estamos no período dark, próxima mudança às 6h
            targetHour = LIGHT_START;
        } else {
            // Estamos no período light, próxima mudança às 18h
            targetHour = DARK_START;
        }

        const target = new Date();
        target.setHours(targetHour, 0, 0, 0);
        
        // Se o horário alvo já passou hoje, adicionar 1 dia
        if (target <= now) {
            target.setDate(target.getDate() + 1);
        }

        return target - now;
    }

    /**
     * Agenda a próxima mudança de tema
     */
    function scheduleNextChange() {
        const msUntilChange = getMillisecondsUntilNextChange();
        const minutesUntilChange = Math.round(msUntilChange / 60000);
        
        console.log(`[IPM Tema] Próxima mudança de tema em ${minutesUntilChange} minutos`);
        
        setTimeout(function() {
            applyTheme(getThemeByTime());
            scheduleNextChange(); // Agendar a próxima mudança
        }, msUntilChange);
    }

    /**
     * Inicializa o sistema de tema
     */
    function init() {
        // Aplicar tema inicial
        applyTheme(getThemeByTime());
        
        // Agendar próxima mudança automática
        scheduleNextChange();
    }

    // Executar quando o DOM estiver pronto
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
