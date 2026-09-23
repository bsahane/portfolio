---
status: final
updated: 2026-09-22
system: Tactical Monospace Native Web
design_tokens: DESIGN.md
---

# EXPERIENCE.md — Interaction & Behavioral Architecture

## Foundation

- **Platform & Form-Factor**: Responsive native web application optimized for desktop workstations, laptops, tablets, and modern mobile devices (375px+).
- **Architecture**: Single-page application, zero JavaScript build framework dependencies (Vanilla ES6, CSS Custom Properties, Semantic HTML5).
- **Design Reference**: Visual identity tokens, colors, typography, and motion specifications inherit from `{DESIGN.md}`.
- **Offline & Fallback First**: The web application must function completely offline or under strict network firewalls. Terminal commands, interactive searches, and contact actions remain fully operational without external server round-trips.

---

## Information Architecture

```
[Sticky Nav Header]
  ├─ Top Scroll Progress Indicator (2px gradient bar tracking viewport position)
  ├─ Brand Identity (`bsahane@portfolio:~$ whoami`)
  ├─ Navigation Links (`projects`, `about`, `stack`, `certs`, `experience`, `journey`, `contact`)
  ├─ Theme Picker (`themeToggleBtn`: native buttons in a palette listbox)
  ├─ Action CTA (`get-in-touch`)
  └─ Mobile Hamburger Drawer (Viewport < 768px, includes drawer theme palette switcher)

[Hero Section]
  ├─ Identity Pill (`AI infrastructure · open-source work`)
  ├─ Headline (`$ hello, I'm Bhushan Sahane`)
  ├─ Subtitle & Specialty Focus (Red Hat, Agentic AI, MCP, RAG, A2A)
  ├─ Primary CTAs (`./init projects`, `github`, `linkedin`)
  ├─ Local Index Stats Grid (Curated repos, stars explicitly labeled as a snapshot, focus, shipping status)
  └─ Interactive Dual-Engine Terminal
       ├─ macOS Traffic Control Dots (Clear / CRT / Maximize) + Sound FX Toggle
       ├─ Typewriter Shell Loop
       ├─ Live Command/Prompt Chat Stream
       ├─ Quick-Prompt Chip Buttons
       └─ Terminal Shell Input with Real-Time Ghost Autocomplete (`Tab` to complete)

[Selected Work (`#projects`, immediately after hero)]
  ├─ Wide MCP Mesh Overview, Source Link, and decocms/studio Fork Attribution
  ├─ mcp-ansible & mcp-proxmox Studies with Illustrative Infrastructure Diagrams
  ├─ Project Actions that Select a Request Example and Focus its Run Button
  ├─ Browser-Only Request Lab (`#request-lab`)
  │    ├─ Native Scenario Selector and Run / Pause / Resume / Replay Button
  │    ├─ Client → Mesh Policy Gateway → Tool Server Topology
  │    ├─ Text Status, Ordered Request Trace, and Sample Result
  │    └─ Expandable JSON-RPC Request Payload and Repository Reference
  └─ Collapsed Repository Index (`#repo-index`, native details/summary)
       ├─ Category Filter Tabs with dynamic count badges (`all`, `featured`, `mcp`, `ai`, `devops`, `tool`)
       ├─ Instant In-Memory Search Bar (`grep ./repos/`) with clear action
       ├─ Filter Status Summary and Local Snapshot Notice
       └─ Project Grid with Star Counts, Repository Links, and 1-Click `git clone`

[About & Protocol Overview]
  ├─ Bio & Architectural Philosophy
  ├─ Core Competencies and Current Browser Tab Session Counter
  └─ Collapsed Full Architecture Reference (Interactive MCP Topology)

[Toolbox & Stack Matrix]
  ├─ Categorized Skill Cards with Cursor Spotlight Lighting
  └─ Interactive Protocol Tags (Open repository index, filter it, scroll to it, and pulse matches)

[Certifications & Verification Portal (`#certs`)]
  ├─ Official Verification Banner (`Primary Red Hat Certificate ID: 170-063-119`)
  ├─ 5 Verified Interactive Credential Cards with Cursor Spotlight
       ├─ Red Hat Certified Engineer (RHCE, Active until Jul 2027)
       ├─ Red Hat Certified System Administrator (RHCSA, Active until Jun 2027)
       ├─ Managing Enterprise Automation with Red Hat AAP (DO467 Specialist)
       ├─ RHCSA Rapid Track (RH199 Advanced Course)
       └─ Red Hat System Administration I (RH124 Credly Digital Badge)
  ├─ 1-Click Credential ID Clipboard Copy with Visual Status & Toast
  └─ Direct Verification Deep-Links opening Red Hat Portal & Credly in new tabs

[Professional Experience (`#experience`)]
  └─ Career Summary and Employer/Role History

