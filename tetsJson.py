import asyncio

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright


async def load_storage_state(playwright):
    # 启动一个浏览器实例
    browser = await playwright.chromium.launch(headless=False)

    # 创建一个新的浏览器上下文，并使用 'state.json' 文件加载存储状态
    context = await browser.new_context(storage_state='state.json')

    # 打开一个新的页面并导航到目标网站
    page = await context.new_page()
    await page.goto("https://medium.com")

    # 可选：截图以验证状态
    # await page.screenshot(path='screenshot.png')

    # 等待一段时间
    # await page.wait_for_timeout(20000)



    # 获取页面的 HTML 内容
    html_content = await page.content()

    # 使用 BeautifulSoup 提取文本
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text(separator='\n', strip=True)
    print(text)
    await page.wait_for_timeout(2000)

    # 关闭浏览器
    await browser.close()
async def main():
    async with async_playwright() as playwright:
        await load_storage_state(playwright)


if __name__ == "__main__":
    asyncio.run(main())
