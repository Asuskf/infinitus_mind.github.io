# Web / HTML — implementación para este repositorio

El sitio es una landing estática (GitHub Pages, dominio en `CNAME`) construida sobre
**Bootstrap 5.1.3 + tema Start Bootstrap Agency**: `index.html`, `css/styles.css` (≈11 900
líneas: Bootstrap compilado + overrides de marca desde ~línea 11300), `js/scripts.js`.

## 1. Usar los tokens en el sitio

Los tokens viven en la skill (`assets/tokens/colors_and_type.css`). Para usarlos en la web,
copia el bloque `:root` (sin los `@font-face`, el sitio ya carga Google Fonts) al **final** de
`css/styles.css` bajo un comentario `/* Infinitus Mind tokens */`, y escribe todo CSS nuevo con
`var(--im-…)`. No publiques la carpeta `.claude/` (Jekyll ignora carpetas con punto; no la
enlaces desde el HTML).

## 2. Patrones canónicos (copiar, no reinventar)

### Título de sección con degradado Mind
```html
<h2 class="section-heading text-uppercase" id="h-seccion">Título</h2>
```
El estilo ya existe (`.page-section h2.section-heading`). En componentes nuevos:
```css
.im-gradient-title {
  font-family: var(--im-font-display);
  font-weight: var(--im-weight-bold);
  text-transform: uppercase;
  background: var(--im-grad-mind);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: var(--im-aqua); /* fallback si no hay background-clip */
}
```
Variantes: `--im-grad-play` (juegos), `--im-grad-heart` (servicios).

### Subtítulo (párrafo con aspecto de h3, sin romper la jerarquía)
```html
<p class="section-subheading h3 text-muted">Texto de apoyo.</p>
```
Nunca uses `<h3>` solo por el tamaño: la jerarquía de encabezados es SEO (ver seo-geo.md).

### CTA principal
```html
<a class="btn btn-primary btn-xl text-uppercase" href="#contact">Quiero saber más</a>
```
Uno por vista (ya usa `--im-grad-action-aa`). Para piezas fuera del sitio:
```css
.im-cta { background: var(--im-grad-action-aa); border-radius: var(--im-radius-pill);
  color: var(--im-white); text-shadow: 0 1px 2px rgb(0 0 0 / .45);
  min-height: var(--im-tap-min); padding: 1.25rem 2.5rem; }
.im-cta:focus-visible { outline: 3px solid var(--im-color-focus); outline-offset: 3px; }
```

### Tarjeta de servicio
```html
<div class="col">
  <div class="text-center"><div class="border-icon">
    <div class="spam-fa-circle fa-stack fa-4x text-center">
      <i class="fas fa-award fa-stack-1x fa-inverse text-secondary" aria-hidden="true"></i>
    </div></div></div>
  <div class="content-service"><div class="title_service"><h4 class="my-3">Título</h4></div></div>
  <p class="text-muted2 p-service">Descripción.</p>
</div>
```
⚠ `css/styles.css` tiene una regla global `h4 { padding-top:10.5rem; background-image:… }`
heredada: **no agregues `<h4>` fuera de `.title_service`** o heredará ese fondo.

### Juego destacado (arte + velo + texto)
```html
<article class="zoo_day" aria-labelledby="h-juego">
  <div class="conten_zoo_day">
    <h3 class="title_zoo" id="h-juego">Nombre del juego</h3>
    <p class="conten_zoo_day_h3 h3 text-muted">Descripción breve con verbo de acción.</p>
  </div>
</article>
```
Para otro juego, duplica `.zoo_day` con un modificador que cambie solo `background-image`
(WebP), y añade su `VideoGame` al JSON-LD.

### Imágenes
```html
<img src="assets/img/nombre.webp" width="1200" height="800" loading="lazy" decoding="async"
     alt="Qué muestra y por qué importa">
```
- Primera imagen visible (hero): sin `lazy`, con `<link rel="preload">` si es LCP.
- Decorativas: `alt="" role="presentation"`.
- El CSS ya incluye `:where(img[width][height]) { height: auto; }` para que los atributos no
  deformen; las clases con altura fija (ej. `.img_game`) siguen ganando.
- Conversión: Pillow → WebP calidad 72–80, ancho ≤ 2× el mostrado.

### Logo
```html
<a class="navbar-brand" href="#page-top">
  <img src="assets/img/infinitus-mind.svg" alt="Infinitus Mind" width="1060" height="247">
</a>
```
`#mainNav .navbar-brand img { width: auto; }` mantiene la proporción.

## 3. Movimiento
- Transiciones existentes: 0.3s ease-in-out (navbar). Mantén ≤ 300 ms en interacciones
  frecuentes.
- Todo efecto nuevo dentro de `@media (prefers-reduced-motion: no-preference)`.
- Brillo/holograma: permitido como un momento (aparición de Gummy), nunca en bucle infinito
  detrás de texto.

## 4. Checklist antes de publicar
- [ ] Colores nuevos solo con `var(--im-…)`; ningún hex nuevo.
- [ ] Contraste calculado (texto ≥ 4.5:1, grande ≥ 3:1) y anotado en el PR.
- [ ] Un solo `<h1>`; secciones con `aria-labelledby`.
- [ ] Imágenes WebP con `width`/`height`/`alt`/`loading`.
- [ ] Probado a 375 px y 1280 px, sin scroll horizontal visible.
- [ ] Foco visible navegando con Tab.
- [ ] JSON-LD sigue siendo JSON válido; `sitemap.xml` `lastmod` actualizado.
