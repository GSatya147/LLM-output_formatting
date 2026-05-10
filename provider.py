import json

from job_postings.job_postings import POST_LIST
from src.pydantic_instr import extractor

def call_api(prompt, options, context) -> dict:
    try:
        index = int(context['vars']['job_index'])
        job_text = POST_LIST[index]
        model_json = extractor(job_text)
        return {"output": model_json}
    except Exception as e:
        with open("debug.log", "a") as f:
            f.write(f"index={context['vars']['job_index']} error={str(e)}\n")
        return {"output": None, "error": str(e)}
