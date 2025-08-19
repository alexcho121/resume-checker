Resume Checker

A small Python script that compares a resume text file and a job description text file to show overlapping keywords, missing keywords, and a simple match rate. The result is also saved as JSON.

##Project Story
1) Why I started

While preparing applications, I wanted a quick way to check:
“Does my resume actually include the keywords the JD asks for?”
Manual comparison was tedious, and I preferred a lightweight, transparent tool over a heavy solution.

2) What I added along the way

Basic preprocessing pipeline: lowercasing → remove special chars → remove stopwords → plural→singular

Simple comparison logic: use sets to compute overlaps, missing terms, and match rate

JSON output: save results to resume_match_result.json so I can keep records per job posting (for later comparison/analysis)

3) What I wanted but postponed

Weighted matching (give more weight to core tech skills)

Synonyms / alias normalization (developer↔programmer, REST↔RESTful, etc.)

JD sentence snippets (show the sentence where a missing keyword appears)
I had these ideas, but with my current time/skill trade-offs, I couldn’t guarantee accuracy. To keep the tool honest, I focused on a checklist-style output first.

4) What worked well / What’s missing

Worked well

Quickly surfaces missing keywords

JSON logging makes per-posting comparison easy

Runs on standard library only

Missing

No context/importance/experience-level understanding → not for precise judgment

Match rate can be skewed if general words slip in (no tech-only filter yet)

##Features

Preprocessing: lowercasing, special-char removal, stopword removal, plural→singular

Comparison: overlapping words, missing words, simple match rate

Output: saves results to resume_match_result.json

Note: No context understanding or importance inference. It’s a checklist tool.

##Usage
```bash
python resume_checker.py <resume_file> <job_description_file>

python resume_checker.py data/resume.txt data/job.txt
```

Output Example
```bash
matching words: ['python', 'sql']
missing words: ['data']
match rate: 66.67%

Saved JSON: resume_match_result.json
```

resume_match_result.json
```json
{
  "matching_words": ["python", "sql"],
  "missing_words": ["data"],
  "match_rate": 66.67
}
```

Tech

Python 3.x

Standard library: argparse, re, json

Next (Optional)

Show JD sentence snippets for each missing keyword

Add a tech-only filter (count only technology terms)

Introduce weights/synonyms gradually if needed











