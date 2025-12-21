---
title: Simulateur de métro
taxonomy:
  readability: 3
---

**Description**
Le simulateur de métro est un système faisant la gestion des trains d'un métro fictif. Il est composé de 3 composantes distinctes communiquant entre elles: Un contrôleur principal, des mini-contrôleurs et des trains. Le contrôleur gère l'ensemble des mini-contrôleurs, alors que chaque mini-contrôleur se charge des trains sur sa voie. Conséquemment, les trains ne se chargent de personne, ils ne font que recevoir des messages d'un des mini-contrôleurs, leur supérieur direct.
La simulation doit gérer le déplacement de l'ensemble des trains afin qu'il n'y ait pas de problèmes (collisions). De plus, on simule des pannes qui ont pour objectif d'arrêter les trains sur une voie spécifique (gérée par un mini-contrôleur).

**Snippet**
<pre><code class="language-cpp line-numbers">
void gererInterruption(int sig)
{
	int status;
	// On envoi un SIGINT à chaque mini-contrôleur
	for (unsigned int i = 0; i &lt; nbLignes; ++i) {
		kill(lignes[i].PID, SIGINT);
		close(lignes[i].fd);
		unlink(lignes[i].nom);
		waitpid(lignes[i].PID, &status, 0);
	}

	printf("FIN DU CONTRÔLEUR PID %d.\n", getpid());

	exit(EXIT_SUCCESS);
}
</code></pre>

**Options(features)**

**Aperçu**
