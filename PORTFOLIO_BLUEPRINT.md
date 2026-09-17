# Plano do portfólio e do lançamento

Preparado em 8 de setembro de 2026 para uma equipe de dois engenheiros de dados freelancers.

## A recomendação

Comece com uma proposta específica: **conectar documentos, serviços em nuvem e sistemas corporativos em fluxos operacionais compreensíveis**. O projeto fornecido se destaca como estudo de caso de automação de documentos para compras. Comece com um estudo de caso substancial e acrescente demonstrações originais ou projetos profissionais revisados separadamente conforme novas evidências estiverem disponíveis.

Use um pequeno **site estático em HTML/CSS/JavaScript**. A implementação que acompanha este plano tem uma página inicial e uma página detalhada de estudo de caso, não exige servidor nem compilação de framework e inclui uma prévia sem internet. A recomendação principal de hospedagem é Cloudflare Pages; a alternativa é Netlify. O código-fonte permanece portável entre provedores de hospedagem estática.

## O que está pronto

| Entrega | Local |
| --- | --- |
| Inventário privado de componentes, evidências no código, limitações e locais de valores sensíveis | `private-repository-analysis.md`, entregue separadamente; nunca publicar |
| Texto original e anonimizado do estudo de caso | `content/case-study.md` dentro do pacote do portfólio |
| Cinco diagramas de arquitetura editáveis | `diagrams/*.mmd` dentro do pacote |
| Diagramas SVG e site público | `dist/` dentro do pacote |
| Cópia independente para revisão | `portfolio-preview.html` |
| Comando de continuidade para o Codex | `CODEX_PROMPT.md` dentro do pacote e no arquivo de comando entregue separadamente |

O protótipo é um rascunho anonimizado de design e conteúdo. Não é uma versão autorizada para publicação. O sistema de engenharia é representado por diagramas e textos criados do zero; nenhuma implementação proprietária está incluída no pacote do site.

## Posicionamento e serviços iniciais

Título da página inicial: **Faça seus dados trabalharem pela sua operação.**

Texto de apoio: “Conectamos serviços em nuvem, documentos e sistemas corporativos para que as equipes avancem de repasses manuais para fluxos de trabalho rastreáveis.”

| Serviço | Primeira contratação adequada | Entrega concreta |
| --- | --- | --- |
| Fluxos de dados e integrações em nuvem | Conectar uma API de negócio, uma camada de armazenamento e uma aplicação de destino | Contrato de dados documentado, caminho de ingestão e integração funcional e guia operacional |
| Processamento e validação de documentos | Transformar planilhas e anexos recorrentes em entradas estruturadas e validadas | Protótipo com dados sintéticos, verificações de entrada, caminho de exceção e critérios de avaliação acordados |
| Automação operacional | Integrar um sistema que ainda exige interação pelo navegador | Um fluxo de navegador delimitado, comportamento de recuperação e transferência para operação |
| Relatórios operacionais no BigQuery | Facilitar a inspeção de status de processos e operações pendentes | Granularidade de relatório acordada, visões ou consultas SQL e formato de entrega útil |

Essas ofertas de serviços são inferidas da implementação demonstrada, não afirmações de que um cliente freelancer já as contratou. Evite preços, economias garantidas, promessas de prazo, depoimentos, logotipos de clientes ou certificações que não tenham sido fornecidos e aprovados.

Nas primeiras conversas, pergunte ao potencial cliente sobre o fluxo manual, os formatos de entrada, os sistemas atuais, as restrições de acesso, os casos de exceção e a saída pretendida. Ofereça um diagnóstico ou piloto delimitado, com critérios de aceitação escritos, antes de assumir uma implementação ampla. Não use contas, dados nem infraestrutura do empregador em demonstrações freelancer.

## Estrutura do site e direção visual

| Área | Conteúdo e finalidade |
| --- | --- |
| Abertura da página inicial | Explicar os problemas de negócio que os engenheiros ajudam a resolver e oferecer links diretos para o estudo de caso e a área de contato |
| Projeto em destaque | Um destaque amplo para o projeto, com resumo e prévia da arquitetura; descrevê-lo como experiência profissional anonimizada |
| Serviços | Quatro ofertas concretas ligadas às evidências fornecidas |
| Equipe | Dois espaços de perfil; o nome de Bruno Santos é conhecido, mas as contribuições e o nome público do Gabriel Silva ainda precisam de confirmação |
| Contato | Convite para descrever um projeto; ativar links de e-mail e perfil somente após o fornecimento pelos responsáveis |
| Página do estudo de caso | Problema, abordagem, etapas de execução, visões de arquitetura, inventário completo de tecnologias, concessões e limites das evidências |

