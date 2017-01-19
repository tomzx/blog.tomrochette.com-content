<?php

if (count($argv) !== 4) {
	echo 'php '.$argv[0].' author title year'.PHP_EOL;
	exit;
}

// Get author name
$author = $argv[1];
// Get book title
$title = $argv[2];
// Get book year
$year = $argv[3];
$folder = preg_replace('/[ -.:!?()\[\]]+/', '-', strtolower($author.' '.$title));
$folder = trim($folder, '-');
$folderPath = 'books/'.$folder;
$articlePath = $folderPath.'/article.md';

// Confirm

// Generate folder
mkdir($folderPath);
// Copy template.md to article.md
copy('template.md', $articlePath);
// Update the article title and date
$articleTitle = $author.' - '.$title.' - '.$year;
$content = file_get_contents($articlePath);
$content = str_replace('Template', $articleTitle, $content);
$content = str_replace('2016-01-01', date('Y-m-d'), $content);
file_put_contents($articlePath, $content);
echo 'Created '.$articlePath.PHP_EOL;

// Append to books/article.md
$authorText = '## '.$author;
$articleText = '* ['.$title.' ('.$year.')]('.$folder.')';
$content = PHP_EOL.PHP_EOL.$authorText.PHP_EOL.$articleText;
file_put_contents('books/article.md', $content, FILE_APPEND);
echo 'Updated books/article.md'.PHP_EOL;

// Append to my-path-to-agi/article.md
$articleText = '### '.$title.' ('.date('Y-m').' - ?)';
$authorText = $author;
$content = PHP_EOL.PHP_EOL.$articleText.PHP_EOL.$authorText;
file_put_contents('my-path-to-agi/article.md', $content, FILE_APPEND);
echo 'Updated my-path-to-agi/article.md'.PHP_EOL;