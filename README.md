# Purpose
Automatically generate pymetrics test report

# Usage
Please login with pymetrics account and download the report (html) manually. For the 3 categories (coginitive, social, emotional) in the report, please download separately.  
(Note: When saving the html file from the browser, please set the format as "Webpage, Complete")
```
usage: parser.py [-h] [-f file_name] [-t threshold] [-v show_title]

optional arguments:
  -h, --help     show this help message and exit
  -f file_name   the html file you want to parse
  -t threshold   the threshold to decide your identities (percentage, default 75)
  -v show_title  if you do not want to show the title on each item, set it as zero (default 1)
```
# Example
```
python parser.py -f pymetrics.html -t 80
```
## Output
```
[Memory Span] You remember longer strings of information (91.09%)
[Planning Accuracy] A planner (89.6%)
[Distraction Filtering Ability] You're great at screening out distractions (85.15%)
[Attention Duration] Attentive (85.15%)
```
## Japanese version output
```
[記憶範囲] 長く連鎖する情報を記憶します (91.09%)
[計画の精度] 綿密な計画を立てます (89.6%)
[障害を判別する能力] 障害を判別することが得意です (85.15%)
[注意力の持続] 注意深いです (85.15%)
```
# Python version
3.5.1

# Issue
3 categories (cognitive, social, emotional) should be processed separately.  
If you want to print the result in the same file, try
```
python parser.py -f social.html >> results.txt
python parser.py -f cogonitive.html >> results.txt
python parser.py -f emotional.html >> results.txt
```
(Thanks Sauyee)
