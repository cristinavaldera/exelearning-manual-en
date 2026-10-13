# Manual de eXeLearning en español

[![eXeLearning 4.0.5](https://img.shields.io/badge/eXeLearning-4.0.5-26ddc7?labelColor=1f2937)](https://exelearning.net)
[![GitHub Pages](https://github.com/exelearning/exelearning-manual-es/actions/workflows/exelearning-pages.yml/badge.svg)](https://github.com/exelearning/exelearning-manual-es/actions/workflows/exelearning-pages.yml)
[![Edit in eXeLearning](https://img.shields.io/badge/Edit%20in-eXeLearning-26ddc7?labelColor=1f2937)](https://github.exelearning.dev/?repo=exelearning/exelearning-manual-es)
[![Licencia: CC BY-SA 4.0](https://img.shields.io/badge/licencia-CC%20BY--SA%204.0-lightgrey?labelColor=1f2937)](LICENSE)

Manual de uso de [eXeLearning](https://exelearning.net), la herramienta libre y de código
abierto para crear recursos educativos digitales. Documenta **eXeLearning 4.0.5**: qué es,
cómo se instala, el entorno de trabajo, cada iDevice con su ejemplo y la descarga y publicación
de los recursos. Lo elabora **Cedec** (INTEF) y está escrito con el propio eXeLearning.

| [**Consultar el manual**](https://exelearning.github.io/exelearning-manual-es/) | [**Editar en eXeLearning**](https://github.exelearning.dev/?repo=exelearning/exelearning-manual-es) | [**Descargar el proyecto**](https://github.com/exelearning/exelearning-manual-es/releases/latest/download/exelearning-manual-es.elpx) |
|:---:|:---:|:---:|
| Versión web, siempre al día con `main` | Edición en el navegador y guardado en GitHub | Último `.elpx` publicado, para abrirlo en eXeLearning |

[![Manual de eXeLearning](.github/screenshot.jpg)](https://exelearning.github.io/exelearning-manual-es/)

## Descargas

Cada [release](https://github.com/exelearning/exelearning-manual-es/releases) incluye:

- [`exelearning-manual-es.elpx`](https://github.com/exelearning/exelearning-manual-es/releases/latest/download/exelearning-manual-es.elpx):
  el proyecto, para abrirlo y modificarlo en eXeLearning (también con versión en el nombre,
  por ejemplo `exelearning-manual-es-v4.0.5.elpx`).
- [`exelearning-manual-es-html.zip`](https://github.com/exelearning/exelearning-manual-es/releases/latest/download/exelearning-manual-es-html.zip):
  el sitio web completo; descomprímelo y abre `index.html`, sin conexión (también como
  `exelearning-manual-es-v4.0.5-html.zip`).

Los enlaces de arriba apuntan siempre a la última release.

## Editar el manual

El proyecto se edita en el navegador con [github.exelearning.dev](https://github.exelearning.dev),
que abre el repositorio en el editor oficial de eXeLearning y guarda los cambios en GitHub.

1. Pulsa **Edit in eXeLearning**. Los repositorios públicos se abren sin iniciar sesión.
   El editor ofrece instalar el estilo **Cedec** del manual: acéptalo.
2. Edita como en cualquier proyecto de eXeLearning. La barra superior indica si hay cambios
   sin guardar.
3. Pulsa **Save to GitHub** (o <kbd>Ctrl</kbd>/<kbd>Cmd</kbd>+<kbd>S</kbd>). La primera vez,
   GitHub pide iniciar sesión y dar acceso a la app *eXeLearning*; con *Only select
   repositories* se limita a este repositorio.
4. Escribe el mensaje del commit y elige **confirmar en `main`** o **crear una rama y abrir un
   pull request**. Si la rama está protegida o alguien ha cambiado los mismos archivos, se abre
   un pull request automáticamente.

Un guardado solo escribe `content.xml`, los archivos nuevos o cambiados de `content/resources/`
y `screenshot.png`, en un único commit. Unos minutos después el workflow de publicación
regenera la web. Sin permiso de escritura, consulta [CONTRIBUTING.md](CONTRIBUTING.md) para
proponer los cambios desde un fork.

## Contribuir

- **Erratas, contenidos desactualizados o enlaces rotos:** abre una
  [issue](https://github.com/exelearning/exelearning-manual-es/issues) con la página afectada.
- **Cambios en el manual:** edítalo con el botón de arriba o envía un
  [pull request](https://github.com/exelearning/exelearning-manual-es/pulls). Cada pull request
  se reconstruye y se valida antes de poder publicarse.

Todos los detalles están en [CONTRIBUTING.md](CONTRIBUTING.md).

## Estructura

La raíz del repositorio es el proyecto `.elpx` descomprimido, sin la exportación HTML:

| Ruta | Contenido |
|---|---|
| `content.xml` | Páginas, iDevices y propiedades del manual |
| `content/resources/` | Imágenes, vídeos, audios y demás archivos que usa el manual |
| `theme/` | Estilo Cedec, con sus fuentes, iconos y logotipos |
| `scripts/build.sh` | Empaqueta el `.elpx`, exporta la web con eXeLearning CLI y la valida |
| `scripts/check.py` | Comprueba el `.elpx` y los enlaces de la web exportada |
| `.github/workflows/` | Publicación en GitHub Pages y releases |

## Publicación automática

- **[Publish eXeLearning resource](.github/workflows/exelearning-pages.yml):** cuando cambian
  `content.xml`, `content/resources/`, `theme/` o los scripts en `main`, empaqueta el proyecto,
  lo exporta a HTML5 con la imagen Docker oficial `exelearning/exelearning:v4.0.5`, valida el
  resultado y lo publica en <https://exelearning.github.io/exelearning-manual-es/>. En un pull
  request solo construye y valida. También se puede lanzar a mano desde *Actions*.
- **[Release](.github/workflows/release.yml):** al subir una etiqueta `v*` genera los paquetes,
  comprueba que son ZIP válidos y los adjunta a la release. Si la construcción o la validación
  fallan, no se publica nada. Lanzado a mano, deja los paquetes como artefacto del workflow.

La web no se guarda en el repositorio: se genera siempre desde `content.xml`, así que no hay dos
versiones que puedan divergir. Cada release lleva la versión de eXeLearning que documenta
el manual (`v4.0.5`).

Para construirlo en local hace falta Docker; el resultado queda en `dist/`:

```sh
scripts/build.sh
```

`build.sh` corrige tres fallos del exportador de eXeLearning CLI 4.0.5 (rutas de recursos con
espacios, el iDevice 3Dmol y los diagramas Mermaid) y `check.py` falla si alguno reaparece.

## Créditos y licencia

- **Manual:** Cedec / eXeLearning (Cedec, INTEF). Publicación original:
  <https://descargas.intef.es/cedec/exe_learning/Manuales/manual_exe405/>. Licencia
  [Creative Commons Reconocimiento-CompartirIgual 4.0 (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/);
  el texto legal está en [LICENSE](LICENSE). Las imágenes y recursos de terceros conservan la
  autoría y licencia que se indican junto a ellos en el manual.
- **Estilo Cedec (`theme/`):** desarrollado por Ignacio Gros para Cedec, CC BY-SA 4.0. Iconos
  de iDevices de Francisco Javier Pulido Cuadrado (CC BY-SA 4.0); fuentes Atkinson Hyperlegible
  del Braille Institute (SIL OFL 1.1, `theme/fonts/OFL.txt`); iconos basados en Material Icons
  de Google (Apache 2.0) y de Wikimedia (CC BY 4.0). Detalles en `theme/config.xml`.
- **Logotipos institucionales** (`theme/img/mefpd.png`, `mefpd_sm.png`, `intef.png`,
  `cedec.png`, `cedec_sm.png` y `favicon.ico`): marcas del Ministerio, del INTEF y de Cedec,
  con todos los derechos reservados y **fuera de la licencia CC BY-SA**. Quien reutilice el
  estilo para otros materiales debe quitarlos (opción `logos` de `theme/style.js`).
- La web generada incluye bibliotecas e iDevices de eXeLearning, que conservan sus propias
  licencias.
