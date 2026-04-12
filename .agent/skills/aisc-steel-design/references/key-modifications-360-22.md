# AISC 360-22 Key Modifications

**Source**: Summary of major changes in 2022 edition from AISC 360-22 Specification pages 7-9.
**Extracted**: 2025-11-09
**Format**: Markdown

---

# PREFACE

(This Preface is not part of ANSI/AISC 360-22, *Specification for Structural Steel Buildings*, but is included for informational purposes only.)

This Specification is based upon past successful usage, advances in the state of knowledge, and changes in design practice. The 2022 American Institute of Steel Construction's *Specification for Structural Steel Buildings* provides an integrated treatment of allowable strength design (ASD) and load and resistance factor design (LRFD), and replaces earlier Specifications. As indicated in Chapter B of the Specification, designs can be made according to either ASD or LRFD provisions.

This ANSI-approved Specification has been developed as a consensus document using ANSI-accredited procedures to provide a uniform practice in the design of steel-framed buildings and other structures. The intention is to provide design criteria for routine use and to provide specific criteria for infrequently encountered problems that occur in the full range of structural design.

This Specification is the result of the consensus deliberations of a committee of structural engineers with wide experience and high professional standing, representing a wide geographical distribution throughout the United States. The committee includes approximately equal numbers of qualified persons in private practice and consulting engineering, engineers in research and teaching, and engineers employed by steel fabricating and producing companies. The contributions and assistance of more than 50 additional professional volunteers working in task committees are also hereby acknowledged.

The Symbols, Glossary, Abbreviations, and Appendices to this Specification are an integral part of the Specification. A nonmandatory Commentary has been prepared to provide background for the Specification provisions and the user is encouraged to consult it. Additionally, nonmandatory User Notes are interspersed throughout the Specification to provide concise practical guidance and suggestions.

A number of significant technical modifications have also been made since the 2016 edition of the Specification, including the following:

- A new table is incorporated into Section A3 that lists allowable grades and strengths and other specific limitations of referenced materials.
- Section J3 adopts ASTM F3148 bolts that provide a strength of 144 ksi. A new SI-unitized installation method is incorporated into Chapter J applicable to these bolts by reference to the RCSC *Specification*.
- Section J4 provides a detailed list related to what information must be provided on structural design documents. These criteria have been moved from the *Code of Standard Practice for Structural Steel Buildings*.
- A new Section A5, Approvals, is added to specifically address the review and approval of approval documents.
- A new Section B8, Dimensional Tolerances, is added to clarify that the provisions of the Specification are based on specific tolerances provided in the *Code of Standard Practice* and referenced ASTM standards.
- Provisions are added in Section E4 for doubly symmetric I-shaped compression members to address lateral bracing that is offset from the shear center.

---


## PREFACE

- For flexural strength of members with holes in the tension flange, it is clarified that the Section F13.1 provisions apply only to bolt holes.
- Provisions are added to Chapter G to permit tension field action in end panels.
- Provisions are added to Chapter H for HSS subjected to combined forces, to include biaxial bending and shear.
- Provisions are added to Chapter I for longitudinal and transverse reinforcing steel requirements for filled composite columns and for both encased composite and filled composite beams.
- Chapter I now includes additional stiffness and strength provisions for concrete filled composite plate shear walls consisting of two steel plates connected by tie bars.
- Provisions for the use of rectangular filled composite members constructed using materials with strengths above the limits noted in Chapter I are added in a new Appendix 2.
- Appendix J2 provides revised requirements to guard against joint-penetration groove welds with effective throats larger than those prescribed in AWS D1.1/D1.1M.
- Requirements regarding the use of low-hydrogen electrodes as they relate to minimum size fillet welds are revised in Table J2.4.
- The directional strength increase for transversely loaded fillet welds is rewritten and prohibited for use on the ends of rectangular HSS.
- An alternative bolt tensile strength based on the net tensile area of bolts is added.
- Added limit states for rectangular HSS moment connections in Chapter K.
- A new Section N8, Minimum Requirements for Shop or Field Applied Coatings, is added.
- Section N9, Design for Ponding, is removed and replaced with updated guidance on this topic in Section B3.10.
- Appendix 4 incorporates temperature-dependent stress-strain equations from the Eurocode to provide material properties for steel at elevated temperatures.
- Prescriptive cold-formed steel fire protection design equations and related information based on standard ASTM E119 fire tests are incorporated into Appendix 4.
- Appendix 4, Section 4.4a1, Design by Simple Methods of Analysis, includes provisions for compressive strength in filled composite columns and for compression in filled composite plate shear walls.
- Provisions for calculating rivet strength are added in Appendix 5.

