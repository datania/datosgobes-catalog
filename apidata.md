Title: API - Datos.gob.es

URL Source: http://datos.gob.es/en/accessible-apidata

Markdown Content:
API - Datos.gob.es
===============

[Skip to content](http://datos.gob.es/en/accessible-apidata#main-content)

[![Image 1: Ministry for Digital Transformation and Public Service](http://datos.gob.es/sites/default/files/2024-03/logo_ministerio_cabecera_0.svg)](https://digital.gob.es/index.html "Ministry for Digital Transformation and Public Service")

Language
--------

EN ![Image 2: Simple arrow icon](http://datos.gob.es/images/blue-arrow.svg)

*   [Español](http://datos.gob.es/es/accessible-apidata)
*   [English](http://datos.gob.es/en/accessible-apidata)
*   [Català](http://datos.gob.es/ca/accessible-apidata)
*   [Galego](http://datos.gob.es/gl/accessible-apidata)
*   [Euskara](http://datos.gob.es/eu/accessible-apidata)

[Publisher](http://datos.gob.es/en/accessible-apidata# "Publisher")

[Log in](http://datos.gob.es/user/login)

[![Image 3: Datos.gob.es. Reuse the public information . Go home](http://datos.gob.es/themes/custom/dge_theme/logo.svg)](http://datos.gob.es/en/ "Home")

[](http://datos.gob.es/en/accessible-apidata)[Toggle menu](http://datos.gob.es/en/accessible-apidata#)

Navigation
----------

*   [Data](http://datos.gob.es/en/accessible-apidata#data)[Open data catalogue](http://datos.gob.es/en/catalogo)[Data request](http://datos.gob.es/en/data-request)[Support for publishers](http://datos.gob.es/en/support-for-publishers)[Safe environments](http://datos.gob.es/en/safe-environments)[Data spaces](http://datos.gob.es/en/data-spaces) 
*   [Community](http://datos.gob.es/en/accessible-apidata#community)[Initiatives](http://datos.gob.es/en/initiatives)[Companies](http://datos.gob.es/en/companies)[Applications](http://datos.gob.es/en/applications)[Challenges](http://datos.gob.es/en/aporta-challenge)[Sectors](http://datos.gob.es/en/sectors) 
*   [Current news](http://datos.gob.es/en/accessible-apidata#current-news)[News](http://datos.gob.es/en/news)[Events](http://datos.gob.es/en/events) 
*   [Knowledge](http://datos.gob.es/en/accessible-apidata#knowledge)[Blog](http://datos.gob.es/en/blog)[Data exercises](http://datos.gob.es/en/conocimiento/tipo/data-exercises-342)[Infographics](http://datos.gob.es/en/conocimiento/tipo/infographics-345)[Interviews](http://datos.gob.es/en/interviews)[Reports and guides](http://datos.gob.es/en/conocimiento/tipo/reports-and-studies-340/tipo/guides-343/tipo/training-materials-344/tipo/regulations-and-strategies-346)[Github datosgob](https://github.com/datosgobes) 
*   [About us](http://datos.gob.es/en/accessible-apidata#about-us)[What we do](http://datos.gob.es/en/what-we-do)[Metrics and impact](http://datos.gob.es/en/metrics-and-impact)[Frequently Asked Questions](http://datos.gob.es/en/preguntas-frecuentes/faq_categoria/general-361)[Technology](http://datos.gob.es/en/technology)[Contact](http://datos.gob.es/en/contact)[Site map](http://datos.gob.es/en/sitemap) 

*   [Español](http://datos.gob.es/es/accessible-apidata)
*   [English](http://datos.gob.es/en/accessible-apidata)
*   [Català](http://datos.gob.es/ca/accessible-apidata)
*   [Galego](http://datos.gob.es/gl/accessible-apidata)
*   [Euskara](http://datos.gob.es/eu/accessible-apidata)

[Log in](http://datos.gob.es/user/login)

 All sections ![Image 4: Blue arrow icon](http://datos.gob.es/images/blue-arrow.svg)
*   [All sections](http://datos.gob.es/en/accessible-apidata)
*   [Data catalogue](http://datos.gob.es/en/accessible-apidata)
*   [Applications](http://datos.gob.es/en/accessible-apidata)
*   [Blog](http://datos.gob.es/en/accessible-apidata)
*   [Companies](http://datos.gob.es/en/accessible-apidata)
*   [Data exercises](http://datos.gob.es/en/accessible-apidata)
*   [Data request](http://datos.gob.es/en/accessible-apidata)
*   [Events](http://datos.gob.es/en/accessible-apidata)
*   [Infographics](http://datos.gob.es/en/accessible-apidata)
*   [Initiatives](http://datos.gob.es/en/accessible-apidata)
*   [Interviews](http://datos.gob.es/en/accessible-apidata)
*   [News](http://datos.gob.es/en/accessible-apidata)
*   [Reports and guides](http://datos.gob.es/en/accessible-apidata)

You are here
------------

*   [Home](http://datos.gob.es/en/)
*   [Data catalogue](http://datos.gob.es/en/catalogo/conjuntos-datos)
*   API

[](http://datos.gob.es/en/accessible-apidata)
API
===

*   [![Image 5: Data Catalog icono](http://datos.gob.es/images/SVG/data-catalogue.svg)Data catalogue](http://datos.gob.es/en/catalogo "Data catalogue")
*   [![Image 6: SPARQL icono](http://datos.gob.es/images/SVG/sparql.svg)SPARQL Endpoint](http://datos.gob.es/en/sparql "SPARQL Endpoint")

The API is a mechanism which allows queries in the datos.gob.es semantic database. It provides access to information from the data catalogue and URIs defined in Annexes IV and V of the Technical Interoperability Regulations on the Re-Use of Information Resources.

These queries can be carried out based on a series of criteria selected by the user and using uniform resource identifiers (URI).

Response formats
----------------

The information available via the API can be obtained in different formats. The formats available are: json, xml, rdf, ttl y csv.

JSON is the default response format; for example: if the following API resource is accessed via the browser `http://datos.gob.es/apidata/catalog/dataset`, the result will be shown in JSON format.

There are two options to indicate the response format you want:

1.   Using the `'Accept'` parameter on the request headers. For example: `Accept:application/rdf+xml`
2.   Indicating the format extension in the request. For example: `http://datos.gob.es/apidata/catalog/dataset.xml`

| Format | 1. 'Accept' Header | 2. Format extension |
| --- | --- | --- |
| JSON | application/json | .json |
| XML | application/xml | .xml |
| RDF | application/rdf+xml | .rdf |
| Turtle | application/x-turtle | .turtle |
| CSV | text/csv | .csv |

API Parameters
--------------

The API offers a series of parameters to customise the responses:

| Parameter | Description | Example |
| --- | --- | --- |
| `_sort` | With this parameter, results can ordered according to one or more response fields. The field name should be entered according to the desired order of the results. To invert the order, add the minus symbol '-'' in front of the field name. Various fields can be combined using a comma ',' to separate them. | For example, if you want to order all data sets by descending date and title: `http://datos.gob.es/apidata/catalog/dataset.json?_sort=-issued,title` |
| `_pageSize` | Use this parameter to set the number of results per page. The maximum value is 50. | For example, to get the results one by one: `http://datos.gob.es/apidata/catalog/dataset.xml?_pageSize=1` |
| `_page` | This parameter indicates the number of the current page. The first page is 0. | For example, to go to the third page of the results: `http://datos.gob.es/apidata/catalog/dataset.xml?_pageSize=1&_page=2` |

Available References
--------------------

### Data catalogue

Set of calls which allow data.gob.es catalogue queries.

**Data sets**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all of the data sets** | `http://datos.gob.es/apidata/catalog/dataset` |  |
| **To obtain a data set identified by the URI indicator** | `http://datos.gob.es/apidata/catalog/dataset/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is: `'a16003011-empresas-y-personas-empleadas-en-la-c-a-de-euskadi-supervivientes-en-2015-altas-en-los-cinco-anos-anteriores-por-territorio-y-comarca-de-sede-social'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/a16003011-empresas-y-personas-empleadas-en-la-c-a-de-euskadi-supervivientes-en-2015-altas-en-los-cinco-anos-anteriores-por-territorio-y-comarca-de-sede-social` |
| **To obtain data sets with a specific title** | `http://datos.gob.es/apidata/catalog/dataset/title/{title}` You must specify the `{title}` value. It can be part of the title. | For example, if the value of the `{title}` is: `'employment'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/title/employment` |
| **To obtain a data set with a specific publisher using their identifier** | `http://datos.gob.es/apidata/catalog/dataset/publisher/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is: `'A16003011'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/publisher/A16003011` |
| **To obtain a data set with a specific category or topic using their identifier** | `http://datos.gob.es/apidata/catalog/dataset/theme/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is: `'hacienda'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/theme/hacienda` |
| **To obtain a data set with distributions in a specific format** | `http://datos.gob.es/apidata/catalog/dataset/format/{format}` | For example, if the value of the `{format}` is: `'csv'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/format/csv` |
| **To obtain a data set containing a specific tag** | `http://datos.gob.es/apidata/catalog/dataset/keyword/{keyword}` | If the value of the `{keyword}` is: `'costs'`, the reference will be: `http://datos.gob.es/apidata/catalog/dataset/keyword/costs` |
| **To obtain a data set from a specific geographic scope** | `http://datos.gob.es/apidata/catalog/dataset/spatial/{spatialWord1}/{spatialWord2}` This reference uses two parameters: `{spatialWord1}` and `{spatialWord2}`. | If the value of the `{spatialWord1}` is: `'Autonomia'` and `{spatialWord2}` is: `'Pais-Vasco'` the reference will be: `http://datos.gob.es/apidata/catalog/dataset/spatial/Autonomia/Pais-Vasco` |
| **Obtener los conjuntos de datos que han sido actualizados entre dos fechas** | `http://datos.gob.es/apidata/catalog/dataset/modified/begin/{beginDate}/end/{endDate}` This reference uses two parameters: `{beginDate}` and `{endDate}`, whose format must be `AAAA-MM-DDTHH:mmZ`. | If the value of the `{beginDate}` is: `2016-04-18T00:00Z` and `{endDate}` is: `2016-06-30T00:00Z` the reference will be: `http://datos.gob.es/apidata/catalog/dataset/modified/begin/2016-04-18T00:00Z/end/2016-06-30T00:00Z?_sort=title&_pageSize=10&_page=0` |

**Distributions**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all distributions** | `http://datos.gob.es/apidata/catalog/distribution` |  |
| **To obtain the distributions of a data set identified by the URI indicator** | `http://datos.gob.es/apidata/catalog/distribution/dataset/{id}` You must specify the `{id}` value. | If the value of the `{id}` is: `'a16003011-empresas-y-personas-empleadas-en-la-c-a-de-euskadi-supervivientes-en-2015-altas-en-los-cinco-anos-anteriores-por-territorio-y-comarca-de-sede-social'`, the reference will be: `http://datos.gob.es/apidata/catalog/distribution/dataset/a16003011-empresas-y-personas-empleadas-en-la-c-a-de-euskadi-supervivientes-en-2015-altas-en-los-cinco-anos-anteriores-por-territorio-y-comarca-de-sede-social` |
| **Obtener las distribuciones que están en un determinado formato** | `http://datos.gob.es/apidata/catalog/distribution/format/{format}` | If the value of the `{format}` is: `'csv'`, the reference will be: `http://datos.gob.es/apidata/catalog/distribution/format/csv` |

**Publishers**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all publishers** | `http://datos.gob.es/apidata/catalog/publisher` |  |

**Geographical scopes**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all geographical coverage options with data sets in the catalogue** | `http://datos.gob.es/apidata/catalog/spatial` |  |

**Categories / Topics**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all categories or topics with data sets in the catalogue** | `http://datos.gob.es/apidata/catalog/theme` |  |

### Technical Interoperability Regulations

Set of references which allow **primary sector taxonomy** queries and the **identification of geographical coverage** defined in Annexes IV and V of the [Technical Interoperability Regulations on the Re-use of Information Resources](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2013-2380)**(NTI)**.

**Primary sectortaxonomy**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all primary sectors** | `http://datos.gob.es/apidata/nti/public-sector` |  |
| **To obtain a specific sector identified by the URI indicator** | `http://datos.gob.es/apidata/nti/public-sector/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is: `'comercio'`, the reference will be: `http://datos.gob.es/apidata/nti/public-sector/comercio` |

**Identificación de cobertura geográfica**| Operation | Description | Examples |
| --- | --- | --- |
| **To obtain all provinces** | `http://datos.gob.es/apidata/nti/territory/Province` |  |
| **To obtain a specific province identified by the URI indicator** | `http://datos.gob.es/apidata/nti/territory/Province/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is: `'Madrid'`, the reference will be: `http://datos.gob.es/apidata/nti/territory/Province/Madrid`. |
| **To obtain all the Autonomous Regions** | `http://datos.gob.es/apidata/nti/territory/Autonomous-region` |  |
| **To obtain a specific Autonomous Region identified by the URI indicator** | `http://datos.gob.es/apidata/nti/territory/Autonomous-region/{id}` You must specify the `{id}` value. | For example, if the value of the `{id}` is `'Comunidad-Madrid'`, the reference will be: `http://datos.gob.es/apidata/nti/territory/Autonomous-region/Comunidad-Madrid` |
| **To obtain the country** | `http://datos.gob.es/apidata/nti/territory/Country/España` |  |

![Image 7: Chica trabajando con tecnologia](http://datos.gob.es/sites/default/files/2024-03/newsletter-datosgob-women-working_1.svg)

### Do you want to keep up to date with data-related news?

Subscribe to our newsletter to receive the latest news published on datos.gob.es

[Subscribe ![Image 8: Decoration arrow icon](http://datos.gob.es/themes/custom/dge_theme/images/icons/decoration-arrow.svg)](http://datos.gob.es/en/formulario-de-alta " Subscription by e-mail to the latest news from datos.gob.es.")

[Unsubscribe](http://datos.gob.es/en/formulario-de-baja "Unsubscribe from the data.gob.es bulletin")

![Image 9: Footer menu decoration arrow icon](http://datos.gob.es/themes/custom/dge_theme/images/icons/footer-decoration-arrow.svg)

*   Contact us
    *   [Contact](http://datos.gob.es/en/contact)

*   Information of interest
    *   [FAQs](http://datos.gob.es/en/preguntas-frecuentes/faq_categoria/general-361)
    *   [Legal notice](http://datos.gob.es/en/legal-notice)
    *   [Site map](http://datos.gob.es/en/sitemap)
    *   [Accessibility](http://datos.gob.es/en/accessibility)

[![Image 10: Certificado de conformidad con el Esquema Nacional de Seguridad](http://datos.gob.es/sites/default/files/2025-03/logo_ENS.png)](http://datos.gob.es/sites/default/files/2025-03/Certificado_ENS.pdf)

[![Image 11: Certificado IQNet](http://datos.gob.es/sites/default/files/2025-03/logo_IQnet.jpg)](http://datos.gob.es/es/iqnet)

[![Image 12: Certificado de calidad ISO-9001:2015](http://datos.gob.es/sites/default/files/2025-03/9001INF.jpg)](http://datos.gob.es/sites/default/files/2025-03/Certificado_ISO_9001.pdf)

[![Image 13: Certificado de calidad UNE-ISO/IEC 27001:2014](http://datos.gob.es/sites/default/files/2025-03/Segur_Info_27001_INF.jpg)](http://datos.gob.es/sites/default/files/2025-03/Certificado_ISO_27001.pdf)

[![Image 14: Follow us on LinkedIn. Opens a new window](http://datos.gob.es/sites/default/files/2024-08/li_rrss.svg)](https://www.linkedin.com/company/datos-gob-es/)

[![Image 15: Follow us on X. Opens a new window](http://datos.gob.es/sites/default/files/2024-03/X_rrss.svg)](https://x.com/datosgob)

[![Image 16: Follow us on Instagram. Opens a new window](http://datos.gob.es/sites/default/files/2024-03/ig_rrss.svg)](https://www.instagram.com/datosgob/)

[![Image 17: Follow us on YouTube. Opens a new window](http://datos.gob.es/sites/default/files/2024-03/yt_rrss.svg)](https://www.youtube.com/user/datosgob)

[![Image 18: Follow us on Spotify. Opens a new window](http://datos.gob.es/sites/default/files/2025-10/spotify_rrss.svg)](https://open.spotify.com/show/32fn8GQ7rDQ9LDNgWsApPt)

[![Image 19: Follow us on SlideShare. Opens a new window](http://datos.gob.es/sites/default/files/2024-08/slideshare_rrss.svg)](https://es.slideshare.net/datosgob)

[![Image 20: Follow us on Flickr. Opens a new window](http://datos.gob.es/sites/default/files/2024-08/flkr_rrss.svg)](https://www.flickr.com/photos/datosgob/)

[![Image 21: Follow us on GitHub. Opens a new window](http://datos.gob.es/sites/default/files/2024-08/github_rrss.svg)](https://github.com/datosgobes)

[![Image 22: Ministry for Digital Transformation and Public Service](http://datos.gob.es/sites/default/files/2025-03/logo_ministerio_transformacion_digital.jpg)](https://digital.gob.es/index.html)

[![Image 23: Red.es](http://datos.gob.es/sites/default/files/2025-03/logo_red-es.svg)](https://www.red.es/es)

[![Image 24: Iniciativa Aporta](http://datos.gob.es/sites/default/files/2024-03/logo-iniciativa-aporta_positivo.svg)](http://datos.gob.es/en/what-we-do)
