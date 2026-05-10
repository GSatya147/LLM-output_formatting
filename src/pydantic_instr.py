"""
Extracting CV example:
1. Handle environmente error if failed to load env var
2. create a pydantic model with fields
name: str
description optional
education qualifications dictionary with branch, gpa as key and college/university value
projects optional 
experience optional 
skills 
hobbies optional 
interests optional 
3. read the contents from the cv using file reading operations and store everything in a string, if the file is large read in chunks. Handle exceptions like file not exist
4. create an instructor LLM client from provider of choice
5. wrap the create block with response model as pydantic model and string as the messages content.
6. and in exception blocks handle client errors, server errors and generic errors.
7. we can access the output using attributes names in our pydantic model
8. the reason for keeping most of the fields  optional is CVs dont follow a madatory structure and to avoid pipeline breakage, safe to assume most of the fields optional
"""

from datetime import datetime
from typing import Optional

import instructor

# from google import genai
from google.genai import errors
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

PROMPT = "Extract details from the job descriptions"

class JobPost(BaseModel):
    title: str
    company_name: str
    company_overview: Optional[str] = None
    description: str
    required_skills: list[str]
    optional_skills: Optional[list[str]] = None
    location: str
    salary: Optional[str] = None
    posted_date: Optional[datetime] = None


class JobPostings(BaseModel):
    postings: list[JobPost]

def extractor(postlist: str):

    client = instructor.from_provider("google/gemini-3-flash-preview")

    try:
        Job_posting = client.create(
            response_model=JobPostings,
            messages=[
                {
                    "role": "user",
                    "content": PROMPT + "\n" + postlist,
                }
            ],
            max_retries=3,
        )

        return Job_posting.model_dump_json()
    
    except errors.ClientError as e:
        if e.code == 429:
            print("Rate limited..")
            raise

    except errors.ServerError as e:
        print(f"Error: {e}")
        raise

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise

