---
name: brand-guidelines-infinitusmind
description: >
  Identidad visual oficial de Infinitus Mind (videojuegos para evaluar y desarrollar habilidades
  blandas / soft skills) para ESTE repositorio: paleta "Mind / Play / Holograma" sobre Void Black,
  degradados de firma, tipografía Montserrat + Roboto, logo, mascota Gummy, layout, accesibilidad
  y SEO/GEO. Úsala siempre que crees, edites o revises cualquier cosa visual de Infinitus Mind:
  secciones nuevas de la landing (index.html, css/styles.css), páginas, banners, posts para redes,
  presentaciones, PDFs, imágenes OG, emails o mockups — aunque no digan "marca". También para
  "¿esto está on-brand?", "arregla los colores", "pon el logo", "revisa el diseño", "que se vea
  menos genérico", auditorías de UI/accesibilidad (lente de diseño estilo Apple HIG) y cualquier
  cambio que deba conservar el SEO de la página.
---

# Infinitus Mind — Brand Guidelines

> **Versión** 1.0 · **Actualizado** 2026-10-08 · **Alcance** este repositorio
> (`infinitusmind.com`, GitHub Pages) · Historial en `CHANGELOG.md`.
>
> Estructura basada en la skill `brand-guidelines-kin` (Kin Analytics) y lente de revisión
> basada en `dickwu/apple-design-skill`. La identidad se **derivó del sitio en producción**
> (`css/styles.css`, `assets/img/`), no se inventó: cada color y tamaño de abajo existe hoy
> en la web.

## AUTORIDAD DE ARCHIVOS

**Nivel 1 — canónico**
- `SKILL.md` — reglas vinculantes (este archivo).
- `assets/tokens/colors_and_type.css` — fuente única de color, tipografía, espaciado y radios.
- `assets/logos/`, `assets/mascots/`, `assets/fonts/` — arte oficial.
- `references/*.md` — implementación por formato y lentes de revisión.

**Nivel 2 — generado (no editar a mano; regenerar)**
- `assets/palette/palette.json`, `assets/palette/palette.png`,
  `assets/quick-reference/InfinitusMind_Brand_Cheatsheet.html` → salen de
  `python assets/quick-reference/build_cheatsheet.py` (ejecutar desde el directorio de la skill).

## ADHERENCIA — reglas duras (cada violación bloquea)

1. **Colores solo desde tokens.** En código nuevo usa `var(--im-…)`. El `css/styles.css`
   heredado (Bootstrap 5 + tema Agency) tiene hex literales: **no los multipliques**; si tocas
   una regla, migra ese valor a su token. Si un color no existe en la paleta, **detente y avisa**.
2. **Nada de colores nuevos.** La paleta tiene 21 valores. No agregues "uno parecido".
3. **Logo solo desde archivo** (`assets/logos/`), como `<img>` con `alt="Infinitus Mind"` y
   `width`/`height`. Nunca redibujarlo, tipearlo en Montserrat, recolorearlo ni deformarlo. El
   wordmark oficial es **blanco**: solo va sobre fondos oscuros. Si un fondo claro necesita logo
   y no hay archivo oscuro, **deja el espacio vacío y avisa**.
4. **Fondo del sitio = Void Black `#0A090F`.** La marca es oscura por naturaleza. El modo claro
   existe solo para documentos/print (`[data-theme="light"]`).
5. **Accesibilidad no negociable** (WCAG 2.2 AA, ver §07): texto ≥ 4.5:1, texto grande ≥ 3:1,
   objetivos táctiles ≥ 44×44 px, foco visible, `prefers-reduced-motion` respetado.
6. **No romper el SEO/GEO** ya implementado (ver `references/seo-geo.md`): un solo `<h1>`,
   `alt` descriptivo, imágenes WebP con `width`/`height` + `loading="lazy"`, JSON-LD válido,
   `lang="es"`. Toda sección nueva se refleja en `sitemap.xml`/`llms.txt`/JSON-LD si cambia
   la oferta.

## Esencia de marca

**Infinitus Mind** crea videojuegos y experiencias de realidad virtual que **evalúan y
desarrollan habilidades blandas** en adultos, adolescentes y niños, combinando juego,
neurociencia, psicología, neuroeducación e IA. Propósito: *"Ayudamos a construir sociedades
más competitivas, justas e inclusivas."*

**Tesis visual (una frase):** *una mente que brilla en la oscuridad* — fondo casi negro donde
la ciencia (azules fríos, "Mind") y el juego (cálidos, "Play") aparecen como luz: degradados
luminosos, hologramas y una mascota amable.