Sistema visual: azul-marinho profundo `#081D32`, azul nítido `#2155E8`, superfícies brancas, azul-acinzentado claro `#F2F6FB` e detalhes verde-azulados para componentes de documentos e IA. Use fontes sem serifa do sistema, títulos grandes e bem compostos, texto de corpo de 18 px, espaçamento generoso, divisórias finas e destaque editorial para o projeto. Evite paredes de logotipos, painéis fictícios, fotos decorativas de banco de imagens e métricas imaginárias de clientes.

Os diagramas concentram o principal interesse visual. Use SVG para ampliação legível, nomes e descrições acessíveis, explicação em linguagem simples junto de cada visão e um controle de ampliação. Em telas pequenas, mantenha o seletor de visões com rolagem horizontal e coloque o diagrama ampliado em sua própria área rolável; nunca faça a página inteira ultrapassar a largura da tela. Preserve o download do código-fonte Mermaid.

A implementação usa links, botões e diálogos nativos, um link para pular ao conteúdo, estados claros de foco e suporte a movimento reduzido. O site deve continuar útil sem animações. Os controles dos diagramas complementam a explicação escrita.

O portfólio deve usar português brasileiro no lançamento, conforme solicitado. Todo o conteúdo visível, incluindo imagens, diagramas, tabelas, controles e textos de acessibilidade, deve estar em português brasileiro. Preserve os nomes oficiais dos produtos e serviços e revise a tradução das afirmações técnicas.

## Comparação de hospedagem gratuita

Estas são verificações de fontes oficiais em 8 de setembro de 2026, não uma promessa de que qualquer serviço permanecerá gratuito para sempre. O registro de domínio é separado da hospedagem; use inicialmente o subdomínio do provedor.

| Tema | Cloudflare Pages — principal | Netlify Free — alternativa |
| --- | --- | --- |
| Portfólio comercial | Adequado com base na oferta do produto e nos termos revisados; não foi encontrada restrição do plano a uso pessoal. Esta é uma avaliação desses documentos, não permissão incondicional para qualquer uso | O anúncio oficial do plano Free permite explicitamente projetos comerciais; use a página atual de preços para as cotas |
| Endereço incluído e HTTPS | Subdomínio `pages.dev` do provedor e SSL | Subdomínio `netlify.app` do provedor e SSL |
| Tráfego | As requisições e a transferência de dados de páginas estáticas são anunciadas como ilimitadas; funções têm cotas separadas | Cota compartilhada de 300 créditos por mês; transferência custa 20 créditos/GB e requisições web custam 2 créditos a cada 10.000 |
| Limites de implantação | 500 compilações/mês, uma compilação simultânea, tempo limite de 20 minutos | Implantações em produção custam 15 créditos cada; uma compilação simultânea; implantações de prévia e de ramificações não recebem a cobrança de produção, mas suas requisições e tráfego podem consumir créditos |
| Visibilidade do código e acesso para duas pessoas | Repositórios Git públicos ou privados; usuários ilimitados no painel do Pages | Um membro gratuito na plataforma; colaboradores Git ilimitados se aplicam a repositórios públicos. O suporte a repositórios privados de organizações é pago; a implantação manual evita publicar um repositório |
| Disponibilidade contínua | Plano gratuito contínuo, sem vencimento fixo do Pages identificado nas páginas revisadas; os termos permitem encerrar serviços gratuitos | Plano gratuito contínuo; os projetos são pausados quando os créditos acabam, até o próximo ciclo. Não foi estabelecido um prazo separado por inatividade no material revisado |
| Formulário de contato | Arquivos estáticos sozinhos não recebem formulários; acrescente um serviço ou função de formulário, ou use apenas um link de e-mail confirmado | O Netlify Forms pode processar um formulário estático configurado; verifique o plano e o consumo atuais antes da ativação |

