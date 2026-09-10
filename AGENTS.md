<!-- bmad:context -->
<!-- Verified 2026-09-10. Managed by bmad-project-context; edits inside this block are replaced on refresh. Keep anything you want preserved outside the markers. -->

## bsahane

Portfolio and technical showcase for Bhushan Sahane — AI Infrastructure Engineer at Red Hat. Single-page native web stack (HTML5/CSS3/Vanilla JS) with optional Python Anthropic proxy.

## Policy

- Zero runtime build steps: keep `index.html` directly servable by any static web server or browser.
- Never commit active raw API keys in `proxy.py` or `index.html`; use environment variable `BROCODE_KEY` or runtime injection.
- Monospace-first dark cyberpunk/terminal aesthetic (`JetBrains Mono`, `Fira Code`, OLED dark palette) must be preserved across all visual updates.
- Maintain WCAG 2.1 AA accessibility (4.5:1 text contrast, full keyboard accessibility, visible focus rings, ARIA live regions).

## Where things are

- Main Web Application: `index.html` (CSS tokens in `<style>`, semantic markup in `<body>`, data & handlers in `<script>`)
- AI Proxy Server: `proxy.py` (optional local bridge for interactive terminal chat)
- Design Specifications: `DESIGN.md` (visual identity tokens) and `EXPERIENCE.md` (interaction & behavioral architecture)
- BMAD Workflows & Customizations: `_bmad/` and `.agent/`

## Running and verifying

- Serve locally: `python3 -m http.server 8000` and open `http://localhost:8000`
- Run interactive AI terminal proxy: `python3 proxy.py` (listens on `http://127.0.0.1:8787`)
- Validate HTML/CSS: test with reduced motion (`prefers-reduced-motion: reduce`) and responsive viewport widths (375px, 768px, 1280px).

## Conventions that differ from defaults

- All icons are inline SVGs (no emoji icons as controls or system icons per ui-ux-pro-max guidelines).
- 1-click clipboard actions (for `git clone`, emails, and links) must trigger immediate visual feedback on the button plus a toast alert.
- Dual-engine terminal must always fall back gracefully to local CLI commands and built-in knowledge engine when `proxy.py` is offline.

## Known pitfalls

- Terminal fetch to `127.0.0.1:8787` will abort after timeout; never display raw networking errors to the user, always delegate to `getLocalKnowledgeAnswer()`.
- Mobile drawer requires scroll lock on `body` (`overflow: hidden`) and clean ESC key listeners to prevent background scrolling.

<!-- /bmad:context -->