**Lo que la hace memorable (firma):** los **títulos en degradado luminoso** sobre Void Black
+ **Gummy**, la mascota con cúpula de cristal y el símbolo ∞-cerebro brillando dentro.

Atributos: lúdica · científica · luminosa · cercana · optimista. Nunca infantil-chillona ni
corporativa-fría.

---

## 01 — Logo

| Archivo | Qué es | Uso |
|---|---|---|
| `assets/logos/infinitusmind-wordmark-white.svg` | Wordmark horizontal "InfinitusMind" + símbolo, blanco (viewBox 1060×247) | Navbar, footers, portadas, OG — **solo sobre oscuro** |
| `assets/logos/infinitusmind-symbol-256.png` · `-192.png` · `.ico` | Símbolo ∞-cerebro blanco, transparente | Favicon, avatar, app icon, JSON-LD `logo` |

- **Espacio de respeto:** mínimo la altura del símbolo alrededor del logo.
- **Tamaño mínimo:** wordmark 120 px de ancho en pantalla; por debajo usa el símbolo.
- **Fondos permitidos:** Void `#0A090F`, Night `#000000`, Deep Ink `#18243B`, Cobalt/Violet
  sólidos, fotos/arte oscurecidos con velo ≥ 60 %.
- **Prohibido:** estirar, rotar, contorno, sombra de color, recolorear, ponerlo sobre degradados
  claros (Holo, Sun) o sobre arte del juego sin velo.
- En HTML, el SVG trae `.cls-1` en un `<style>` interno: **no lo inlines** (las clases se filtran
  al documento); úsalo como `<img src>` o data-URI.

## 02 — Paleta

Valores y contraste completos en `assets/palette/palette.json`; tablero visual en
`assets/palette/palette.png`.

| Grupo | Nombre | Hex | Token | Contraste sobre Void | Rol |
|---|---|---|---|---|---|
| Base | Void Black | `#0A090F` | `--im-void` | — | Fondo de página |
| Base | Night | `#000000` | `--im-night` | — | Navbar / chrome |
| Base | Deep Ink | `#18243B` | `--im-ink-blue` | 1.3:1 (blanco encima 15.5:1) | Tarjetas sobre oscuro |
| Base | White | `#FFFFFF` | `--im-white` | 19.8:1 | Texto principal |
| Mind | Neuro Aqua | `#53F7E0` | `--im-aqua` | 14.9:1 | Inicio de degradado Mind, foco |
| Mind | Synapse Sky | `#29A1E8` | `--im-sky` | 6.9:1 | Degradado Mind |
| Mind | Cobalt | `#004CEF` | `--im-cobalt` | 3.1:1 ⚠ solo grande | Fin de degradado Mind |
| Mind | Signal Cyan | `#00C0FF` | `--im-cyan` | 9.4:1 | Enlaces, inicio CTA |
| Mind | Royal Blue | `#3B68E3` | `--im-royal` | 4.0:1 ⚠ solo grande | Discos de íconos |
| Mind | Infinite Violet | `#5640D6` | `--im-violet` | 2.9:1 ⛔ no texto | Fin de CTA / íconos |
| Mind | Cerulean | `#09A4DE` | `--im-cerulean` | 7.0:1 | `--bs-primary` |
| Play | Zoo Sun | `#FCC612` | `--im-sun` | 12.5:1 | Títulos de juego |
| Play | Ember | `#ED5735` | `--im-ember` | 5.7:1 | Títulos de servicio |
| Play | Coral | `#EB5151` | `--im-coral` | 5.5:1 | Títulos juego/servicio |
| Play | Gummy Rose | `#E84A75` | `--im-rose` | 5.4:1 | Mascota, acentos cálidos |
| Holo | Holo Blue | `#61C9EA` | `--im-holo-blue` | 10.4:1 | Banda de contacto |
| Holo | Holo Mist | `#7FBCEC` | `--im-holo-mist` | 9.7:1 | Banda de contacto |
| Holo | Holo Lilac | `#D598F2` | `--im-holo-lilac` | 9.1:1 | Banda de contacto |
| Neutro | Gray 300 | `#CED4DA` | `--im-gray-300` | 13.3:1 | Bordes en claro |
| Neutro | Gray 500 | `#ADB5BD` | `--im-gray-500` | 9.6:1 | Texto secundario |
| Neutro | Gray 600 | `#6C757D` | `--im-gray-600` | 4.2:1 ⚠ solo grande | Meta / deshabilitado |

### Proporción
- **~70 % Void/Night** · **~20 % blanco/gris** (texto) · **~10 % luz de marca** (degradados,
  CTA, íconos, mascota). La luz es escasa: por eso brilla.