Fontes da Cloudflare: [produto Pages e oferta de SSL e tráfego](https://www.cloudflare.com/products/pages/), [limites e suporte a repositórios privados e públicos](https://developers.cloudflare.com/pages/platform/limits/), [contrato de assinatura, incluindo encerramento de serviços gratuitos](https://www.cloudflare.com/terms/) e [instruções de envio direto e subdomínio](https://developers.cloudflare.com/pages/get-started/direct-upload/).

Fontes do Netlify: [declaração de uso comercial](https://www.netlify.com/blog/introducing-netlify-free-plan/), [preços atuais e limites de colaboração](https://www.netlify.com/pricing/), [comportamento quando os créditos acabam](https://www.netlify.com/pricing/personal-vs-free/), [domínios do provedor](https://docs.netlify.com/manage/domains/get-started-with-domains/) e [configuração do Forms](https://docs.netlify.com/manage/forms/setup/). As cotas de tráfego e compilação do anúncio antigo foram substituídas pelos preços atuais e não são usadas aqui.

Como ilustração, duas implantações em produção no Netlify, 1 GB de transferência e 50.000 requisições totalizam aproximadamente 60 créditos nessas tarifas publicadas, antes de qualquer outro consumo medido. É um exemplo de orçamento, não uma previsão do tráfego deste site. A cota é compartilhada: não oferece, de forma independente, 20 implantações mais 15 GB de tráfego.

O Cloudflare Pages é preferível aqui porque seu acesso para duas pessoas e sua oferta de tráfego estático atendem ao projeto, e a entrega não depende de um serviço de aplicação em execução. Mantenha o código portável e o site exportado para poder trocar de hospedagem se os termos ou requisitos mudarem.

### Opções não selecionadas

| Opção | Decisão |
| --- | --- |
| Vercel Hobby | Excluir deste site de captação de clientes: o plano gratuito é restrito a uso pessoal e não comercial. A documentação revisada também lista 100 implantações/dia e limites de uso, mas a elegibilidade é o ponto decisivo. [Documentação oficial do Hobby](https://vercel.com/docs/plans/hobby) |
| GitHub Pages | Um portfólio pessoal de trabalhos pode ser diferente de operar um negócio on-line. Porém, este site divulga explicitamente serviços freelancer; por isso, evite depender de uma interpretação limítrofe das restrições a negócios on-line e transações comerciais. O Pages no GitHub Free também exige repositório público; o tamanho publicado é limitado a 1 GB, com limites flexíveis de 100 GB/mês e 10 compilações/hora. É uma recomendação conservadora, não uma afirmação de que todos os portfólios profissionais são proibidos. [Limites oficiais](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits) |

Nenhum domínio comprado, banco de dados, assinatura de análise de tráfego, modelo pago ou demonstração GCP em execução é necessário para lançar o portfólio. Manter o site público estático não significa que o sistema GCP original seria gratuito para operar.

## Instruções concretas de implantação — após aprovação do conteúdo

### Cloudflare Pages

Para colaboração regular, crie um novo repositório privado contendo apenas o pacote do portfólio. Convide os dois engenheiros para esse repositório usando as contas escolhidas. Nunca conecte o repositório do empregador.

1. No Cloudflare, abra a área de Workers e Pages, escolha o fluxo de criação de Pages e conecte o novo repositório do portfólio.
2. Selecione a ramificação de lançamento revisada. Não use predefinição de framework e deixe o comando de compilação vazio, pois os arquivos publicados já estão prontos. Defina o diretório de saída como `dist`.
3. Revise o conteúdo exato da ramificação e garanta que somente `dist` seja publicado. A análise privada e as exportações originais devem estar ausentes do repositório, não apenas omitidas da página inicial.
4. Defina o nome pretendido para o projeto e revise o subdomínio resultante. Publicar é uma decisão separada dos responsáveis; conectar uma ramificação com implantação automática pode publicar envios posteriores automaticamente.
5. Após aprovação explícita, implante a revisão aprovada, abra os endereços da página inicial e do estudo de caso, verifique HTTPS e links e peça ao segundo engenheiro que confirme o acesso.
6. Mantenha uma revisão conhecida e funcional para reversão. Alterações futuras de conteúdo devem ser revisadas por solicitações de integração antes de chegar à ramificação de lançamento.

[Guia oficial de integração com Git](https://developers.cloudflare.com/pages/get-started/git-integration/).

Para uma primeira publicação manual, o envio direto do Pages aceita a pasta `dist` preparada ou um arquivo compactado com seu conteúdo. Um projeto de envio direto não pode mudar posteriormente para integração com Git; use um novo projeto Pages se precisar desse fluxo. Não envie o ZIP completo da entrega como conteúdo do site. [Guia oficial de envio direto](https://developers.cloudflare.com/pages/get-started/direct-upload/).

### Alternativa Netlify

1. O responsável designado pela implantação deve criar o projeto na própria conta.
2. Use o fluxo de implantação manual do Netlify e selecione a pasta `dist` preparada. Isso não exige tornar público um repositório de código-fonte.
3. Revise a visibilidade e o estado de publicação apresentados pela conta, o subdomínio pretendido e o conteúdo exato enviado antes de torná-lo público.
4. Após aprovação, publique, verifique HTTPS e as duas páginas e consulte o consumo de créditos no painel.
5. Mantenha os dois engenheiros colaborando no repositório de código separado. Não presuma que a segunda pessoa recebe uma licença gratuita de usuário na plataforma Netlify nem direitos de implantação de repositórios privados.

[Instruções oficiais de implantação](https://docs.netlify.com/deploy/create-deploys/).

Use inicialmente um contato `mailto:` confirmado. Um formulário só deve ser adicionado com destinatário e serviço de recebimento reais, estados de envio compreensíveis e teste que confirme o recebimento efetivo. Nunca mostre uma mensagem de sucesso para um formulário que não envia nada.

## Fases de implementação e critérios de aceitação

| Fase | Trabalho | Critérios de aceitação |
| --- | --- | --- |
| 1. Evidências | Reconstruir o sistema fornecido e distinguir código, configuração, documentação e inferência | Cada serviço e conexão públicos correspondem a evidências; todas as lacunas do código são registradas em privado |
| 2. Abstração pública | Escrever o texto original do estudo de caso e cinco diagramas | Nenhum nome ou logotipo do empregador, identificador interno, código copiado, comando ou regra proprietária, credencial, captura de tela ou registro real no pacote público |
| 3. Implementação visual | Criar página inicial, estudo de caso completo, visões de diagramas e seções de equipe e contato | Arquivos locais abrem sem servidor; hierarquia legível; ausência de métricas falsas, depoimentos e links inventados |
| 4. Informações dos responsáveis | Confirmar nomes, contribuições, contatos, posicionamento e permissão de divulgação | Os dois perfis são verdadeiros; contatos funcionam; o conteúdo anonimizado exato está liberado para publicação |
| 5. Verificação de qualidade | Verificar páginas em 360, 390, 768, 1280 e 1440 px; navegação por teclado, ampliação de texto de 200%, movimento reduzido, ampliação de diagramas e links | Sem transbordamento da página inteira nem texto cortado; diálogos contêm e restauram o foco; links funcionam; capturas revisadas; revisão de confidencialidade aprovada |
| 6. Lançamento | Preparar a saída revisada, obter aprovação de publicação e implantar | Revisão exata aprovada; termos da hospedagem conferidos novamente; HTTPS verificado; revisão para reversão preservada |

O pacote fornecido inclui verificações concluídas de código, links, sintaxe e confidencialidade. A verificação de responsividade e interação em navegador ainda precisa ser executada localmente antes da publicação; este ambiente não oferece um servidor de prévia compatível com este site estático sem compilação. O HTML para download é a prévia concreta de revisão. Verificações automatizadas do código não estabelecem correção visual em nível de pixels nem conformidade com WCAG.

## Decisões ainda necessárias antes da publicação

- Perfis públicos preferidos dos dois engenheiros.
- Endereço de contato pessoal ou profissional pertencente à equipe, não uma caixa de e-mail do empregador.
- Contribuições individuais e eventuais medições de resultados não confidenciais aprovadas.
- Confirmação de que essa arquitetura corporativa abstraída pode ser publicada. Caso não possa, substituir o estudo de caso profissional por uma demonstração sintética implementada de forma independente.
- Aprovação do conteúdo final específico e da revisão antes da implantação pública.

Nenhuma implantação pública foi realizada. A entrega do código e de um rascunho anonimizado não implica permissão para divulgar material derivado do empregador.
