/**
* Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
*/
export enum Orientation {
    
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



