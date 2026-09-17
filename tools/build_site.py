"""Gerar novamente as páginas HTML portáveis a partir do conteúdo original do portfólio; sem acesso à rede."""
from pathlib import Path
import base64
import html
import json
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / 'dist'

def inline(text):
    text = html.escape(text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    return text

def markdown(text):
    lines = text.strip().splitlines()
    out, i = [], 0
    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue
        if line.startswith('|'):
            rows=[]
            while i < len(lines) and lines[i].strip().startswith('|'):
                row=[c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[: -]+',c) for c in row): rows.append(row)
                i += 1
            out.append('<div class="table-scroll" tabindex="0" role="region" aria-label="Comparação técnica com rolagem"><table><thead><tr>'+''.join('<th scope="col">'+inline(c)+'</th>' for c in rows[0])+'</tr></thead><tbody>')
            for row in rows[1:]: out.append('<tr>'+''.join('<td>'+inline(c)+'</td>' for c in row)+'</tr>')
            out.append('</tbody></table></div>')
        elif re.match(r'^\d+\. ',line):
            out.append('<ol>')
            while i<len(lines) and re.match(r'^\d+\. ',lines[i].strip()):
                out.append('<li>'+inline(re.sub(r'^\d+\. ','',lines[i].strip()))+'</li>');i+=1
            out.append('</ol>')
        else:
            paragraph=[line];i+=1
            while i<len(lines) and lines[i].strip() and not lines[i].startswith('|') and not re.match(r'^\d+\. ',lines[i]):
                paragraph.append(lines[i].strip());i+=1
            out.append('<p>'+inline(' '.join(paragraph))+'</p>')
    return '\n'.join(out)

def data_uri(path,mime):
    return 'data:'+mime+';base64,'+base64.b64encode(path.read_bytes()).decode()

graphs=json.loads((ROOT/'content/architecture.json').read_text())
source=(ROOT/'content/case-study.md').read_text()
parts=re.split(r'^## (.+)$',source,flags=re.M)
sections={parts[i]:parts[i+1] for i in range(1,len(parts),2)}

def header(home='index.html'):
    return f'''<a class="skip-link" href="#main">Ir para o conteúdo</a>
    <div class="review-note">Rascunho do portfólio · Experiência profissional anonimizada · Preparado para revisão</div>
    <header class="site-header"><div class="wrap header-row"><a class="brand" href="{home}" aria-label="Página inicial de Engenharia de Dados"><span class="brand-mark" aria-hidden="true">/ /</span><span>Engenharia<br>de Dados</span></a><nav class="nav" aria-label="Navegação principal"><a href="{home}#work">Projetos</a><a href="{home}#services">Serviços</a><a href="{home}#team">Equipe</a><a class="nav-contact" href="{home}#contact">Vamos conversar</a></nav></div></header>'''

def footer():
    return '''<footer class="site-footer"><div class="wrap footer-row"><span>Engenharia de dados · Integrações em nuvem · Automação operacional</span><span>Apresentação original do portfólio · 2026</span></div></footer>'''

def diagrams(embedded=False):
    short=['Entrada e roteamento','Documentos','Conclusão','Implantação','Visibilidade']
    buttons=[];panels=[]
    for i,g in enumerate(graphs):
        gid=g['id']
        svg=ROOT/'dist/assets/diagrams'/f'{gid}.svg'
        uri=data_uri(svg,'image/svg+xml') if embedded else f'assets/diagrams/{gid}.svg'
        mmd=(ROOT/'diagrams'/f'{gid}.mmd').read_text()
        download='data:text/plain;charset=utf-8,'+quote(mmd,safe='')
        svg_download=data_uri(svg,'image/svg+xml') if embedded else uri
        buttons.append(f'<button type="button" role="tab" id="tab-{gid}" aria-selected="{str(i==0).lower()}" aria-controls="panel-{gid}" tabindex="{0 if i==0 else -1}">{short[i]}</button>')
        hidden=' hidden' if i else ''
        panels.append(f'''<div class="diagram-panel" role="tabpanel" id="panel-{gid}" aria-labelledby="tab-{gid}" tabindex="0"{hidden}><h3>{html.escape(g['title'])}</h3><p>{html.escape(g['summary'])}</p><div class="diagram-stage" tabindex="0" role="region" aria-label="Diagrama de arquitetura com rolagem"><img id="img-{gid}" src="{uri}" alt="{html.escape(g['title'])}" loading="lazy"></div><div class="diagram-actions"><button class="button subtle" type="button" data-expand-diagram="img-{gid}">Ampliar diagrama <span aria-hidden="true">↗</span></button><a href="{download}" download="{gid}.mmd">Código-fonte Mermaid</a><a href="{svg_download}" download="{gid}.svg">Baixar SVG</a></div><p class="detail">{html.escape(g['detail'])}</p></div>''')
    return '<div class="legend"><span><i aria-hidden="true"></i>Dados ou mensagens</span><span><i class="dashed" aria-hidden="true"></i>Chamadas de controle ou contratos externos identificados</span></div><div class="diagram-tabs" role="tablist" aria-label="Visões da arquitetura" data-tabs>'+''.join(buttons)+'</div>'+''.join(panels)+'<noscript><p>A seleção de visões exige JavaScript. O fluxo completo descrito abaixo continua disponível; os códigos-fonte de todos os diagramas estão incluídos no pacote do portfólio.</p></noscript>'

def case_body(embedded=False):
    mapping=[('problem','O problema operacional','O problema operacional'),('implementation','A implementação','Como o sistema se conecta'),('flow','Execução técnica','Da entrada à saída'),('decisions','Decisões de engenharia e concessões','Decisões de engenharia'),('modeling','Modelagem de dados','Semântica dos dados e relatórios'),('controls','Confiabilidade e segurança','Controles e limites'),('stack','Inventário de tecnologias','Todas as tecnologias utilizadas'),('contributions','Resultados e contribuições','Resultados e contribuições'),('fit','Projetos freelancer relacionados','Onde essa experiência se aplica')]
    content=[]
    for id,key,title in mapping:
        content.append(f'<section id="case-{id}"><h2>{title}</h2>{markdown(sections[key])}</section>')
        if id=='implementation': content.append('<section id="case-architecture"><div class="eyebrow blue">Arquitetura / cinco visões</div><h2>Acompanhe as conexões.</h2>'+diagrams(embedded)+'</section>')
    nav='<nav class="case-nav" aria-label="Seções do estudo de caso"><span class="nav-label">Por dentro do projeto</span><a href="#case-problem">O problema</a><a href="#case-architecture">Arquitetura</a><a href="#case-flow">Fluxo técnico</a><a href="#case-decisions">Decisões</a><a href="#case-stack">Tecnologias utilizadas</a><a href="#case-contributions">Contribuições</a></nav>'
    return '''<div class="wrap"><div class="case-hero"><div class="eyebrow blue">Experiência profissional / estudo de caso anonimizado</div><h1>Dos documentos recebidos<br>às ações de compras.</h1><p>Uma plataforma na GCP que conecta validação de documentos, roteamento de eventos, automação de navegador e relatórios operacionais.</p></div><div class="case-layout">'''+nav+'<div class="case-body">'+''.join(content)+'''<p class="case-note">Esta é uma apresentação original e anonimizada de experiência profissional. Ela descreve a arquitetura sustentada pelo código e limites explicitamente identificados. Nomes, contribuições individuais e permissão de publicação precisam ser confirmados pelos responsáveis antes do lançamento.</p><div class="case-end"></div></div></div></div>'''

def diagram_dialog():
    return '''<dialog id="diagram-dialog" class="diagram-dialog" aria-labelledby="diagram-dialog-title"><div class="dialog-header"><span id="diagram-dialog-title">Diagrama de arquitetura</span><button type="button" class="close-button" data-close-dialog autofocus>Fechar</button></div><div class="dialog-image" tabindex="0" role="region" aria-label="Diagrama ampliado; role para examinar"><img alt="Arquitetura ampliada"></div></dialog>'''

def homepage(embedded=False):
    target='#case-dialog' if embedded else 'case-study.html'
    open_attr=' data-open-case' if embedded else ''
    services=[('01','Fluxos de dados e integrações em nuvem','Conecte APIs, armazenamento e sistemas de destino com contratos definidos e visibilidade operacional.'),('02','Processamento e validação de documentos','Transforme planilhas recorrentes e arquivos de apoio em entradas estruturadas com caminhos claros para exceções.'),('03','Automação operacional','Conecte fluxos corporativos executados no navegador ao processamento em nuvem e a um comportamento de recuperação compreensível.'),('04','Relatórios operacionais no BigQuery','Reúna status de processos, operações pendentes e resultados de entregas em visões SQL e relatórios úteis.')]
    service_html=''.join(f'<article class="service"><span class="service-number">{num}</span><div><h3>{title}</h3><p>{text}</p></div></article>' for num,title,text in services)
    body=f'''{header('' if embedded else 'index.html')}<main id="main"><div class="wrap hero"><div><div class="eyebrow blue">Engenharia de dados · Automação · GCP</div><h1>Faça seus dados<br><span>trabalharem pela</span><br>sua operação.</h1><p class="lead">Conectamos serviços em nuvem, documentos e sistemas corporativos para que as equipes avancem de repasses manuais para fluxos de trabalho rastreáveis.</p><div class="actions"><a class="button" href="{target}"{open_attr}>Conheça nossos projetos <span class="arrow" aria-hidden="true">↗</span></a><a class="button secondary" href="#contact">Converse sobre um projeto</a></div></div><aside class="hero-card" aria-label="Nosso foco em engenharia"><div class="eyebrow">Da entrada à ação operacional</div><h2>Um processo conectado.<br>Diferentes disciplinas de engenharia.</h2><div class="flow-row"><span class="flow-no">01</span><div><strong>Entender a entrada</strong><p>Documentos, APIs, regras de negócio<br>e as exceções entre as etapas.</p></div></div><div class="flow-row"><span class="flow-no">02</span><div><strong>Conectar o fluxo</strong><p>Serviços em nuvem, contratos de eventos<br>e integrações corporativas.</p></div></div><div class="flow-row"><span class="flow-no">03</span><div><strong>Dar visibilidade às operações</strong><p>Status de processamento, artefatos de entrega<br>e relatórios operacionais úteis.</p></div></div><div class="flow-foot">Python e SQL &nbsp; / &nbsp; Arquitetura em nuvem &nbsp; / &nbsp; Automação</div></aside></div>
    <section id="work" class="section work-section"><div class="wrap"><div class="section-top"><div><div class="eyebrow blue">Projeto selecionado / 01</div><h2>Sistemas complexos.<br>Explicados com clareza.</h2></div><p>Uma análise da engenharia por trás de um fluxo corporativo orientado por documentos.</p></div><article class="project-feature"><div class="project-copy"><span class="pill">Experiência profissional anonimizada</span><h3>Automação de documentos<br>para compras</h3><p>Uma plataforma conectada para validar solicitações, interpretar anexos, rotear operações de navegador e reportar resultados operacionais.</p><a class="text-link" href="{target}"{open_attr}>Leia o estudo de caso <span class="arrow" aria-hidden="true">↗</span></a><div class="scope-bar"><div><strong>11</strong><span>Funções<br>HTTP</span></div><div><strong>03</strong><span>Fluxos de<br>navegador</span></div><div><strong>02</strong><span>Visões de<br>relatórios</span></div></div><p class="scope-note">Escopo da arquitetura definido no código. Não representa métricas de desempenho em produção.</p></div><div class="project-visual" aria-label="Componentes selecionados do estudo de caso"><div class="architecture-label">VISÃO GERAL DA ARQUITETURA</div><div class="work-node"><strong>Processamento de documentos</strong><p>Cloud Run · Cloud Vision · Vertex AI</p></div><div class="work-node blue"><strong>Validação e roteamento de operações</strong><p>Cloud Functions · Pub/Sub · Cloud Storage</p></div><div class="work-split"><div class="work-node"><strong>Operações no navegador</strong><p>Compute Engine<br>Playwright</p></div><div class="work-node"><strong>Visibilidade operacional</strong><p>BigQuery<br>Cloud Monitoring</p></div></div><div class="architecture-label">EXPLORE CINCO VISÕES EDITÁVEIS DA ARQUITETURA</div></div></article></div></section>
    <section id="services" class="section"><div class="wrap"><div class="section-top"><div><div class="eyebrow blue">Como podemos ajudar</div><h2>Comece pelo fluxo<br>que você quer melhorar.</h2></div><p>Trabalho de engenharia focado, com entradas, entregas e critérios de aceitação claros.</p></div><div class="service-grid">{service_html}</div></div></section>
    <section id="team" class="section team-section"><div class="wrap"><div class="section-top"><div><div class="eyebrow">A equipe</div><h2>Dois engenheiros.<br>O mesmo foco na entrega.</h2></div><p>Experiência profissional em engenharia de dados corporativa, aplicada a projetos freelancer com escopo bem definido.</p></div><div class="team-grid"><article class="person"><div class="number">ENGENHEIRO / 01</div><h3>Bruno Santos</h3><div class="role">Especialista em Engenharia de Dados</div><div class="pending">Perfil e contribuições individuais no projeto<br>a confirmar antes da publicação.</div></article><article class="person"><div class="number">ENGENHEIRO / 02</div><h3>Gabriel Silva</h3><div class="role">Especialista em Engenharia de Dados</div><div class="pending">Nome público, perfil e contribuições no projeto<br>a confirmar antes da publicação.</div></article></div></div></section>
    <section id="contact" class="contact-section"><div class="wrap contact-box"><div><div class="eyebrow blue">Vamos conversar sobre seu projeto</div><h2>O que sua equipe gostaria<br>de deixar de fazer manualmente?</h2></div><div><p>Conte sobre o fluxo de trabalho, os sistemas envolvidos e o resultado de que você precisa.</p><div class="contact-pending">Os contatos públicos da equipe serão adicionados antes do lançamento.</div><details><summary>O que incluir na descrição do seu projeto</summary><ul><li>O fluxo atual e seu principal problema.</li><li>Os formatos de entrada e os sistemas conectados.</li><li>A saída necessária e como você vai avaliá-la.</li><li>As restrições de acesso e o prazo desejado.</li></ul></details></div></div></section></main>{footer()}'''
    if embedded: body+='<dialog id="case-dialog" class="case-dialog" aria-labelledby="case-dialog-title"><div class="dialog-header"><span id="case-dialog-title">Projeto / Automação de documentos para compras</span><button type="button" class="close-button" data-close-dialog autofocus>Fechar</button></div>'+case_body(True)+'</dialog>'+diagram_dialog()
    return body

def page(title,body,embedded=False):
    style='<style>'+(DIST/'assets/styles.css').read_text()+'</style>' if embedded else '<link rel="stylesheet" href="assets/styles.css">'
    script='<script>'+(DIST/'assets/site.js').read_text()+'</script>' if embedded else '<script src="assets/site.js" defer></script>'
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex,nofollow"><meta name="description" content="Dois engenheiros de dados conectando serviços em nuvem, documentos, automação corporativa e relatórios operacionais."><meta name="color-scheme" content="light"><title>{html.escape(title)}</title>{style}</head><body>{body}{script}</body></html>'''

(DIST/'index.html').write_text(page('Engenharia de Dados | Integrações em nuvem e automação operacional',homepage()))
(DIST/'case-study.html').write_text(page('Automação de documentos para compras | Engenharia de Dados',header()+'<main id="main"><div class="wrap"><a href="index.html#work" class="back-link">← Voltar ao projeto selecionado</a></div>'+case_body()+'</main>'+footer()+diagram_dialog()))
(ROOT/'portfolio-preview.html').write_text(page('Portfólio de engenharia de dados — prévia para revisão',homepage(True),True))
print('Página inicial, estudo de caso e prévia independente gerados.')
