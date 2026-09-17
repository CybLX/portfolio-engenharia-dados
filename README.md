# Portfólio de engenharia de dados

Projeto separado e original de portfólio estático. Não inclui código-fonte nem dados do empregador. O conteúdo é um rascunho anonimizado que exige revisão dos responsáveis antes da publicação.

## Prévia

Abra `portfolio-preview.html` diretamente em um navegador para revisar todo o conteúdo sem internet. Abra `dist/index.html` para acessar o site de duas páginas; o link do estudo de caso abre `dist/case-study.html`. O JavaScript permite selecionar as visões de arquitetura e ampliar os diagramas. Nenhum serviço em produção, fonte remota, script de análise de tráfego ou serviço de contato é chamado.

## Estrutura

- `dist/`: único diretório destinado à hospedagem pública, após aprovação.
- `content/case-study.md`: texto original do estudo de caso.
- `content/architecture.json`: descrições, nós e conexões compartilhados das cinco visões.
- `diagrams/`: códigos-fonte Mermaid e descrições DOT usadas para renderizar os SVGs.
- `tools/build_site.py`: gerador opcional de páginas sem acesso à rede, usando a biblioteca padrão do Python.
- `CODEX_PROMPT.md`: instruções de continuidade e conclusão.
- `PORTFOLIO_BLUEPRINT.md`: posicionamento, pesquisa verificada de hospedagem e plano de lançamento.

O site não tem dependências em tempo de execução e não exige comando de compilação para hospedagem. Depois de editar o Markdown, os modelos das páginas ou o CSS/JavaScript, gere novamente as páginas e a prévia sem internet com:

```bash
python tools/build_site.py
```

O CSS e o JavaScript em `dist/assets/` são código-fonte autoral. Os SVGs já estão renderizados. Ao atualizar a arquitetura, altere JSON, Mermaid e SVG juntos; todos devem descrever o mesmo grafo. A renderização original dos grafos usou Viz.js 3.25.0 (Graphviz), a partir dos mesmos nós e conexões da saída Mermaid. Não é necessário renderizar Mermaid no navegador do visitante.

## Antes do lançamento

Confirme os dois perfis públicos, as contribuições individuais, o canal de contato da equipe e a permissão para divulgar o estudo de caso abstraído. Os contatos estão intencionalmente sem configuração. Substitua os avisos visíveis de rascunho e `noindex,nofollow` somente após a aprovação do conteúdo. `noindex` é uma orientação de indexação, não um controle de acesso.

Mantenha as exportações originais e o relatório privado de evidências fora deste repositório. Não envie o arquivo de entrega inteiro a um provedor de hospedagem estática; selecione somente `dist`. A publicação não está autorizada até que os responsáveis aprovem o conteúdo e a revisão exatos.

Execute as verificações de responsividade, teclado, diálogos, links, contato e confidencialidade do plano antes do lançamento. A entrega atual inclui validação de código e arquivos, mas a verificação de leiaute e interação em navegador ainda é necessária.

## Hospedagem

Principal: Cloudflare Pages com diretório de saída `dist`, sem predefinição de framework e sem comando de compilação. Alternativa: implantação manual de `dist` no Netlify. Consulte o plano para as restrições e referências atuais dos planos; confira novamente antes do lançamento. Hospedagem gratuita não é garantia permanente, e domínios comprados são cobrados separadamente.
