from app.schemas.input_data import InputData
from pandas import DataFrame
from pydantic import BaseModel, validator
from sklearn.pipeline import Pipeline


class Model(BaseModel):
    model: Pipeline

    @validator("model")
    def pipeline_has_predict(cls, model: Pipeline) -> Pipeline:
        if not hasattr(model[-1], "predict"):
            raise ValueError("Model has no predict method.")
        return model

    def predict(self, input_data: InputData) -> float:
        input_dataframe = DataFrame.from_records([input_data.dict()])

        pred_value = self.model.predict(input_dataframe)

        return pred_value

    class Config:
        arbitrary_types_allowed = True
