# Portfolio comparison and direction

Reviewed 23 September 2026: [Bhushan Sahane](https://bhushan.sahane.in/) and [Dhruv Mehta](https://www.dhruvmehta.dev/), using both rendered pages and their content. The changes described below were deployed to the live site on 22 September 2026 (18:39 GMT) and committed afterwards.

## What to learn from the comparison

| Area | Dhruv’s site | Bhushan’s site before this update | Direction for Bhushan |
|---|---|---|---|
| First impression | An illustrated nighttime workspace, hand-drawn lettering, and a strong personal setting | A terminal-led identity with dense technical language and a staged entrance | Keep the terminal identity; immediately show a clear engineering proposition |
| Personality | Workspace imagery, green-tea references, day/night control | Shell commands, ASCII art, editor palettes, interactive terminal | Make infrastructure itself the memorable interaction |
| Recruiter scanning | Explicit developer positioning and prominent contact actions | Good technical depth, but evidence scattered across a long page | Add a short briefing and direct links to experience and credentials |
| Work presentation | Projects sit within a coherent personal narrative | Selected work included an upstream fork alongside original tools | Lead with two non-fork infrastructure repositories and inspectable source |
| Interaction | Illustrated scene and visible theme controls support the personal world | Terminal, topology explorer, theme picker, filters, and request simulation compete for attention | Give request tracing the central role; keep other controls secondary |
| Credibility | Personal positioning and project/experience content | Employer history, verifiable Red Hat credentials, repository links, working examples | Emphasize evidence; remove unsupported authorship implications |

My design judgment: borrow the coherence and personality of Dhruv’s presentation. Bhushan’s distinguishing material is infrastructure engineering. A visitor should remember discovering how an agent request reaches a host—and how a policy can stop it.

## Implemented in this update

- Removed A2A from the website’s markup, metadata, skill tags, architecture nodes, terminal content, and local knowledge responses.
- Removed seven GitHub-confirmed forks from the repository catalogue and related narrative: mesh, strix, slack-mcp-client, fixtral, cc_peng_mcp, template-mcp-server, and 10x-Tool-Calls.
- Kept 13 repositories marked `fork: false` by GitHub. This metadata is evidence of repository status, not a claim that every line was written solely by Bhushan.
- Removed the fork-led Mesh showcase; mcp-ansible and mcp-proxmox lead selected work.
- Reframed the existing request simulation’s gateway as an explicitly illustrative policy layer.
- Changed the hero to “AI meets infrastructure.” Its identity, description, and actions are readable immediately.
- Added a native 30-second briefing with career, credential, and email links.
- Added a direct hero route to request tracing; retained user-controlled playback, pause, replay, and reduced-motion behavior.
- Added a brief active-node lock-in effect and a small directional arrow response. Kept the existing terminal identity and native static-site stack.
- Updated repository stars and counts from the GitHub snapshot; removed the old hero metrics cluster.

Repository metadata source: [GitHub repositories API](https://api.github.com/users/bsahane/repos?per_page=100). Static snapshot: 23 September 2026. Source ownership should also be checked through individual repository histories when making detailed authorship claims.

## Recommended next additions, in priority order

### 1. Evidence-rich project stories

For each lead repository, show the problem, Bhushan’s specific contribution, one important design tradeoff, a real source excerpt, and a reproducible command. Add measured outcomes only when a benchmark, issue, or deployment record supports them. This will contribute more to recruiter confidence than another decorative effect.

### 2. A debugging mode for the request simulator

Let visitors introduce a timeout or unavailable tool server, then inspect the error boundary and recovery. Add manual next-step controls and a timeline scrubber so engineers can investigate at their own pace. Clearly label every scenario as simulated. Keep failure states deterministic and offline-capable.

### 3. Source-to-system transitions

Select a tool in a source excerpt to highlight the corresponding server in the architecture diagram. A single 200–350ms connector sweep can explain the relationship. Keyboard selection should produce the same highlight; reduced motion should change the state instantly.

### 4. A real terminal recording

Capture a 15–25 second demonstration from an original repository: tool discovery, one read operation, and its result. Provide an accessible transcript, explicit play controls, a poster frame, and no autoplay. Real output makes a better project artifact than a decorative stock illustration.

### 5. A recruiter-ready resume route

Provide a maintained PDF or print-friendly career summary once the source resume and official role wording are confirmed. Link it beside contact. The existing experience section names “Senior System Administrator” while the portfolio positions Bhushan as an AI infrastructure engineer; distinguish official title from technical focus explicitly in the resume.

### 6. Progressive detail for the long page

Keep selected work, credentials, experience, and contact readily visible. Place extended tool inventories and architecture reference material behind native disclosures. This preserves depth while shortening the first reading path.

### 7. Measured performance and accessibility

Before adding heavy visual assets, establish real mobile performance measurements. Keep visual effects event-driven and pause them offscreen. Audit all optional color themes independently; checking the default palette alone cannot establish WCAG conformance for every theme.

Avoid cursor replacement, scroll hijacking, autoplay sound, fake live telemetry, invented impact metrics, and particle backgrounds. The strongest memorable interaction here is an inspectable system with a clear result.

## Validation and limits

- JavaScript syntax check passed.
- Browser layout checked at 375, 768, and 1280 pixels; no horizontal page overflow.
- Request simulator: normal allowed playback and reduced-motion denial checked; denial reports `toolExecuted: false`.
- Local MCP knowledge response checked after removing fork claims.
- Mechanical design scan surfaced legacy style warnings (including pinned cyberpunk glows and unused gradient declarations). These are not evidence of a clean full-site accessibility audit.
- No deployment, repository deletion, or GitHub account changes performed.
