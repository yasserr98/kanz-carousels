"""Export local carousel HTML files to numbered PNGs in the requested order."""
import argparse
from pathlib import Path
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', nargs='+', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    paths = [p.resolve(strict=True) for p in args.html]
    args.output.mkdir(parents=True, exist_ok=True)
    number = 0
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={'width': 1080, 'height': 1350}, device_scale_factor=1)
        for path in paths:
            errors = []
            def failed(request):
                errors.append(request.url)
            page.on('requestfailed', failed)
            page.goto(path.as_uri(), wait_until='networkidle')
            page.evaluate('document.fonts.ready')
            broken = page.locator('img').evaluate_all('(imgs) => imgs.filter(i => !i.complete || !i.naturalWidth).map(i => i.getAttribute("src"))')
            if errors or broken:
                raise RuntimeError(f'Missing assets in {path.name}: {errors + broken}')
            slides = page.locator('.slide, .poster')
            if not slides.count():
                raise RuntimeError(f'No .slide or .poster element in {path}')
            for slide in slides.all():
                number += 1
                output = args.output / f'{number:02}.png'
                if output.exists():
                    raise FileExistsError(f'Refusing to replace {output}; choose a new output directory')
                slide.screenshot(path=str(output), animations='disabled')
            page.remove_listener('requestfailed', failed)
        browser.close()
    print(f'Exported {number} slides to {args.output}')


if __name__ == '__main__':
    main()
