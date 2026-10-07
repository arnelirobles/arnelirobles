<h1 align="center">Arnel Robles</h1>

<p align="center">
  <strong>I design and build the systems a business runs on, then keep them running.</strong><br>
  <em>Multi-tenant platforms, the data underneath them, the AI on top, and the audit that checks it all holds.</em><br>
  <sub>.NET and PostgreSQL · multi-tenant SaaS · LLM and agent systems · security audits · Philippines, fully remote since 2020</sub>
</p>

<p align="center">
  <a href="mailto:arnelirobles@gmail.com?subject=Hello%20from%20your%20GitHub"><img alt="Email me" src="https://img.shields.io/badge/email-arnelirobles%40gmail.com-1f6feb?style=flat-square&logo=gmail&logoColor=white"></a>
  <a href="https://baryo.dev"><img alt="baryo.dev" src="https://img.shields.io/badge/site-baryo.dev-8957e5?style=flat-square"></a>
  <a href="https://baryodev.medium.com"><img alt="Writing" src="https://img.shields.io/badge/writing-medium-333?style=flat-square&logo=medium"></a>
  <a href="https://huggingface.co/arnelirobles"><img alt="Hugging Face" src="https://img.shields.io/badge/models-hugging%20face-ffcc4d?style=flat-square&logo=huggingface&logoColor=black"></a>
</p>

<p align="center"><sub>
  <a href="#the-platform-i-design-and-run">Platform</a> ·
  <a href="#llm-and-agent-systems">LLM and agents</a> ·
  <a href="#security-audits">Security audits</a> ·
  <a href="#open-source-contributor">Upstream</a> ·
  <a href="#what-i-have-built-for-other-people">Client work</a> ·
  <a href="#libraries-and-tools">Libraries</a> ·
  <a href="#writing">Writing</a> ·
  <a href="#stack">Stack</a>
</sub></p>

> **You can contact me at [arnelirobles@gmail.com](mailto:arnelirobles@gmail.com?subject=Hello%20from%20your%20GitHub).**

---

14 years in production software, most of it on systems where being wrong costs something: derivatives for US financial institutions, hospital and national health insurance systems, ERP and payroll. Remote since 2020, on teams in the US and New Zealand.

In 30 seconds:

