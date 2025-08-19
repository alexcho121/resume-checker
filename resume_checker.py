import re
import argparse
import json


STOPWORDS = {
     "a","an","the","and","or","but","to","of","for","in","on","with","by","at","from",
    "as","is","are","be","this","that","it","its","your","you","we","our"
}

def singularize(w: str) -> str:

    if len(w)<=2:
        return w
    
    # -ies -> -y (policies -> policy)
    if len(w)>3 and w.endswith("ies"):
        return w[:-3] + "y"
    
    # remove -es (boxes -> box)
    if len(w)>2 and w.endswith("es"):
        return w[:-2] 
    
    # remove -s (skills -> skill)
    if w.endswith(("ss","us","is")):
        return w
    
    if len(w)>1 and w.endswith("s"):
        return w[:-1]
    
    return w

def preprocess_text(text):
    text=text.lower()
    text=re.sub(r"[^a-z0-9\s]", " ", text)
    words=text.split()
    words = [w for w in words if w not in STOPWORDS]
    normed=[singularize(w) for w in words if w]
    return normed

def main():
    parser=argparse.ArgumentParser()
    #Create an ArgumentParser object
    parser.add_argument("resume_file", help="Path to the resume text file")
    parser.add_argument("job_file", help="Path to the job description text file")
     # These are the "fields" in the form: resume_file and job_file
    args=parser.parse_args()
    try:
        with open(args.resume_file, 'r', encoding='utf-8') as c:
            resume_text=c.read()
            if resume_text.strip()=="":
                print("resume file is empty. ")
                exit(1)

    except FileNotFoundError:
        print(f"Cannot find files: {args.resume_file}")
        exit(1)   

    try:     
        with open(args.job_file, 'r', encoding='utf-8') as c:
            job_text=c.read()
            if job_text.strip()=="":
                print("job file is empty. ")
                exit(1)
                
    except FileNotFoundError:
        print(f"Cannot find files: {args.job_file}")
        exit(1)

    print("Resume content: ")
    print(resume_text[:200])

    print("\nJob description: ")
    print(job_text[:200])

    resume_words=preprocess_text(resume_text)
    job_words = preprocess_text(job_text)

    print("\nProcessed Resume Words (20):")
    print(resume_words[:20])

    print("\nProcessed Job Words (20):")
    print(job_words[:20])

    resume_set = set(resume_words)
    job_set = set(job_words)

    matching_words = resume_set&job_set
    missing_words = job_set-resume_set

    if job_set:
        match_rate=len(matching_words) / len(job_set) * 100
    else:
        match_rate=0

    print(f"\nmatching words: {sorted(list(matching_words))}")
    print(f"\nmissing words: {sorted(list(missing_words))}")
    print(f"\nmatch rate: {match_rate:.2f}%")

    result={
        "matching_words":sorted(list(matching_words)),
        "missing_words": sorted(list(missing_words)),
        "match_rate": round(match_rate,2)
    }

    with open("resume_match_result.json", "w", encoding="utf-8") as f:
        json.dump(result,f, ensure_ascii=False, indent=2)
    
    print("\n Saved JSON: resume_match_result.json")


if __name__=="__main__":
    main()