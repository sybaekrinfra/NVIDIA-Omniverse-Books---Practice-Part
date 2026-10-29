// Bundled @oai/artifact-tool을 사용합니다. tools나 패키지를 설치하지 않습니다.
import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {slides} from './content.mjs';

const HERE=path.dirname(fileURLToPath(import.meta.url));
const build=process.env.CBNU_DECK_BUILD;
if(!build || !process.env.ARTIFACT_TOOL_PATH) throw new Error('CBNU_DECK_BUILD, ARTIFACT_TOOL_PATH를 지정하세요.');
const {Presentation,PresentationFile}=await import(pathToFileURL(process.env.ARTIFACT_TOOL_PATH).href);
const {applyPresentationChartFont}=await import(pathToFileURL(path.join(process.env.PRESENTATION_SKILL_DIR,'container_tools/artifact_tool_utils.mjs')).href);
const font='Malgun Gothic';
const ink='#202322',muted='#58615C',green='#25634B';
const p=Presentation.create({slideSize:{width:1600,height:900}});
const manifest=JSON.parse(await fs.readFile(path.join(HERE,'assets/manifest.json'),'utf8'));
const parts=JSON.parse(await fs.readFile(path.join(HERE,'parts.json'),'utf8'));
await fs.mkdir(path.join(build,'previews'),{recursive:true});

