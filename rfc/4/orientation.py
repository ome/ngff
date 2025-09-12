from __future__ import annotations 

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal 
from enum import Enum 
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    field_validator
)


metamodel_version = "None"
version = "0.2.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'contributors': ['orcid:0000-0001-9475-3756', 'orcid:0000-0002-4920-8123'],
     'created_by': 'orcid:0000-0003-1666-5421',
     'created_on': '2025-05-29T00:00:00',
     'default_prefix': 'ngff',
     'default_range': 'string',
     'description': 'This schema defines a standardized way to describe the axes '
                    'of multidimensional image data. It allows each axis to be '
                    'clearly labeled (e.g., spatial, temporal, channel), assigned '
                    'appropriate units (such as micrometers or seconds), and, when '
                    'relevant, include orientation information to specify the '
                    'direction of measurement. The goal is to make axis metadata '
                    'explicit, consistent, and machine-readable—helping tools, '
                    'datasets, and users work together seamlessly and reduce '
                    'ambiguity in data interpretation and processing.',
     'id': 'https://w3id.org/ome/ngff',
     'imports': ['linkml:types'],
     'name': 'OME_NGFF_Axes',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'ngff': {'prefix_prefix': 'ngff',
                           'prefix_reference': 'https://w3id.org/ome/ngff/'},
                  'ome': {'prefix_prefix': 'ome',
                          'prefix_reference': 'https://w3id.org/ome/'},
                  'orcid': {'prefix_prefix': 'orcid',
                            'prefix_reference': 'https://orcid.org/'}},
     'source_file': 'orientation.yml'} )

class AxesNames(str, Enum):
    t = "t"
    """
    Axis name relating to the time axis.
    """
    c = "c"
    """
    Axis name relating to the channel axis.
    """
    z = "z"
    """
    Axis name relating to the z or depth axis.
    """
    y = "y"
    """
    Axis relating to the y or height axis.
    """
    x = "x"
    """
    Axis relating to the x or width axis.
    """


class SpaceAxesNames(str, Enum):
    z = "z"
    """
    Axis name relating to the z or depth axis.
    """
    y = "y"
    """
    Axis relating to the y or height axis.
    """
    x = "x"
    """
    Axis relating to the x or width axis.
    """


class AxisType(str, Enum):
    channel = "channel"
    """
    Represents distinct image acquisition channels, typically corresponding to different fluorescence markers, stains, or detection modalities. Each channel captures a specific signal or wavelength, and the axis distinguishes among them in the image data.

    """
    space = "space"
    """
    Denotes spatial dimensions of the image, such as physical axes in 2D or 3D (e.g., x, y, z). These axes map directly to coordinates in the sample or scene and often have associated physical units like microns.

    """
    time = "time"
    """
    Represents a temporal axis capturing the progression of image data over time points or frames. It is used in time-lapse imaging or dynamic studies to distinguish image slices acquired at different moments.

    """


class SpaceUnit(str, Enum):
    angstrom = "angstrom"
    attometer = "attometer"
    centimeter = "centimeter"
    decimeter = "decimeter"
    exameter = "exameter"
    femtometer = "femtometer"
    foot = "foot"
    gigameter = "gigameter"
    hectometer = "hectometer"
    inch = "inch"
    kilometer = "kilometer"
    megameter = "megameter"
    meter = "meter"
    micrometer = "micrometer"
    mile = "mile"
    millimeter = "millimeter"
    nanometer = "nanometer"
    parsec = "parsec"
    petameter = "petameter"
    picometer = "picometer"
    terameter = "terameter"
    yard = "yard"
    yoctometer = "yoctometer"
    yottameter = "yottameter"
    zeptometer = "zeptometer"
    zettameter = "zettameter"


