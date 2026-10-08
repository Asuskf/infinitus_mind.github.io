# Lente de revisión de diseño (adaptada de Apple HIG para la web de Infinitus Mind)

> Método destilado de **dickwu/apple-design-skill** (`SKILL.md`), que a su vez se basa en las
> Human Interface Guidelines de Apple. Aquí está **resumido con nuestras palabras y adaptado a
> una landing web**. No incluye el texto de las 123 páginas de la HIG (son contenido de Apple).
> Para revisar apps nativas o citar la HIG literal, instala la skill original (ver al final).

## Rol
Revisa con dos cabezas a la vez: **el auditor** que conoce las guías y mantiene el diseño
honesto, y **el director de estudio** que evita que se vea como cualquier plantilla. Cada
revisión lleva ambas.

## Los 8 principios (primer filtro)
| Principio | Pregunta para Infinitus Mind |
|---|---|
| Propósito | ¿Esta sección ayuda a entender que evaluamos y desarrollamos soft skills con juegos? |
| Agencia | ¿La persona puede explorar, saltar al contacto o volver arriba cuando quiera? |
| Responsabilidad | ¿Somos transparentes con datos, evaluaciones y contacto (privacidad, términos)? |
| Familiaridad | ¿Navegación, botones y formularios se comportan como la web espera? |
| Flexibilidad | ¿Funciona en 320–1920 px, con zoom 200 %, teclado y lector de pantalla? |
| Simplicidad | ¿Cada elemento se ganó su lugar? |
| Craft | Espaciado, alineación, redacción, animación: ¿está terminado? |
| Deleite | ¿Hay emoción (Gummy, la luz)? ¿Es la correcta? Deleite ≠ decoración. |

## Proceso

### Paso 1 — Contexto
Plataforma (web móvil/escritorio), audiencia (empresas, educadores, familias), artefacto
(captura, código, mockup — di qué puedes y no puedes verificar), **tesis de la pantalla en una
frase** y objetivo del usuario (auditoría completa, una duda puntual o una mejora).

### Paso 2 — Cinco lentes, en este orden

**Lente 1 · Accesibilidad (fallas = Crítico)**
- Texto escala con el zoom del navegador; a 200 % no se rompe la jerarquía.
- Tamaños: cuerpo ≥ 16 px; nada bajo 12 px. Evitar pesos 100–300 en texto pequeño sobre oscuro.
- Contraste: texto normal ≥ 4.5:1; texto ≥ 24 px o ≥ 18.66 px bold ≥ 3:1; UI/íconos ≥ 3:1.
  **Calcúlalo con los hex** (`assets/palette/palette.json`) y muestra la cifra.
- Objetivos táctiles ≥ 44×44 px, con espacio entre ellos.
- Nada se comunica solo con color. Todo botón de solo ícono tiene `aria-label`.
- Navegable con teclado; foco visible; orden lógico.
- Movimiento opcional (`prefers-reduced-motion`) y nunca el único portador de significado.

**Lente 2 · Convenciones web (fallas = Alto normalmente)**
- Navegación principal visible o en un menú hamburguesa estándar con `aria-expanded`.
- Enlaces parecen enlaces; botones hacen acciones; un CTA principal por vista.
- Anclas internas con `scroll-margin-top` suficiente para la navbar fija.
- Formularios: `label` real, tipo de input correcto, validación en vivo, mensajes claros.
- Enlaces externos con `target="_blank" rel="noopener"`.
- Modo oscuro nativo de la marca: no agregar un interruptor de tema en la web.

**Lente 3 · Visual y craft (Alto o Medio)**
- Un color significa una cosa: Mind = conocimiento/navegación, Play = juego/servicio,
  Holo = cierre humano.
- Pocas fuentes (2), escala clara; el peso y el tamaño llevan la jerarquía.
- Alineación y agrupamiento muestran estructura; divulgación progresiva (FAQ en `<details>`).
- Íconos de un solo lenguaje (Font Awesome sólido en disco degradado).
- **Lente de craft:**
  - ¿Tiene punto de vista? Debe recordarse por *la luz sobre la oscuridad + Gummy*.
  - ¿Es plantilla? Señales de alerta: negro con un único acento ácido sin razón; número gigante
    sobre etiqueta pequeña con degradado; marcadores 01/02/03 en contenido que no es secuencia.
  - ¿La estructura codifica información? Eyebrows, divisores y numeración deben decir algo
    cierto del contenido.
  - ¿La audacia se gasta en un solo lugar por vista?
  - **Quita un accesorio.** Si nada sobra, dilo.

**Lente 4 · Interacción (Medio normalmente)**
- Algo aparece de inmediato al cargar; las imágenes no empujan el layout (CLS ≈ 0).
- La retroalimentación vive en la interfaz, no en `alert()`.
- Acciones irreversibles con confirmación; modales con salida obvia y una sola tarea.
- Los `mailto:` y enlaces sociales dicen a dónde llevan.

**Lente 5 · Contenido y redacción (Medio normalmente)**
- Cada etiqueta dice qué pasa: "Enviar mensaje", no "Enviar"; "Quiero saber más" lleva a
  "¿Qué hacemos?".
- Mayúsculas consistentes: títulos y botones en MAYÚSCULAS (estilo actual del sitio); párrafos
  en oración. No mezclar en la misma vista.
- Español neutro, tuteo (el sitio usa "Comunícate", "Acompáñanos"). Sin jerga ni relleno.
- Errores: qué pasó y cómo arreglarlo, sin disculparse.

### Paso 3 — Informe
```text
## Revisión de diseño: <nombre>
### Resumen
2–3 frases. Calificación: Excelente / Bien / Necesita trabajo / Problemas críticos.
Tesis de la pantalla y su elemento memorable (o que le falta).
### Crítico
- **Qué**: problema con números · **Por qué**: principio/lente · **Arreglo**: cambio concreto
  (clase, token, valor) en HTML/CSS/Bootstrap.
### Mejoras   (cada una con etiqueta Alto / Medio / Bajo)
### Notas de craft
### Qué funciona
```
Calificación: algún Crítico → *Problemas críticos*; varios Altos → *Necesita trabajo*;
≤ 2 Altos → *Bien*; nada sobre Medio y con punto de vista → *Excelente*.

## Modo mejora ("que se vea menos genérico")
1. Anclar en el tema: juegos, mente, aprendizaje, Gummy, hologramas.
2. Plan de tokens antes del layout: solo con `colors_and_type.css` (no inventar colores).
3. Criticar el plan: ¿lo habrías propuesto igual para otro producto? Entonces es un default.
4. Cambios concretos con cifras: "subtítulo Gray 600 → Gray 500, 4.2:1 → 9.6:1".
5. Orden: accesibilidad → convenciones → craft → pulido.
6. Volver a criticar: quitar una cosa; confirmar 375 px, foco visible, movimiento reducido.

## Reglas de trabajo
Números, no adjetivos · cita la lente o marca como juicio propio · habla en HTML/CSS/Bootstrap ·
nombra el trade-off cuando una guía choca con el negocio · revisa el flujo completo, no solo la
pantalla · no sobre-critiques · **no aplanes la personalidad**.

## Skill original completa (HIG literal, apps nativas)
```bash
npx skills add dickwu/apple-design-skill -a claude-code
```
Repositorio: https://github.com/dickwu/apple-design-skill