function textbox(s,text,x,y,w,h,size=32,opts={}) {
  const box=s.shapes.add({geometry:'textbox',name:opts.name||text.slice(0,30),
    position:{left:x,top:y,width:w,height:h},fill:'none',line:{fill:'none',width:0}});
  box.text=text;
  box.text.style={fontSize:size,typeface:font,color:opts.color||ink,bold:opts.bold||false,
    insets:0,autoFit:'none',wrap:'square',verticalAlignment:'top',...opts.style};
  return box;
}
function normalHeader(s,item,index){
  const part=parts.find(x=>x.id===item.part);
  const label=part?`${item.part.replace('D1P','DAY 1   PART ').replace('D2P','DAY 2   PART ')}     ${part.title}`:item.part;
  textbox(s,label,88,44,1400,36,20,{color:green});
  textbox(s,item.title,88,100,1424,92,52,{bold:true,name:'Title'});
  textbox(s,`${String(index+1).padStart(2,'0')}   /   CBNU Omniverse Workshop`,88,848,1424,28,17,{color:muted});
}
function drawTable(s,item){
 const rows=item.rows,n=rows.length,c=rows[0].length;
 const metrics=Array.from({length:c},(_,j)=>Math.min(44,Math.max(13,...rows.map(r=>[...r[j]].reduce((a,x)=>a+(x.charCodeAt(0)>255?1.7:1),0)))));
 const total=metrics.reduce((a,b)=>a+b,0);
 const widths=metrics.map(x=>1424*x/total);
 const height=Math.min(535,n*90);
 const t=s.tables.add({rows:n,columns:c,left:88,top:230,width:1424,height,columnWidths:widths,values:rows});
 t.borders.assign({fill:'#CFD5D1',width:1,style:'solid'});
 t.cells.block({row:0,column:0,rowCount:n,columnCount:c}).assign({
   textStyle:{typeface:font,fontSize:28,color:ink},margins:{top:15,bottom:12,left:18,right:18},anchor:'center'});
 for(let i=0;i<n;i++)for(let j=0;j<c;j++){
   const cell=t.getCell(i,j);
   cell.fill=i===0?'#E8EEE9':'#FFFFFF';
   cell.text.style={typeface:font,fontSize:28,color:ink,bold:i===0};
 }
 if(item.foot)textbox(s,item.foot,88,794,1424,42,22,{color:muted});
}
const tableOwners=[],chartOwners=[];
for(let i=0;i<slides.length;i++){
 const d=slides[i],s=p.slides.add();s.background.fill='#FFFFFF';
 let note=d.notes||'';
 const part=parts.find(x=>x.id===d.part);
 if(part)note+=`\n\n실습 연결: ${part.path}/EXPANDED_LAB.md\n시간: 기본 실습 ${part.base}분 + 선택 확장 ${part.extra}분.\n진단 질문: ${part.question}\n예상 답: ${part.answer}`;
 note+='\n\n자료: 사용자 제공 수정 Agenda, 기존 교재 및 본 저장소. 상세 출처는 docs/SOURCES.md.';
 if(d.type==='cover'){
   textbox(s,d.subtitle,100,104,1390,60,34,{color:green});
   textbox(s,'Omniverse\n실습 워크숍',100,245,1390,230,86,{bold:true,name:'Title'});
   textbox(s,d.lines.join('\n'),105,562,1320,180,34);
   textbox(s,'DAY 1 + DAY 2    /    CAD · OpenUSD · Python',105,805,1390,40,22,{color:muted});
 }else if(d.type==='section'){
   textbox(s,d.part,100,105,1300,55,30,{color:green});
   textbox(s,d.title,100,270,1390,180,72,{bold:true,name:'Title'});
   textbox(s,d.lines.join('\n'),105,555,1360,200,34);
 }else{
   normalHeader(s,d,i);
   if(d.type==='table'){drawTable(s,d);tableOwners.push(i+1);}
   if(d.type==='text')d.lines.forEach((line,j)=>{
     textbox(s,line[0],88,234+j*135,250,65,32,{bold:true,color:green});
     textbox(s,line[1],380,234+j*135,1110,105,32);
   });
   if(d.type==='code'){
     const lines=d.code.split('\n').length;
     const h=Math.max(180,lines*50);
     const bx=textbox(s,d.code,108,240,1380,h,30,{style:{typeface:'Consolas'},name:'Code'});
     d.lines.forEach((line,j)=>textbox(s,line,108,260+h+j*65,1380,55,30));
   }
   if(d.type==='exercise'){
     textbox(s,d.file,88,218,1424,64,25,{color:green});
     d.steps.forEach((step,j)=>{
       textbox(s,String(j+1).padStart(2,'0'),88,330+j*105,80,58,36,{color:green,bold:true});
       textbox(s,step,205,330+j*105,1300,88,32);
     });
   }
   if(d.type==='image'){
     const a=manifest[d.image];if(!a)throw new Error('image missing '+d.image);
     const blob=await fs.readFile(path.join(HERE,'assets',a.file));
     const portrait=a.height>a.width;
     const frame=portrait?{left:88,top:225,width:640,height:555}:{left:88,top:225,width:940,height:520};
     s.images.add({blob:blob.buffer.slice(blob.byteOffset,blob.byteOffset+blob.byteLength),contentType:'image/png',
       position:frame,fit:'contain',alt:`기존 교육 교재 화면: ${d.title}`});
     const x=portrait?835:1090,w=portrait?660:420;
     d.lines.forEach((line,j)=>textbox(s,line,x,245+j*125,w,112,30));
     textbox(s,'기존 교재 화면 예시. 앱 버전에 따라 메뉴와 배치가 다를 수 있습니다.',88,795,1410,35,19,{color:muted});
     note+=`\n\n화면 출처: ${a.source}, 슬라이드 ${a.slide}. 원본 이미지 추출, 합성 UI 아님.`;
   }
   if(d.type==='chart'){
     const chart=s.charts.add('line',{position:{left:88,top:220,width:1424,height:550},
       title:'온도 (°C)',titlePlacement:'aboveChart',
       categories:d.categories,series:d.series.map(x=>({name:x.name,values:x.values,line:{fill:x.color,width:3},fill:x.color})),
       hasLegend:true,legend:{position:'bottom',textStyle:{fontFamily:font,fontSize:22}},
       titleTextStyle:{fontFamily:font,fontSize:26},
       xAxis:{textStyle:{fontFamily:font,fontSize:22}},yAxis:{minimumScale:0,maximumScale:100,textStyle:{fontFamily:font,fontSize:22},majorGridlines:{fill:'#D4DAD6',width:1}},
       chartFill:'#FFFFFF',plotAreaFill:'#FFFFFF',lineOptions:{smooth:false}});
     applyPresentationChartFont(chart,{fontFamily:font});
     chartOwners.push(i+1);
     textbox(s,d.foot,88,795,1424,38,22,{color:muted});
   }
 }
 s.speakerNotes.text=note;
 const png=await p.export({slide:s,format:'png',scale:1});
 await fs.writeFile(path.join(build,'previews',`slide-${String(i+1).padStart(2,'0')}.png`),new Uint8Array(await png.arrayBuffer()));
 await fs.writeFile(path.join(build,'previews',`slide-${String(i+1).padStart(2,'0')}.layout.json`),await (await s.export({format:'layout'})).text());
 if((i+1)%10===0)console.log('Rendered',i+1,'/',slides.length);
}
await (await PresentationFile.exportPptx(p)).save(path.join(build,'candidate.pptx'));
await fs.writeFile(path.join(build,'requirements.json'),JSON.stringify({count:slides.length,tableOwners,chartOwners},null,2));
await fs.writeFile(path.join(HERE,'slide_index.json'),JSON.stringify(slides.map((s,i)=>({slide:i+1,part:s.part,title:s.title})),null,2));
const manuscript=slides.map((s,i)=>`## ${i+1}. ${s.title}\n\n${s.part}\n\n${s.notes}`).join('\n\n');
await fs.writeFile(path.join(HERE,'../LECTURE_NOTES.md'),'# 통합 강의 발표자 원고\n\n'+manuscript+'\n');
console.log('Draft complete',slides.length,path.join(build,'candidate.pptx'));
