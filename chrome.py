from pathlib import Path

from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
import asyncio


async def run(playwright):
    # 使用相对路径获取用户数据目录
    # 假设 user_data_dir 文件夹与代码在同一路径下
    base_dir = Path(__file__).parent  # 获取当前脚本所在目录
    user_data_dir = base_dir / 'User Data'  # 构建用户数据目录路径\

    print(user_data_dir)
    # 启动浏览器
    browser = await playwright.chromium.launch_persistent_context(
        user_data_dir=user_data_dir,
        headless=False  # 设置为 False 以查看浏览器界面
    )

    # 创建一个新的页面
    page = await browser.new_page()

    # 访问 Medium 网站
    await page.goto("https://medium.com")

    # 进行其他操作，例如截图
    # await page.screenshot(path="medium_screenshot.png")
    # 获取页面的 HTML 内容
    html_content = await page.content()

    # 使用 BeautifulSoup 提取文本
    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.get_text(separator='\n', strip=True)
    print(text)
    await page.wait_for_timeout(2000)
    # await page.pause()


    # 关闭浏览器
    await browser.close()


# 主函数
async def main():
    async with async_playwright() as playwright:
        await run(playwright)


# 运行主函数
if __name__ == "__main__":
    asyncio.run(main())
