/*
 title: Simulateur de tic tac toe
 Author: tomzx
 Template: page
 Permalink: /portfolio/simulateur-de-tic-tac-toe/
*/
**Description**  
Le simulateur de TicTacToe est un système très simple développé en microC. Il s'agit d'un système communicant via mailboxes (sémaphores). Il est possible de créer des grilles de jeux de tailles variables (3 à 25), dans lesquels une intelligence articifielle «de base» essaie de gagner la partie contre des rivaux (aussi intelligences artificielles).

**Snippet**

<pre><code class="language-cpp line-numbers">for(;;) {
    OSMboxPend(mailboxJoueurs[numero-1], &messageLu, 0);
    // Réfléchir durant une periode de temps
    OSTimeDly((rand() % 2*MAX_TICKS) + MAX_TICKS);
    messageEnvoye.ligne = rand() % tailleGrille;
    messageEnvoye.colonne = rand() % tailleGrille;
    
    while(grilleMiroir[messageEnvoye.ligne][messageEnvoye.colonne] !=0) {
        messageEnvoye.ligne = rand() % tailleGrille;
        messageEnvoye.colonne = rand() % tailleGrille;
    }
    
    printf("Joueur %d : (%d,%d)\n", numero, messageEnvoye.ligne, messageEnvoye.colonne);
    OSMboxPost(mailboxControleur[numero-1], (void *)&messageEnvoye);
}
</code></pre>

**Options(features)**

*   Possibilité de créer des grilles de TicTacToc de 3 à 25 de côté
*   Intelligences artificielles «stupides»
*   Gestion des priorités dans le système (il s'agit d'un système en temps réel)

**Aperçu**
