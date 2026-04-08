from typing import Literal,Annotated
import pickle
import pandas as pd
from pydantic import BaseModel,Field
from fastapi import FastAPI
from fastapi.responses import JSONResponse


with open('model2.pkl','rb') as f:
    model=pickle.load(f)

app=FastAPI()

class USerInput(BaseModel):
    continent:Annotated[str,Field(...)]
    education_of_employee:Annotated[str,Field(...)]
    has_job_experience:Annotated[str,Field(...)]
    requires_job_training:Annotated[str,Field(...)]

    no_of_employees:Annotated[int,Field(...)]
    
    region_of_employment:Annotated[str,Field(...)]

    prevailing_wage:Annotated[int,Field(...)]
    unit_of_wage:Annotated[str,Field(...)]
    full_time_position:Annotated[str,Field(...)]




@app.post('/predict')
def predict_output(data:USerInput):
    input_df=pd.DataFrame([{
        'continent':data.continent,
        'education_of_employee':data.education_of_employee,
        'has_job_experience':data.has_job_experience,
        'requires_job_training':data.requires_job_training,
        'no_of_employees':data.no_of_employees,
        'region_of_employment':data.region_of_employment,
        'prevailing_wage':data.prevailing_wage,
        'unit_of_wage':data.unit_of_wage,
        'full_time_position':data.full_time_position
}])
    prediction=int(model.predict(input_df)[0])
    result = "Denied" if prediction == 0 else "Approved"
    return JSONResponse(status_code=200,content={'predict USA visa ':result})
    


