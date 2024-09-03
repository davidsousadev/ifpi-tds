const url = 'https://servicodados.ibge.gov.br/api/v3/noticias/';
function busca() {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro na resposta da API');
            }
            return response.json();
        })
        .then(data => {
            if (data.erro) {
                console.log('Erro ao buscar as notícias.');
                return;
            }
            alimentarBlog(data);
        })
        .catch(error => {
            console.error('Erro ao buscar notícias:', error);
            console.log('Erro ao buscar as notícias.');
        });
}
function alimentarBlog(data) {
    if (data.items && Array.isArray(data.items) && data.items.length > 0) {
        const ids = ['1', '2', '3', '4', '5', '6'];

        ids.forEach(id => {
            const item = data.items[id - 1];
            const p = document.querySelector(`#p${id}`);
            const ip = document.querySelector(`#ip${id}`);
            const imagens = JSON.parse(item.imagens.replace(/\\/g, ''));
            p.textContent = item.titulo;
            p.href = item.link;
            ip.src = "https://agenciadenoticias.ibge.gov.br/" + imagens.image_intro;
            console.log(ip.src);
        });
    } else {
        console.log('Nenhuma notícia encontrada.');
    }
}
busca();