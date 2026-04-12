# Chapter 1: Introduction

<!-- Consolidated from pages 1-10 -->


## Table of Contents

- 1.1 History

- 1.2 Manufacturing

- 1.3 Nomenclature

- 1.4 Introduction of Design Guide


---


<!-- Page 1 -->

<!-- Page 1 -->

![AISC Logo](logo)

# 31
# Steel Design Guide

# *Castellated and Cellular Beam Design*

![Diagram showing two beam cross-sections:
- Top beam: Wide-flange section with hexagonal (castellated) web openings in a repeating pattern
- Bottom beam: Wide-flange section with circular (cellular) web openings in a repeating pattern]






<!-- Page 2 -->

<!-- Page 2 -->

![AISC Logo](logo)

# 31
# Steel Design Guide

# *Castellated and Cellular Beam Design*

**Sameer S. Fares, P.E., S.E., P. Eng**
New Millenium Building Systems
Hope, AR

**John Coulson, P.E.**
Integrity Structural Corporation
Houston, TX

**David W. Dinehart, Ph.D.**
Villanova University
Villanova, PA







<!-- Page 3 -->

<!-- Page 3 -->

AISC © 2016

by

American Institute of Steel Construction

*All rights reserved. This book or any part thereof
must not be reproduced in any form without the
written permission of the publisher.*

*The AISC logo is a registered trademark of AISC.*

The information presented in this publication has been prepared following recognized principles of design and construction. While it is believed to be accurate, this information should not be used or relied upon for any specific application without competent professional examination and verification of its accuracy, suitability and applicability by a licensed engineer or architect. The publication of this information is not a representation or warranty on the part of the American Institute of Steel Construction, its officers, agents, employees or committee members, or of any other person named herein, that this information is suitable for any general or particular use, or of freedom from infringement of any patent or patents. All representations or warranties, express or implied, other than as stated above, are specifically disclaimed. Anyone making use of the information presented in this publication assumes all liability arising from such use.

Caution must be exercised when relying upon standards and guidelines developed by other bodies and incorporated by reference herein since such material may be modified or amended from time to time subsequent to the printing of this edition. The American Institute of Steel Construction bears no responsibility for such material other than to refer to it and incorporate it by reference at the time of the initial publication of this edition.

Printed in the United States of America






<!-- Page 4 -->

<!-- Page 4 -->

# Authors

**Sameer S. Fares, P.E., S.E., P. Eng** is an engineer at New Millenium Building Systems, Hope, AR.

**John Coulson, P.E.,** is a Principal and Vice President at Integrity Structural Corporation, Houston, TX.

**David W. Dinehart, Ph.D.,** is a Professor at Villanova University, Villanova, PA.

# Acknowledgments

The authors have been actively engaged in the design, research, and/or advancement of castellated and cellular beams for more than 10 years. Over that time frame, there have been many peers who have assisted the authors in bettering their understanding of the behavior of castellated and cellular beams. The support of Tim Bradshaw, Shawn Gross, Rebecca Hoffman, Billy Milligan, Serge Parent, Joe Pote, John Robins and Joseph Robert Yost has been invaluable and is greatly appreciated. Many thanks go to the graduate and undergraduate students who have conducted the experimental and analytical research at Villanova University sponsored by Commercial Metals Company, Inc.: Nicole Alyz (Hennessey), Dominic Borda, Michelle Donisio (Callow), Jason Hennessey, Matthew Reiter, Jason Reither, Ryan Smoke and James Sutton. The authors are grateful to the reviewers of this document who provided insightful commentary:

Allen Adams                    Steven Hofmeister
Leigh Arber                     Larry Kloiber
Reidar Bjorhovde               Roberto Leon
Jason Caldwell                 Tom Murray
Charles Churches               Roger O'Hara
John Cross                     Davis Parsons
David Darwin                   Daryll Radcliffe
Tom Faraone                    Richard Redmond
Pat Fortney                    David Ruby
Ted Galambos                   Bill Scott
Ed Garvin                      Robert Shaw
Louis Geschwindner             Victor Shneur
Scott Goodrich                 Derek Tordoff
Jay Harris                     Chia-Ming Uang
Tony Hazel

