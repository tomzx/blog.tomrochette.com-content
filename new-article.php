<?php

if (count($argv) !== 2) {
	echo 'php '.$argv[0].' title'.PHP_EOL;
	exit;
}

// Get paper title
$title = $argv[1];
$folder = preg_replace('/[ -.:!?()\[\]\\/]+/', '-', strtolower($title));
$folder = trim($folder, '-');
$folderPath = $folder;
$articlePath = $folderPath.'/article.md';
$bibliographyPath = $folderPath.'/article.bib';

// Confirm

if (file_exists($folderPath)) {
	echo 'Article already exist. Stopping.'.PHP_EOL;
	exit(-1);
}

// Generate folder
mkdir($folderPath);
// Copy template.md to article.md
copy('template.md', $articlePath);
touch($bibliographyPath);
// Update the article title and date
$content = file_get_contents($articlePath);
$content = str_replace('Template', $title, $content);
$content = str_replace('YYYY-MM-DD', date('Y-m-d'), $content);
file_put_contents($articlePath, $content);
echo 'Created '.$articlePath.PHP_EOL;
