<?php

if (count($argv) !== 4) {
	echo 'php '.$argv[0].' author title year'.PHP_EOL;
	exit;
}

// Get author name
$author = $argv[1];
// Get paper title
$title = $argv[2];
// Get paper year
$year = $argv[3];
$folder = preg_replace('/[ -.:!?()\[\]]+/', '-', strtolower($author.' '.$title));
$folder = trim($folder, '-');
$folderPath = 'papers/'.$folder;
$articlePath = $folderPath.'/article.md';
$bibliographyPath = $folderPath.'/article.bib';

// Confirm

if (file_exists($folderPath)) {
	echo 'Paper article already exist. Stopping.'.PHP_EOL;
	exit(-1);
}

// Generate folder
mkdir($folderPath);
// Copy template.md to article.md
copy('template.md', $articlePath);
touch($bibliographyPath);
// Update the article title and date
$articleTitle = $author.' - '.$title.' ('.$year.')';
$content = file_get_contents($articlePath);
$content = str_replace('Template', $articleTitle, $content);
$content = str_replace('YYYY-MM-DD', date('Y-m-d'), $content);
file_put_contents($articlePath, $content);
echo 'Created '.$articlePath.PHP_EOL;

// Append to papers/article.md
$authorText = '## '.$author;
$articleText = '* ['.$title.' ('.$year.')]('.$folder.')';
$content = PHP_EOL.PHP_EOL.$authorText.PHP_EOL.$articleText;
file_put_contents('papers/article.md', $content, FILE_APPEND);
echo 'Updated papers/article.md'.PHP_EOL;

// Append to my-path-to-agi/article.md
$articleText = '### '.$title.' ('.date('Y-m').' - ?)';
$authorText = $author;
$content = PHP_EOL.PHP_EOL.$articleText.PHP_EOL.$authorText;
file_put_contents('my-path-to-agi/article.md', $content, FILE_APPEND);
echo 'Updated my-path-to-agi/article.md'.PHP_EOL;

// Go to Google scholar to get appropriate reference
$escapedTitle = urlencode($title);
$url = 'https://scholar.google.ca/scholar?hl=en&q='.$escapedTitle;
$url = str_replace('&', '^&', $url);
passthru('start '.$url);
