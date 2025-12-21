---
title: Apache Logger/Splitter
taxonomy:
  readability: 3
---

**Description**  
Apache Logger/Splitter enregistre les logs d'Apache dans des fichiers différents dans le but de pouvoir donner accès à ces fichiers aux utilisateurs qui désireraient les consulter. Par défaut, Apache n'offre pas de moyen de séparer automatiquement les logs autre que par des logiciels tierce. Apache Logger/Splitter est simple et extrèmement facile à employer.  
Il se connecte via *pipe* à la sortie des logs, **CustomLog "| /usr/local/bin/splitme -d /var/logs/access -f access_log" combined** et reçoit un **LogFormat "%v %h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\"" combined** assez complet (semblable à celui de Awstats).

**Snippet**
<pre class="brush: cpp; title: ; notranslate" title="">void Pointeur::write(string vhost, string content)
{
   if (files.find(vhost) == files.end()) {
      open(vhost);
   }
   // Remettre l'usage à la fin
   list&lt;string&gt;::iterator pos = usage.begin();
   if (size != 0) {
      while (pos != usage.end()) {
         if (*pos == vhost) {
            break;
         }
         ++pos;
      }
      if (pos != usage.end()) {
         usage.erase(pos);
      }
   }
   usage.push_back(vhost);
   if (streams[files[vhost]].is_open()) {
      streams[files[vhost]] &lt;&lt; content &lt;&lt; endl;
   }
   streams[files[vhost]].flush();
}
</pre>

**Options(features)**
*   Facile à ajouter à Apache
*   Sépare les logs Apache par hôte virtuel, pour les écrirent dans des fichier/répertoires différents
*   Round-robin de 100 unités

**Aperçu**
