import fs from 'node:fs';
import { instance } from '@viz-js/viz';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const graphs=JSON.parse(fs.readFileSync(`${root}/content/architecture.json`,'utf8'));
const viz=await instance();
const palette={function:'#E7EFFF',compute:'#DAE6FF',queue:'#D5F0FA',storage:'#EDF2F8',control:'#EEF1FC',external:'#FFFFFF',ai:'#D8F4EA',documented:'#F1F2F6',inferred:'#F1F2F6'};
const q=x=>JSON.stringify(x);
for(const g of graphs){
  const mermaid=['flowchart TD'];
  for(const [id,label] of g.nodes) mermaid.push(`    ${id}[${JSON.stringify(label)}]`);
  for(const [a,b,label,kind] of g.edges) mermaid.push(kind==='data' ? `    ${a} -->|${JSON.stringify(label)}| ${b}` : `    ${a} -. ${JSON.stringify(label)} .-> ${b}`);
  fs.writeFileSync(`${root}/diagrams/${g.id}.mmd`,mermaid.join('\n')+'\n');
  const nodeIds=new Set(g.nodes.map(n=>n[0]));
  for(const edge of g.edges) if(!nodeIds.has(edge[0])||!nodeIds.has(edge[1])) throw new Error('Nó desconhecido no diagrama');
  const lines=['digraph G {','graph [rankdir=TB, bgcolor="transparent", pad="0.4", nodesep="0.45", ranksep="0.7", splines=polyline, fontname="Arial", outputorder=edgesfirst];','node [shape=box, style="rounded,filled", fontname="Arial", fontsize=15, fontcolor="#102B44", color="#BFCFE1", penwidth=1.2, margin="0.24,0.17"];','edge [fontname="Arial", fontsize=12, fontcolor="#34516D", color="#496C95", arrowsize=0.7, penwidth=1.2];'];
  for(const [id,label,kind] of g.nodes){
    const wrapped=label.replace(': ',':\n');
    lines.push(`${id} [label=${q(wrapped)}, fillcolor=${q(palette[kind])}${['inferred','documented'].includes(kind)?', style="rounded,dashed,filled"':''}];`);
  }
  for(const [a,b,label,kind] of g.edges) lines.push(`${a} -> ${b} [label=${q(label)}, style=${kind==='data'?'solid':'dashed'}${kind==='contract'?', color="#788795", fontcolor="#526477"':''}];`);
  lines.push('}');
  let svg=viz.renderString(lines.join('\n'),{format:'svg',engine:'dot'});
  svg=svg.replace(/<\?xml[^>]*\?>\s*/,'').replace(/<!DOCTYPE[\s\S]*?>\s*/,'');
  svg=svg.replace('<svg ',`<svg role="img" aria-labelledby="title-${g.id} desc-${g.id}" `);
  svg=svg.replace(/(<svg[^>]*>)/,`$1\n<title id="title-${g.id}">${g.title}</title>\n<desc id="desc-${g.id}">${g.summary.replace(/&/g,'&amp;')}</desc>`);
  fs.writeFileSync(`${root}/dist/assets/diagrams/${g.id}.svg`,svg);
  fs.writeFileSync(`${root}/diagrams/${g.id}.dot`,lines.join('\n'));
}
console.log(`${graphs.length} diagramas renderizados a partir do modelo compartilhado de arquitetura.`);
