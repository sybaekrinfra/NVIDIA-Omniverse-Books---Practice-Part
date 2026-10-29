import fs from 'node:fs/promises';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const skill=process.env.PRESENTATION_SKILL_DIR;
const build=process.env.CBNU_DECK_BUILD;
const python=process.env.ARTIFACT_PYTHON;
if(!skill||!build||!python)throw new Error('PRESENTATION_SKILL_DIR, CBNU_DECK_BUILD, ARTIFACT_PYTHON 필요');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const r=JSON.parse(await fs.readFile(path.join(build,'requirements.json'),'utf8'));
await fs.mkdir(path.join(build,'final'),{recursive:true});
const result=await finalizePresentation({workspaceDir:build,candidatePath:path.join(build,'candidate.pptx'),
 finalPath:path.join(build,'final/CBNU_Omniverse_Workshop_Integrated.pptx'),
 explicitTotalSlideCount:r.count,pythonExecutable:python,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 layoutArgs:['--expected-slide-size-emu','15240000,8572500','--validate-bullet-geometry','--validate-heading-fit',...r.tableOwners.flatMap(n=>['--require-native-table-slide',String(n)])],
 requiredNativeTableOwnerSlides:r.tableOwners,requiredNativeChartOwnerSlides:r.chartOwners,
 fontPolicy:{basis:'design',families:['Malgun Gothic','Consolas']},verifyArtifactToolImport:true,
 materializeLiteralChartWorkbooks:true,
 receiptPath:path.join(build,'validation.json')});
console.log(JSON.stringify(result));
