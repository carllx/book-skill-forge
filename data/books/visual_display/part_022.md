## Part 22

> [BREADCRUMB_CTX: 《visual_display》 > Part 22]

Thetable recordsan enormous diversity of graphical performances both within and between publications. Afewdata-rich designs appearinnearly every publication. The opportunity is therebut itis rarely exploited: the average published graphic israther thin, based on about 5o numbers shown at the rate of 10 per square inch. Among the world’s newspapers,the Wall StreetJournal, The Times (London), and Asahi publish data-rich graphics,with data densities equal to those of theJournal ofthe American Statistical Association. Mostof the American papers and magazines, along with Pravda, publish less data per graphic than the major papers ofother industrialized countries.

Data Density and Size ofData Matrix, Statistical Graphics inSelected Publications, Circa 1979-1980   
![](images/4de17fd7cb9ded1d188a16bd9be96f3fd11a5eca1ebb2880cd86e657460e68a0.jpg)

Very few statistical graphics achievethe information display rates found in maps. Highly detailed maps portray 100,000 to 150,000 bits per square inch. Forexample, the averageU.S. Geological Survey topographic quadrangle (measuring 17by 23 inches) is estimated to contain over100million bits ofinformation, or about25o,ooo per square inch (40,000 per square centimeter).3 Perhaps some day statistical graphics will perform as successfully as maps in carrying information.

# High-Information Graphics

Data graphics should oftenbebased on large rather than small data matricesand have a highrather than low data density. More information is betterthan less information, especially when the marginal costs of handling and interpreting additional information are low,as they are for most graphics. The simple things belong in tables or in the text;graphics can givea sense oflarge and complex data sets that cannot bemanaged in any other way. If thegraphic becomes overcrowded (although several thousand numbersrepresented may be just fine),a variety ofdata-reduction techniques-averaging, clustering,smoothing-can thinthe numbers out before plotting.4 Summary graphics can emerge from high-information displays,but there isnowhere togo ifwebegin with a low-information design.

Data-rich designs give a contextand credibility to statistical evidence. Low-information designs are suspect: whatis leftout, whatis hidden, why are we shown so litte?High-density graphics help us to compare parts ofthe data by displaying much information within theview of the eye: we look at onepage ata time and the more on the page, themore effectiveand comparative oureye can be.5 The principle, then,is:

Maximizedata densityand the size ofthedata matrix, within reason.

High-information graphics mustbedesigned with special care. As the volumeofdata increases, datameasures must shrink (smaller dots for scatters, thinner lines for busy time-series). Theclutter of chartjunk, non-data-ink, and redundant data-ink iseven more costly than usual in data-rich designs.

The way to increase data density other than by enlarging the data matrix is to reduce the area ofa graphic. The Shrink Principle has wide application:

Graphics can be shrunk way down.

Many data graphics can be reduced in area to half their currently published sizewith virtually no loss in legibility and information. For example, Bertin's crisp and elegant line allows the display of 17 small-scale graphics on a single page along with extensive text. Repeated application ofthe Shrink Principleleads to a powerful and effective graphical design,the small multiple.

![](images/eb4671b679e19f8e0c735f3d1e5fcfa796f03aa9cae47d6535e0fa9853978e06.jpg)

Jacques Bertin, Semiologie Graphique (Paris, second edition, 1973),p.214.

# PROBLEMES GRAPHIQUES POSES PAR LES CHRONIQUES

Untotal surdeux cases(sur deux ans) doitetre divisepardeux (1).   
Untotalpour SiX moisseramultiplie pardeux dans des cases annuelles. Courbestrop pointues, reduirel'echelle desQ; la sensibilite angulaire s'inscrit dans une zone moyenne autour de 70.   
Si la courbe n'est pas reductible (grandes el petitesvariations) employer les colonnes remplies(5).   
Courbes tropplates augmenterl'echelledesQ.