[Journey & Timeline]
  └─ Chronological Engineering Progression (RHCE/DO467 -> Legal MCP -> MCP Mesh -> Red Hat AI Infra)

[Terminal Contact Console]
  ├─ Interactive Contact Cards (`mailto`, `git clone`, `curl linkedin`, `ping bhushan.sahane.in`)
  └─ 1-Click Copy with Toast Alerts

[Footer]
  ├─ Identity, Copyright, Build Credit, and EOF
  └─ CRT Scanline Mode & Back-To-Top Floating Controls
```

---

## Voice and Tone

- **Perspective**: Senior AI Infrastructure Engineer. Concise, technically precise, zero marketing fluff.
- **Microcopy Conventions**:
  - Unix filesystem metaphors: paths prefixed with `~/`, scripts prefixed with `./`, environment files with `// ~ ./config.env`.
  - Action labels: `copy`, `clone`, `source`, `get-in-touch`, `ask →`.
  - Terminal feedback: Prefixed with directional arrows (`→`) or system comments (`//`).
  - Toast alerts: Fast, unpretentious confirmations (`Copied: git clone https://...`).

---

## Component Patterns

### 1. Dual-Engine Interactive Terminal
- **Dual Routing Model**:
  1. *Local CLI Engine*: Immediate interception of shell keywords (`help`, `whoami`, `skills`, `projects`, `certs`, `contact`, `uptime`, `date`, `matrix`, `theme`, `clear`, `arch`, `ls`, `pwd`, `id`, `uname`, `history`, `say`, `echo`, `cat`). Executed synchronously in 0ms.
  2. *Cloud AI Proxy*: For non-command questions, queries `/api/v1/messages` (or `http://127.0.0.1:8787/v1/messages` on localhost) with a 2200ms abort controller.
  3. *Contextual Knowledge Fallback*: If the proxy is offline or times out, the local knowledge base answers instantly without showing connection failure errors.
- **Authentic Linux Shell User Prompt**: User commands and queries format as `visitor@terminal:~$ <cmd>` with distinct color syntax tokens.
- **Adaptive Typewriter Streaming**: Assistant responses stream chunk-by-chunk with a blinking phosphor cursor (`▋`) and automatic scroll tracking.
- **1-Click Output Copy**: Dedicated copy button in the response header provides immediate tactile confirmation (`copied!`) and system clipboard synchronization.
- **Ghost Autocomplete**: As the user types in `#chatInput`, matching shell commands display as faint ghost text. Pressing `Tab` or `ArrowRight` auto-completes the command.
- **Command History**: `ArrowUp` and `ArrowDown` navigate past typed commands in the active session.
- **Quick-Run Command & Query Chips**: Categorized `$ command` and `? query` pill switches trigger immediate execution.
- **Optional Mechanical Sound FX**: Synthesized mechanical clicks via native Web Audio API (strictly muted by default, toggleable via terminal header).

### 2. Cursor-Following Spotlight Lighting
- Project and skill cards compute mouse coordinates (`--mouse-x`, `--mouse-y`) relative to the card on `pointermove`.
- A subtle radial gradient illuminates the border and card surface directly under the cursor, giving physical depth without layout shifts.

### 3. Interactive Skills-to-Projects Cross-Filtering with Visual Pulse
- Clicking any skill tag (e.g., `MCP Protocol`, `Ansible`, `LangChain`, `Proxmox`):
  1. Sets search term and filters repository list.
  2. Opens `#repo-index` and scrolls to the archive (instant under reduced motion).
  3. Announces the search and actual match count in a toast.
  4. Triggers a 1.4-second luminous accent pulse (`card-highlight-pulse`) on all matching project cards to orient the user.

### 4. One-Click Copy Actions
- Clicking any copy action (`git clone`, email, URL) copies the string to the system clipboard, temporarily swaps the button label to `✓ copied` (in green) for 1800ms, and dispatches an accessible toast notification.


### 5. Selected Work and Browser-Only Request Lab
- **Evidence and Entry Points**: Selected work appears immediately after the hero. Mesh links to its fork and credits `decocms/studio`; Ansible and Proxmox diagrams identify their data as illustrative. Project demo buttons select the corresponding scenario, reset playback, scroll to the lab, and focus Run without starting automatically.
- **Three Scenarios**: `ansible-inventory` reads `/demo/hosts.ini`; `proxmox-list-vms` requests running VMs on `pve-01`; `ansible-playbook` demonstrates rejection by an illustrative read-only policy for `portfolio-reader`. Payloads and results are local examples; no request leaves the page.
- **Trace and Results**: Allowed scenarios progress through request, identity, policy, route, tool result, and delivered response. Denied playback stops after the third step, marks the tool server “Not executed,” and displays a JSON-RPC gateway error with `toolExecuted: false`. Successful outputs are labeled decoded sample data. The native payload disclosure exposes the selected JSON-RPC `tools/call` request at any time.
- **Explicit Playback**: The same native button offers Run, Pause, Resume, and Replay. Steps advance every 850ms; changing scenarios resets the trace and pending result. Completion leaves the final trace and output visible until an explicit replay or scenario change.
- **Visibility and Motion**: Playback pauses when the tab becomes hidden or the lab leaves the viewport; resumption is explicit. Reduced motion makes Run/Replay reveal the complete outcome immediately. Enabling reduced motion during playback also completes the trace immediately.
- **Accessible Static State**: Text node states and the ordered trace supplement color and packet motion; status updates use a polite live region. Without JavaScript, the topology and initial request remain readable, the Run button stays disabled, and a noscript message explains playback availability. On mobile, topology and inspection columns stack vertically.

