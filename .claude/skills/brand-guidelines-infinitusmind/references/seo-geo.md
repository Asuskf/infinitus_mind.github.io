# SEO, SEM y GEO — lo que ya está implementado y no se debe romper

Estado al 2026-10-08. Todo cambio visual debe preservar estos puntos.

## Head (`index.html`)
- `lang="es"`, `<title>` ≤ 60 caracteres, `meta description` ≤ 155 caracteres.
- `canonical`, `hreflang` (`es`, `x-default`) → `https://infinitusmind.com/`.
- `robots` con `max-image-preview:large`.
- Open Graph + Twitter Card con `assets/img/og-image.jpg` (1200×630).
- Íconos: `Icono.ico`, `icon-192.png`, `apple-touch-icon.png`, `site.webmanifest`.
- `preconnect` a Google Fonts/jsDelivr, `preload` del fondo del hero, scripts con `defer`.

## Datos estructurados (JSON-LD `@graph`)
`Organization` · `WebSite` · `WebPage` · `VideoGame` ("Un día en el zoo") · `Service` con
`OfferCatalog` (3 servicios) · `FAQPage` (6 preguntas, **idénticas** a la sección visible `#faq`).
- Nuevo juego → agregar `VideoGame`. Nuevo servicio → agregar `Offer`. Nueva FAQ → agregarla
  en el HTML **y** en el JSON-LD con el mismo texto.
- Validar: `python -c` con `json.loads` del bloque, y en https://validator.schema.org.
- Actualizar `WebPage.dateModified` en cada cambio de contenido.

## Estructura semántica
- Un `<h1>` (hero). `<h2>` por sección, `<h3>` para subelementos (juegos, preguntas).
- `<main>`, `<nav aria-label>`, `<footer>`, secciones con `aria-labelledby`.
- Texto que está dentro de imágenes (rueda de competencias, cerebro) se repite como texto
  (FAQ / `figcaption`) para buscadores e IA.

## Rendimiento (Core Web Vitals)
- Imágenes WebP (~1.9 MB total vs 35 MB originales), `width`/`height`, `loading="lazy"`.
- LCP: fondo del hero (`header-bg.webp`, precargado).
- No volver a referenciar los PNG originales pesados (`04.png` 14.8 MB, etc.).

## GEO (motores generativos)
- `llms.txt` en la raíz: resumen factual de la marca, servicios, competencias, juegos y contacto.
  Actualizarlo cuando cambie la oferta.
- `robots.txt` permite GPTBot, OAI-SearchBot, ClaudeBot, PerplexityBot, Google-Extended,
  Applebot-Extended, etc.
- Redactar respuestas cortas, factuales y autocontenidas (citables): "Infinitus Mind es…".

## Archivos raíz
`robots.txt` · `sitemap.xml` (con imágenes; actualizar `lastmod`) · `llms.txt` ·
`site.webmanifest` · `CNAME` (`infinitusmind.com` — no tocar).

## SEM — pendiente (requiere al cliente)
- GA4 + Google Ads tag (IDs del cliente), conversión en clic de "Enviar mensaje".
- Google Search Console + Bing Webmaster Tools, enviar `sitemap.xml`.
- Páginas reales de Política de privacidad y Términos (hoy `#!`).
