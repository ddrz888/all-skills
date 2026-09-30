# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this directory is

`/Users/jarvis/Desktop/AiOS-SYSTEMS` is not a single codebase or a git repository. It is a working folder collecting many independent AI projects and downloads (the user's personal AI/SYSTEMS workspace). Content spans:

- **AiOS** — the user's flagship SMB-AI brand ("Advanced Intelligence Operating System", B2B market in Slovakia). Contains `AiOS/CLAUDE.md` — **read that first when working on anything AiOS-related** (docs, brand-site, prompt packs, React brand-site stack).
- **Weby/** — website projects: `aios-platform`, `aios-webhosting`, `demo-auto-detailing`, demos.
- **Code_Projects/ & JarvisProjects/** — vendored/working copies of code repos (e.g. `aios-brand-site`, `aios-landing`, `aios_app`, scrapers, skills collections).
- **Standalone downloaded repos** (git-ignored copies) — e.g. `aios-main/` ("All In One Script", a V2Ray/Xray/Cloudflare router script in Chinese), `AIS-OS-main/`, `snagtime-main/`, `promptimizer-main/`, `a-bunch-of-skills-master/`, `MasterClassn8n-main/`, `NEROZBALENE /` (unzipped), `Archives/`, plus assorted PDFs in `Documents/` and images in `Obrazky/`.

## Working here

- **There is no unified build/lint/test.** Each subfolder is an independent unit with its own tooling, README, and dependency manifest (if any). Check the subfolder's own `README.md` / `CLAUDE.md` before running anything.
- **How to find the right code**: this folder holds many copies/versions of the same projects across `AiOS/`, `Weby/`, `Code_Projects/`, `JarvisProjects/` and loose repos. Before editing, confirm which copy is the working one (check timestamps and which one a `README`/`CLAUDE.md` names as active), rather than assuming the first match.
- **AiOS brand-site dev flow** (from `AiOS/CLAUDE.md`): React 19 + Vite + TypeScript + Tailwind v4 + Express; package manager is pnpm — `pnpm install`, `pnpm dev`, `pnpm build` from the brand-site dir.
- Trust each subproject's own documentation; do not treat one repo's conventions as applying repo-wide.

## Conventions worth preserving

- Many folders are downloads / git-cloned snapshots; leave them as-is unless work is explicitly scoped to them.
- Secrets and personal data (numerous PDFs, zips, backups) live in `Documents/` and `Archives/` — don't index or summarize their contents unless asked.
- Prefer updating the subproject-local `CLAUDE.md`/`README.md` over describing everything here.
