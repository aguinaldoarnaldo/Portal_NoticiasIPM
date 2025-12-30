document.addEventListener('DOMContentLoaded', () => {
    // ----------------------------------------------------
    // 1. Funcionalidade de Troca de Abas (Recentes/Vistas)
    // ----------------------------------------------------
    const tabButtons = document.querySelectorAll('.tab-button');
    const newsFeed = document.querySelector('.recent-news');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            // Remove a classe 'active' de todos os botões
            tabButtons.forEach(btn => btn.classList.remove('active'));

            // Adiciona a classe 'active' ao botão clicado
            button.classList.add('active');

            const filterType = button.getAttribute('data-filter');
            
            // SIMULAÇÃO DA TROCA DE CONTEÚDO
            const items = newsFeed.querySelectorAll('.news-item');

            // Aqui você faria uma requisição AJAX para carregar dados reais
            // Ou, como simulação, apenas troca o conteúdo de um dos itens
            
            if (filterType === 'vistas') {
                console.log("Carregando Notícias Mais Vistas...");
                // Simulação: Apenas para mostrar que algo mudou (na vida real, você trocaria todos os itens)
                items[0].querySelector('h4').textContent = "AVISO URGENTE: Datas de Provas Alteradas!";
                items[0].querySelector('.category-tag').textContent = "IMPORTANTE";
            } else {
                console.log("Carregando Notícias Mais Recentes...");
                // Retorna ao estado inicial (Simulação)
                items[0].querySelector('h4').textContent = "Festa Junina Bate Recorde de Público";
                items[0].querySelector('.category-tag').textContent = "CULTURA";
            }
        });
    });

    // ----------------------------------------------------
    // 2. Funcionalidade de Menu Mobile (Opcional, se o menu for complexo)
    // ----------------------------------------------------
    // Se você usar um ícone de "hamburguer" no mobile, adicione aqui a função
    // para abrir/fechar o menu de navegação.
});