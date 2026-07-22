## Part 1

> [BREADCRUMB_CTX: 《visual_display》 > Part 1]

Edward R.Tufte

# The Visual Display of Quantitative Information

SECOND EDITION

Copyright $\circledcirc$ 2001 by Edward RolfTufte PUBLISHED BY GRAPHICS PRESS LLC POST OFFICE Box 430, CHESHIRE, CONNECTICUT 06410

AllrightstoillustrationsandtextreservedbyEdwardRolfTufte. Thiswork may not becopied,eproduced,ortrstedin wholeorin part without writenpermissonofthepublisher, exceptforbriefexcerptsinconnectionwithreviewsor scholarlyanalysis. Usewith any form of information storage and retrieval,electronicadaptationorwhatever,computersoftware,orbysimlarordissmilarmethodsnow known ordeveloped in thefutureisalsostrictlyforbiddenwithout writtenpermisionofthepublisher. Anumberofillustrationsarereproduced by permission;thosecopyright-holders are credited onpage197.

# Contents

# PARTI GRAPHICAL PRACTICE

1 Graphical Excellence 13   
2 Graphical Integrity 53   
3 Sources of Graphical Integrity and Sophistication 79

# PART II THEORY OF DATA GRAPHICS

4 Data-Ink and Graphical Redesign 91   
5 Chartjunk: Vibrations, Grids, and Ducks 107   
6 Data-Ink Maximization and Graphical Design 123   
7 Multifunctioning Graphical Elements 139   
8 Data Density and Small Multiples 161   
9 Aesthetics and Technique in Data Graphical Design 177

Epilogue: Designs for the Display of Information 191

For my parents Edward E. Tufte and Virginia James Tufte

Tothe memory of John W. Tukey (1915-2000)

# Introduction to the Second Edition

Thisnew edition provides high-resolution colorreproductions of the many graphics ofWilliam Playfair,adds color to other images whereappropriate,and includesall the changes and corrections accumulated during the 17 printings of the first edition.

Thisbook beganin 1975when Dean Donald Stokes ofPrinceton's Woodrow Wilson School asked metoteach statistics to a dozen journalists who were visiting that year to learn some economics. Iannotated a collection of readings,with a long section on statistical graphics. The literature here was thin, too often grimly devoted to explaining use of the ruling pen and to promulgating graphic standards' indifferent to thenature of visual evidenceand quantitative reasoning. Soon wroteup some ideas. ThenJohn Tukey,the phenomenal Princeton statistician, suggested thatwe give a series of joint seminars. Since the mid-196os,Tukey had opened up the field, ashis brilliant technical contributionsmade itclear thatthestudyofstatistical graphics was intellectually respectable and not just about pie chartsand ruling pens.

After moving to Yale University,I finished the manuscript in 1982. Apublisherwas interested but planned to print only 2,000 copiesand to charge a very high price,contrary to my hopes for a widereadership. also sought to design the book so as to make it self-exemplifying-thatis,thephysicalobjectitselfwould reflect theintellectual principlesadvanced in the book. Publishersseemed appalled at the prospect that an author might govern design.

Consequently investigated self-publishing.This required a firstrate book designer, a lot of money (at least for a young professor), and a large garage. found HowardGrallawho haddesigned many museum catalogs with great care and craft. He was willing to work closely with thisdifficultauthor who was filledwith all sorts ofopinions about designand typography. We spent the summer in his studio laying out the book,page by page. We were able to integrate graphics right into the text,sometimes into themiddle ofa sentence, eliminating the usual separation oftext and imageone of the ideas Visual Display advocated. To finance the book I took out another mortgage on myhome. Thebank officer said this was the second most unusual loan that she had evermade; first placebelonged to aloan toa circus to buy an elephant!

![](images/ed45825cae6aa3b3d9e6d0c90fba8f6d0177805de5f43eae6fdd9adbffd9fc82.jpg)

# Introduction

Data graphics visually display measured quantities by means of the combined use of points, lines, a coordinate system, numbers, symbols, words, shading,and color.

Theuse ofabstract,non-representational pictures to show numbers isasurprisingly recent invention, perhaps becauseofthe diversity ofskills required-the visual-artistic, empirical-statistical,and mathematical. It was not until $1 7 5 0 - 1 8 0 0$ thatstatistical graphicslength and area to show quantity, time-series,scatterplots, and multivariate displays-were invented, long after such triumphs of mathematical ingenuity as logarithms, Cartesian coordinates, the calculus,and thebasics of probability theory.Theremarkable William Playfair (1759-1823) developed orimproved upon nearly all the fundamental graphical designs, seeking to replace conventional tables ofnumbers with thesystematic visual representations ofhis "linear arithmetic."

Modern data graphics can do much more thansimply substitute forsmall statistical tables. At their best,graphics areinstruments for reasoning about quantitative information. Often the most effectiveway to describe, explore,and summarize a set ofnumberseven avery large set-is to look atpictures of those numbers. Furthermore,ofall methods for analyzing and communicating statistical information, well-designed data graphics are usually the simplest and at the same time themost powerful.

The first part ofthis book reviews the graphical practice of the two centuries since Playfair. The readerwill, I hope, rejoice in the graphical glories shown in Chapter 1 and then condemn the lapses and lostopportunities exhibited in Chapter 2. Chapter 3, on graphical integrity and sophistication,seeks to account forthese differences in quality of graphical design.

The second part of the book provides a languagefor discussing graphicsand a practical theory of datagraphics. Applying to most visual displaysofquantitative information, the theory leads to changes and improvements in design, suggests why some graphics might be better than others, and generatesnew types of graphics. Theemphasis is on maximizing principles, empirical measures of graphical performance,and thesequential improvement of graphics through revision and editing. Insights into graphical design are to be gained, believe, from theoriesofwhat makes for excellence inart, architecture, and prose.

Thisisa book about thedesign of statistical graphics and, assuch, itis concerned both with design and with statistics. Butitis also abouthow tocommunicate information through the simultaneous presentation ofwords, numbers, and pictures. The design of statistical graphics is a universal matter-like mathematics-and is not tied to theunique features ofa particular language. The descriptive concepts (avocabulary for graphics) and the principlesadvanced apply to most designs. Ihaveat times provided evidence about the scope of these ideas,by showing how frequently a principle applies to （a random sample of) newsand scientific graphics.

Each year,the world over,somewhere between900 billion $\left( 9 \times 1 0 ^ { 1 1 } \right)$ and 2 trillion $\left( 2 \times 1 0 ^ { 1 2 } \right)$ images of statistical graphics are printed. The principles of this book apply to most of those graphics. Some of the suggested changes are small,butothers are substantial, with consequences for hundreds ofbillions ofprinted pages.

But Ihope also that thebook has consequences for the viewers and makers of those images- that they will never view or createstatistical graphics the same way again. That isin part because weare about to see, collected here, so manywonderful drawings, those ofPlayfair, ofMinard, ofMarey,and, nowadays, ofthe computer.

Most ofall, then, this book isa celebration ofdata graphics.

# Graphical Practice

# I Graphical Excellence

Excellence in statistical graphics consists ofcomplex ideas communicated with clarity, precision, and efficiency. Graphical displays should