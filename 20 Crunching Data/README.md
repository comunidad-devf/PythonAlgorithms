# Crunching Data

En Dev.f contamos con una base de datos de usuarios la cual tiene la siguiente estructura:

| id | email | first_name | last_name | age | program | score  |
|----|-------|------------|-----------|-----|---------|--------|

Te será entregada toda esa información pero de manera desordenada y dispersa en muchos archivos, tu tarea es analizar esa data, unificarla y reunirla de nuevo en un tres formatos, JSON, XML y CSV.

El archivo `users_database.json` contiene únicamente el **id**, el **email** y la **age**.

El archivo `users_database.xml` contiene únicoamente el **id**, el **first_name** y el **last_name**

Y el archivo `users_database.csv` contiene únicamente el **id**, el **program** y el **score**

Notarás que cada archivo **no** tiene ordenada la información, es decir que el **JSON** puede comenzar con el usuario **144**, el **XML** con el usuario **1421** y el **CSV** con el **1** así que analiza toda esta información cuidadosamennte de manera que no haya conflictos. 

**Nota** : Estaría genial que puedieras seguir las normas y guías de estilo de cada formato a la hora de nombrar a las propiedades, las buenas prácticas son nuestras amigas.
