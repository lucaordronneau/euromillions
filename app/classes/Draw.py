from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Draw(BaseModel):
    """Class of a complete draw

    Args:
        BaseModel
    """
    Date : Optional[datetime] = Field(None, description = "date time format exiged YYYY-MM-DD")
    N1 : int = Field(..., gt = 0, lt = 51 , description = ' N1 must be an INT between 1 and 50 (included)' , example = 1)
    N2 : int = Field(..., gt = 0, lt = 51 , description = ' N2 must be an INT between 1 and 50 (included)' , example = 34)
    N3 : int = Field(..., gt = 0, lt = 51 , description = ' N3 must be an INT between 1 and 50 (included)' , example = 2)
    N4 : int = Field(..., gt = 0, lt = 51 , description = ' N4 must be an INT between 1 and 50 (included)' , example = 13)
    N5 : int = Field(..., gt = 0, lt = 51 , description = ' N5 must be an INT between 1 and 50 (included)' , example = 50)
    E1 : int = Field(..., gt = 0, lt = 13 , description = ' E1 must be an INT between 1 and 12 (included)' , example = 1)
    E2 : int = Field(..., gt = 0, lt = 13 , description = ' E2 must be an INT between 1 and 12 (included)' , example = 12)
    Winner : Optional[int] = Field(None, ge = 0, description = 'nb of winner must be an INT > 0')
    Gain : Optional[int] = Field(..., ge = 0, description= " monney ammount should be an INT > 0 ")
    

class DrawPredict(BaseModel):
    """Class of a draw with only numbers

    Args:
        BaseModel
    """
    N1 : int = Field(..., gt = 0, lt = 51 , description = ' N1 must be an INT between 1 and 50 (included)' , example = 1)
    N2 : int = Field(..., gt = 0, lt = 51 , description = ' N2 must be an INT between 1 and 50 (included)' , example = 34)
    N3 : int = Field(..., gt = 0, lt = 51 , description = ' N3 must be an INT between 1 and 50 (included)' , example = 2)
    N4 : int = Field(..., gt = 0, lt = 51 , description = ' N4 must be an INT between 1 and 50 (included)' , example = 13)
    N5 : int = Field(..., gt = 0, lt = 51 , description = ' N5 must be an INT between 1 and 50 (included)' , example = 50)
    E1 : int = Field(..., gt = 0, lt = 13 , description = ' E1 must be an INT between 1 and 12 (included)' , example = 1)
    E2 : int = Field(..., gt = 0, lt = 13 , description = ' E2 must be an INT between 1 and 12 (included)' , example = 12)
