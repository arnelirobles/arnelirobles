# Writes one HTML page per banner into art/html at 2x zoom. Screenshot each page at the
# printed size with a transparent background (Playwright omitBackground) into assets/.
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "html")
OUT = os.path.join(HERE, "..", "assets")
W = 1280

BASE = """<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=IBM+Plex+Mono:wght@500&display=block" rel="stylesheet">
<style>
:root{--ink:#1c2321;--body:#4d5552;--leaf:#0b7a55;--leaf-dark:#075a3e;--rust:#c2461a;--cream:#fff8e8;
--sun:#ffcd3c;--sun-soft:#ffe08a;--mint:#7cc4a4;--tangerine:#f08a24;--peach:#f6a99a;--coral:#e8755a;--line:#ece4d0}
*{box-sizing:border-box;margin:0;padding:0}
html{zoom:2}html,body{background:transparent;width:%(w)dpx;height:%(h)dpx;overflow:hidden}
body{font-family:'Plus Jakarta Sans',system-ui,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.card{position:absolute;inset:0;border-radius:28px;background:var(--cream);overflow:hidden}
.stripes{position:absolute;background:repeating-linear-gradient(135deg,var(--c,#ffcd3c) 0 3px,transparent 3px 11px)}
.dots{position:absolute;width:34px;height:34px;border-radius:50%%;background:repeating-linear-gradient(135deg,var(--c,#ffcd3c) 0 3px,transparent 3px 7px)}
.eyebrow{font-size:15px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--rust)}
.pill{position:absolute;font-weight:700;font-size:22px;line-height:1.15;padding:13px 18px;color:var(--ink)}
</style></head><body>%(body)s</body></html>"""

HERO = """
<div class="card">
  <div style="position:absolute;left:-110px;top:-90px;width:300px;height:300px;border-radius:50%;background:var(--sun-soft)"></div>
  <div class="dots" style="left:640px;top:58px"></div>
  <div class="dots" style="left:600px;top:478px;--c:#e8755a;width:26px;height:26px"></div>
  <div style="position:absolute;left:64px;top:92px;width:640px">
    <div style="font-size:24px;font-weight:700;color:var(--leaf);letter-spacing:-.01em">Arnel Robles · Software developer &amp; consultant</div>
    <div style="margin-top:14px;font-size:50px;line-height:1.08;font-weight:800;letter-spacing:-.025em">
      I design and build the <span style="color:var(--leaf)">systems a business runs on,</span> then keep them running.</div>
    <div style="margin-top:22px;font-size:19px;line-height:1.6;color:var(--body);max-width:560px">
      Fourteen years in production. Multi-tenant platforms, the data underneath them, the AI on top, and the audit that checks it all holds.</div>
  </div>
  <div style="position:absolute;left:800px;top:70px;width:400px;height:380px;border-radius:58% 42% 52% 48%/46% 54% 46% 54%;background:var(--mint)"></div>
  <div class="stripes" style="left:1040px;top:300px;width:170px;height:150px;border-radius:30px"></div>
  <img src="../fox.webp" style="position:absolute;left:830px;top:80px;width:340px;height:340px">
  <div class="pill" style="left:740px;top:90px;background:var(--tangerine);border-radius:14px 14px 14px 4px;box-shadow:0 10px 24px rgba(240,138,36,.28)">.NET 10</div>
  <div class="pill" style="left:1060px;top:230px;background:var(--peach);border-radius:14px 14px 4px 14px;box-shadow:0 10px 24px rgba(246,169,154,.35)">PostgreSQL</div>
  <div class="pill" style="left:770px;top:400px;background:#fff;color:var(--leaf);font-size:20px;padding:12px 18px;border-radius:14px 14px 4px 14px;box-shadow:0 10px 24px rgba(28,35,33,.12)">LLM &amp; agents</div>
</div>"""

SECTION = """
<div class="card">
  <div class="dots" style="left:%(dx)dpx;top:%(dy)dpx;--c:%(dc)s"></div>
  <div class="stripes" style="right:-20px;bottom:-30px;width:150px;height:90px;border-radius:24px;--c:%(sc)s;opacity:.9"></div>
  <div style="position:absolute;left:64px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
    <div class="eyebrow">%(eyebrow)s</div>
    <div style="margin-top:8px;font-size:40px;line-height:1.15;font-weight:800;letter-spacing:-.02em">%(title)s</div>
  </div>
</div>"""

STATS = [("14", "years in production"), ("15", "changes merged upstream"),
         ("8", "accepted bug reports"), ("31", "public repos at BaryoDev")]

STATS_HTML = """
<div class="card" style="background:var(--leaf-dark)">
  <div class="stripes" style="right:-30px;bottom:-40px;width:160px;height:80px;border-radius:24px;opacity:.45"></div>
  <div style="position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);align-items:center;padding:0 40px">
  %s
  </div>
</div>""" % "".join(
    '<div style="text-align:center;color:#fff"><div style="font-size:54px;font-weight:800;letter-spacing:-.03em;color:var(--sun)">%s</div>'
    '<div style="margin-top:4px;font-size:17px;font-weight:600;opacity:.92">%s</div></div>' % s for s in STATS)

CONTACT = """
<div class="card">
  <div style="position:absolute;right:-70px;top:-80px;width:240px;height:240px;border-radius:50%;background:var(--sun-soft)"></div>
  <div class="dots" style="left:640px;top:28px;--c:#e8755a"></div>
  <div style="position:absolute;left:64px;top:0;bottom:0;display:flex;flex-direction:column;justify-content:center">
    <div style="font-size:34px;font-weight:800;letter-spacing:-.02em">Have something that has to last?</div>
    <div style="margin-top:8px;font-size:19px;color:var(--body)">Email me, or book a call on baryo.dev.</div>
  </div>
  <div style="position:absolute;right:120px;top:50%;transform:translateY(-50%);background:var(--leaf);color:#fff;font-weight:700;font-size:19px;padding:18px 30px;border-radius:999px">arnelirobles@gmail.com</div>
</div>"""

ACCENTS = [("#ffcd3c", "#7cc4a4"), ("#e8755a", "#ffcd3c"), ("#7cc4a4", "#f6a99a"), ("#f08a24", "#7cc4a4")]

SECTIONS = [
    ("platform", "Platform", "The platform I design and run"),
    ("agents", "LLM and agents", "LLM and agent systems"),
    ("security", "Security", "Security audits"),
    ("upstream", "Upstream", "Open source contributor"),
    ("client", "Client work", "What I have built for other people"),
    ("libraries", "Libraries", "Libraries and tools"),
    ("writing", "Writing", "Things I have written"),
    ("how", "Practice", "How I work"),
    ("stack", "Stack", "What I work with"),
]


def render(name, w, h, body):
    path = os.path.join(HTML, name + ".html")
    with open(path, "w") as f:
        f.write(BASE % {"w": w, "h": h, "body": body})
    print(name, w * 2, h * 2)


os.makedirs(HTML, exist_ok=True)
only = set(sys.argv[1:])
jobs = [("hero", 540, HERO), ("stats", 170, STATS_HTML), ("contact", 170, CONTACT)]
for i, (key, eb, title) in enumerate(SECTIONS):
    dc, sc = ACCENTS[i % len(ACCENTS)]
    jobs.append(("section-" + key, 150, SECTION % {"eyebrow": eb, "title": title,
                 "dx": 980 - (i % 3) * 140, "dy": 30 + (i % 2) * 70, "dc": dc, "sc": sc}))
for name, h, body in jobs:
    if not only or name in only:
        render(name, W, h, body)
