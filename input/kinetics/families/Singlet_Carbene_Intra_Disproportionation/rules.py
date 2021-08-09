#!/usr/bin/env python
# encoding: utf-8

name = "Singlet_Carbene_Intra_Disproportionation/rules"
shortDesc = "Convert a singlet carbene to a closed-shell molecule through a concerted 1,2-H shift + 1,2-bond formation"
longDesc = """
Reaction site *1 should always be a singlet in this family.
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.24504e+18,'s^-1'), n=-2.07738, w0=(553800,'J/mol'), E0=(114447,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8618513601060084, var=17.95971135271405, Tref=1000.0, N=5, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 5 training reactions at node Root
    Total Standard Deviation in ln(k): 10.661302344983834"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 10.661302344983834""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root
Total Standard Deviation in ln(k): 10.661302344983834
""",
)

entry(
    index = 2,
    label = "Root_1C-inRing",
    kinetics = ArrheniusBM(A=(4.29565e+18,'s^-1'), n=-1.98121, w0=(539000,'J/mol'), E0=(112368,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8244034383540874, var=17.07856576123755, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1C-inRing',), comment="""BM rule fitted to 4 training reactions at node Root_1C-inRing
    Total Standard Deviation in ln(k): 10.356177990909988"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 10.356177990909988""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1C-inRing
Total Standard Deviation in ln(k): 10.356177990909988
""",
)

entry(
    index = 3,
    label = "Root_N-1C-inRing",
    kinetics = ArrheniusBM(A=(1.91033e+10,'s^-1'), n=0.827, w0=(613000,'J/mol'), E0=(212825,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 4,
    label = "Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.067e+10,'s^-1'), n=0.649, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.454e+12,'s^-1'), n=0.178, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-4R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 6,
    label = "Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C",
    kinetics = ArrheniusBM(A=(1.19752e-13,'s^-1'), n=7.15292, w0=(539000,'J/mol'), E0=(-2634.85,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.22451706692118498, var=51.16218975222221, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
    Total Standard Deviation in ln(k): 14.903532113840376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 14.903532113840376""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C
Total Standard Deviation in ln(k): 14.903532113840376
""",
)

entry(
    index = 7,
    label = "Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(1.61832e+16,'s^-1'), n=-0.885455, w0=(539000,'J/mol'), E0=(109382,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(4.66894e+13,'s^-1'), n=-1.27142, w0=(539000,'J/mol'), E0=(78261.5,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-4R!H-1C_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