- **I design platforms.** [barakoCMS](https://github.com/BaryoDev/barakoCMS) is a multi-tenant, metadata-driven data platform on .NET and PostgreSQL, with its console, renderer, client and deploy tool, all public and all running.
- **I ship LLM and agent systems** that respect permissions and get checked by something other than a person's say-so.
- **I audit web applications** against OWASP WSTG and ASVS and hand back a report ranked by what to fix first.
- **Fifteen changes merged upstream** in Umbraco, Marten and Testcontainers, nearly all for a bug my own projects hit.

---

### The platform I design and run

**[barakoCMS](https://github.com/BaryoDev/barakoCMS)** is an open-source data platform for .NET 10 on PostgreSQL. Customers define their own content types, fields, choice lists and references at runtime through the API, and tenant isolation, roles, field-level masking and audit apply to all of it. Event-sourced on Marten, so every change is on record. An event-driven workflow engine, 15 opt-in modules, and about 2,050 test methods (3,009 test cases) run against real PostgreSQL and MinIO through Testcontainers. MPL-2.0, currently 4.4.1.

The decisions are the work. Event sourcing over CRUD, and what that costs on the read side. Modules compiled in rather than loaded at runtime, because a plugins folder is a place where writing a file runs code. One cheap VM instead of a platform, and what that trades away. Each is written up with the reasoning, not just the outcome.

The rest of the platform, all public:

| Piece | What it does |
|---|---|
| **[barakoBrew](https://github.com/BaryoDev/barakoBrew)** | The console: design content types, roles, workflows and integrations against the API. Next.js and TypeScript. |
| **[barakoPress](https://github.com/BaryoDev/barakoPress)** | The renderer: pages from blocks, collections and docs trees, server rendered and cached per tenant until the CMS says otherwise. [barakocms.com](https://barakocms.com) runs on it. |
| **[barako-client](https://github.com/BaryoDev/barako-client)** | Typed TypeScript client. API key or JWT, tenant-aware, isomorphic. |
| **[create-barako-app](https://github.com/arnelirobles/create-barako-app)** | `npm create barako-app` gives you a Next.js project with the API, console and renderer in docker compose, seeded content and sign-in already working. |
| **[BaryoVM](https://github.com/BaryoDev/BaryoVM)** | PaaS-style deploys onto your own cheap VMs. Agentless, over SSH, one Go binary. Every BaryoDev deploy goes through it, which is how its gaps get found. |

**Live** at [playground.baryo.dev/barakocms](https://playground.baryo.dev/barakocms).

---

### LLM and agent systems

| Project | What it does |
|---|---|
| **[barakoCMS AI](https://github.com/BaryoDev/barakoCMS)** | Semantic search over tenant content with a self-hosted embedding model, no third-party key. It indexes only public fields and re-checks every result as published and public at query time, so retrieval cannot return what the caller could not read. |
| **[Baryo CLI](https://github.com/BaryoDev/Baryo.CLI)** | An agent CLI in Go for local models (Ollama, Docker Model Runner) and 18+ cloud providers. Tool calling with file, shell and git tools, an MCP client, and permission modes that ask before a destructive tool runs. Most of the work went into failure paths: MCP tools that skipped the permission gate, and a failed context compaction that silently overwrote the conversation. |
| **[lean-agent](https://github.com/arnelirobles/lean-agent)** | How I run AI coding agents over a real ticket backlog, packaged as a Claude Code plugin. I now run it as one session on one model: it drafts, scripts run the mechanical checks, then it reviews its own change against six fixed questions in two passes, one to find problems and one to refute them. A finding not fixed in two rounds comes to me. The cascade mode is still in the plugin (a cheap model drafts and critiques, the expensive one sees only what the critic cannot close), and it took me from about **66 dollars of model use per change to about 25**, measured from the agent transcripts. My numbers, one .NET codebase, list prices. |
| **[Abogado](https://huggingface.co/arnelirobles/abogado)** | A Philippine law assistant in English and Tagalog, published on Hugging Face. Qwen2.5-3B-Instruct fine-tuned with QLoRA on a Kaggle T4, with a [GGUF build](https://huggingface.co/arnelirobles/abogado-gguf) to run it locally. A small first version, 106 question and answer pairs from the 1987 Constitution. It refuses requests for private data and points people to a real lawyer instead of playing one. Apache-2.0. |

---

### Security audits

I audit web applications end to end and hand back a report a team can act on. The method was built on my own stack first, barakoCMS with its console and renderer exactly as deployed, before I would point it at anyone else's.

- **Source review of what is actually deployed**, pinned to the running commits rather than the branch tip.
- **Non-destructive checks against production.** GET and HEAD only, no accounts created, nothing written.
- **Anything that needs a signed-in user or a write runs on a local copy** built from the production images and the production proxy config, on loopback only.
- **A test catalogue mapped to OWASP WSTG and ASVS**, each test with an honest status: built, partial, broken or missing. The report says what was not checked as plainly as what was.
- **Each finding** comes with its CWE, where it is, what an attacker does with it, the specific fix, the order to fix in, and a script that reruns it once the fix lands.

The part most audits skip: checking the checks. On my own stack that meant finding scripts that went green without proving anything, and fixing those before writing new ones.

<details>
<summary>What I look for</summary>

Broken access control and IDOR (an id from the URL used to load or mutate another user's object with no ownership check), authorization mistaken for authentication, privilege escalation on write paths and across tenants, ownership checks that run after the mutation instead of before, unauthenticated reads of private data, stored and reflected XSS including what a markdown renderer lets through, clickjacking, token storage and session revocation, committed secrets and long-lived tokens, open redirects in login flows, and header and proxy trust. A finding I cannot trace to a concrete failure does not go in the report.

</details>

---

### Open source contributor

<a href="https://github.com/search?q=author%3Aarnelirobles+type%3Apr+is%3Amerged+org%3Aumbraco+org%3Atestcontainers+org%3AJasperFx&type=pullrequests"><img alt="15 merged upstream" src="https://img.shields.io/badge/upstream-15%20merged-2ea44f?style=flat-square&logo=github"></a>
<a href="https://github.com/search?q=author%3Aarnelirobles+type%3Aissue+org%3Aumbraco+org%3Atestcontainers+org%3AJasperFx&type=issues"><img alt="8 accepted bug reports" src="https://img.shields.io/badge/bug%20reports%20accepted-8-1f6feb?style=flat-square&logo=github"></a>
<a href="https://github.com/BaryoDev"><img alt="30 public repositories" src="https://img.shields.io/badge/%40BaryoDev-30%20public%20repos-8957e5?style=flat-square&logo=github"></a>

**Fifteen merged changes and eight accepted bug reports** in libraries I run in production, across four repos totalling 13k stars. Most started from a bug I hit in my own projects rather than from browsing a tracker for something to fix. The badges are live searches, so they answer for themselves.

| Project | What was wrong |
|---|---|
| **[umbraco/Umbraco-CMS](https://github.com/umbraco/Umbraco-CMS)**<br><sub>★5.3k</sub> | Instances sharing a database failed each other's requests registering the same OpenIddict application. [#23599](https://github.com/umbraco/Umbraco-CMS/pull/23599), [#23727](https://github.com/umbraco/Umbraco-CMS/pull/23727), shipped in 17.7 and 18.2. A disabled or locked out user kept a valid back-office cookie, so they were issued fresh tokens and landed in an empty back office where every call returned 403 and there was no way to log out. [#23995](https://github.com/umbraco/Umbraco-CMS/pull/23995) signs them out instead, queued for 17.8 and 18.3 |
| **[testcontainers/testcontainers-dotnet](https://github.com/testcontainers/testcontainers-dotnet)**<br><sub>★4.4k</sub> | MongoDB replica-set init was not idempotent, so a reused container hung against a one-hour timeout. [#1731](https://github.com/testcontainers/testcontainers-dotnet/pull/1731), [#1735](https://github.com/testcontainers/testcontainers-dotnet/pull/1735). A reused Couchbase container then stalled on the first step of configuring a cluster that was already configured. [#1736](https://github.com/testcontainers/testcontainers-dotnet/pull/1736). Confluent Platform 8.x images exited on startup because the module left a trailing comma in the advertised listeners, which Kafka 4 rejects. [#1772](https://github.com/testcontainers/testcontainers-dotnet/pull/1772). With that fixed, they still defaulted to ZooKeeper, which 8.x removed. [#1775](https://github.com/testcontainers/testcontainers-dotnet/pull/1775). The docs never said how builder calls combine, so setting your own startup callback on a module silently replaced its provisioning, and MongoDB never initiated its replica set. [#1770](https://github.com/testcontainers/testcontainers-dotnet/pull/1770) documents the rules on a page of their own |
| **[JasperFx/marten](https://github.com/JasperFx/marten)**<br><sub>★3.5k</sub> | `HardDeleteWhere` could not remove already soft-deleted rows, and returned cleanly either way. [#5215](https://github.com/JasperFx/marten/pull/5215), [#5202](https://github.com/JasperFx/marten/pull/5202), [#5240](https://github.com/JasperFx/marten/pull/5240). The parameterised `MatchesJsonPath` overload threw on every call, so no one could have been using it. [#5289](https://github.com/JasperFx/marten/pull/5289). The pgvector docs still described a recall cap the library had stopped applying, and the caveat that replaced it was wrong for hybrid search. [#5467](https://github.com/JasperFx/marten/pull/5467) |
| **[JasperFx/jasperfx](https://github.com/JasperFx/jasperfx)**<br><sub>core library</sub> | The event loader claimed a ceiling it had never scanned, so a fully skipped batch could advance past events and lose them permanently. Reported on Marten, then fixed at the source. [#670](https://github.com/JasperFx/jasperfx/pull/670) |

Most of these reports were fixed by the projects' own maintainers rather than by me, which is the part worth pointing at: the report carried enough evidence for someone else to act on it.

| Reported | Outcome |
|---|---|
| [marten#5501](https://github.com/JasperFx/marten/issues/5501) | When the event loader fell back to skipping ahead, it reported a floor above the one requested, so the projection's progress write matched no rows. Fixed the same day in [#5506](https://github.com/JasperFx/marten/pull/5506), shipped in 9.39.1. |
| [marten#5502](https://github.com/JasperFx/marten/issues/5502) | Only the first progress write in a batch had its row count checked, so a stale one after it committed silently. The fix in [#5507](https://github.com/JasperFx/marten/pull/5507) found this also covered every member of a composite projection. Shipped in 9.39.1. |
| [marten#5239](https://github.com/JasperFx/marten/issues/5239) | A projection's event loader reported a ceiling it never scanned, so events could be skipped permanently. Confirmed by the maintainer as silent, permanent data loss, fixed in [#5242](https://github.com/JasperFx/marten/pull/5242), and I then fixed the same flaw in the shared library underneath in [jasperfx#670](https://github.com/JasperFx/jasperfx/pull/670). |
| [marten#5234](https://github.com/JasperFx/marten/issues/5234) | Event masking and stream compaction wrote across tenants under partitioned event tenancy. Fixed in [#5236](https://github.com/JasperFx/marten/pull/5236). |
| [marten#5222](https://github.com/JasperFx/marten/issues/5222) | An audit reported a check as passing that it had not actually performed. Fixed in [#5231](https://github.com/JasperFx/marten/pull/5231). |
| [umbraco#23598](https://github.com/umbraco/Umbraco-CMS/issues/23598) | The Delivery API's subscriber guard can never match, because the server role is not elected until after the boot notification it reads from. Fixed by an Umbraco developer in [#23801](https://github.com/umbraco/Umbraco-CMS/pull/23801), a change spanning 21 files, merged and queued for 17.8. |
| [testcontainers#1732](https://github.com/testcontainers/testcontainers-dotnet/issues/1732) | A readiness check counted log lines and compared the count for equality, so a container either hung against a one-hour timeout or was reported ready before the server was listening. Two other users confirmed it independently. Fixed in [#1735](https://github.com/testcontainers/testcontainers-dotnet/pull/1735). |

Sometimes the useful contribution is not a pull request. On [marten#5457](https://github.com/JasperFx/marten/issues/5457), someone else's leak report, I could confirm half of it and disprove the other half, and said so rather than opening a fix I could not demonstrate. The maintainer's own [#5466](https://github.com/JasperFx/marten/pull/5466) opens by crediting that comment: *"right on both counts and shaped this."*

**[upstream-fixes](https://github.com/arnelirobles/upstream-fixes)** writes each one up, and carries a runnable reproduction for marten#5215 against published NuGet packages, so you can watch that bug appear on one version and disappear on the next rather than take my word for it.

---

### What I have built for other people

The open source is the visible half. The other half is client and product work, mostly in places where a wrong number is somebody's money or somebody's medical record.

| Area | What I built |
|---|---|
| **Financial systems** | A SaaS platform US financial institutions use to manage interest rate, FX and commodity derivatives. Designed a general ledger and a document management system from first principles, and built the star schema warehouse behind daily cashflow and hedge accounting reporting. Distributed services over RabbitMQ, SQS and SNS, on ECS and Fargate with infrastructure as code. |
| **Case and document workflow** | ASP.NET Core and EF Core behind a React front end for a national dispute resolution body, handling case and document workflows. Azure Functions, App Services and Storage, with CI/CD on Azure DevOps. Also maintained and extended an Umbraco CMS platform, which is where the upstream contributions started. |
| **Gaming management and analytics** | Led the early build of a casino management and analytics platform on .NET, React and SQL Server, running the development and QA teams and owning the release pipelines. |
| **Enterprise and healthcare integration** | .NET and Java integrations across ERP, financial, materials and payroll systems at a large agribusiness, plus hospital and national health insurance systems. SOAP and XML services, SSIS between AS400 DB2 and SQL Server, and AS400 administration at 24/7 availability. |
| **Independent client delivery** | Feature and defect delivery across established codebases, middleware, third-party and Stripe payment integrations in JavaScript for a client platform. Took a production application from .NET 8 to .NET 10 with its ORM and test framework, 651 tests passing. |

Modernisation is a thread through most of it: ASP.NET MVC and AngularJS onto current .NET with the business running throughout, VB6 rebuilt on ASP.NET Core, and a large Oracle schema moved to PostgreSQL behind a live application to remove the licensing cost.

Fully remote, across distributed teams in several time zones. Alongside the building: leading and mentoring developers, setting the standards the team codes against, running code review, technical discovery and estimation with stakeholders, and interviewing.

---

### Libraries and tools

30 public repositories under [@BaryoDev](https://github.com/BaryoDev). Each solves one problem, ships to a package registry, and is tested rather than described.

#### .NET

| Project | What it does |
|---|---|
| **[Verdict](https://github.com/BaryoDev/Verdict)** | Result pattern with a zero-allocation core, 3.0.0. The allocation promise is the product, so it is enforced by benchmark rather than asserted in a README: 0 B and 0 collections measured over 1.6M operations on 8 threads. |
| **[Mapsicle](https://github.com/BaryoDev/Mapsicle)** | Object mapping, fourteen packages at 2.5.0, one test project per integration. Benchmarked on x64 and arm64 against AutoMapper and Mapperly, and the published numbers say where it loses as well as where it wins. [Side-by-side sample](https://github.com/arnelirobles/mapsicle_samples). |
| **[Carom](https://github.com/BaryoDev/Carom)** | Resilience: retry, timeout, circuit breaker, bulkhead, rate limiting, fallback, hedging. Zero dependencies in the core, netstandard2.0 upward. |
| **[Talaan](https://github.com/BaryoDev/Talaan)** | Spreadsheet and CSV reader, xlsx and CSV, zero dependencies. barakoCMS consumes it as a published package rather than a project reference, so the packaging is exercised for real. |
| **[umbraco-pwa](https://github.com/BaryoDev/umbraco-pwa)** | Turns an Umbraco site into an installable, offline-capable app. On the Umbraco Marketplace, 0.5.2 on NuGet. |
| **[umbraco-read-aloud](https://github.com/BaryoDev/umbraco-read-aloud)** | Read-aloud for an Umbraco site using Microsoft Edge neural voices. |

#### TypeScript and JavaScript

| Project | What it does |
|---|---|
| **[rnxjs](https://github.com/BaryoDev/rnxjs)** | 46 components for Django, Rails and Laravel templates. One script tag, no build step. [Worked examples](https://github.com/BaryoDev/rnxJS_samples). |
| **[rnxORM](https://github.com/BaryoDev/rnxORM)** | Node.js ORM, integration-tested against PostgreSQL, SQL Server and MariaDB rather than mocked. |
| **[Kapehan](https://github.com/BaryoDev/Kapehan)** | 42 hand-drawn coffee icons, MIT. Full-colour and `currentColor` builds come from the same geometry, and `npm test` fails if the CSS and the component manifest drift apart. [Browse the set](https://baryodev.github.io/Kapehan/). |
| **[read-aloud](https://github.com/BaryoDev/read-aloud)** | Read-aloud for any site. Headless controller, web component, word highlighting. |
| **[pwa-kit](https://github.com/BaryoDev/pwa-kit)** | Install prompt for Android and iOS, a network-first service worker, and the helpers around them. |
| **[dopaminejs](https://github.com/BaryoDev/dopaminejs)** | Progression mechanics for web apps: XP, levels, achievements and timezone-correct daily streaks. |

#### Tools I use every day

| Tool | What it does |
|---|---|
| **gh-ci-local** <sub>private</sub> | A GitHub CLI extension that runs a repository's Actions jobs on your own machine, for repos where Actions is off or the minutes ran out. Stops at the first failing step and exits non-zero. |
| **provstrip** <sub>private</sub> | Strips provenance metadata from PNG and SVG without re-encoding, in Rust. It splices rather than rewrites, and the tests assert the kept bytes are identical to the input. |
| **[fastendpoints-wolverine-lab](https://github.com/arnelirobles/fastendpoints-wolverine-lab)** | One operation written twice, on FastEndpoints and on Wolverine, against the same Marten database. The companion to a write-up comparing them. |

---

### Writing

Mostly postmortems of my own mistakes, and decisions with the reasoning attached.

| Article | About |
|---|---|
| [My benchmark said my library was 2x faster. It was not.](https://baryodev.medium.com/my-benchmark-said-my-library-was-2x-faster-it-was-not-d6a6110bf354) | A performance gate that could not have failed for its own reason, and what it took to make it resolve what it reports |
| [We built a modular CMS and deliberately did not make the modules plugins](https://baryodev.medium.com/we-built-a-modular-cms-and-deliberately-did-not-make-the-modules-plugins-66a30c79b1e5) | Runtime assembly loading forecloses Native AOT permanently, and a plugins folder is a place where writing a file runs code |
| [Your ORM is reading your lambdas with a regex](https://javascript.plainenglish.io/your-orm-is-reading-your-lambdas-with-a-regex-c1ebaede899d) | What lambda-parsing query builders actually do, and where that breaks |
| [Migrating from Polly to Carom](https://medium.com/codetodeploy/migrating-from-polly-to-carom-04791978a963) | The Polly maintenance fee is reasonable, the mechanism is the problem, and here is a pattern-by-pattern migration |
| [Mapsicle 2.1: honest numbers against AutoMapper](https://baryodev.medium.com/mapsicle-2-1-an-mpl-2-0-object-mapper-and-honest-numbers-against-automapper-fc0f726369dd) | Two architectures, medians of repeated runs, and a section on where it loses |
| [The tenant filter that only worked on the way in](https://baryodev.medium.com/the-tenant-filter-that-only-worked-on-the-way-in-3bad8544d165) | A multi-tenant event-sourcing bug that reads correctly and leaks on the way out |
| [One cheap VM, nineteen containers, no platform](https://medium.com/codetodeploy/one-cheap-vm-nineteen-containers-no-platform-5e76ff4e5c68) | What running everything on one box costs, and what it saves |
| [What two hundred issues taught us about building with AI](https://javascript.plainenglish.io/what-two-hundred-issues-taught-us-about-building-with-ai-e6b315bf59ad) | Where AI-assisted work fails quietly, and which gates catch it |

More at [baryodev.medium.com](https://baryodev.medium.com).

---

### How I work

I sort decisions by how expensive they are to reverse. A storage engine, a tenancy model, a public contract and a licence are one-way doors: those get argued out in writing first, with the reasoning kept rather than just the outcome, so the next person can disagree with the argument instead of guessing at it. Most other things are cheaper to try than to debate. That is why barakoCMS 4.0 shipped one-way doors only and everything else waited for 5.0.

Tests that cannot fail are the defect I look for first: a mock returning what the real dependency never returns, an assertion satisfied by a type's default value, a benchmark that prints and exits zero. Before trusting a gate I break the thing it guards and check it goes red.

AI-assisted daily, held to the same gates as everything else. The failure mode I design against is a green suite that proves nothing, which is why the mechanical checks are scripts and every change gets a critic before it gets an expensive model.

<details>
<summary>Beyond the code: triage, write-ups, reports, and working on systems that aren't mine</summary>


A review that turns up twenty findings is a triage problem before it is a fixing problem. I sort them by what is already exposed or hard to undo, act on those, and let the rest wait. Fixing them in the order they were found buries the one that mattered.

When something works twice I write down how, so it isn't luck the third time. barakoCMS ships a runbook for handing a project to a client, not just the product. The AI workflow has a script that measures cost per change, not a blog post about using AI.

The reports are the work as much as the commits are. My upstream bug reports got fixed by other people because they carried enough to act on. My writing is mostly postmortems of my own mistakes. When you hand someone a report instead of a patch, whether they can act on it is the only thing that counts.

Some of this touches systems and data that aren't mine. I stay inside what I'm authorised to do, read before I probe, and keep client specifics out of anything public. That is not politeness. It is why there is a next engagement.

</details>

---

### Stack

| Area | Tools and practice |
|---|---|
| **Languages** | C#, TypeScript, JavaScript, Go, SQL, Python and Rust for tooling |
| **Architecture** | Event sourcing and projections, multi-tenancy (conjoined and database-per-tenant), modular monoliths over plugin runtimes, API contracts and versioning, licensing and one-way-door calls |
| **Backend** | .NET Framework to .NET 10, ASP.NET Core and MVC, REST and GraphQL, EF Core and LINQ, microservices, event-driven and domain-driven design, CQRS-influenced design |
| **Messaging** | RabbitMQ, SQS, SNS, webhooks, background jobs |
| **Data** | PostgreSQL, SQL Server and Azure SQL, Marten, Redis, Oracle, DB2, star schema modelling, execution plan analysis and query tuning, SSIS and SSRS |
| **Cloud and delivery** | AWS (CDK, ECS, Fargate, SQS, SNS), Azure (Functions, App Services, Storage, SQL, DevOps), Oracle Cloud, Docker, Kubernetes, GitHub Actions, Octopus Deploy, OpenTelemetry, Sentry, SBOM |
| **Frontend** | React, Next.js, Angular, TypeScript, Razor, accessibility to WCAG |
| **Testing** | xUnit, NUnit, Moq, Testcontainers, Playwright, Vitest, BenchmarkDotNet, test-driven development, mutation testing, security scanning in CI |
| **AI and agents** | Claude and the Anthropic API, tool calling and MCP, embeddings and semantic search, local models on Ollama and Docker Model Runner |
| **Security** | OWASP Top 10 and CWE secure code review, access-control and IDOR analysis, OAuth 2.0, OIDC and JWT, secrets and dependency auditing, static-first with read-only verification |

---

<p align="center">
  You can contact me at any of these.<br>
  📫 <a href="mailto:arnelirobles@gmail.com?subject=Hello%20from%20your%20GitHub">arnelirobles@gmail.com</a> · 🌐 <a href="https://baryo.dev">baryo.dev</a> · ✍️ <a href="https://baryodev.medium.com">baryodev.medium.com</a>
</p>
