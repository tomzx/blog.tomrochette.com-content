<?php

if (count($argv) !== 2) {
	echo 'php '.$argv[0].' title'.PHP_EOL;
	exit;
}

// Get paper title
$title = $argv[1];
$folder = preg_replace('/[ -.:!?()\[\]]+/', '-', strtolower($author.' '.$title));
$folder = trim($folder, '-');
$folderPath = $folder;
$articlePath = $folderPath.'/article.md';

// Confirm

// Generate folder
mkdir($folderPath);
// Copy template.md to article.md
copy('template.md', $articlePath);
// Update the article title and date
$content = file_get_contents($articlePath);
$content = str_replace('Template', $title, $content);
$content = str_replace('2016-01-01', date('Y-m-d'), $content);
file_put_contents($articlePath, $content);
echo 'Created '.$articlePath.PHP_EOL;