Finally, and most importantly, the authors thank their spouses and families for their support during the writing of this document.

# Preface

This Design Guide provides guidance for the design of castellated and cellular beams based on structural principles and adhering to the 2016 AISC *Specification for Structural Steel Buildings* and the 14th Edition AISC *Steel Construction Manual*. Both load and resistance factor design and allowable strength design methods are employed in the design examples.

i






<!-- Page 5 -->

<!-- Page 5 -->

ii






<!-- Page 6 -->

<!-- Page 6 -->

# TABLE OF CONTENTS

**CHAPTER 1   INTRODUCTION . . . . . . . . . . . . . . . . . 1**

1.1     HISTORY . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
1.2     MANUFACTURING. . . . . . . . . . . . . . . . . . . . .1
1.3     NOMENCLATURE  . . . . . . . . . . . . . . . . . . . . .2
1.4     INTRODUCTION OF DESIGN GUIDE. . . . . . .3

**CHAPTER 2   USE OF CASTELLATED AND
            CELLULAR BEAMS . . . . . . . . . . . . . . . . . . . . 5**

2.1     GENERAL  . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
2.2     APPLICATIONS AND ADVANTAGES  . . . . . . .5
  2.2.1   Parking Structures. . . . . . . . . . . . . . . . . .5
  2.2.2   Industrial Facilities . . . . . . . . . . . . . . . . .6
  2.2.3   Service/HVAC Integration  . . . . . . . . . . .6
  2.2.4   Construction Efficiency . . . . . . . . . . . . . .6
  2.2.5   Vibration Resistance  . . . . . . . . . . . . . . . .7
  2.2.6   Asymmetric Sections. . . . . . . . . . . . . . . . .7
  2.2.7   Aesthetics . . . . . . . . . . . . . . . . . . . . . . . . .7
2.3     WEB OPENING SIZE AND SPACING
        AND TYPICAL CONNECTIONS  . . . . . . . . . . . .8
  2.3.1   End Connections. . . . . . . . . . . . . . . . . . . .8
  2.3.2   Infilling of Openings . . . . . . . . . . . . . . . . .8
  2.3.3   Large Copes  . . . . . . . . . . . . . . . . . . . . . . .9
2.4     SPECIAL CONSIDERATIONS. . . . . . . . . . . . . .9
  2.4.1   Concentrated Loads. . . . . . . . . . . . . . . . . .9
  2.4.2   Depth-Sensitive Projects. . . . . . . . . . . . . .9
  2.4.3   Erection Stability  . . . . . . . . . . . . . . . . . . .9
  2.4.4   Fireproofing. . . . . . . . . . . . . . . . . . . . . . .10
  2.4.5   Coating Systems. . . . . . . . . . . . . . . . . . . .10

**CHAPTER 3   DESIGN PROCEDURES . . . . . . . . . . 11**

3.1     INTRODUCTION  . . . . . . . . . . . . . . . . . . . . . .11
3.2     VIERENDEEL BENDING IN
        NONCOMPOSITE BEAMS . . . . . . . . . . . . . . . .11
  3.2.1   Calculation of Axial Force and
          Vierendeel Moment at Each Opening . . . .11
  3.2.2   Calculation of Available Axial (Tensile/
          Compressive) and Flexural Strength of
          Top and Bottom Tees . . . . . . . . . . . . . . . .12
  3.2.3   Check of Top and Bottom Tees
          Subjected to Combined Flexural and
          Axial Forces  . . . . . . . . . . . . . . . . . . . . . .15

3.3     VIERENDEEL BENDING IN COMPOSITE
        BEAMS  . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .16
  3.3.1   Calculation of Axial Force
          and Vierendeel Moment at
          Each Opening. . . . . . . . . . . . . . . . . . . . . .16
  3.3.2   Calculation of Vierendeel Bending
          Moment of the Upper and
          Lower Tees  . . . . . . . . . . . . . . . . . . . . . . .18
  3.3.3   Calculation of Available Axial and
          Flexural Strength of Top and
          Bottom Tees. . . . . . . . . . . . . . . . . . . . . . .19
