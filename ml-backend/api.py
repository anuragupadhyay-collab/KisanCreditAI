import os
import sys
from fastapi import FastAPI, HTTPException
from typing import Union, List, Dict, Any
import sklearn
import joblib
import sys

# Ensure that the src directory is in sys.path
SRC_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if SRC_DIR not in sys.path:
    sys.path.insert(0, SRC_DIR)

from src.module_predict import predict

app = FastAPI(title="KisanCredit AI Backend API")


@app.get("/")
def read_root():
    return {
        "status": "running",
        "service": "KisanCredit AI Backend"
    }

@app.get("/version")
def version():
    return {
        "python": sys.version,
        "sklearn": sklearn.__version__,
        "joblib": joblib.__version__,
    }


@app.post("/predict")
def get_prediction(payload: Union[Dict[str, Any], List[Dict[str, Any]]]):
    try:
        prediction = predict(payload)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
