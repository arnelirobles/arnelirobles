<h1 align="center">Arnel Robles</h1>

<p align="center">
  <em>I design systems end to end, then run them in production.</em><br>
  <a href="https://baryo.dev">baryo.dev</a> ·
  <a href="https://github.com/BaryoDev">@BaryoDev</a> ·
  <a href="https://baryodev.medium.com">writing</a> ·
  <a href="mailto:arnelirobles@gmail.com">email</a>
</p>

<p align="center"><sub>
  <a href="#open-source-contributor">Open source</a> ·
  <a href="#what-i-have-built-for-other-people">Client work</a> ·
  <a href="#barakocms">barakoCMS</a> ·
  <a href="#libraries-and-tooling">Libraries</a> ·
  <a href="#writing">Writing</a> ·
  <a href="#how-i-work">How I work</a> ·
  <a href="#stack">Stack</a>
</sub></p>

---

15 years in production software, most of it on systems where being wrong costs something: derivatives trading for US financial institutions, hospital, medical records and national health insurance systems, ERP and payroll, billing and cashiering.

The open source below is what I build when I get to choose the constraints. I design systems end to end and then run them: an event-sourced multi-tenant CMS, the deploy tooling it ships through, the libraries underneath it, and the front end on top. Strongest in .NET, though most of what I ship is not.

The decisions are the work. Event sourcing over CRUD and what that costs on the read side. Modules compiled in rather than loaded at runtime, because a plugins folder is a place where writing a file runs code. One cheap VM instead of a platform, and what that trades away. Each of those is written up with the reasoning, not just the outcome.