class TimeUnit(str, Enum):
    attosecond = "attosecond"
    centisecond = "centisecond"
    day = "day"
    decisecond = "decisecond"
    exasecond = "exasecond"
    femtosecond = "femtosecond"
    gigasecond = "gigasecond"
    hectosecond = "hectosecond"
    hour = "hour"
    kilosecond = "kilosecond"
    megasecond = "megasecond"
    microsecond = "microsecond"
    millisecond = "millisecond"
    minute = "minute"
    nanosecond = "nanosecond"
    petasecond = "petasecond"
    picosecond = "picosecond"
    second = "second"
    terasecond = "terasecond"
    yoctosecond = "yoctosecond"
    yottasecond = "yottasecond"
    zeptosecond = "zeptosecond"
    zettasecond = "zettasecond"


class AnatomicalOrientationValues(str, Enum):
    """
    Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
    """
    left_to_right = "left-to-right"
    """
    Describes the directional orientation from the left side to the right lateral side of an anatomical structure or body.
    """
    right_to_left = "right-to-left"
    """
    Describes the directional orientation from the right side to the left lateral side of an anatomical structure or body.
    """
    anterior_to_posterior = "anterior-to-posterior"
    """
    Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body.
    """
    posterior_to_anterior = "posterior-to-anterior"
    """
    Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body.
    """
    inferior_to_superior = "inferior-to-superior"
    """
    Describes the directional orientation from below (inferior) to above (superior) in an anatomical structure or body.
    """
    superior_to_inferior = "superior-to-inferior"
    """
    Describes the directional orientation from above (superior) to below (inferior) in an anatomical structure or body.
    """
    dorsal_to_ventral = "dorsal-to-ventral"
    """
    Describes the directional orientation from the top/upper (dorsal) to the belly/lower (ventral) in an anatomical structure or body.
    """
    ventral_to_dorsal = "ventral-to-dorsal"
    """
    Describes the directional orientation from the belly/lower (ventral) to the top/upper (dorsal) in an anatomical structure or body.
    """
    dorsal_to_palmar = "dorsal-to-palmar"
    """
    Describes the directional orientation from the top/upper (dorsal) to the palm of the hand (palmar) in a body.
    """
    palmar_to_dorsal = "palmar-to-dorsal"
    """
    Describes the directional orientation from the palm of the hand (palmar) to the top/upper (dorsal) in a body.
    """
    dorsal_to_plantar = "dorsal-to-plantar"
    """
    Describes the directional orientation from the top/upper (dorsal) to the sole of the foot (plantar) in a body.
    """
    plantar_to_dorsal = "plantar-to-dorsal"
    """
    Describes the directional orientation from the sole of the foot (plantar) to the top/upper (dorsal) in a body.
    """
    rostral_to_caudal = "rostral-to-caudal"
    """
    Describes the directional orientation from the nasal (rostral) to the tail (caudal) end of an anatomical structure, typically used in reference to the central nervous system.
    """
    caudal_to_rostral = "caudal-to-rostral"
    """
    Describes the directional orientation from the tail (caudal) to the nasal (rostral) end of an anatomical structure, typically used in reference to the central nervous system.
    """
    cranial_to_caudal = "cranial-to-caudal"
    """
    Describes the directional orientation from the head (cranial) to the tail (caudal) end of an anatomical structure or body.
    """
    caudal_to_cranial = "caudal-to-cranial"
    """
    Describes the directional orientation from the tail (caudal) to the head (cranial) end of an anatomical structure or body.
    """
    proximal_to_distal = "proximal-to-distal"
    """
    Describes the directional orientation from the center of the body to the periphery of an anatomical structure or limb.
    """
    distal_to_proximal = "distal-to-proximal"
    """
    Describes the directional orientation from the periphery of an anatomical structure or limb to the center of the body.
    """



