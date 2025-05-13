import puppeteer from 'puppeteer';

(async () => {
  console.log('==== Puppeteer测试开始 ====');
  let browser;
  
  try {
    console.log('正在启动浏览器...');
    browser = await puppeteer.launch({
      headless: false,
      defaultViewport: null,
      args: ['--no-sandbox', '--disable-setuid-sandbox']
    });
    console.log('浏览器已启动');
    
    const page = await browser.newPage();
    console.log('正在打开新页面...');
    
    console.log('导航到Google...');
    await page.goto('https://www.google.com', {
      waitUntil: 'domcontentloaded',
      timeout: 30000
    });
    
    console.log('页面已加载，正在获取标题...');
    const title = await page.title();
    console.log(`页面标题: ${title}`);
    
    console.log('正在截取屏幕截图...');
    await page.screenshot({ path: 'google_homepage.png' });
    console.log('截图已保存为google_homepage.png');
    
    // 等待5秒
    console.log('等待5秒...');
    await new Promise(r => setTimeout(r, 5000));
    
    console.log('测试完成，正在关闭浏览器...');
  } catch (error) {
    console.error('发生错误:', error);
  } finally {
    if (browser) {
      await browser.close();
      console.log('浏览器已关闭');
    }
    console.log('==== Puppeteer测试结束 ====');
  }
})(); 