3.4     WEB POST BUCKLING. . . . . . . . . . . . . . . . . .19
  3.4.1   Web Post Buckling in
          Castellated Beams. . . . . . . . . . . . . . . . . . .19
  3.4.2   Web Post Buckling in
          Cellular Beams . . . . . . . . . . . . . . . . . . . . .21
3.5     HORIZONTAL AND VERTICAL SHEAR . . . .22
  3.5.1   Calculation of Available Horizontal
          Shear Strength . . . . . . . . . . . . . . . . . . . . .22
  3.5.2   Calculation of Available Vertical
          Shear Strength . . . . . . . . . . . . . . . . . . . . .22
3.6     LATERAL-TORSIONAL BUCKLING. . . . . . . .23
3.7     DEFLECTION. . . . . . . . . . . . . . . . . . . . . . . . .23
3.8     CONCENTRATED LOADING . . . . . . . . . . . . .23

**CHAPTER 4   DESIGN EXAMPLES. . . . . . . . . . . . . 25**

4.1     NONCOMPOSITE CASTELLATED
        BEAM DESIGN . . . . . . . . . . . . . . . . . . . . . . . . .25
4.2     NONCOMPOSITE CELLULAR
        BEAM DESIGN . . . . . . . . . . . . . . . . . . . . . . . . .40
4.3     COMPOSITE CASTELLATED
        BEAM DESIGN. . . . . . . . . . . . . . . . . . . . . . . . .55
4.4     COMPOSITE CELLULAR
        BEAM DESIGN. . . . . . . . . . . . . . . . . . . . . . . . .78

**SYMBOLS . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 101**

**REFERENCES. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 103**

**FURTHER READING  . . . . . . . . . . . . . . . . . . . . . . . 105**

iii






<!-- Page 7 -->

<!-- Page 7 -->

iv






<!-- Page 8 -->

<!-- Page 8 -->

# Chapter 1
# Introduction

## 1.1   HISTORY

The idea of creating single web openings in wide-flange steel beams by removing portions (hot cutting) has been around since the early 1900s. However, the creative idea of cutting the web of a steel section along a zigzag pattern through the web through the AISC Design Guide 2, *Design of Steel and Composite Beams with Web Openings* (Darwin, 1990). Through the 1960s and 1970s, extensive research was completed on castellated web sections that included repeating openings (Hosain, Speirs and Januwala, 1972), nonrepeating patterns (Bower, 1966), and the use of asymmetric sections (Toprac and Cooke, 1959). Similarly extensive research was done on cellular openings. Cellular beams are defined as expanded steel sections with the basic shape formed by cutting a wide-flange beam into two symmetric pieces through a series of precise circular cuts along the web, then shifting the two pieces from West, Fles and Seuer, 1964). This idea was first published at the meeting of the American Institute of Steel Construction in 1934 at a paper (Seuer and Fles, 1934) and was described in the 1938 AISC Convention (Seuer and Fles, 1938). The Convention in 1991 (Seuer, 1991). In the 1990s, the use of castellated and cellular beams began to increase, in part, due to a much larger number of domestic and international companies manufacturing both types of beams in Europe, Asia and the United States (Salem et al., 2002). Steel mills could efficiently produce a number of large section sizes used to manufacture beams because of the economy of scale. The use of castellated and cellular beams becomes attractive because large spans could be economically achieved. Manufacturers could use smaller (more cost effective and less costly ways to utilize) larger structural shapes to produce more efficient and less costly ways to bridge large structures. In addition, large web openings can be used to pass building services, such as electrical conduit or HVAC equipment in a variety of ways, as described in greater detail in the second edition of the International Building of Cellular Beam Manufacture's Guide (Lawson and Hicks, 2011) or AISC Design Guide 31 (2015) for multiple and maintain standards for both asymmetric castellated and cellular beams worldwide.

## 1.2   MANUFACTURING

Castellated and cellular beams are custom designed for a specific location or a specific project. The process by which these beams are manufactured requires hot cutting a hot rolled or welded built-up section using a zigzag pattern along

