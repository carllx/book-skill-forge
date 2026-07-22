## Part 8

> [BREADCRUMB_CTX: 《visual_display》 > Part 8]

Muchof twentieth-century thinking about statistical graphics has been preoccupied with thequestion ofhow some amateurish chart might fool a naiveviewer. Other important issues,such as the use of graphics for serious data analysis, were largely ignored. Atthe core of the preoccupation with deceptive graphics wasthe assumption that data graphics were mainly devices for showing the obvious to the ignorant. It is hard to imagine any doctrine more likely to stifle intellectual progress in a field. The assumptionled down two fruitless paths in the graphically barren years from 1930 to 1970: First, that graphics had tobe“alive,” "communicatively dynamic, overdecorated and exaggerated (otherwiseallthedullards in the audience would fall asleep in theface ofthose boring statistics). Second, that themain task of graphical analysis wasto detectand denounce deception (the dullards could not protect themselves).

Then,in the late196os,John Tukey made statistical graphics respectable, putting an end to theview that-graphics were only for decorating a fewnumbers. For herewasa world-class data analyst spinning offhalf dozen new designs and, more importantly,using them effectively to explore complex data. Nota word about deception; no tortured attempts to construct more graphical standards" in a hopeless effort toend all distortions. Instead, graphics wereused asinstruments for reasoning about quantitative information. With this good example,graphical work has come to fourish.

Of course false graphics are still with us. Deception must always be confronted and demolished, even iflie detection isno longer at the forefront ofresearch. Graphical excellence beginswith telling thetruth about the data.

Hereare several graphics thatfail to tell the truth. First, thecase ofthe disappearing baseline in theannual report ofa company that would just as soon forget about 1970. Acareful look at the middle panel reveals a negative income in 1970, which is disguised by having the bars begin at the bottom at approximately minus \$4,200,000:

![](images/715a1ff37e1b2c059143c46653b1cc29574d871062c16b338cf13d9a72ac1749.jpg)

This pseudo-decline was created by comparing sixmonths' worth of payments in 1978 to a full year's worth in 1976 and 1977, with the lierepeated four times over.

![](images/fc6c74c87a4b9598d6dfe505290ce6589ae52a91906ba0b6d7047f8f20e8af1e.jpg)

And sometimes thefact that numbers have a magnitude aswell as an order is simply forgotten:

![](images/303edf5cea2883ef9f379ed0151bb089bb4a85b7cabd55b13c546e30710a0ca0.jpg)  
Pittsburgh Civic Commission, Report on ExpendituresoftheDepartmentofCharities (Pittsburgh, 1911),p. 7.

# What is Distortion in a Data Graphic?

Agraphic doesnot distort ifthe visual representation ofthedata is consistent with thenumerical representation. What then is the "visual representation" ofthe data? As physically measured on the surface of the graphic? Or the perceived visual effect? How do we know that thevisual image represents the underlying numbers?

One way to try to answer these questions isto conduct experimentson the visual perception of graphics-having people look at lines of varying length, circles of different areas, and then recording their assessments ofthe numerical quantities.

![](images/ef68eef4f52a9b858fb3634798f5700f84d1c03f969f9a115fe544c5df0a289e.jpg)

Such experiments have discovered very approximatepower laws relating the numerical measure to thereported perceived measure. For example, the perceived areaofa circle probably grows somewhat more slowly than theactual (physical, measured) area: thereported perceived area $\ c =$ (actual area)x,where $\mathbf { x } = . 8 \pm . 3$ a discouraging result. Different people see the sameareassomewhat differently; perceptions change with experience; and perceptions arecontext-dependent.2 Particularly disheartening is the securely established finding that thereported perception of something as clear and simple as line length depends on the contextand what other people have alreadysaid about thelines.3

Misperception and miscommunication are certainly not special to statistical graphics,

![](images/b0658ae16373cee9fdc807628f891cd261667edc9f630d1fdbf3aad170e7cacb.jpg)

but whatis a poor designer to do? A different graphic for each perceiver in each context? Or designs thatcorrect for the visual transformations of the average perceiver participating in theaverage psychological experiment?

One satisfactory answerto these questions isto useatable to show the numbers. Tablesusually outperform graphics in reporting on small data sets of 20 numbers orless. Thespecial power of graphics comes in the display of large data sets.

At any rate, given the perceptual difficulties, the best we can hope for is some uniformity ingraphics (ifnot in the perceivers) and some assurance that perceivers havea fair chance of getting the numbers right. Two principles lead toward these goals and, in consequence, enhancegraphical integrity:

Therepresentation ofnumbers, as physically measured on the surface of the graphic itself, should bedirectly proportional to thenumerical quantities represented.

Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity. Write out explanations ofthe data on the graphic itself. Label important events inthedata.

2Theextensive literature is summarized in MichaelMacdonald-Ross,"How NumbersAreShown:A Review of Research on thePresentation ofQuantitativeData inTexts, 3 Audio-Visual Communication Review, 25 (1977),359- 409.In particular, H.J.Meihoefer finds greatvariability among perceivers; see “TheUtility of the Circleas an Effective CartographicSymbol,”Canadian Cartographer, 6 (1969), 105-117and"The Visual Perception ofthe Circle inThematicMaps:Experimental Results," ibid.,10 (1973),63-84.

# 3S.E. Asch, "Studies of Independence and Submission to Group Pressure. A Minority ofOne Against a Unanimous Majority,' PsychologicalMonographs (1956), 70.

Drawing by CEM; copyright 1961, TheNew Yorker.

Violations ofthe first principle constitute one form ofgraphic misrepresentation, measured by the

If theLie Factorisequal to one, then the graphic might be doing areasonable job of accurately representing the underlying numbers. Lie Factors greater than 1.05or less than.95 indicatesubstantial distortion, far beyond minorinaccuraciesin plotting. Thelogarithm of the Lie Factorcan be taken in order to compare overstating $( \log \mathrm { L F } > 0 )$ ） with understating $( \log \mathrm { L F } < 0 )$ 0 errors.In practice almostalldistortions involve overstating,and Lie Factorsof two to five are not uncommon.

Here is an extremeexample. A newspaper reported thatthe U.S. Congress and the Department of Transportation had seta series offuel economy standards to be met by automobile manufacturers, beginning with 18 milesper gallon in 1978 and moving in stepsup to 27.5 by 1985, an increase of53 percent:

$$
\frac { 2 7 . 5 - 1 8 . 0 } { 1 8 . 0 } \times 1 0 0 = 5 3 \%
$$

These standards and the dates for their attainment were shown:

This line,representing18miles per gallon in 1978, is 0.6inches long.

![](images/cfed799890403814c3d1e397fa7d09eddecda28358abe244587c10f82aa1cf30.jpg)

This line,representing 27.5 miles per gallon in $1 9 8 5 ,$ is 5.3inches long.

Themagnitude ofthe change from 1978 to $1 9 8 \xi$ is shown in the graph by therelative lengths ofthe two lines:

$$
\frac { 5 . 3 - 0 . 6 } { 0 . 6 } \times 1 0 0 = 7 8 3 \%
$$

Thus the numerical change of53 percent is presented by some lines that changed 783 percent, yielding

$$
{ \mathrm { L i e ~ F a c t o r } } = { \frac { 7 8 3 } { 5 3 } } = 1 4 . 8
$$

which is too big.

The display also has several peculiarities of perspective: