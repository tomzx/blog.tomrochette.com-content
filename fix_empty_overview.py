#!/usr/bin/env python3

import re
import os

def fix_empty_overview(file_path):
    """
    Remove empty Overview sections from a markdown file.
    Returns True if the file was modified, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Pattern to match:
        # - Overview header (# or ## or ### etc. followed by "Overview")
        # - Any number of blank lines
        # - Until the next header (# line) or end of file
        pattern = r'^(#{1,6})\s*Overview\s*$\n(\s*\n)*(?=^#{1,6}|\Z)'
        
        # Replace with empty string, using multiline mode
        content = re.sub(pattern, '', content, flags=re.MULTILINE)
        
        # Check if file was modified
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

# List of files to process
files_to_fix = [
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/value-estimation/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/research-methodology-and-organization/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/neurosciences/an-integrative-theory-of-prefrontal-cortex-function/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/note-taking/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/php/business-model/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/php/halite/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/yuxuan-wang-tacotron-towards-end-to-end-speech-synthesis/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/shallow-iterative-networks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/template.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/tomas-mikolov-efficient-estimation-of-word-representations-in-vector-space/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/volodymyr-mnih-human-level-control-through-deep-reinforcement-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/volodymyr-mnih-playing-atari-with-deep-reinforcement-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/wei-ping-deep-voice-3-2000-speaker-neural-text-to-speech/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/xuan-bach-le-history-driven-program-repair/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/yingfei-xiong-precise-condition-synthesis-for-program-repair/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/yoav-freund-a-decision-theoretic-generalization-of-on-line-learning-and-an-application-to-boosting/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/yoshua-bengio-curriculum-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/neil-rabinowitz-machine-theory-of-mind/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/ralf-herbrich-learning-and-generalization-theoretical-bounds/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/ronen-brafman-r-max-a-general-polynomial-time-algorithm-for-near-optimal-reinforcement-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/theodore-bluche-scan-attend-and-read-end-to-end-handwritten-paragraph-recognition-with-mdlstm-attention/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/thomas-anthony-thinking-fast-and-slow-with-deep-learning-and-tree-search/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/tom-mitchell-never-ending-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/levente-kocsis-bandit-based-monte-carlo-planning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/manuel-lopes-the-strategic-student-approach-for-life-long-exploration-and-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/max-jaderberg-reading-text-in-the-wild-with-convolutional-neural-networks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/nal-kalchbrenner-grid-long-short-term-memory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/eric-laukien-feynman-machine-the-universal-dynamical-systems-computer/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/greg-linden-amazon-com-recommendations-item-to-item-collaborative-filtering/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/j-r-quinlan-induction-of-decision-trees/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/jacob-devlin-robustfill-neural-program-learning-under-noisy-i-o/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/karl-friston-the-free-energy-principle-a-unified-brain-theory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/kelvin-xu-show-attend-and-tell-neural-image-caption-generation-with-visual-attention/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/burr-settles-a-trainable-spaced-repetition-model-for-language-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/david-silver-mastering-chess-and-shogi-by-self-play-with-a-general-reinforcement-learning-algorithm/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/david-silver-the-predictron-end-to-end-learning-and-planning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/alex-graves-offline-handwriting-recognition-with-multidimensional-recurrent-neural-networks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/andrew-barto-intrinsically-motivated-learning-of-hierarchical-collections-of-skills/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/ashish-vaswani-attention-is-all-you-need/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/frameworks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/handwriting-recognition/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/alex-graves-automated-curriculum-learning-for-neural-networks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/alex-graves-multi-dimensional-recurrent-neural-networks/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/papers/alex-graves-neural-turing-machines/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/daily-log/2017-06-02/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/daily-log/2017-07-29/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/daily-log/2018-01-20/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/daily-log/2018-02-17/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/machine-learning/courses/david-silver-reinforcement-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/identity-and-access-management/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/intelligence-augmentation/text-autocompletion/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/kubernetes/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/books/kenneth-blanchard-the-one-minute-manager/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/docker/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/books/andy-hunt-pragmatic-thinking-and-learning/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/books/daniel-kahneman-thinking-fast-and-slow/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/wikibot/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/structuring-an-agi-research/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/template.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/the-brain/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/tom-bot/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/understanding-games/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/resources-limited-agents/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/reverse-engineering/eurisko/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/state-machines/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/recording-information/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/program-equivalence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/presentations/principles-of-hierarchical-temporal-memory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/presentations/the-future-of-artificial-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/problem-resolution-approaches/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/roman-yampolskiy-from-seed-ai-to-technological-singularity-via-recursively-self-improving-software/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/scott-aaronson-why-philosophers-should-care-about-computational-complexity/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/shane-legg-machine-super-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/the-copycat-project-a-model-of-mental-fluidity-and-analogy-making/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/the-novamente-artificial-intelligence-engine/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/the-opennars-implementation-of-the-non-axiomatic-reasoning-system/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/viggo-ahl-an-experimental-comparison-of-five-prioritization-methods/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/perfect-storage-medium/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/playing-with-data/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/marcus-hutter-a-complete-theory-of-everything-will-be-subjective/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/marcus-hutter-can-intelligence-explode/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/max-tegmark-is-the-theory-of-everything-merely-the-ultimate-ensemble-theory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/patrice-godefroid-automating-software-testing-using-program-analysis/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/peter-voss-essentials-of-general-intelligence-the-direct-path-to-artificial-general-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/report-on-a-general-problem-solving-program/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/john-storrs-hall-self-improving-ai-an-analysis/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/jurgen-schmidhuber-godel-machines-fully-self-referential-optimal-universal-self-improvers/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/jurgen-schmidhuber-one-big-net-for-everything/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/jurgen-schmidhuber-the-new-ai-general-sound-relevant-for-physics/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/keith-hoyes-3d-simulation-the-key-to-ai/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/kun-xie-brain-computation-is-organized-via-power-of-two-based-permutation-logic/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/lukasz-kaiser-program-search-as-a-path-to-artificial-general-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/hans-moravec-when-will-computer-hardware-match-the-human-brain/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/hugo-de-garis-artificial-brains/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/irving-john-good-speculations-concerning-the-first-ultraintelligent-machine/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/jack-copeland-computable-number-a-guide/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/joe-tsien-a-postulate-on-the-brain-s-basic-wiring-logic/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/breden-lake-building-machines-that-learn-and-think-like-people/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/contemporary-approaches-to-artificial-general-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/my-path-to-agi/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/natural-language/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/alan-biermann-approaches-to-automatic-programming/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/alan-turing-computing-machinery-and-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/papers/alan-turing-systems-of-logic-based-on-ordinals/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/mass-refactoring/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/mathematics-based-agi/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/memory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/minimal-skills-curriculum/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/my-approach-to-agi/v0.3.0/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/interacting-with-an-agi/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/knowledge-base/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/life-recording/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/graph-architectures/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/intelligence-amplification/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/compression/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/consciousness/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/current-approaches/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/databases/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/code-architect/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/communication-medium/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatgpt/assistant/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatgpt/chatgpt-self/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatgpt/limitations/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatgpt/memory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/thomas-cover-elements-of-information-theory/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/thomas-fahringer-advanced-symbolic-analysis-for-compilers/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/toby-segaran-programming-the-semantic-web/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/build-an-agi-using-polya-method/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatbot/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/chatgpt/anthropomorphgpt/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/scott-gilbert-developmental-biology/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/max-tegmark-life-3-0-being-human-in-the-age-of-artificial-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/nick-bostrom-superintelligence-paths-dangers-strategies/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/paul-jorgensen-software-testing-a-craftsmans-approach/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/jeff-hawkins-on-intelligence/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/john-johnston-the-allure-of-machinic-life-cybernetics-artificial-life-and-the-new-ai/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/jose-hernandez-orallo-the-measure-of-all-minds/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/lion-kimbro-how-to-make-a-complete-map-of-every-thought/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/david-sterratt-principles-of-computational-modelling-in-neuroscience/article.md",
    "/home/runner/work/blog.tomrochette.com-content/blog.tomrochette.com-content/agi/books/flemming-nielson-principles-of-program-analysis/article.md"
]

modified_files = []

print("Processing files with empty Overview sections...")
for file_path in files_to_fix:
    if fix_empty_overview(file_path):
        modified_files.append(file_path)
        print(f"✓ Fixed: {file_path}")
    else:
        print(f"- No changes needed: {file_path}")

print(f"\nTotal files processed: {len(files_to_fix)}")
print(f"Files modified: {len(modified_files)}")

print("\nModified files:")
for file_path in modified_files:
    print(f"  {file_path}")