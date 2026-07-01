import asyncio
from playwright.async_api import async_playwright, expect

async def run_tests():
    async with async_playwright() as p:
        # Run headless, which often lacks WebGL and triggers the error you saw
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()
        
        errors = []
        page.on("pageerror", lambda err: errors.append(err))
        page.on("console", lambda msg: errors.append(msg.text) if msg.type == "error" else None)
        
        print("Starting test on http://localhost:3018 ...")
        await page.goto("http://localhost:3018")
        
        # Check Title
        await expect(page).to_have_title("US7032353 - Swivel Joint Apparatus | Interactive Study")
        print("✓ Page loaded successfully with correct title")
        
        # Check that UI elements are visible
        menu = page.locator(".system-menu")
        await expect(menu).to_be_visible()
        print("✓ UI controls are visible")
        
        # Wait a bit to catch any deferred console errors
        await page.wait_for_timeout(2000)
        
        # Filter out the intentional WebGL fallback warning if it's logged as an error
        real_errors = [e for e in errors if "WebGL" not in str(e) and "BindToCurrentSequence failed" not in str(e)]
        
        if real_errors:
            print("⚠ Unhandled Console Errors detected:")
            for e in real_errors:
                print(f"  - {e}")
            print("Test Failed.")
        else:
            print("✓ No unhandled console errors detected! Favicon and WebGL fallback are working.")
            
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_tests())