manufacturing a castellated beam is presented in Figure 1-1. The idea is to first cut through the web of the rolled beam to first cut along a zig zag path (Figure 1-1a). This zigzag cutting path has two halves offset by roughly 1.5 times typically from one side of the section to the other. The two halves also produce a castellated beam as shown in Figure 1-1c. The two cutting pattern insures that the material is conserved instead of wasted as a compared to plain a castellated beam. The cuts are made at most the same process. One of the advantages of using a manufacturing process, and it is manufactured by a welding process. Once the cells have been offset, the two halves also move as compared to a castellated beams, as shown in Figure 1-4B1. Once the cuts have been made, one of the pieces is rotated and the process is then for producing a cellular beam is presented in Figure 1-4.

[THIS IS FIGURE: Four diagrams showing different cut patterns labeled (a) through (d):
(a) Cut line - shows a zigzag pattern
(b) Waste - shows alternating waste sections
(c) Shows final castellated beam pattern
(d) Shows final cellular beam pattern with waste sections marked]

*Fig. 1-1. Manufacture of a castellated beam.*

AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN /1






<!-- Page 9 -->

<!-- Page 9 -->

![Photo showing cutting of a castellated pattern with bright welding/cutting light]

*Fig. 1-2. Cutting of a castellated pattern.*

![Diagram showing manufacturing steps of cellular beam:
(a) First cut line - showing circular pattern
(b) Second cut line with "Waste" sections marked
(c) Final assembled beam with circular openings
(d) Cross-section showing "Waste" sections on both sides
(e) Final cross-section with circular openings]

*Fig. 1-3. Manufacturing of a cellular beam.*

![Photo showing second cutting of a cellular pattern]

*Fig. 1-4. Second cutting of a cellular pattern.*

## 1.3   NOMENCLATURE

Typical nomenclature for a steel section indicates the shape type, the approximate depth, and the approximate weight of the shape per linear foot. For example, a W8×10 represents a wide-flange section with a depth of approximately 8 in. and a nominal weight of 10 lb/ft. A similar nomenclature is used for castellated and cellular beams. Castellated beams are represented by CB, while cellular beams are noted as LB. The number representations are identical to those of standard steel sections. For example a castellated and cellular beam constructed from a W8×10 root beam is called out as a CB12×10 and LB12×10, respectively, as the depth is approximately one and half times that of the root beam and the weight is the same as the root beam. Under certain conditions, it is beneficial to produce an asymmetric section. In this case, the nomenclature for these sections is based on the two different root beams used to make the castellated or cellular section. For example, if the root beam for the top tee of the castellated or cellular beam is a W21×44 and the root beam for the bottom is a W21×57, then the castellated and cellular beam call outs would be CB30×44/57 and LB30×44/57, respectively. The first number presents the approximate depth and the second pair of numbers provides

2 / CASTELLATED AND CELLULAR BEAM DESIGN / AISC DESIGN GUIDE 31






<!-- Page 10 -->

<!-- Page 10 -->

the nominal weight of the root beam used for the top of the section followed by a forward slash and the nominal weight of the root beam used for the bottom of the section. The weight per foot of the resulting asymmetric beam is the average of the two nominal weights. The use of asymmetric sections is discussed in further detail in Section 2.2.6.

## 1.4   INTRODUCTION OF DESIGN GUIDE

Although the use of castellated and cellular beams around the world has become very commonplace and there is a growing body of literature on the topic, there are very few publications that include comprehensive design recommendations. This Design Guide presents the state of the practice for the design of castellated and cellular beams in the United States. The Guide provides a unified approach to the design of castellated and cellular beams for noncomposite

and composite applications. Chapter 2 presents information pertaining to appropriate applications for castellated and cellular beams, including advantages, efficiencies, and limitations of use. The differences between designing traditional beams versus those with web openings are identified in Chapter 3, along with the detailed procedures for designing castellated and cellular beams in accordance with the 2016 AISC *Specification for Structural Steel Buildings*, hereafter referred to as the AISC *Specification* (AISC, 2016). The procedures presented include both noncomposite and composite design for both castellated and cellular beams. Chapter 4 presents detailed design examples conforming to the procedures presented in Chapter 3. A detailed listing of the symbols used throughout the Design Guide is supplied at the end of the document, as is a complete list of references cited in the Design Guide and a bibliography of publications for further reading.

AISC DESIGN GUIDE 31 / CASTELLATED AND CELLULAR BEAM DESIGN / 3




