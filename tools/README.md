# Ferramentas opcionais de edição

O site entregue não precisa de instalação de pacotes nem de etapa de compilação para ser servido.

Para atualizar a renderização dos diagramas, edite `content/architecture.json`. Na raiz do portfólio, instale o renderizador opcional com `npm install --no-save @viz-js/viz@3.25.0` e execute `node tools/render_diagrams.mjs`. Ele gera novamente os arquivos Mermaid, DOT e SVG a partir do mesmo grafo. Em seguida, execute `python tools/build_site.py` para atualizar as duas páginas e a prévia sem internet.

Não publique `node_modules`, arquivos de edição nem evidências privadas do código. Publique somente o diretório `dist` revisado.
