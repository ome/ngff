from __future__ import annotations
from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict, conlist
from typing import Annotated, Hashable, List, TypeVar
from pydantic_core import PydanticCustomError
from pydantic import AfterValidator, Field, ValidationError

T = TypeVar('T', bound=Hashable)

def _validate_unique_list(v: list[T]) -> list[T]:
    if len(v) != len(set(v)):
        raise PydanticCustomError('unique_list', 'List must be unique')
    return v

UniqueList = Annotated[List[T], AfterValidator(_validate_unique_list), Field(json_schema_extra={'uniqueItems': True})]

class Axis(BaseModel, frozen=True):
    name: str
    type: Optional[str] = None
    unit: Optional[str] = None

class ScaleTransform(BaseModel, frozen=True):
    type: Literal["scale"]
    scale: conlist(float, min_length=1)

class TranslationTransform(BaseModel, frozen=True):
    type: Literal["translation"]
    translation: conlist(float, min_length=1)

class Dataset(BaseModel, frozen=True):
    path: str
    coordinateTransformations: tuple[ScaleTransform] | tuple[ScaleTransform, TranslationTransform]

class Multiscale(BaseModel, frozen=True):
    """
    The multiscale datasets for this image
    """
    name: Optional[str] = None
    datasets: conlist(Dataset, min_length=1)
    axes: UniqueList[Axis]
    coordinateTransformations: Optional[tuple[ScaleTransform] | tuple[ScaleTransform, TranslationTransform]] = None
    version: Literal['0.5-dev']

class Window(BaseModel, frozen=True):
    start: float
    end: float
    min: float
    max: float

class RenderingSettings(BaseModel, frozen=True):
    window: Window
    label: str
    family: str
    color: str
    active: bool

class Omero(BaseModel, frozen=True):
    channels: list[RenderingSettings]

class GroupMetadata(BaseModel, frozen=True):
    """
    JSON from OME-NGFF .zattrs
    """
    model_config = ConfigDict(title="NGFF Image")
    multiscales: conlist(Multiscale, min_length=1)
    omero: Optional[Omero] = None

def make_schema():
    import json
    schema = GroupMetadata.model_json_schema()
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"
    schema["$id"] = "https://ngff.openmicroscopy.org/latest/schemas/image.schema"

    print(json.dumps(schema, indent=2))

if __name__ == '__main__':
    make_schema()