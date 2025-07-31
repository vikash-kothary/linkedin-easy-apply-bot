from datetime import datetime
import re
from linkedin_easy_apply_bot.backend.utils import json_utils

job_ids = None


def get_job_ids():
    global job_ids
    if job_ids is None:
        job_ids = json_utils.read_json_from_file("files/data/jobs.json")
    return job_ids


def create_new_job(job_id):

    job_ids = get_job_ids()

    if job_id not in job_ids:

        job_ids[job_id] = {"is_processed": False}

    return job_ids[job_id]


def update_job(
    job_id,
    button,
    browserTitle,
    salary,
    has_applied=False,
    file_path="files/data/jobs.csv",
):

    job_ids = get_job_ids()

    if job_id in job_ids:
        job_ids[job_id]["is_processed"] = True

    def re_extract(text, pattern):
        target = re.search(pattern, text)
        if target:
            target = target.group(1)
        return target

    job_ids[job_id]["timestamp"] = datetime.now().isoformat()
    job_ids[job_id]["can_easy_apply"] = False if button == False else True
    job_ids[job_id]["job"] = re_extract(
        browserTitle.split(" | ")[0], r"\(?\d?\)?\s?(\w.*)"
    )
    job_ids[job_id]["company"] = re_extract(browserTitle.split(" | ")[1], r"(\w.*)")
    job_ids[job_id]["salary"] = salary

    json_utils.data_to_json("files/data/jobs.json", job_ids)
