---
title: "Knowledge Layer"
sidebar_position: 7
description: "Capa de proyectos dedicada a ingestar, estructurar, publicar y consultar conocimiento de manera reutilizable."
---

# Knowledge Layer

**Group ID:** `G`

## One-liner

Capa de proyectos dedicada a ingestar, estructurar, publicar y consultar conocimiento de manera reutilizable.

## Context

Este grupo reúne los componentes que convierten chats, documentos, medios, sesiones y otros materiales en una base de conocimiento consultable, publicable y aprovechable por personas o agentes. Su propósito es evitar que el trabajo cognitivo quede atrapado en historiales o archivos sueltos y darle una forma más durable, recuperable y transformable. Sigue activo porque funciona como sustrato transversal para memoria, publicación, retrieval, resúmenes y automatización inteligente. El progreso real en este grupo se ve cuando los contratos son más claros, la ingesta más robusta y las superficies de consulta o publicación más útiles.

## Projects

## GPT Chats Ingest to Bus

**Project ID:** `8`

**One-liner**

Pipeline para transformar historiales de chats en eventos o registros integrables al bus de conocimiento.

**Context**

Este proyecto busca tomar conversaciones de ChatGPT u otras sesiones afines y llevarlas a una estructura compatible con tu ecosistema de buses y procesamiento de conocimiento. Existe para que esos chats no queden como islas cerradas, sino como materia prima reutilizable para resumen, clustering, búsqueda, publicación o memoria. Sigue activo porque gran parte de tu trabajo intelectual pasa por chats y capturas conversacionales, y perderlos como activos estructurados sería costoso. El progreso real consiste en mejorar la ingesta, preservar mejor contexto y producir registros suficientemente limpios para downstream.

## KB September 2025 Sandbox

**Project ID:** `10`

**One-liner**

Sandbox experimental para probar ideas tempranas de knowledge base y procesamiento cognitivo.

**Context**

Este proyecto funciona como un espacio de exploración y prueba para enfoques de base de conocimiento desarrollados en una etapa temprana de tu ecosistema. Su motivación es conservar, revisar o rescatar primitivas, patrones y decisiones técnicas que pudieron haber sido exploratorias pero todavía útiles. Sigue activo porque sirve como cantera de ideas y como registro de evolución conceptual y técnica de tu stack de conocimiento. El progreso real se ve cuando lográs distinguir mejor qué vale rescatar, qué conviene archivar y qué puede integrarse a sistemas más maduros.

## Session Mining / Clustering

**Project ID:** `11`

**One-liner**

Herramientas para minar sesiones y agrupar trabajo cognitivo en clusters o buckets reutilizables.

**Context**

Este proyecto apunta a extraer estructura de sesiones, conversaciones o logs para agruparlas en temas, frentes o buckets más manejables. Existe para reducir caos en el historial de trabajo y facilitar reentrada, análisis y gobierno de grandes volúmenes de material cognitivo. Sigue activo porque la utilidad de tu journal, tus chats y tus sesiones depende en parte de poder encontrar patrones y agrupaciones útiles sin releer todo manualmente. El progreso real consiste en obtener clusters más interpretables, mejores criterios de agrupación y salidas que ayuden a gestión o recuperación.

## KB Contracts

**Project ID:** `13`

**One-liner**

Contratos canónicos para gobernar cómo entra, circula y se transforma el conocimiento en tu ecosistema.

**Context**

Este proyecto define reglas, formatos y seams de integración para que distintos componentes de tu capa de conocimiento hablen el mismo idioma. Su motivación es evitar una proliferación de pipelines incompatibles, decisiones locales incoherentes y outputs difíciles de reutilizar. Sigue activo porque tu ecosistema creció lo suficiente como para necesitar contratos explícitos que ordenen inputs, outputs y responsabilidades. El progreso real se ve cuando más componentes respetan esos contratos y la integración entre sistemas de conocimiento requiere menos trabajo ad hoc.

## Digest Engine

**Project ID:** `15`

**One-liner**

Motor para producir digests a partir de eventos, sesiones o materiales estructurados del ecosistema.

**Context**

Este proyecto se encarga de generar resúmenes periódicos o temáticos que condensan actividad, señales o contenidos del sistema en artefactos más legibles. Existe para convertir acumulación de material en una vista sintetizada que sirva para review, seguimiento o publicación interna. Sigue activo porque el digest es una de las salidas más valiosas cuando el volumen de información crece y la lectura directa deja de escalar. El progreso real consiste en separar mejor cómputo y publicación, mejorar calidad del resumen y lograr que los digests sirvan realmente para orientarse o decidir.

## Media-to-Text Pipeline

**Project ID:** `19`

**One-liner**

Pipeline para convertir contenido mediático en texto procesable por herramientas de análisis y conocimiento.

**Context**