### 6. Progressive Disclosure and Session Evidence
- **Repository Archive**: The native `details` starts closed. Skill filtering opens it automatically; visitors can otherwise expand it to use the existing search, category filters, source links, and clone actions.
- **Architecture Reference**: The full interactive topology lives inside a native disclosure in About. Hash navigation opens containing disclosures before scrolling to nested targets, including on initial page load.
- **Session Clock**: The About session counter and terminal `uptime` command use `performance.now()` to measure elapsed time in this browser tab. They do not report infrastructure availability.
- **Repository Evidence**: Hero stars are explicitly a snapshot; the repository index explains that counts and stars come from the local index and points to GitHub for current activity.

---

## State Patterns

| Component | Default | Hover / Focus | Active / Loading | Disabled / Empty |
|---|---|---|---|---|
| **Terminal Input** | Inset dark background, ghost autocomplete behind | Green outline (2px, offset 2px) | Thinking dots animation, disabled submit button | Submitting disabled when empty |
| **Spotlight Card** | Subtle dark border `#21262d` | Radial phosphor spotlight under cursor, `translateY(-3px)` | `card-highlight-pulse` green bloom when filtered | N/A |
| **Filter Tab** | Muted text, subtle border | Accent color border and text | Inverted background `#39d353`, dark text `#0a0e14` | N/A |
| **Request Lab** | Ready, pending response | Native select/button focus treatment | Tracing, Paused, Completed, or Denied; explicit replay | Run disabled without JavaScript |
| **Repository / Architecture Disclosure** | Collapsed | Native summary keyboard focus | Expanded on activation or linked descendant | Static content remains inspectable |
| **Toast Alert** | Hidden, `opacity: 0`, translated down | Visible on hover | `opacity: 1`, translated into view, auto-dismiss 2400ms | Removed from viewport |

---

## Interaction Primitives

- **Keyboard Shortcuts**:
  - `⌘ + /` or `Ctrl + /`: Focuses the interactive terminal prompt.
  - `Tab` or `ArrowRight` (in terminal input): Completes ghost command autocomplete.
  - `ArrowUp` / `ArrowDown` (in terminal input): Traverses shell command history.
  - `Escape`: Closes mobile drawer or clears the terminal input.
- **Scrollspy Navigation**: Active section automatically updates `aria-current="page"` on header navigation links based on `IntersectionObserver`.
- **Top Scroll Progress Bar**: Updates width (`0%` to `100%`) linearly with document scroll position.

---

## Accessibility Floor

1. **Semantic HTML5**: Native elements used exclusively (`<nav>`, `<header>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>`, `<button>`, `<a>`, `<details>`, `<summary>`, `<select>`).
2. **Text Contrast**: Normal body and secondary text verified at >= 4.5:1 against surfaces (`#94a3b8` on `#0a0e14` = 7.1:1).
3. **Screen Reader Announcements**:
   - `aria-live="polite"` on chat response stream, project filter status counter, and request lab status.
   - `aria-live="assertive"` on toast alerts.
   - `aria-expanded` and `aria-controls` on mobile hamburger and drawer.
4. **Touch Target Dimensions**: Minimum 44x44px bounding box on all mobile tap targets.
5. **Reduced Motion**: Full compliance with `@media (prefers-reduced-motion: reduce)` — disabling typewriter loop, instant scrolling, disabling counter rollups, and collapsing all transition durations to 0ms.

## Portfolio curation — 23 September 2026

Only GitHub repositories with `fork: false` belong in the portfolio catalogue. Selected work is mcp-ansible and mcp-proxmox. Remove excluded repositories from biography, timeline, terminal suggestions, canned replies, and architecture attribution as well as cards. The policy gateway in the browser request simulator is an illustrative pattern, not a portfolio repository or deployed service.

The hero immediately exposes identity, technical focus, source links, and credentials. A native “30-second briefing” disclosure supports recruiter scanning without a modal. A direct hero link leads to the request simulator; no simulation starts without visitor action.
