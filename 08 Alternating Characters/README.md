# Utopian Tree

Eme es una persona un poco especial, a él sólo le gustan las cadenas de texto que
contengan letras consecutivas que sean diferentes. Por ejemplo, a el le encanta
la cadena de texto `ABABA`, mientras que odia y lo pone de malas la cadena `ABAA`.

Dicho esto, dada una cadena de texto que sólo contiene los caracteres `A` y `B`,
tenemos que escribir un programa que convierta esa cadena de texto en una que a Eme
le guste. Para hacer esto, únicamente tenemos permitido borrar letras.

Tu tarea es escribir un programa que encuentre el número mínimo de letras que
tenemos que borrar para obtener un texto que tranquilice a Eme.

**Nota:** Alternando caracteres es un problema de implementación originalmente escrito
en [Hacker Rank](https://www.hackerrank.com/challenges/alternating-characters).

## Ejemplo

**Entrada**: `AAAA`

**Salida**: `3`

**Explicación**: `A`
____

**Entrada**: `BBBBB`

**Salida**: `4`

**Explicación**: `B`
____

**Entrada**: `ABABABAB`

**Salida**: `0`

**Explicación**: `ABABABAB` es un texto que a Eme le gustaría.
____

**Entrada**: `BABABA`

**Salida**: `0`

**Explicación**: `BABABA` es un texto que a Eme le gustaría.
____

**Entrada**: `AAABBB`

**Salida**: `4`

**Explicación**: `AB` es un texto que a Eme le gustaría. Tuvimos que borrar 2 `A`s y 2 `B`s
____
