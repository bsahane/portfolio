---
name: Bhushan Sahane Portfolio Design System
description: Tactical cybernetic monospace design system for AI infrastructure & protocol engineering showcase.
colors:
  bg-base: '#0a0e14'
  bg-raised: '#0f141b'
  bg-overlay: '#141a23'
  bg-elevated: '#1a212c'
  bg-hover: '#232b37'
  border-subtle: '#21262d'
  border-default: '#30363d'
  border-strong: '#484f58'
  border-hover: '#586069'
  text-primary: '#e6edf3'
  text-secondary: '#b1bac4'
  text-tertiary: '#a1abb7'
  text-muted: '#94a3b8'
  accent-green: '#39d353'
  accent-cyan: '#39c5cf'
  accent-blue: '#58a6ff'
  accent-purple: '#bc8cff'
  accent-yellow: '#d29922'
  accent-orange: '#f0883e'
  accent-pink: '#ff7b72'
  accent-mint: '#7ee787'
  accent-red: '#f85149'
themes:
  cyberpunk:
    name: 'Cyberpunk OLED (Default)'
    bg: '#0a0e14'
    bg-raised: '#0f141b'
    fg: '#e6edf3'
    green: '#39d353'
    cyan: '#39c5cf'
    yellow: '#d29922'
    orange: '#f0883e'
  gruvbox:
    name: 'Gruvbox Retro Groove (morhetz/gruvbox)'
    bg: '#1d2021'
    bg-raised: '#282828'
    bg-overlay: '#32302f'
    bg-elevated: '#3c3836'
    border: '#504945'
    fg: '#ebdbb2'
    fg-secondary: '#d5c4a1'
    fg-muted: '#a89984'
    green: '#b8bb26'
    cyan: '#8ec07c'
    blue: '#83a598'
    purple: '#d3869b'
    yellow: '#fabd2f'
    orange: '#fe8019'
    red: '#fb4934'
typography:
  fontFamily: "'JetBrains Mono', 'Fira Code', ui-monospace, 'SF Mono', Consolas, monospace"
  codeFamily: "'JetBrains Mono', 'Fira Code', monospace"
  display:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '44px'
    fontWeight: '700'
    lineHeight: '1.15'
    letterSpacing: '-1px'
  headline:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '32px'
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: '-0.5px'
  title:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '19px'
    fontWeight: '600'
    lineHeight: '1.3'
  body:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '14px'
    fontWeight: '400'
    lineHeight: '1.6'
  caption:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '13px'
    fontWeight: '400'
    lineHeight: '1.5'
  eyebrow:
    fontFamily: "'JetBrains Mono', monospace"
    fontSize: '11px'
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '2.5px'
rounded:
  sm: '4px'
  md: '6px'
  lg: '10px'
  xl: '16px'
  full: '9999px'
spacing:
  '1': '4px'
  '2': '8px'
  '3': '12px'
  '4': '16px'
  '6': '24px'
  '8': '32px'
  '12': '48px'
  '16': '64px'
  '24': '96px'
  container-max: '1280px'
  gutter-desktop: '24px'
  gutter-mobile: '18px'
motion:
  easing-spring: 'cubic-bezier(0.16, 1, 0.3, 1)'
  easing-smooth: 'cubic-bezier(0.4, 0, 0.2, 1)'
  duration-instant: '80ms'
  duration-fast: '160ms'
  duration-standard: '260ms'
  duration-flow: '600ms'
components:
  terminal-card:
    background: '{colors.bg-raised}'
    border: '1px solid {colors.border-default}'
    radius: '{rounded.lg}'
    shadow: '0 8px 32px rgba(0,0,0,0.6)'
  project-card:
    background: '{colors.bg-raised}'
    border: '1px solid {colors.border-subtle}'
    radius: '{rounded.md}'
    hover-border: '{colors.accent-green}'
    hover-shadow: '0 8px 28px rgba(0,0,0,0.5), 0 0 20px rgba(57, 211, 83, 0.12)'
    spotlight: 'radial-gradient(circle 280px at var(--mouse-x) var(--mouse-y), rgba(57, 211, 83, 0.12), transparent 70%)'
  skill-card:
    background: '{colors.bg-raised}'
    border: '1px solid {colors.border-subtle}'
    radius: '{rounded.md}'
    hover-border: '{colors.accent-cyan}'
    spotlight: 'radial-gradient(circle 280px at var(--mouse-x) var(--mouse-y), rgba(57, 197, 207, 0.10), transparent 70%)'
  badge:
    radius: '{rounded.sm}'
    padding: '2px 8px'
    fontSize: '{typography.caption.fontSize}'
  button-primary:
    background: '{colors.accent-green}'
    color: '{colors.bg-base}'
    radius: '{rounded.md}'
    fontWeight: '600'
    glow: '0 0 20px rgba(57, 211, 83, 0.25)'
---

# Brand & Style

Tactical Cybernetic Monospace. Designed to feel like a high-uptime production control console rather than an interchangeable corporate portfolio. It speaks directly to staff engineers, infrastructure architects, and AI researchers who respect raw performance, verifiable telemetry, and deep protocol fluency.

