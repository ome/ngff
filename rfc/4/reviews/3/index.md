# **RFC-4: Review 3**

(rfcs:rfc4:review3)=

* [https://github.com/ome/ngff/pull/253](https://github.com/ome/ngff/pull/253)
* [https://ngff.openmicroscopy.org/rfc/4/](https://ngff.openmicroscopy.org/rfc/4/)
* [https://ngff.openmicroscopy.org/rfc/1/templates/review\_template.html](https://ngff.openmicroscopy.org/rfc/1/templates/review_template.html)

**Review Authors**: Dave Horsfall
**Conflicts of Interest**: None declared

This review was primarily generated through discussions during a Hannifa Lab meeting, which involved diverse roles, including wet lab scientists, clinicians, bioinformaticians, data scientists, and engineers. I have tried to capture the key points of discussion in this review.

## Summary

The RFC proposes an optional ***orientation*** field for the OME-NGFF specification to explicitly define axis direction using a controlled vocabulary. We support this addition. In fields like spatial transcriptomics and high-resolution histology, biological symmetry often makes it impossible to determine orientation after acquisition.

## Significant Comments and Questions

### **Clarification: "Subject-Local" vs "Patient-Global" Orientation**

The current proposal seems primarily geared toward imaging where the subject is a whole patient. In spatial transcriptomics and pathology, our subject is frequently a tissue biopsy, or histology slide.

* **The Gap:** The RFC states this metadata "MUST only be used... where the subject is roughly aligned to the imaging axes." In our use cases, we may not know how the biopsy was aligned to the patient, but we do know the internal orientation of the tissue itself.
* **Recommendation:** Clarify that "subject" can refer to local tissue structures. For a skin biopsy, the z-axis is "Superficial-to-Deep" regardless of the sample's original global position on the donor. Supporting local orientation makes this RFC universally applicable to the tissue-profiling community without requiring full "Patient-to-Atlas" registration.

### **Controlled Vocabulary Expansion**

The current vocabulary has a focus on biped/quadruped canonical directions. To support clinical and other research contexts (e.g., dermatology, cardiology, and oncology), we recommend adding terms that describe layered and polarized tissues to controlled vocabulary:

* ***superficial-to-deep*** / ***deep-to-superficial***: for layered tissues like skin, gut, or cortex.
* ***apical-to-basal*** / ***basal-to-apical***: for epithelial layers and polarized cell structures.
* ***apex-to-base*** / ***base-to-apex***: for specific organs like the heart or lungs.

### **Integration with RFC-5: A semantic bridge to Transformation?**

We see RFC-4 is a critical prerequisite for the successful implementation of RFC-5 (Transformations). While RFC-5 provides the mathematical framework for coordinate transforms, RFC-4 provides the necessary biological context.

* **Semantic Labeling:** RFC-5 allows us to define a transformation to a Common Coordinate Framework. We envisage that through explicit labels provided by RFC-4, a registration tool might programmatically determine if it needs to apply a flip or rotation to align with an atlas, etc.
* This might be outside the scope of this RFC, but establishing the relationship between RFC-4 and RFC-5 is important and we would be happy to offer input and collaborate on this in the future.

### **Recommendation**

* Accept, with minor changes

Explicitly support Subject-Local orientation and expand the vocabulary to include layered-tissue terms.