class Axes(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ome/ngff'})

    axes: Optional[list[Union[ChannelAxis, SpaceAxis, TimeAxis]]] = Field(default=None, description="""A list of axes. Although serialized as list, it MUST be dealt with as being a set as in the name of each axis MUST be unique. Furthermore, if the attribute orientation is defined for one axis of type space, it MUST be defined for all the axes of type space. In this case, the type of each orientation MUST be the same and the value MUST be unique.
""", json_schema_extra = { "linkml_meta": {'alias': 'axes',
         'any_of': [{'range': 'SpaceAxis'},
                    {'range': 'TimeAxis'},
                    {'range': 'ChannelAxis'}],
         'domain_of': ['Axes']} })


class Axis(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/ome/ngff'})

    name: AxesNames = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Axis']} })
    type: AxisType = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Axis', 'Orientation']} })


class ChannelAxis(Axis):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'defining_slots': ['name', 'type'],
         'from_schema': 'https://w3id.org/ome/ngff',
         'slot_usage': {'name': {'equals_string': 'c',
                                 'ifabsent': 'string(c)',
                                 'name': 'name',
                                 'range': 'string'},
                        'type': {'equals_string': 'channel',
                                 'ifabsent': 'string(channel)',
                                 'name': 'type',
                                 'range': 'string'}}})

    name: Literal["c"] = Field(default="c", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Axis'],
         'equals_string': 'c',
         'ifabsent': 'string(c)'} })
    type: Literal["channel"] = Field(default="channel", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Axis', 'Orientation'],
         'equals_string': 'channel',
         'ifabsent': 'string(channel)'} })


class SpaceAxis(Axis):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'defining_slots': ['name', 'type', 'unit'],
         'from_schema': 'https://w3id.org/ome/ngff',
         'slot_usage': {'name': {'name': 'name', 'range': 'SpaceAxesNames'},
                        'type': {'equals_string': 'space',
                                 'ifabsent': 'string(space)',
                                 'name': 'type',
                                 'range': 'string'}}})

    unit: SpaceUnit = Field(default=..., description="""Physical unit for spatial measurement along the axis, selected from a standardized list of distance units (e.g., micrometer, nanometer).
""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['SpaceAxis', 'TimeAxis']} })
    orientation: Optional[AnatomicalOrientation] = Field(default=None, description="""The direction of an axis of type space.""", json_schema_extra = { "linkml_meta": {'alias': 'orientation',
         'any_of': [{'range': 'AnatomicalOrientation'}],
         'domain_of': ['SpaceAxis']} })
    name: SpaceAxesNames = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'name', 'domain_of': ['Axis']} })
    type: Literal["space"] = Field(default="space", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Axis', 'Orientation'],
         'equals_string': 'space',
         'ifabsent': 'string(space)'} })


class TimeAxis(Axis):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'defining_slots': ['unit'],
         'from_schema': 'https://w3id.org/ome/ngff',
         'slot_usage': {'name': {'equals_string': 't',
                                 'ifabsent': 'string(t)',
                                 'name': 'name',
                                 'range': 'string'},
                        'type': {'equals_string': 'time',
                                 'ifabsent': 'string(time)',
                                 'name': 'type',
                                 'range': 'string'}}})

    unit: TimeUnit = Field(default=..., description="""Temporal unit of measurement for the axis, selected from standardized time units (e.g., second, minute, hour).
""", json_schema_extra = { "linkml_meta": {'alias': 'unit', 'domain_of': ['SpaceAxis', 'TimeAxis']} })
    name: Literal["t"] = Field(default="t", json_schema_extra = { "linkml_meta": {'alias': 'name',
         'domain_of': ['Axis'],
         'equals_string': 't',
         'ifabsent': 'string(t)'} })
    type: Literal["time"] = Field(default="time", json_schema_extra = { "linkml_meta": {'alias': 'type',
         'domain_of': ['Axis', 'Orientation'],
         'equals_string': 'time',
         'ifabsent': 'string(time)'} })


class Orientation(ConfiguredBaseModel):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True, 'from_schema': 'https://w3id.org/ome/ngff'})

    type: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Axis', 'Orientation']} })
    value: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Orientation']} })


class AnatomicalOrientation(Orientation):
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ome/ngff'})

    type: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'type', 'domain_of': ['Axis', 'Orientation']} })
    value: str = Field(default=..., json_schema_extra = { "linkml_meta": {'alias': 'value', 'domain_of': ['Orientation']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
Axes.model_rebuild()
Axis.model_rebuild()
ChannelAxis.model_rebuild()
SpaceAxis.model_rebuild()
TimeAxis.model_rebuild()
Orientation.model_rebuild()
AnatomicalOrientation.model_rebuild()

