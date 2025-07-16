
export enum AxesNames {
    
    /** Axis name relating to the time axis. */
    t = "t",
    /** Axis name relating to the channel axis. */
    c = "c",
    /** Axis name relating to the z or depth axis. */
    z = "z",
    /** Axis relating to the y or height axis. */
    y = "y",
    /** Axis relating to the x or width axis. */
    x = "x",
};

export enum SpaceAxesNames {
    
    /** Axis name relating to the z or depth axis. */
    z = "z",
    /** Axis relating to the y or height axis. */
    y = "y",
    /** Axis relating to the x or width axis. */
    x = "x",
};

export enum AxisType {
    
    /** Represents distinct image acquisition channels, typically corresponding to different fluorescence markers,  stains, or detection modalities. Each channel captures a specific signal or wavelength, and the axis  distinguishes among them in the image data.
 */
    channel = "channel",
    /** Denotes spatial dimensions of the image, such as physical axes in 2D or 3D (e.g., x, y, z). These axes map  directly to coordinates in the sample or scene and often have associated physical units like microns.
 */
    space = "space",
    /** Represents a temporal axis capturing the progression of image data over time points or frames.  It is used in time-lapse imaging or dynamic studies to distinguish image slices acquired at different moments.
 */
    time = "time",
};

export enum SpaceUnit {
    
    angstrom = "angstrom",
    attometer = "attometer",
    centimeter = "centimeter",
    decimeter = "decimeter",
    exameter = "exameter",
    femtometer = "femtometer",
    foot = "foot",
    gigameter = "gigameter",
    hectometer = "hectometer",
    inch = "inch",
    kilometer = "kilometer",
    megameter = "megameter",
    meter = "meter",
    micrometer = "micrometer",
    mile = "mile",
    millimeter = "millimeter",
    nanometer = "nanometer",
    parsec = "parsec",
    petameter = "petameter",
    picometer = "picometer",
    terameter = "terameter",
    yard = "yard",
    yoctometer = "yoctometer",
    yottameter = "yottameter",
    zeptometer = "zeptometer",
    zettameter = "zettameter",
};

export enum TimeUnit {
    
    attosecond = "attosecond",
    centisecond = "centisecond",
    day = "day",
    decisecond = "decisecond",
    exasecond = "exasecond",
    femtosecond = "femtosecond",
    gigasecond = "gigasecond",
    hectosecond = "hectosecond",
    hour = "hour",
    kilosecond = "kilosecond",
    megasecond = "megasecond",
    microsecond = "microsecond",
    millisecond = "millisecond",
    minute = "minute",
    nanosecond = "nanosecond",
    petasecond = "petasecond",
    picosecond = "picosecond",
    second = "second",
    terasecond = "terasecond",
    yoctosecond = "yoctosecond",
    yottasecond = "yottasecond",
    zeptosecond = "zeptosecond",
    zettasecond = "zettasecond",
};
/**
* Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
*/
export enum AnatomicalOrientationValues {
    
    /** Describes the directional orientation from the left side to the right lateral side of an anatomical structure or body. */
    left_to_right = "left-to-right",
    /** Describes the directional orientation from the right side to the left lateral side of an anatomical structure or body. */
    right_to_left = "right-to-left",
    /** Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. */
    anterior_to_posterior = "anterior-to-posterior",
    /** Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. */
    posterior_to_anterior = "posterior-to-anterior",
    /** Describes the directional orientation from below (inferior) to above (superior) in an anatomical structure or body. */
    inferior_to_superior = "inferior-to-superior",
    /** Describes the directional orientation from above (superior) to below (inferior) in an anatomical structure or body. */
    superior_to_inferior = "superior-to-inferior",
    /** Describes the directional orientation from the top/upper (dorsal) to the belly/lower (ventral) in an anatomical structure or body. */
    dorsal_to_ventral = "dorsal-to-ventral",
    /** Describes the directional orientation from the belly/lower (ventral) to the top/upper (dorsal) in an anatomical structure or body. */
    ventral_to_dorsal = "ventral-to-dorsal",
    /** Describes the directional orientation from the top/upper (dorsal) to the palm of the hand (palmar) in a body. */
    dorsal_to_palmar = "dorsal-to-palmar",
    /** Describes the directional orientation from the palm of the hand (palmar) to the top/upper (dorsal) in a body. */
    palmar_to_dorsal = "palmar-to-dorsal",
    /** Describes the directional orientation from the top/upper (dorsal) to the sole of the foot (plantar) in a body. */
    dorsal_to_plantar = "dorsal-to-plantar",
    /** Describes the directional orientation from the sole of the foot (plantar) to the top/upper (dorsal) in a body. */
    plantar_to_dorsal = "plantar-to-dorsal",
    /** Describes the directional orientation from the nasal (rostral) to the tail (caudal) end of an anatomical structure, typically used in reference to the central nervous system. */
    rostral_to_caudal = "rostral-to-caudal",
    /** Describes the directional orientation from the tail (caudal) to the nasal (rostral) end of an anatomical structure, typically used in reference to the central nervous system. */
    caudal_to_rostral = "caudal-to-rostral",
    /** Describes the directional orientation from the head (cranial) to the tail (caudal) end of an anatomical structure or body. */
    cranial_to_caudal = "cranial-to-caudal",
    /** Describes the directional orientation from the tail (caudal) to the head (cranial) end of an anatomical structure or body. */
    caudal_to_cranial = "caudal-to-cranial",
    /** Describes the directional orientation from the center of the body to the periphery of an anatomical structure or limb. */
    proximal_to_distal = "proximal-to-distal",
    /** Describes the directional orientation from the periphery of an anatomical structure or limb to the center of the body. */
    distal_to_proximal = "distal-to-proximal",
};



export interface Axes {
    /** A list of axes. Although serialized as list, it MUST be dealt with as being a set as in the name of each axis MUST be unique. Furthermore, if the attribute orientation is defined for one axis of type space, it  MUST be defined for all the axes of type space. In this case, the type of each orientation MUST be the same and the value MUST be unique.
 */
    axes?: string[],
}



export interface Axis {
    name: string,
    type: string,
}



export interface ChannelAxis extends Axis {
}



export interface SpaceAxis extends Axis {
    /** Physical unit for spatial measurement along the axis, selected from a standardized list of distance units  (e.g., micrometer, nanometer).
 */
    unit: string,
    /** The direction of an axis of type space. */
    orientation?: string,
}



export interface TimeAxis extends Axis {
    /** Temporal unit of measurement for the axis, selected from standardized time units (e.g., second, minute, hour).
 */
    unit: string,
}



export interface Orientation {
    type: string,
    value: string,
}



export interface AnatomicalOrientation extends Orientation {
    type: string,
    value: string,
}



