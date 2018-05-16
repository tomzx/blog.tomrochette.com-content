---
title: Gestionnaire d’espace web pour hébergeur
---

**Description**
Il s'agit d'un système complet de panneau de contrôle pour hébergement. Il permet entre autre de modifier les préférences de l'utilisateur, de modifier ses configurations de bases de données, de modifier les accès à ses fichiers via FTP et beaucoup plus. L'architecture modulaire de l'application permet de facilement ajouter de nouvelles options au panneau de contrôle.

**Snippet**
<pre><code class="language-php line-numbers">
public function addModules($name)
{
	$module = new $name();
	if ($module-&gt;getStatus() === 'ON') {
   		$this-&gt;modules_[$module-&gt;getModuleName()] = $module;
		++$this-&gt;nModules_;
	}
}
</code></pre>

**Options(features)**
*   Gestion complète d'un compte utilisateur
*   Gestion de base de données et utilisateurs MySQL
*   Gestion d'accès FTP
*   Gestion DNS
*   Gestion courriel
*   Gestion d'abonnements
*   Modulaire, ajout de nouveaux modules facile
*   Support multilingue

**Aperçu**
