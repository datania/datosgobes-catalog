Title: API - datos.gob.es

URL Source: http://datos.gob.es/en/accessible-apidata

Markdown Content:
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