- **Mind** (fríos) = conocimiento, evaluación, ciencia → títulos de sección, navegación, CTA.
- **Play** (cálidos) = juego, emoción, servicios → títulos de juegos y de servicios.
- **Holograma** (pastel) = cierre / contacto / momentos humanos. Un bloque por página.
- No mezcles Mind y Play en el mismo título. Una sección = una familia.

### Degradados de firma (tokens `--im-grad-*`)

| Token | Composición | Dónde |
|---|---|---|
| `--im-grad-mind` | 45° Aqua 20 % → Sky 60 % → Cobalt 80 % | `h2.section-heading` (texto recortado) |
| `--im-grad-play` | 45° Sun → Coral → Rose | Títulos de juego (`.title_zoo`) |
| `--im-grad-heart` | 45° Ember / Coral / Rose | Títulos de servicio (`.title_service`) |
| `--im-grad-action-aa` | → Cobalt → Royal → Violet | Botón principal (`.btn-primary`), todo CTA con texto blanco |
| `--im-grad-action` | → Cyan → #1C96F2 → Violet | Solo piezas sin texto encima (falla contraste con blanco) |
| `--im-grad-icon` | 90° Cyan → Royal → Violet | Discos de íconos (`.spam-fa-circle`) |
| `--im-grad-holo` | 90° Holo Blue → Mist → Lilac | Fondo de `#contact` |
| `--im-grad-zoo-veil` | velo púrpura-negro 270° | Texto sobre arte de juego |

**Reglas de degradado:** solo en títulos ≥ 24 px, CTA, discos de íconos y una banda de fondo.
Nunca en párrafos, nunca en el logo, nunca dos degradados de fondo en la misma vista.

### Contraste — corregido en el sitio (2026-10-08)
Bloque "Correcciones de contraste WCAG 2.2 AA" al final de `css/styles.css`:
- **CTA:** el degradado original Cyan→Violet daba 2.1:1 con texto blanco. El botón usa ahora
  `--im-grad-action-aa` = Cobalt → Royal → Violet (blanco ≥ 4.9:1). **Todo CTA con texto
  blanco usa esta versión**; `--im-grad-action` (con cian) queda solo para piezas sin texto.
- **Contacto:** texto sobre `--im-grad-holo` en Void `#0A090F` (≥ 9:1), nunca blanco.
- **Footer:** texto Gray 500 (9.6:1) y enlaces blancos subrayados (antes 1.3:1).
- **Botones sociales:** 44×44 px; foco visible con anillo Aqua de 3 px.

## 03 — Tipografía

| Rol | Fuente | Pesos | Notas |
|---|---|---|---|
| Display, títulos, navegación, botones, eyebrows | **Montserrat** | 400, 700 | Títulos en MAYÚSCULAS; variable 100–900 disponible |
| Cuerpo, subtítulos, descripciones, kicker del hero | **Roboto** | 400, 700 | Variable `wght` 100–900, `wdth` 75–100 |

Escala (desde el sitio): Display sección 4rem (2.5rem móvil, degradado, MAYÚS.) · Hero H1
3.25rem / 2.25rem · Título de juego 3rem · Título de tarjeta 2rem · Lead 1.5rem · Botón
1.125rem Bold MAYÚS. · Cuerpo 1rem (mín. 16 px) · interlineado 1.5 cuerpo / 1.2 títulos.

- Dos familias. Nada de una tercera.
- No uses pesos 100–300 por debajo de 24 px (legibilidad sobre fondo oscuro).
- Archivos locales en `assets/fonts/` (TTF variable para Office/Pillow; `*-latin.woff2` para
  web/PDF). Licencias OFL junto a las fuentes: deben viajar con ellas.
- La web hoy carga Montserrat + Roboto desde Google Fonts con `display=swap` y `preconnect`;
  es aceptable en el sitio. En piezas autocontenidas (PDF, HTML para compartir), incrusta las
  woff2 locales.

## 04 — Mascota e imágenes

**Gummy** (`assets/mascots/`) es la mascota: un personaje redondo con cúpula de cristal y el
símbolo ∞-cerebro luminoso dentro.
- `gummy-puzzle.webp`: rosa, armando un rompecabezas (aprendizaje); `gummy-hologram.webp`:
  versión holográfica cian saludando (contacto, bienvenida).
- `symbol-glow.webp` (símbolo con brillo) y `purpose-ring.webp` (anillos de propósito) son
  apoyos decorativos: `alt=""` + `role="presentation"`.
- Máximo **una aparición de Gummy por sección**; nunca deformarlo, recortarle la cúpula ni
  cambiarle el color fuera de sus dos versiones.
- Arte de juego (capturas tipo "Un día en el zoo"): ilustración 3D colorida; si lleva texto
  encima, aplica `--im-grad-zoo-veil`.
