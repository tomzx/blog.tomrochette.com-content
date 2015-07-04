/*
 title: Apache Hit Tracker
 Author: tomzx
 Template: page
 Permalink: /portfolio/apache-hit-tracker/
*/
**Description**  
Compte le nombre de d'accès et la taille de chaque requête exécutée par un serveur Apache. Il s'agit d'un petit outil qui se grèffe à Apache, c'est-à-dire que l'ensemble des sorties vers les logs sont redirigées vers ce programme.  
En utilisant **LogFormat "%v %B" hits** comme format de log, et **CustomLog "| /usr/local/bin/hitme" hits** afin de rediriger la sortie des logs, ce programme comptabilise l'utilisation des ressources du serveur par hôte virtuel.

**Snippet**

<pre class="brush: cpp; title: ; notranslate" title="">class Hit {
public:
   Hit();
   ~Hit();
   void nHit(unsigned int size);
   int getHits();
   long long getBytes();
   void setHits(int h);
   void setBytes(long long b);
private:
   int hits;
   long long bytes;
};
</pre>

**Options(features)**

*   Comptabilise le nombre de requêtes et bande passante totale
*   Simple à attacher
*   Garde en mémoire l'ensemble des activités dans les 5 dernières minutes, puis les flush régulièrement

**Aperçu**