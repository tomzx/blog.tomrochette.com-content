<?php

// TODO(tom@tomrochette.com): Check if reachable from given entry points

$pagesDirectory = realpath(__DIR__);
$agiDirectory = realpath($pagesDirectory.'/agi');
$machineLearningDirectory = realpath($pagesDirectory.'/machine-learning');
$problemsDirectory = realpath($pagesDirectory.'/problems');
$processesDirectory = realpath($pagesDirectory.'/processes');
$questionsDirectory = realpath($pagesDirectory.'/questions');

$startPages = [
    $agiDirectory => true,
    $machineLearningDirectory => true,
    $problemsDirectory => true,
    $processesDirectory => true,
    $questionsDirectory => true,
];

$redBackground = "\033[41m";
$greenBackground = "\033[42m";
$endColor = "\033[0m";

$countBroken = 0;
$references = [];
$articles = [];

$pattern = '/\.md$/';

foreach ($startPages as $startPage => $dontCare) {
    $directoryIterator = new RecursiveDirectoryIterator($startPage);
    $iterator = new RecursiveIteratorIterator($directoryIterator);
    $files = new RegexIterator($iterator, $pattern, RegexIterator::MATCH);

    // TODO: It appears that the article regex matches #anchor
    $articleRegex = '/\[[^\]]+\]\((?!.{0,5}\:\/\/|#)(?<path>[^)]+?)(?<alt> "[^)]+")?\)/';
    foreach ($files as $file) {
        $file = (string)$file;
        echo 'Scanning ' . $file . PHP_EOL;
        $fileDirectory = dirname($file);
        $articles[$file] = true;
        $content = file_get_contents($file);
        preg_match_all($articleRegex, $content, $matches);
        foreach ($matches['path'] as $path) {
            // $directory = realpath($fileDirectory.'/'.$path);
            // if ( ! $directory) {
            //     $fileExists = false;
            // } else {
            //     $references[$directory][$fileDirectory] = true;
            //     $file = file_exists($directory); // If an asset, check the file exists
            //     $files = glob($directory.'/{item,article}.md', GLOB_BRACE);
            //     $fileExists = $file || count($files) > 0;
            // }
            $hashPosition = strpos($path, '#');
            if ($hashPosition !== false) {
                $path = substr($path, 0, $hashPosition);
            }
            $fullPath = realpath($fileDirectory.'/'.$path);
            $fileExists = file_exists($fullPath);
            if ($fileExists) {
                $references[$fullPath][$file] = true;
            }

            $countBroken = $fileExists ? $countBroken : ++$countBroken;
            $color = $fileExists ? $greenBackground : $redBackground;
            echo "\t" . $color . $path . ' ' . ($fileExists ? 'OK' : 'BROKEN') . $endColor . PHP_EOL;
        }
    }
}

echo 'Scan done.'.PHP_EOL.PHP_EOL;

echo 'References'.PHP_EOL;
foreach ($references as $reference => $referrers) {
    echo $reference . PHP_EOL;
    foreach ($referrers as $reference => $dontCare) {
        echo "\t" . $reference . PHP_EOL;
    }
}

echo PHP_EOL.PHP_EOL;
echo 'Articles not referred'.PHP_EOL;

$notReferred = array_keys(array_diff_key($articles, $references, $startPages));
sort($notReferred);
$countNotReferred = count($notReferred);
foreach ($notReferred as $article) {
    echo $article.PHP_EOL;
}

echo PHP_EOL;
$color = $countBroken === 0 ? $greenBackground : $redBackground;
echo $color . 'Broken: ' . $countBroken . $endColor . PHP_EOL;
$color = $countNotReferred === 0 ? $greenBackground : $redBackground;
echo $color . 'Not referred: ' . $countNotReferred . $endColor . PHP_EOL;