Variationstresfaiblesparrapportautotal. Celui-ci perd del'importance et le zero peut etre supprime, a condition que le lecteur voit sasuppression(9).Legraphiquepeutetre interprete comme uneacceleration sil'etudefine des variationsestnecessaire(echellelogarithmique (10)(v.p. 240).

Tresgrande amplitude entreles valeurs extremes.Il fautadmettre ：   
10) Soit de ne pas percevoir les plus petites variations.   
20 Soit de ne s'interesser qu'aux differences relatives(echellelogarithmique)sans connaitre la quantite absolue.   
30） Soit admettre des periodes differentes dansla composante ordonnee et les traiter a desechelles differentesau-dessus de T'echelle commune (12).

Cyclestres marques.

Sil'etudeporte surla comparaison desphases de chaque cycle, i est preferable de decomposer(13) de manierea superposer les cycles (14).Laconstructionpolairepeutetre employee. depreferencedansuneformespirale(I5)(nepas commencerparun troppetit cercle);pourspectaculaire quelle soit, elle est moins efficace que laconstructionorthogonale.

Courbesannuellesde pluie ou detemperature. Uncycle possede deux phases (17). pourquoi n'en offrir qu'une a la perception du spectateur？(16).

# Small Multiples

Small multiples resemble the frames ofa movie: aseries of graphics, showing the same combination ofvariables, indexed by changes in another variable. Twenty-three hours ofLos Angeles air pollution areorganized into this display, based on a computer generated video tape. Shown is the hourly average distribution of reactive hydrocarbon emissions. The design remains constant through all the frames, SO that attention is devoted entirely to shifts in thedata:

From video tape byGregoryJ.McRae, California Instituteof Technology. Themodel is described inG.J.McRae, W. R. Goodin, andJ.H. Seinfeld, "Development ofaSecond-Generation Mathematical Model for Urban Air Pollution. I. Model Formulation," Atmospheric Environment, 16 (1982), 679-696.

![](images/22d2ffb98661e71d02ad3fea86c4b0bd33e73831f9cb90cd63c323b9e8ed8dd8.jpg)

These grimsmall multiples show the distribution of occurrence ofthe cancermelanoma. The sites of269 primary melanomas are recorded, along with the distribution between menand women. Note thedata graphical arithmetic, similar to that ofthe multiwindow plot.

![](images/b65df1a3ef70f40a95a4675e3f22ac6ce9ff254a6c7b2fcff16ac9a3150ec14b.jpg)  
Abb.1. Verteilung von 269 primaren Melanomen auf Kopf undHals

![](images/ddf2e99d1683c8798c5556fb85aaa57b0190cc1c7f70ef5e449e9d68030d9bf0.jpg)  
Abb. 2 u.3. DifferenzierungderMelanomverteilung nach Geschlechtern

Arthur Wiskemann, "ZurMelanomentstehungdurch chronische Lichteinwirkung, DerHautarzt, 25 (1974), 21.

Theeffects of sampling errors areshown in these 12 distributions, each based ona sample of50 random normal deviates:

社金公会会室

These six distributions show the age composition of herring catches eachyear from 1908 to 1913. A tremendous number of herring were spawned in 1904,and thatclass began to dominate the 1908 catch as four-year-olds, then the 1909catch as five-year-olds, and SO on:

![](images/3427769c0403392460cbde44f0a356afb7b263ec9d83f647eb31e7d4a2a0ea59.jpg)  
EdmondA.Murphy,"One Cause? Many Causes?The Argument from the BimodalDistribution, Journal of   
Johan Hjort, "Fluctuations in theGreat Fisheries ofNorthern Europe, Rapports etProces-Verbaux,20 (1914),in Susan Schlee,The Edge of an UnfamiliarWorld (NewYork,1973）, P.226.   
JorgeJ.Yunis and Om Prakash, "The Origin ofMan:A Chromosomal PictorialLegacy,' Science, 215 (March19, 1982),1527.

Thisnext design compares a complex set ofdata: shown are the chromosomesof(fromleft to right) man, chimpanzee, gorilla, and orangutan. The similarities between humansand the great apes are to benoted.

![](images/994ae932c8fcc4a6be6a3e82dd337dd88a2d78c21bdd439ec08386cfcd1953d7.jpg)