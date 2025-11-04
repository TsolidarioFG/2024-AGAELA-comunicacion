# ComunicELA: Software de Asistencia para la Comunicación en Pacientes con Esclerosis Lateral Amiotrófica

La Esclerosis Lateral Amiotrófica (ELA) es una enfermedad neurodegenerativa irreversible que resulta en la pérdida gradual de neuronas, deteriorando progresivamente las funciones motrices, así como la capacidad de hablar, tragar o respirar. Las personas con ELA que carecen de capacidad de comunicarse experimentan una mejora significativa en su calidad de vida cuando utilizan sistemas de comunicación aumentativa y alternativa (CAA). Sin embargo, muchos de estos sistemas no están específicamente adaptados a sus necesidades únicas, lo que limita su efectividad.

Este proyecto, desarrollado en colaboración con la [Asociación Galega de Afectados pola Esclerose Lateral Amiotrófica (AGAELA)](agaela.es) y la [Cátedra NTT DATA en Diversidad y Tecnología](https://www.fundacion.udc.es/catedra-nttdata/), propone un sistema basado en inteligencia artificial que mejora significativamente la calidad de comunicación de las personas con esta enfermedad. Gracias a la colaboración con AGAELA, se ha adaptado el diseño y las funcionalidades del sistema a las necesidades reales de los usuarios, asegurando su aplicabilidad y relevancia. La solución propuesta es una aplicación con una interfaz intuitiva, accesible, adaptable y sencilla, que facilita la comunicación mediante tableros personalizables controlados por movimientos oculares y parpadeo. Las frases formadas pueden ser reproducidas a través de síntesis de voz, mejorando la interacción y la autonomía de los pacientes.

El sistema fue validado tanto con un grupo control como con pacientes diagnosticados con ELA en diversas etapas de la enfermedad, cubriendo un amplio espectro de variaciones en sus habilidades de movilidad y comunicación. Este riguroso proceso de validación incluyó pruebas de usabilidad y efectividad, asegurando que el sistema funcione de manera efectiva bajo una variedad de condiciones y necesidades específicas.

Este enfoque integrador y colaborativo no solo mejora la comunicación sino que también amplía la interacción social y la calidad de vida de los afectados por la ELA. Diseñado para adaptarse a futuras innovaciones en tecnologías asistenciales, el sistema facilita la integración con otros dispositivos y plataformas, ofreciendo soluciones más personalizadas. Así, el proyecto no solo atiende las necesidades actuales sino que también evoluciona y se adapta a los avances tecnológicos y médicos, contribuyendo continuamente a la mejora de la autonomía y el bienestar de los usuarios. 

Además, al estar disponible como código libre, el sistema invita a desarrolladores y usuarios de todo el mundo a contribuir, promoviendo un entorno abierto y colaborativo que enriquece continuamente su desarrollo y aplicación.


## Ejecución de la Aplicación

La configuración de la API de Google Gemini es opcional, pero se recomienda encarecidamente para aprovechar la funcionalidad del conjugador automático. Este conjugador permite que las frases creadas con infinitivos en los tableros se conjuguen antes de ser reproducidas en alto, proporcionado una comunicación más fluida y natural. Sigue estos pasos para configurar la API, si no deseas esta característica salta al paso 3.

1. **Obtener una clave API:**
    - Ve a [obtener clave API](https://aistudio.google.com/app/apikey) y apunta la clave.

2. **Establecer una variable de entorno:**
    - Abre el menú de inicio de Windows y busca "variables de entorno".
    - Selecciona "Editar las variables de entorno del sistema".
    - En la ventana de "Propiedades del sistema", haz clic en "Variables de entorno".
    - En la sección "Variables de usuario", haz clic en "Nueva" para agregar la nueva variable de entorno.
    - Introduce el nombre: `GOOGLE_API_KEY`.
    - En el campo del valor, introduce la clave obtenida del enlace anterior.
    - Si en la configuración de la aplicación el conjugador aún aparece como "No disponible", reinicia el sistema.

3. **Descargar y extraer la aplicación:**
    - Descarga el archivo comprimido `ComunicELA.zip` disponible en el siguiente [enlace](https://drive.google.com/file/d/1ly-fBQTh3I30p7BFrTMlSRBhE76WCO7A/view?usp=sharing).
    - Extrae el contenido del archivo zip.
    - Dentro de la carpeta extraída `ComunicELA`, encontrarás:
        - La carpeta `tableros`, donde puedes personalizar los tableros según tus necesidades como se explica más adelante.
        - El archivo `ComunicELA.exe`.

4. **Ejecución de la aplicación:**
    - Para abrir la aplicación, simplemente ejecuta el archivo `ComunicELA.exe`.
    - Asegúrate de que la carpeta `tableros` y el archivo `ComunicELA.exe` permanezcan en la misma carpeta. Si se encuentran en ubicaciones diferentes, el software no podrá encontrar los tableros.





## Edición de Tableros
### Estructura de Carpetas
- **Carpeta "pictogramas":** Contiene todas las fotografías utilizadas en las casillas con pictogramas. Estas fotografías son genéricas para todos los idiomas.

- **Archivos "tablero_XX_XX":**
    - Los tableros son archivos con extensión `.xlsx`, cada uno nombrado según el idioma correspondiente.
    - Dentro de cada archivo, los diferentes tableros se distribuyen en hojas. El primer tablero que aparece al abrir el archivo es el de la primera hoja, llamada `TAB. INICIAL`.
    - Los códigos de idioma siguen el formato XX_XX, donde:
        - es_ES corresponde a español de España.
        - gal_ES corresponde a gallego de España.
        - Por el momento son los dos idiomas soportados.
### Personalización de Casillas
- Cada casilla tiene dos columnas reservadas:
    - **Primera columna:** Nombre de la fotografía correspondiente de la carpeta de pictogramas.
    - **Segunda columna:** Nombre de la palabra a mostrar.
- Para personalizar una casilla, añade la fotografía con el nombre deseado a la carpeta de pictogramas y escribe este nombre en la primera columna reservada para la casilla que quieras modificar.

### Enlaces a Otros Tableros
- Si la palabra de la casilla comienza por `"TAB. "`, el software la reconoce como un enlace a otro tablero (otra hoja del archivo).
- Por ejemplo, si en la palabra de una casilla se escribe `TAB. RÁPIDO`, al pulsar esta casilla se abrirá el tablero correspondiente a la hoja `TAB. RÁPIDO`.

### Consejo Adicional
- Es recomendable incluir en cada tablero (excepto en el inicial) una casilla que permita volver al tablero inicial. Esto posibilita la navegación entre los diferentes tableros.


## Licencia

Este proyecto está licenciado bajo la **GPL-3.0**.  
Consulta el archivo `LICENSE` o el texto completo en:  
https://www.gnu.org/licenses/gpl-3.0.html


## Premios y Reconocimientos

- **Premio al Mejor TFG Aplicado** – Facultad de Informática, Universidade da Coruña (2025).  
- **Mención de Honor en los Premios CREAIMPACTO** – Uno de los tres mejores proyectos de España en la categoría Salud (2025).  
- **2º Premio al Mejor Trabajo de Fin de Grado** – Asociación Española para la Inteligencia Artificial (AEPIA) (2025).  
- **Premio al Mejor Trabajo de Fin de Estudios en Emprendimiento** – Categoría Ciencias de la Salud, Universidade da Coruña (2025).  

## Difusión en medios
- [LinkedIn - Introducing ComunicELA](https://www.linkedin.com/posts/pabloparamotelle_introducing-comunicela-comunicela-activity-7253848414939955202-dNCy?utm_source=social_share_send&utm_medium=member_desktop_web&rcm=ACoAAByHYYkB_E_HDtRnYXUh-XtJ0k-h_0mzfnQ)
- [El Ideal Gallego - Un estudiante de la UDC, entre los tres mejores de España en los Premios CREAIMPACTO 2025](https://www.elidealgallego.com/articulo/a-coruna/estudiante-udc-entre-tres-mejores-espana-premios-creaimpacto-2025-5349103)  
- [El Ideal Gallego - Pablo Páramo | “La idea es que todos los pacientes con ELA puedan descargar el código, utilizarlo e incluso mejorarlo”](https://www.elidealgallego.com/articulo/a-coruna/pablo-paramo-idea-todos-pacientes-ela-puedan-descargar-codigo-utilizarlo-e-incluso-mejorarlo-5351524)  
- [UDC - Un estudante da UDC, entre os tres mellores de España nos Premios CREAIMPACTO 2025](https://www.udc.es/novas/Un-estudante-da-UDC-entre-os-tres-mellores-de-Espana-nos-Premios-CREAIMPACTO-2025/?fbclid=IwY2xjawLPagNleHRuA2FlbQIxMQABHmoErZkbHRHc8se3bh5jEwb2b_TUPh_Z2HtHwwYRcrfFSh6WLGRryYHJBKlq_aem_HIMF6ydyiBnKz8q-T7Z2Vw)  
- [Fundación UDC - Un estudiante de la UDC, entre los tres mejores de España en los Premios CREAIMPACTO 2025](https://www.fundacion.udc.es/site_noticia.asp?id=949&idioma=ES)
- [ABC - Un trabajo de fin de grado de la UDC sienta las bases para mejorar la comunicación de pacientes con ELA](https://www.abc.es/espana/galicia/trabajo-fin-grado-udc-sienta-bases-mejorar-20250701134827-nt.html?ref=https%3A%2F%2Fwww.google.com%2F)
- [El Español / Quincemil - Un estudiante de la Universidade da Coruña, entre los mejores de los Premios CREAIMPACTO](https://www.elespanol.com/quincemil/cultura/educacion/20250630/estudiante-universidade-da-coruna-mejores-premios-creaimpacto/1003743827602_0.html)  
- [La Opinión de A Coruña - Un alumno de la UDC, galardonado en Creaimpacto](https://www.laopinioncoruna.es/coruna/2025/06/30/alumno-udc-galardonado-creaimpacto-119226674.html)
- [Onda Cero - Podcast de Ciencia de Onda Cero en colaboración con la UDC](https://amp-ondacero-es.cdn.ampproject.org/c/s/amp.ondacero.es/emisoras/galicia/coruna/mas-de-uno/ciencia/udciencia-01072025_20250704686780d777c93072586743e6.html) 
- [Código Cero - Os Premios CreaImpacto recoñecen ao estudante Pablo Páramo (UDC) polo proxecto ComunicELA](https://codigocero.com/Os-Premios-CreaImpacto-reconecen-ao-estudante-Pablo-Paramo-UDC-polo-proxecto)  
- [CODDII - Un estudiante de Informática de la UDC, entre los tres mejores de España en los Premios CREAIMPACTO 2025](https://coddii.org/un-estudiante-de-informatica-la-udc-entre-los-tres-mejores-de-espana-en-los-premios-creaimpacto-2025)  