# Manual de eXeLearning

- La raíz es el `.elpx` del manual descomprimido, solo con las fuentes: `content.xml`,
  `content/resources/` y `theme/` (estilo Cedec). No hay más código que `scripts/` y los workflows.
- Nunca subir una exportación HTML (`index.html`, `html/`, `libs/`, `idevices/`, `search_index.js`,
  `content/css/`, `content/img/`): la genera GitHub Actions y `.gitignore` la excluye.
- El contenido se edita con eXeLearning, preferiblemente en
  `https://github.exelearning.dev/?repo=exelearning/exelearning-manual-es`. Al guardar, el editor
  solo escribe `content.xml`, `content/resources/` y `screenshot.png`; nunca `theme/`.
- No cambiar el contenido educativo sin que se pida. Si hay que tocar `content.xml` a mano, un
  iDevice guarda el mismo contenido en `htmlView` y en `jsonProperties`: cambiar ambos y dejar el
  XML válido. Los recursos se citan como `{{context_path}}/content/resources/<archivo>`.
- `scripts/build.sh` empaqueta `dist/exelearning-manual-es.elpx`, exporta `dist/site/` con Docker
  y ejecuta `scripts/check.py`. Validar siempre con él antes de proponer cambios.
- La imagen del CLI está fijada en `build.sh` (`exelearning/exelearning:v4.0.5`), y solo ahí. Al
  subirla, probar a quitar los arreglos marcados con `ponytail:` (rutas `resources/resources/`,
  iDevice 3Dmol como `dmole`, Mermaid sin `libs/mermaid/`); `check.py` falla si alguno vuelve.
- `check.py` da como avisos, no errores, los enlaces a archivos internos del editor (`files/perm/`):
  vienen del original (Lupa y Vídeo interactivo). El iDevice Mapa también cita archivos que nunca
  estuvieron en el paquete. Son del contenido; se corrigen desde el editor.
- `exelearning-pages.yml` construye los pull requests y publica `main` en GitHub Pages cuando
  cambian las fuentes o `scripts/`. Conserva el nombre de la plantilla de github.exelearning.dev
  para que su opción *Publish on GitHub Pages* no añada un segundo workflow.
- Releases: la etiqueta es la versión de eXeLearning que documenta el manual (`v4.0.5`); las
  correcciones posteriores para esa versión son `v4.0.5-1`, `v4.0.5-2`… Las etiquetas no se mueven
  ni se reutilizan. El título de la release es solo la etiqueta y la última se marca como *Latest*.
  `release.yml` adjunta el `.elpx` y el ZIP HTML, con versión y con nombre estable
  (`exelearning-manual-es.elpx`, `exelearning-manual-es-html.zip`).
- README, CONTRIBUTING y los textos para personas, en español; nombres técnicos y código, tal cual.
- Licencia CC BY-SA 4.0 (Cedec / eXeLearning). No quitar créditos ni pies de imagen. Los logotipos
  institucionales de `theme/img/` tienen todos los derechos reservados y no se reutilizan.
- No modificar los repositorios de referencia (`erseco/github-exelearning`,
  `ateeducacion/exelearning-style-book`) ni eXeLearning para arreglar algo de este manual.
