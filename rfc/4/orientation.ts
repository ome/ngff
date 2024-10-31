/**
* Anatomical orientation refers to the specific arrangement and directional alignment of anatomical structures within an imaging dataset. It is crucial for ensuring accurate alignment and comparison of images to anatomical atlases, facilitating consistent analysis and interpretation of biological data.
*/
export enum Orientation {
    
    /** Describes the directional orientation from the left side to the right side of an anatomical structure or body. */
    left_to_right = "left-to-right",
    /** Describes the directional orientation from the right side to the left side of an anatomical structure or body. */
    right_to_left = "right-to-left",
    /** Describes the directional orientation from the front (anterior) to the back (posterior) of an anatomical structure or body. */
    anterior_to_posterior = "anterior-to-posterior",
    /** Describes the directional orientation from the back (posterior) to the front (anterior) of an anatomical structure or body. */
    posterior_to_anterior = "posterior-to-anterior",
    /** Describes the directional orientation from the lower (inferior) to the upper (superior) part of an anatomical structure or body. */
    inferior_to_superior = "inferior-to-superior",
    /** Describes the directional orientation from the upper (superior) to the lower (inferior) part of an anatomical structure or body. */
    superior_to_inferior = "superior-to-inferior",
    /** Describes the directional orientation from the back (dorsal) to the front (ventral) of an anatomical structure or body. */
    dorsal_to_ventral = "dorsal-to-ventral",
    /** Describes the directional orientation from the front (ventral) to the back (dorsal) of an anatomical structure or body. */
    ventral_to_dorsal = "ventral-to-dorsal",
    /** Describes the directional orientation from the front (rostral) to the back (caudal) end of an anatomical structure, typically used in reference to the central nervous system. */
    rostral_to_caudal = "rostral-to-caudal",
    /** Describes the directional orientation from the back (caudal) to the front (rostral) end of an anatomical structure, typically used in reference to the central nervous system. */
    caudal_to_rostral = "caudal-to-rostral",
};



