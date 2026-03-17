from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

#TODO Fix recitation hours to be correct for this semester.
RECITATION_HOURS = {
    "a": ("09:00", "09:50"),
    "b": ("10:00", "10:50"),
    "c": ("11:00", "11:50"),
    "d": ("12:00", "12:50"),
    "e": ("13:00", "13:50"),
    "f": ("14:00", "14:50"),
}
MICROSERVICE_LINK = "http://17313-teachers.s3d.cmu.edu:8080/section_info/"


@app.get("/section_info/{section_id}")
def get_section_info(section_id: str):

    if section_id is None:
        raise HTTPException(status_code=404, detail="Missing section id")

    section_id = section_id.lower()

    if section_id not in RECITATION_HOURS:
        raise HTTPException(status_code=404, detail="Invalid section id")

    response = requests.get(MICROSERVICE_LINK + section_id)

    data = response.json()
    print(data)
    ta_name_list = data["ta"]
    ta1_name = ta_name_list[0]
    ta2_name = ta_name_list[1]

    print(ta1_name)

    start_time, end_time = RECITATION_HOURS[section_id]
    return {
        "section": section_id,
        "start_time": start_time,
        "end_time": end_time,
        "ta": ta_name_list
    }
