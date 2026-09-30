async (page) => {
  page.setDefaultTimeout(7000);
  const result = {};
  await page.setViewportSize({width:1280,height:900});
  const layers = page.locator('#architektura');
  await layers.getByRole('tab', {name:/05 Governance/}).click();
  result.architecture = (await layers.innerText()).slice(-1200);
  const faq = page.getByRole('button', {name:/Ako dlho trvá audit/});
  await faq.click();
  result.faqExpanded = await faq.getAttribute('aria-expanded');
  const readiness = page.locator('#readiness');
  const sliders = readiness.locator('input[type="range"]');
  result.sliderCount = await sliders.count();
  result.readinessBefore = await readiness.innerText();
  if (result.sliderCount) {
    await sliders.first().focus();
    await page.keyboard.press('End');
  }
  result.readinessAfterKeyboard = await readiness.innerText();
  await readiness.getByRole('button', {name:'Resetovať hodnoty'}).click();
  result.readinessReset = await readiness.innerText();
  const demo = page.locator('#transformacia');
  await demo.getByRole('button', {name:'Zamietnuť', exact:true}).click();
  result.demoAfterReject = (await demo.innerText()).slice(0,2300);
  await demo.getByRole('button', {name:'Spustiť ukážku znova'}).click();
  await page.locator('a[href="#audit"]').filter({hasText:'Dohodnúť vstupný audit'}).first().click();
  result.auditNavigation = {hash: await page.evaluate(()=>location.hash),heading: await page.locator('#audit h2').innerText()};
  await page.locator('#audit').scrollIntoViewIfNeeded();
  await page.screenshot({path:'.playwright-mcp/aios-desktop-form.png',scale:'css'});
  result.formValidityWithoutSubmission = await page.locator('form').evaluate(f=>({valid:f.checkValidity(),required:[...f.elements].filter(e=>e.required).map(e=>({name:e.name,valid:e.validity.valid,message:e.validationMessage}))}));
  await page.setViewportSize({width:375,height:812});
  await page.evaluate(()=>scrollTo(0,0));
  await page.screenshot({path:'.playwright-mcp/aios-mobile-hero.png',scale:'css'});
  await page.getByRole('button',{name:'Otvoriť menu',exact:true}).click();
  result.menuExpanded = await page.locator('header button[aria-expanded]').first().getAttribute('aria-expanded');
  await page.screenshot({path:'.playwright-mcp/aios-mobile-menu.png',scale:'css'});
  result.mobileNav = await page.locator('header').innerText();
  await page.locator('a[href="#readiness"]:visible').first().click();
  result.mobileNavAfterClick = {hash:await page.evaluate(()=>location.hash),expanded:await page.locator('header button[aria-expanded]').first().getAttribute('aria-expanded')};
  await readiness.scrollIntoViewIfNeeded();
  await page.screenshot({path:'.playwright-mcp/aios-mobile-readiness.png',scale:'css'});
  await page.locator('#audit').scrollIntoViewIfNeeded();
  await page.screenshot({path:'.playwright-mcp/aios-mobile-form.png',scale:'css'});
  result.mobileFinalWidth = await page.evaluate(()=>({viewport:innerWidth,scrollWidth:document.documentElement.scrollWidth}));
  result.loadedImages = await page.evaluate(()=>[...document.images].map(e=>({alt:e.alt,src:e.currentSrc,width:e.naturalWidth,complete:e.complete})));
  return result;
}
