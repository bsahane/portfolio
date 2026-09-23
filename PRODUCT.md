# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary: technical hiring managers and recruiters evaluating Bhushan Sahane for a senior AI-infrastructure / platform engineering role. They typically arrive from a LinkedIn profile, a resume link, or a GitHub profile, are skimming under time pressure, and need to establish quickly whether the depth is real and verifiable.

Secondary (confirmed as real traffic, not the design target): engineering peers, infra architects, and AI researchers arriving from repo READMEs to evaluate the MCP/agentic projects for use or contribution.

## Product Purpose

A single-page personal portfolio and technical showcase for Bhushan Sahane, AI Infrastructure Engineer at Red Hat, Inc. It exists to convert a cold skim into a warm conversation.

Success is any of:
- inbound contact (email, LinkedIn, or a copied address);
- credibility established — the visitor leaves convinced the depth is real, certifications verified, projects inspected, even without contacting;
- project adoption — click-through to GitHub, clone, star, or use of the MCP/AI repositories;
- forward motion in a specific hiring or promotion conversation.

## Positioning

Demonstration over assertion: the site is itself an artifact of the engineering it describes. Depth is provable in-page rather than claimed — live credential verification deep-links, a working dual-engine terminal, real repositories with real star counts, and a protocol-flow visualizer. The specific expertise combination is Red Hat enterprise automation (RHCE, RHCSA, Ansible Automation Platform) crossed with agentic AI infrastructure (MCP servers, RAG pipelines) — a pairing a generic AI portfolio cannot truthfully copy.

## Operating Context

- Visitors arrive from LinkedIn, resumes, GitHub profiles, and repo READMEs; many are on mobile and many are skimming in under a minute.
- Evaluation behavior includes: verifying certifications on the Red Hat portal and Credly, opening repositories on GitHub, and copying contact details.
- The site must function completely offline or behind strict corporate firewalls; terminal commands, project search/filter, and contact actions all work without external round-trips.
- Local workflow: `python3 -m http.server 8000`; optional AI proxy `python3 proxy.py` on `http://127.0.0.1:8787`.

## Capabilities and Constraints

- Single-page application in one file: `index.html` (CSS tokens in `<style>`, semantic markup in `<body>`, data and handlers in `<script>`). HTML5 / CSS3 / vanilla ES6, no framework, no build step — it must remain directly servable by any static web server.
- `proxy.py` is an optional local bridge to the Anthropic API for the interactive terminal. The site is fully functional without it; proxy failure must never surface a raw networking error — it falls back silently to the local knowledge engine and local CLI commands.
- No API keys committed; the proxy reads `BROCODE_KEY` from the environment.
- Sections: hero + interactive terminal, about + MCP architecture visualizer, toolbox/stack matrix, projects (filter + in-memory search), certifications and verification portal, journey timeline, contact console, footer telemetry.
- All icons are inline SVG. Emoji are never used as controls or system icons.
- One-click clipboard actions (git clone, email, credential IDs, links) must give immediate on-button feedback plus a toast.
- Terminology follows Unix filesystem metaphors: `~/path`, `./script`, `// comment`, `$ command`.

## Brand Commitments

- Name and identity: Bhushan Sahane · `bsahane`. Domain `bhushan.sahane.in`.
- Voice: senior AI infrastructure engineer. Concise, technically precise, zero marketing fluff.
- Red Hat is the employer only. The site is personal and must never imply it is an official Red Hat property, or that Red Hat endorses it.
- The monospace-first dark terminal aesthetic (JetBrains Mono / Fira Code, OLED dark palette, Cyberpunk and Gruvbox themes) is an established, binding part of the identity. See `DESIGN.md` for the recorded visual system and `EXPERIENCE.md` for interaction architecture.

## Evidence on Hand

Real and verifiable:
- Employment: AI Infrastructure Engineer at Red Hat, Inc.
- Five certifications, primary Red Hat Certificate ID `170-063-119`, with live verification deep-links to the Red Hat portal and Credly: RHCE (active to Jul 2027), RHCSA (active to Jun 2027), Managing Enterprise Automation with Red Hat AAP (DO467), RHCSA Rapid Track (RH199), Red Hat System Administration I (RH124, Credly badge).
- Public GitHub repositories with real star counts, including Legal MCP, mcp-ansible, and mcp-proxmox.
- Working in-page demonstrations: dual-engine terminal, MCP architecture visualizer.

Absent — must never be fabricated: testimonials, client names or logos, employer endorsements, performance benchmarks, adoption or traffic metrics, invented star counts, awards, press mentions, and speaking history.

## Product Principles

1. **Prove, do not claim.** Every assertion of depth should be checkable in-page or one click away — a verification link, a repository, a running demo.
2. **Respect the skim.** The primary visitor is time-boxed; the first viewport must establish who, what, and credibility before any interaction is required.
3. **Interaction is evidence, not decoration.** The terminal, filters, and visualizer exist because they demonstrate the engineering; anything that does not carry that weight is ornament.
4. **Degrade without apology.** Offline, firewalled, reduced-motion, keyboard-only, and 375px are all first-class. Failures fall back silently to something that works.
5. **Zero build, one file.** Portability and inspectability are part of the argument the site makes.

## Accessibility & Inclusion

WCAG 2.1 AA is a hard floor: ≥4.5:1 text contrast, full keyboard operability, visible focus rings, ARIA live regions on the chat stream, filter status, and toasts, 44×44px minimum touch targets, and full `prefers-reduced-motion: reduce` compliance.