This Specification was approved by the Committee on Specifications:

| **Committee Members** | **Committee Members** |
|----------------------|----------------------|
| James O. Malley, Chair | Bruce R. Ellingwood, Emeritus |
| Scott F. Armbrust, Vice Chair | Michael D. Engelhardt |
| Allen Adams | Shu-Jin Fang, Emeritus |
| Taha D. Al-Shawaf | James M. Fisher, Emeritus |
| Jennifer A. Baker | John W. Fisher, Emeritus |
| John M. Barsom, Emeritus | Theodore V. Galambos, Emeritus |
| Roger L. Brockenbrough, Emeritus | Michael E. Gase |
| Susan B. Burmeister | Louis F. Geschwindner |
| Gregory G. Deierlein | Ramon E. Gilsanz |
| Bo Dowswell | Lawrence G. Griffis |
| Carol J. Drucker | Jerome F. Hajjar |
| W. Samuel Easterling | Ronald O. Hamburger |

---


## PREFACE

| **Committee Members** | **Committee Members** |
|----------------------|----------------------|
| Patrick M. Hassett | R. Shankar Nair, Emeritus |
| Tony C. Hazel | Conrad Paulson |
| Todd A. Helwig | Douglas A. Rees-Evans |
| Richard A. Henige, Jr. | Rafael Sabelli |
| Mark V. Holland | Thomas A. Sabol |
| John D. Hooper | Fahim H. Sadek |
| Nestor R. Iwankiw | Benjamin W. Schafer |
| William P. Jacobs, V | Robert E. Shaw, Jr. |
| Ronald J. Janowiak | Donald R. Sherman, Emeritus |
| Lawrence A. Kloiber, Emeritus | W. Lee Shoemaker |
| Lawrence F. Kruth | William A. Thornton, Emeritus |
| Jay W. Larson | Chia-Ming Uang |
| Roberto T. Leon | Amit H. Varma |
| Judy Liu | Donald W. White |
| Duane K. Miller | Jamie Winans |
| Larry S. Muir | Ronald D. Ziemian |
| Thomas M. Murray, Emeritus | Cynthia J. Duncan, Secretary |

The Committee honors former members, vice-chair, Patrick J. Fortney, and emeritus members, Reidar Bjorhovde, Duane S. Ellifritt, and Raymond H.R. Tide, who passed away during this cycle.

The Committee gratefully acknowledges AISC Board Oversights, Matt Smith and Duff Zimmerman; advisory members, Carlos Aguirre and Tiziano Perea; and the following task committee and staff members for their involvement in the development of this document.

| **Task Committee Members** | **Task Committee Members** |
|---------------------------|---------------------------|
| Farid Alfawakhiri | Rodney D. Gibble |
| Abbas Aminmansour | Nathaniel P. Gonner |
| Caroline R. Bennett | Arvind V. Goverdhan |
| Robert Berhinig | Perry S. Green |
| Eric Bolin | Christina Harber |
| Mark Braekevelt | John Harris |
| Michel Bruneau | Alfred A. Herget |
| Art Bustos | Stephen M. Herlache |
| Joel A. Chandler | Steven J. Herth |
| Robert Chmielowski | Devin Huber |
| Lisa Choe | Ronald B. Johnson |
| Douglas Crampton | Jeffrey Keilch |
| Rachel Chicchi Cross | Kerry Kreitman |
| Mark D. Denavit | David W. Landis |
| Matthew F. Fadden | Chad M. Larson |
| Larry A. Fahnestock | Dawn E. Lehman |
| Shelley C. Finnigan | Andres Lepage |
| Erica C. Fischer | Brent Leu |
| Timothy P. Fraser | Carlo Lini |
| Christine Freisinger | LeRoy A. Lutz |
| Michael Gannon | Andrew Lye |
| Rupa Garai | Bonnie E. Manley |
| Jeffrey Gasparott | Michael R. Marian |

---
