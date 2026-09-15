# Layout packs

Default layout is the screenshot structure. That is free. Do not invent a pack to describe it.

## Cap

- At most one alternate pack per *page type* (landing, study, product).
- Do not ship `pages × themes × layouts` as a promise.

## Allowed

- Change wrap, flex-direction, grid columns, and `order` on named regions.
- Hide or show regions marked `data-slot="optional"`.
- Density only through existing TUNE tokens (`--space-gutter`, stack), not new magic numbers.

## Forbidden

- New copy or a second DOM.
- Palette or type-face changes.
- Removing the only h1 or the only primary CTA.

## Switch

```html
<html data-theme="default" data-layout="default">
```

```css
@layer layout {
  :root[data-layout="stack"] #hero { }
}
```

## Test

- Semantics once per page (themes and packs must not change the heading tree).
- Visual: default theme + default layout vs `source.png`.
- Each extra theme on default layout — contrast on ink over surface and over hero overlay.
- Each extra pack on default theme — h1 and CTA still visible.
- Full cross only for `#hero` and the primary button.