- Fotografía: personas reales usando VR/juegos, iluminación fría azul (como `header-bg`).
  Sin fotos de stock genéricas de oficina.
- Formato: **WebP**, máx. 2× el tamaño mostrado, con `width`/`height`; OG en JPG 1200×630.

## 05 — Iconografía

- Font Awesome 5 Free (ya en el sitio), estilo sólido, blanco (`fa-inverse`) dentro de un
  **disco** de 124 px con `--im-grad-icon`.
- Íconos decorativos: `aria-hidden="true"`. Botones de solo ícono: `aria-label` en español
  (ej. "Instagram de Infinitus Mind").
- Un solo set de íconos. No mezclar Font Awesome con otros.

## 06 — Layout y componentes

- **Contenedor:** Bootstrap `.container`; secciones `.page-section` con 6rem de padding
  vertical. Ritmo: título de sección centrado → subtítulo → contenido.
- **Radios:** tarjeta 10 px · media 20 px · botón pill 100 px · disco 50 %.
- **Botón principal:** `.btn.btn-primary.btn-xl.text-uppercase`; un solo CTA principal por
  vista; hover = opacidad 0.8.
- **Botones sociales:** círculo blanco 44 px (`.btn-light.btn-social`), objetivo táctil mínimo.
- **Tarjeta de servicio:** disco de ícono + marco blanco superior (`.border-icon`) + título
  `--im-grad-heart` + párrafo blanco.
- **Navegación:** barra negra fija, enlaces en MAYÚSCULAS Montserrat, se compacta al hacer
  scroll; un ítem por sección (`#nosotros`, `#about`, `#portfolio`, `#service`, `#proposito`,
  `#contact`, `#faq`).
- **Orden canónico de la landing:** Hero → ¿Qué hacemos? (+juegos) → ¿Qué ofrecemos? →
  ¿Qué evaluamos? → ¿Cómo lo hacemos? → Servicio → Propósito → FAQ → Contacto → Footer.
- Implementación y snippets: `references/web-html.md`.

## 07 — Revisión de diseño (lente Apple HIG adaptada a web)

Toda revisión o pieza nueva pasa por las **cinco lentes** de `references/apple-design-lens.md`,
en orden: **1 Accesibilidad** (fallas = Críticas) → **2 Convenciones de plataforma web** →
**3 Visual y craft** → **4 Interacción** → **5 Contenido y redacción**. Reglas de oro:
- **Números, no adjetivos:** "Gray 600 16 px sobre Void = 4.2:1 < 4.5:1", no "se ve tenue".
- **La audacia se gasta en un solo lugar** por vista: el degradado del título o Gummy o la
  banda Holo, no los tres compitiendo.
- **Quita un accesorio:** antes de entregar, pregunta qué se puede eliminar sin pérdida.
- **No aplanes la personalidad:** las correcciones no deben dejar la página como plantilla
  genérica; la firma (degradado luminoso + Gummy) se conserva.

## 08 — Voz visual por formato

| Formato | Regla |
|---|---|
| Landing / web | Esta skill + `references/web-html.md` + `references/seo-geo.md` |
| Post 1080×1350 / 1080×1080 | Fondo Void, un título con degradado, Gummy o captura de juego, logo blanco en una esquina con margen = altura del símbolo |
| OG / social card 1200×630 | Arte de juego o Gummy + velo; texto ≤ 6 palabras; logo blanco |
| Presentación 16:9 | Portada Void + título degradado Mind; contenido en Void con tarjetas Deep Ink; cierre con banda Holo y texto Void |
| PDF / documento | `[data-theme="light"]`; títulos Montserrat en Void; acentos de marca solo en filetes y números |
| Email | Fondo Void, CTA pill sólido Royal `#3B68E3` (sin degradado: los clientes de correo los rompen) |

## Referencia rápida

**Fondo** `#0A090F` · **Texto** `#FFFFFF` / `#ADB5BD`
**Mind** `#53F7E0` `#29A1E8` `#004CEF` `#00C0FF` `#3B68E3` `#5640D6` · **Play** `#FCC612` `#ED5735` `#EB5151` `#E84A75` · **Holo** `#61C9EA` `#7FBCEC` `#D598F2`
**Fuentes** Montserrat (títulos, MAYÚS.) · Roboto (cuerpo) · **Radios** 10 / 20 / pill
**Firma** título con degradado luminoso + Gummy · **Web** infinitusmind.com
**Contacto** infinitusmind@gmail.com

Hoja imprimible para todo el equipo: `assets/quick-reference/InfinitusMind_Brand_Cheatsheet.html`.
