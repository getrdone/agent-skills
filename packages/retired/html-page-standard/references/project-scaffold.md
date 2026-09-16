# Project scaffold

Create this tree at the start of Pass A or Pass B.

```text
<page-slug>/
  source.png          # visual contract (original screenshot)
  clone.html          # Pass A output, never overwrite after B/C
  core.css            # TUNE + containers + component rules
  theme-default.css   # palette
  index.html          # Pass C living page
```

Link order in `index.html`:

```html
<link rel="stylesheet" href="core.css">
<link rel="stylesheet" href="theme-default.css">
<!-- optional -->
<link rel="stylesheet" href="layout-stack.css">
```

Root:

```html
<html lang="en" data-theme="default" data-layout="default">
```

Region markup (Pass C):

```html
<section id="hero" data-region="hero" aria-labelledby="hero-title">
  <h1 id="hero-title">…</h1>
</section>
```

Keep `clone.html` as the pixel contract. Repair edits `index.html`.