Este proyecto transforma materiales provenientes de medios o formatos no textuales en texto utilizable para clasificación, búsqueda, resumen o incorporación a la base de conocimiento. Su motivación es ampliar el universo de fuentes que pueden entrar a tu ecosistema, evitando que audio, video u otras superficies queden fuera del procesamiento downstream. Sigue activo porque la inteligencia producida por tus sistemas mejora cuando más fuentes pueden entrar en forma tratable. El progreso real consiste en hacer la conversión más confiable, conservar mejor información útil y facilitar su integración con pipelines posteriores.

## NER-to-Knowledge-Base Pipeline

**Project ID:** `21`

**One-liner**

Pipeline que usa reconocimiento de entidades para poblar o enriquecer la base de conocimiento.

**Context**

Este proyecto toma salidas de NER o extracción de entidades y las convierte en insumos útiles para construir o enriquecer estructuras de conocimiento. Existe para pasar de menciones sueltas en texto a objetos o relaciones más reutilizables dentro de tu ecosistema. Sigue activo porque la extracción semiestructurada de entidades puede acelerar mucho clasificación, linking y navegación del conocimiento. El progreso real se ve cuando las entidades son más limpias, el mapeo al modelo de KB es más claro y los resultados enriquecen de verdad la base downstream.

## Quartz Dev Journal / Docusaurus Publication Infrastructure

**Project ID:** `30`

**One-liner**

Infraestructura de publicación para materializar journals y conocimiento en superficies navegables.

**Context**

Este proyecto reúne la capa de tooling, scripts y convenciones que permite publicar tu dev journal y otros materiales en superficies como Quartz o Docusaurus. Su motivación es convertir contenido acumulado en una publicación estable, navegable y mantenible, sin exigir reconstrucción manual permanente. Sigue activo porque la publicación es una pieza central para memoria, reentrada y visibilidad del trabajo realizado. El progreso real consiste en mejorar materialización, automatización, robustez de build y calidad de las superficies generadas.

## AI Paper Chunker (RAG System - Nov 2025)

**Project ID:** `32`

**One-liner**

Sistema para fragmentar papers y prepararlos como corpus utilizable por pipelines de retrieval y RAG.

**Context**

Este proyecto se centra en tomar papers académicos y convertirlos en chunks bien estructurados para búsqueda, embedding, resumen o retrieval asistido. Existe para que los documentos largos entren mejor en sistemas de consulta y procesamiento, y para sostener una plataforma de trabajo más escalable sobre literatura académica. Sigue activo porque el chunking de calidad condiciona fuertemente la utilidad del retrieval downstream. El progreso real se ve cuando los chunks preservan mejor sentido, la preparación del corpus es más robusta y el sistema soporta mejor consultas o análisis posteriores.

## Doc retrieval UI (cheap streamlit query-retrieval tool)

**Project ID:** `37`

**One-liner**

Interfaz liviana para consultar corpus documentales mediante retrieval sin montar una plataforma pesada.

**Context**

Este proyecto ofrece una superficie barata y rápida para hacer consultas sobre documentos ya indexados, priorizando utilidad inmediata sobre sofisticación de producto. Su motivación es contar con una forma práctica de probar y usar retrieval sobre corpus propios sin esperar una UI compleja o full-stack. Sigue activo porque te permite validar valor, depurar pipelines y usar conocimiento indexado con baja fricción. El progreso real consiste en mejorar experiencia de consulta, relevancia de resultados y acople limpio con la infraestructura de indexing existente.

## EPH Survey ML Student Thesis Supervision

**Project ID:** `51`

**One-liner**

Frente de supervisión técnica para una tesis de ML aplicada a datos de la EPH.

**Context**

Este proyecto cubre tu trabajo de acompañamiento, revisión y dirección técnica sobre una tesis estudiantil basada en datos de la EPH y modelos de machine learning. Existe para sostener continuidad, feedback útil y criterio metodológico sin perder tiempo en reentender todo desde cero cada semana. Sigue activo porque la supervisión requiere memoria operativa, control de avances y capacidad de intervenir sobre riesgos metodológicos o de implementación. El progreso real se ve cuando recuperás rápidamente contexto, detectás mejor los puntos críticos y lográs guiar al estudiante hacia avances más sólidos y consolidables.

## EPH / INDEC Extract & Harmonize

**Project ID:** `52`

**One-liner**

Pipeline para extraer y armonizar datos de EPH/INDEC en una estructura usable para análisis y modelado.

**Context**

Este proyecto se ocupa de tomar fuentes de EPH/INDEC y llevarlas a una forma más homogénea y explotable para análisis, modelado y trabajo académico. Su motivación es reducir la fricción recurrente de trabajar con datos complejos, variables heterogéneas y convenciones cambiantes, creando una base más limpia para downstream. Sigue activo porque la calidad de los análisis y modelos depende mucho de la solidez de la extracción y armonización inicial. El progreso real consiste en mejorar cobertura, consistencia de variables y facilidad de uso del dataset resultante.
