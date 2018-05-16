---
title: Simulateur de réseau
---

**Description**
Le simulateur de réseau émule un système de communication faisant usage de sémaphores afin de partager un nombre limité d'imprimantes communes. Tous les ordinateurs reçoivent une partie différente d'un «feed» qui contient des instructions sur ce que l'ordinateur doit effectuer. L'une de ces instructions est d'imprimer le contenu actuel de la mémoire de l'ordinateur. Pour se faire, il faut toutefois obtenir une imprimante, ce qui n'est pas toujours possible.

**Snippet**
<pre><code class="language-cpp line-numbers">
// Attendre le mutex de cet ordinateur
sem_wait(&mutexOrdinateurs[ordi-&gt;mId-1]);

// Si terminé, simplement activer le prochain ordi
if (ordi-&gt;aTermine) {
   	// Libérer le mutex du prochain ordinateur
    prochain = (ordi-&gt;mId) % nbOrdinateurs;

    if (prochain != 0) {
        sem_post(&mutexOrdinateurs[prochain]);
    } else {
        // Libérer le mutex principal
        sem_post(&mutexPrincipal);
    }
    continue;
}

// Quelle instruction?
instructionMaintenant = ordi-&gt;instructions.front();
</code></pre>

**Options(features)**

**Aperçu**
