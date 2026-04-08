import json

jobs_dict = {}


def import_jobs():
    with open("jobs.json") as f:
        jobs_dict = json.load(f)

    return jobs_dict