**[@BaryoDev](https://github.com/BaryoDev)** is 30 public repositories across C#, TypeScript, Go and JavaScript, all open source and self-hostable. No paid tier, no seat cap, no metered anything.

---

### Open source contributor

<a href="https://github.com/search?q=author%3Aarnelirobles+type%3Apr+is%3Amerged+org%3Aumbraco+org%3Atestcontainers+org%3AJasperFx&type=pullrequests"><img alt="12 merged upstream" src="https://img.shields.io/badge/upstream-12%20merged-2ea44f?style=flat-square&logo=github"></a>
<a href="https://github.com/search?q=author%3Aarnelirobles+type%3Aissue+org%3Aumbraco+org%3Atestcontainers+org%3AJasperFx&type=issues"><img alt="7 accepted bug reports" src="https://img.shields.io/badge/bug%20reports%20accepted-7-1f6feb?style=flat-square&logo=github"></a>
<a href="https://github.com/BaryoDev"><img alt="30 public repositories" src="https://img.shields.io/badge/%40BaryoDev-30%20public%20repos-8957e5?style=flat-square&logo=github"></a>

**Twelve merged fixes and seven accepted bug reports** in libraries I run in production, across four repos totalling 13k stars. Most started from a bug I hit in my own projects rather than from browsing a tracker for something to fix. The badges are live searches, so they answer for themselves.

| Project | What was wrong |
|---|---|
| **[umbraco/Umbraco-CMS](https://github.com/umbraco/Umbraco-CMS)**<br><sub>★5.2k</sub> | Instances sharing a database failed each other's requests registering the same OpenIddict application. [#23599](https://github.com/umbraco/Umbraco-CMS/pull/23599), [#23727](https://github.com/umbraco/Umbraco-CMS/pull/23727), shipped in 17.7 and 18.2 |
| **[testcontainers/testcontainers-dotnet](https://github.com/testcontainers/testcontainers-dotnet)**<br><sub>★4.4k</sub> | MongoDB replica-set init was not idempotent, so a reused container hung against a one-hour timeout. [#1731](https://github.com/testcontainers/testcontainers-dotnet/pull/1731), [#1735](https://github.com/testcontainers/testcontainers-dotnet/pull/1735). A reused Couchbase container then stalled on the first step of configuring a cluster that was already configured. [#1736](https://github.com/testcontainers/testcontainers-dotnet/pull/1736). Confluent Platform 8.x images exited on startup because the module left a trailing comma in the advertised listeners, which Kafka 4 rejects. [#1772](https://github.com/testcontainers/testcontainers-dotnet/pull/1772) |
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
| **Independent client delivery** | Feature and defect delivery across established codebases, a high-throughput API gateway with 15+ third-party integrations, and third-line escalation on a platform with a large organisational customer base. Took a production application from .NET 8 to .NET 10 with its ORM and test framework, 651 tests passing. |

Modernisation is a thread through most of it: ASP.NET MVC and AngularJS onto current .NET with the business running throughout, VB6 rebuilt on ASP.NET Core, and a large Oracle schema moved to PostgreSQL behind a live application to remove the licensing cost.

Fully remote, across distributed teams in several time zones. Alongside the building: leading and mentoring developers, setting the standards the team codes against, running code review, technical discovery and estimation with stakeholders, and interviewing.

---

### barakoCMS

**[Open-source headless CMS for .NET](https://github.com/BaryoDev/barakoCMS).** Event-sourced on Marten and PostgreSQL, multi-tenant, user-defined content schemas, 13 opt-in modules, an event-triggered workflow engine, and a Next.js admin UI.

127 endpoints and 2,284 tests, run against real PostgreSQL and MinIO through Testcontainers. On .NET 10 and Marten 9. MPL-2.0, and every module is included rather than sold separately.

**4.0.0 shipped in September 2026** to NuGet, GHCR and Docker Hub: four auth and file-access holes closed, GDPR erasure, tenancy resolved from a domain, content references, multi-architecture non-root images, an SBOM, and a WCAG pass.

The claims are gates rather than sentences. CI restores a backup, upgrades a 3.x database, applies the Kubernetes manifests, generates the SBOM, scaffolds a module from the template and builds it, resolves every compose file, and refuses an image tag that is amd64-only.

**Live** at [playground.baryo.dev/barakocms](https://playground.baryo.dev/barakocms). **Console:** [barakoBrew](https://github.com/BaryoDev/barakoBrew), for designing content types, roles, workflows and integrations against the API. **Typed client:** [barako-client](https://github.com/BaryoDev/barako-client). [baryo.dev](https://baryo.dev) itself is rendered from it.

---

### Running agents over a backlog

**[lean-agent-method](https://github.com/arnelirobles/lean-agent-method).** How I put AI coding agents through a real ticket backlog without burning a month of plan in one night, plus the script that measures cost per change.

A cheaper model drafts every change. Scripts, not instructions, run the mechanical checks. A cheap critic reviews every change against six fixed questions, and the expensive model only sees what the critic cannot close. At most four changes in flight.

That took me from roughly **66 dollars of model use per change to about 25**, with no drop in what got caught. Those are my numbers, at list prices, on one .NET codebase, so treat them as a shape rather than a benchmark. The method and the measuring script are both in the repo.

---

### Security review

Proactive secure code review against the OWASP Top 10: read the code and config, find what an attacker would find, hand back a ranked fix list before anyone exploits it. Static-first, verified with read-only checks, no live offensive testing. The point is to close the holes ahead of the pen test, not to stage the attack.

<details>
<summary>What I look for, and what you get back</summary>

What I look for: broken access control and IDOR (an id from the URL used to load or mutate another user's object with no ownership check), authorization mistaken for authentication (a logged-in check where an owner-or-admin check belonged), privilege escalation on write paths, ownership checks that run after the mutation instead of before, unauthenticated reads of private data, committed secrets and long-lived tokens, open redirects in login flows, and stored or reflected XSS from unsanitised user content.

The deliverable is the report: each finding with where it is, what an attacker does with it, and the specific fix, ranked worst first, and an honest account of what was already secured. The same discipline as the rest of my work applies here: a finding I cannot trace to a concrete failure does not go in the report.

</details>

---

### Libraries and tooling

30 public repositories under [@BaryoDev](https://github.com/BaryoDev). Each solves one problem, ships to a package registry, and is tested rather than described.

#### .NET

| Project | What it does |
|---|---|
| **[Verdict](https://github.com/BaryoDev/Verdict)** | Result pattern with a zero-allocation core, eight packages. The allocation promise is the product, so it is enforced by benchmark rather than asserted in a README: 0 B and 0 collections measured over 1.6M operations on 8 threads. |
| **[Mapsicle](https://github.com/BaryoDev/Mapsicle)** | Object mapping, thirteen packages at 2.2.0, one test project per integration. Benchmarked on x64 and arm64 against AutoMapper and Mapperly, and the published numbers say where it loses as well as where it wins. |
| **[Carom](https://github.com/BaryoDev/Carom)** | Resilience: retry, timeout, circuit breaker, bulkhead, rate limiting, fallback, hedging. Zero dependencies in the core, netstandard2.0 upward, seven packages, 503 tests run against both .NET 8 and .NET 10. |
| **[Talaan](https://github.com/BaryoDev/Talaan)** | Spreadsheet and CSV reader, xlsx and CSV, zero dependencies. barakoCMS consumes it as a published package rather than a project reference, so the packaging is exercised for real. |

#### Umbraco

| Project | What it does |
|---|---|
| **[umbraco-pwa](https://github.com/BaryoDev/umbraco-pwa)** | Turns an Umbraco site into an installable, offline-capable app. On the Umbraco Marketplace, 0.5.0 on NuGet. |
| **[umbraco-read-aloud](https://github.com/BaryoDev/umbraco-read-aloud)** | Read-aloud for an Umbraco site using Microsoft Edge neural TTS. |

#### TypeScript and JavaScript

| Project | What it does |
|---|---|
| **[rnxjs](https://github.com/BaryoDev/rnxjs)** | Reactive UI framework. Bootstrap-native, no build step. Suite green on every pull request after four URL-sanitisation fixes and a CI gate that could not fail before. [Worked examples](https://github.com/BaryoDev/rnxJS_samples). |
| **[Kapehan](https://github.com/BaryoDev/Kapehan)** | 42 hand-drawn coffee icons, MIT, plus a token-driven component sheet. The full-colour and `currentColor` mono builds come from the same geometry rather than being drawn twice. The CSS styles 34 component families against a 30-component manifest, and `npm test` asserts both counts and fails if either side gains an orphan. [Browse the set](https://baryodev.github.io/Kapehan/). |
| **[rnxORM](https://github.com/BaryoDev/rnxORM)** | Node.js ORM, integration-tested against PostgreSQL, SQL Server and MariaDB rather than mocked. |
| **[pwa-kit](https://github.com/BaryoDev/pwa-kit)** | Install prompt for Android and iOS, a network-first service worker, and the helpers around them. |
| **[read-aloud](https://github.com/BaryoDev/read-aloud)** | Read-aloud for any site. Headless controller, web component, word highlighting. |
| **[feed-slurp](https://github.com/BaryoDev/feed-slurp)** | RSS and Atom fetching in the browser. |
| **[dopaminejs](https://github.com/BaryoDev/dopaminejs)** | Game feel engine: juice, rewards and feedback for HTML5 games. [Built with it](https://github.com/BaryoDev/dopa-dopa). |
| **[BaryoDev.Libraries.JavaScript](https://github.com/BaryoDev/BaryoDev.Libraries.JavaScript)** | Zero-dependency TypeScript utilities on npm. |

#### Go

| Project | What it does |
|---|---|
| **[BaryoVM](https://github.com/BaryoDev/BaryoVM)** | PaaS-style deploys onto your own cheap VMs. Agentless, over SSH, one binary. Every BaryoDev deploy goes through it, which is how its gaps get found. |
| **[Baryo.CLI](https://github.com/BaryoDev/Baryo.CLI)** | Local AI chat on Docker Model Runner. Models run on your machine, no API keys, nothing leaves the laptop. |

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

---

### Beyond the code

Work that isn't writing the code, but decides whether the code was worth writing.

<details>
<summary>Triage, write-ups, reports, and working on systems that aren't mine</summary>

A review that turns up twenty findings is a triage problem before it is a fixing problem. I sort them by what is already exposed or hard to undo, act on those, and let the rest wait. Fixing them in the order they were found buries the one that mattered.

When something works twice I write down how, so it isn't luck the third time. barakoCMS ships a runbook for handing a project to a client, not just the product. The AI workflow has a script that measures cost per change, not a blog post about using AI.

The reports are the work as much as the commits are. My upstream bug reports got fixed by other people because they carried enough to act on. My writing is mostly postmortems of my own mistakes. When you hand someone a report instead of a patch, whether they can act on it is the only thing that counts.

Some of this touches systems and data that aren't mine. I stay inside what I'm authorised to do, read before I probe, and keep client specifics out of anything public. That is not politeness. It is why there is a next engagement.

</details>

---

### Stack

| Area | Tools and practice |
|---|---|
| **Languages** | C#, TypeScript, JavaScript, Go, SQL, Python for tooling |
| **Architecture** | Event sourcing and projections, multi-tenancy (conjoined and database-per-tenant), modular monoliths over plugin runtimes, API contracts and versioning, licensing and one-way-door calls |
| **Backend** | .NET Framework to .NET 10, ASP.NET Core and MVC, REST and GraphQL, EF Core and LINQ, microservices, event-driven and domain-driven design, CQRS-influenced design |
| **Messaging** | RabbitMQ, SQS, SNS, webhooks, background jobs |
| **Data** | PostgreSQL, SQL Server and Azure SQL, Marten, Redis, Oracle, DB2, star schema modelling, execution plan analysis and query tuning, SSIS and SSRS |
| **Cloud and delivery** | AWS (CDK, ECS, Fargate, SQS, SNS), Azure (Functions, App Services, Storage, SQL, DevOps), Oracle Cloud, Docker, Kubernetes, GitHub Actions, Octopus Deploy, OpenTelemetry, Sentry, SBOM |
| **Frontend** | React, Next.js, Angular, TypeScript, Razor, accessibility to WCAG |
| **Testing** | xUnit, NUnit, Moq, Testcontainers, Playwright, Vitest, BenchmarkDotNet, test-driven development, mutation testing, security scanning in CI |
| **Security** | OWASP Top 10 and CWE secure code review, access-control and IDOR analysis, OAuth 2.0, OIDC and JWT, secrets and dependency auditing, static-first with read-only verification |

---

📫 [arnelirobles@gmail.com](mailto:arnelirobles@gmail.com) · 🌐 [baryo.dev](https://baryo.dev) · ✍️ [baryodev.medium.com](https://baryodev.medium.com)
