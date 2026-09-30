async (page) => {
  await page.setViewportSize({width:1280,height:900});
  await page.evaluate(() => document.fonts.ready);
  const content = await page.evaluate(() => ({
    url: location.href,
    title: document.title,
    lang: document.documentElement.lang,
    meta: [...document.querySelectorAll('meta[name],meta[property],link[rel="canonical"]')].map(e => ({name:e.name||e.getAttribute('property')||e.rel,content:e.content||e.href})),
    headings: [...document.querySelectorAll('h1,h2,h3')].map(e=>({tag:e.tagName,text:e.textContent.trim()})),
    sections: [...document.querySelectorAll('section[id]')].map(e=>({id:e.id,title:e.querySelector('h1,h2,h3')?.textContent.trim()})),
    links:[...document.querySelectorAll('a')].map(e=>({text:e.textContent.trim(),href:e.getAttribute('href'),label:e.getAttribute('aria-label')})),
    buttons:[...document.querySelectorAll('button')].map(e=>({text:e.textContent.trim(),label:e.getAttribute('aria-label'),type:e.type,expanded:e.getAttribute('aria-expanded')})),
    forms:[...document.querySelectorAll('form')].map(e=>({action:e.getAttribute('action'),method:e.method,fields:[...e.querySelectorAll('input,textarea,select')].map(x=>({tag:x.tagName,name:x.name,id:x.id,type:x.type,required:x.required,labels:[...x.labels||[]].map(z=>z.textContent.trim())}))})),
    images:[...document.images].map(e=>({src:e.currentSrc,alt:e.getAttribute('alt'),width:e.naturalWidth,height:e.naturalHeight,loading:e.loading})),
    structuredData:[...document.querySelectorAll('script[type="application/ld+json"]')].map(e=>e.textContent),
    text:document.body.innerText
  }));
  const viewportChecks=[];
  for (const width of [375,768,1280,1920]) {
    await page.setViewportSize({width,height:900});
    const data=await page.evaluate(()=>({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyWidth:document.body.scrollWidth,overflow:[...document.querySelectorAll('main *,header *,section *')].filter(e=>{const r=e.getBoundingClientRect();const s=getComputedStyle(e);return r.width>0&&s.visibility!=='hidden'&&s.display!=='none'&&(r.right>innerWidth+2||r.left< -2)}).slice(0,15).map(e=>({tag:e.tagName,class:e.className,text:e.textContent.trim().slice(0,90)}))}));
    viewportChecks.push(data);
  }
  await page.setViewportSize({width:1280,height:900});
  await page.evaluate(()=>scrollTo(0,0));
  const fs = require('fs');
  fs.writeFileSync('/home/ubuntu/aios-site-audit/evidence/inspection.json', JSON.stringify({content,viewportChecks},null,2));
  return {content,viewportChecks};
}
