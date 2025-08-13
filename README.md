Resume Checker
A simple Python script that compares a resume text file against a job description text file to identify matching and missing keywords.

Features
Stopwords removal: Ignores common filler words like the, and, is, etc.

Plural normalization: Converts plural words to singular form (e.g., skills → skill, policies → policy).

Keyword matching: Finds words that appear in both files.

Missing keyword detection: Shows words in the job description that are not in the resume.

Requirements
Python 3.x

Usage
```bash
python resume_checker.py <resume_file> <job_description_file>
```

Example
```bash
python resume_checker.py data/resume.txt data/job.txt
```

Output Example
```
Resume content:
...

Job description:
...

Processed Resume Words (20):
['python', 'sql', 'skill', ...]

Processed Job Words (20):
['python', 'sql', 'data', ...]

matching words: ['python', 'sql']
missing words: ['data']
match rate: 66.67%
```