Every layout element carries semantic terminal discipline:
- Leading prompts (`$`, `//`, `~/`, `● LIVE`) anchor visual hierarchy.
- Dark ambient radial glows evoke CRT phosphors and modern OLED hardware monitors.
- High micro-interaction responsiveness conveys low latency and instant feedback.

# Colors

- **`{colors.bg-base}` (`#0a0e14`)**: Deep OLED pitch-black foundation. Keeps energy emission low, eliminates distraction, and provides maximum contrast for phosphors.
- **`{colors.accent-green}` (`#39d353`)**: Primary operational accent. Denotes active systems, command prompts, success states, and primary CTAs.
- **`{colors.accent-cyan}` (`#39c5cf`)**: Protocol and networking accent. Symbolizes Model Context Protocol (MCP), mesh proxies, and telemetry streams.
- **`{colors.accent-blue}` (`#58a6ff`)**: DevOps & orchestration accent. Represents Ansible, Kubernetes, Linux, and repository structures.
- **`{colors.accent-purple}` (`#bc8cff`)**: Agent-to-Agent (A2A) and multi-agent coordination.
- **`{colors.accent-yellow}` (`#d29922`)**: Star counts, telemetry metrics, and alert highlights.
- **`{colors.text-primary}` (`#e6edf3`)** & **`{colors.text-muted}` (`#94a3b8`)**: Strictly calibrated to guarantee >= 4.5:1 contrast against dark background surfaces (WCAG AA).

# Typography

Strict monospace hierarchy built upon **JetBrains Mono** and **Fira Code**:
- **Display & Section Titles**: Bold monospace with leading bash command symbols (`$ ls -la ~/toolbox`, `$ tree -L 2 ~/repos`).
- **Body Text**: 14px on 1.6 line height for effortless readability of dense engineering specifications.
- **Eyebrows**: Uppercase 11px with 2.5px tracking formatted as Unix file comments (`// ~ ./contact.env`).

# Layout & Spacing

An 8dp structural rhythm ensures consistent vertical cadence:
- Section padding: 100px desktop, 80px mobile.
- Grids: Responsive CSS Grid with 1fr columns on mobile expanding to 2 and 4 columns on wide displays.
- Container: Capped at 1280px with fluid gutter insets (24px desktop, 18px mobile).

# Elevation & Depth

- Ambient backdrop: Multi-origin radial gradients (`rgba(57, 211, 83, 0.06)`, `rgba(88, 166, 255, 0.05)`, `rgba(188, 140, 255, 0.04)`).
- Elevation 1 (Cards): Dark surface `#0f141b` with subtle 1px border `#21262d`.
- Elevation 2 (Interactive Elements & Drawers): Elevated `#1a212c` with drop shadows `0 8px 32px rgba(0,0,0,0.6)`.
- Glow effects: Soft Gaussian phosphor bloom (`0 0 24px rgba(57, 211, 83, 0.18)`).
- Cursor Spotlight: Dynamic radial gradient overlay (`{components.project-card.spotlight}`) driven by `--mouse-x` and `--mouse-y` for tactile depth without DOM overhead.

# Shapes

- Controls and tags use crisp, deliberate radii (`4px` to `6px`) reflecting industrial terminal hardware.
- Status dots and pill tags use `9999px` (full round) to contrast sharply against rectangular terminal boxes.

# Components & Motion

- **Terminal Console**:
  - macOS traffic lights (Red = Clear, Yellow = CRT toggle, Green = Maximize).
  - Ghost autocomplete overlay offering inline tab-completion for shell commands.
  - Optional synthesized mechanical click feedback via Web Audio API.
- **Repository Cards**:
  - Spotlight cursor illumination tracking pointer movements.
  - Cross-filter accent highlight pulse (`cardHighlightPulse`) on skill selection.
  - 1-click clone button with instant inline feedback and toast alert.
- **Interactive MCP Topology**:
  - Traveling packet flow pulses on connectors illustrating live protocol traffic.
  - Interactive node selection with real-time specification rendering.
- **Scroll Progress**:
  - Ultra-thin 2px green-to-cyan gradient progress bar anchored at viewport top.

# Do's and Don'ts

### Do
- Keep motion subtle: card elevation transforms must remain between 2px and 4px to read as tactile feedback, not jarring movement.
- Animate only `transform` and `opacity` properties to guarantee 60fps/120fps hardware acceleration on the GPU compositor thread.
- Always provide `prefers-reduced-motion: reduce` overrides that collapse all animation durations to 0ms and preserve readable final states immediately.
- Use vector SVG icons with consistent 2px stroke or solid silhouette; never emojis for navigation or controls.

### Don't
- Never animate layout-affecting properties (`width`, `height`, `margin`, `padding`) on hover or scroll.
- Never use infinite looping bounce or spin animations on decorative elements; reserve pulsing loops exclusively for operational status dots.
- Never let dark mode muted text drop below 4.5:1 contrast against adjacent background surfaces.
