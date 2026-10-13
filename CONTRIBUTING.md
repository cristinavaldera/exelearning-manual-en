# Cómo contribuir

Gracias por ayudar a mejorar el Manual de eXeLearning. Todas las aportaciones se publican con
la licencia del manual, [CC BY-SA 4.0](LICENSE).

## Avisar de un problema

Abre una [issue](https://github.com/exelearning/exelearning-manual-es/issues) con:

- el enlace a la página del [manual publicado](https://exelearning.github.io/exelearning-manual-es/);
- qué está mal (errata, captura antigua, enlace roto, actividad que no funciona…);
- si puedes, el texto o la imagen que propones.

## Proponer cambios

### Con permiso de escritura

Abre el manual con
[github.exelearning.dev](https://github.exelearning.dev/?repo=exelearning/exelearning-manual-es),
edítalo y pulsa **Save to GitHub**. Para cambios grandes o que deban revisarse, elige
*Create a branch for this change and start a pull request*: los guardados siguientes van a esa
rama hasta que se mezcle.

### Sin permiso de escritura

1. Haz un fork del repositorio.
2. Ábrelo en `https://github.exelearning.dev/?repo=TU-USUARIO/exelearning-manual-es`, edítalo y
   guarda los cambios en tu fork.
3. Desde tu fork en GitHub, abre un pull request hacia `exelearning/exelearning-manual-es`.

### Con eXeLearning de escritorio

1. Descarga el [`.elpx` de la última release](https://github.com/exelearning/exelearning-manual-es/releases/latest/download/exelearning-manual-es.elpx)
   (o genera uno con `scripts/build.sh`) y edítalo en eXeLearning.
2. Guárdalo como `.elpx` y copia en tu rama solo las fuentes:

   ```sh
   unzip -o manual.elpx 'content.xml' 'content/resources/*'
   ```

3. Borra de `content/resources/` los archivos que hayas eliminado en eXeLearning y abre un pull
   request.

## Normas

- **Solo fuentes.** No subas la exportación HTML (`index.html`, `html/`, `libs/`, `idevices/`…):
  la genera GitHub Actions y `.gitignore` la excluye.
- **Un tema por pull request**, con una descripción breve de qué cambia y por qué.
- **Imágenes con licencia compatible** con CC BY-SA 4.0, indicando autoría y licencia en el pie,
  como en el resto del manual. No añadas logotipos ni material con todos los derechos reservados.
- **No quites los créditos** ni los avisos de licencia existentes.
- Actualiza el **Historial de versiones** de la página *Créditos y descarga* en los cambios
  importantes.

## Revisión y publicación

Cada pull request ejecuta el workflow *Publish eXeLearning resource*: exporta el manual con
eXeLearning CLI y comprueba el `.elpx`, los recursos referenciados y los enlaces. Al mezclarlo en
`main`, el mismo workflow publica la web en GitHub Pages.

Para publicar una nueva edición descargable, quien mantenga el repositorio crea una etiqueta
siguiendo [SemVer](https://semver.org/lang/es/) según el alcance de los cambios:

```sh
git tag v1.1.0
git push origin v1.1.0
```

El workflow *Release* genera `exelearning-manual-es-v1.1.0.elpx`,
`exelearning-manual-es-v1.1.0-html.zip` y sus copias con nombre estable, y los adjunta a la
release.
