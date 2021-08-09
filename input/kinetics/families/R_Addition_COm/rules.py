#!/usr/bin/env python
# encoding: utf-8

name = "R_Addition_COm/rules"
shortDesc = ""
longDesc = """
.. [MRHCBSQB31DHR] M.R. Harper (mrharper_at_mit_dot_edu or michael_dot_harper_dot_jr_at_gmail_dot_com)
The geometries of all reactants, products, and the transition state were optimized using the CBS-QB3 method.
The zero-point energy is that computed by the CBS-QB3 calculations.  The frequencies were computed with B3LYP/CBSB7.
In computing k(T), an asymmetric tunneling correction was employed, the calculated frequencies were scaled by 0.99, and the 
temperatures used were from 600 K to 2000 K (in 200 K increments).
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(1.06012e-07,'m^3/(mol*s)'), n=4.03373, w0=(310789,'J/mol'), E0=(-711.823,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11642338415204595, var=7.8942473961530455, Tref=1000.0, N=19, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 19 training reactions at node Root
    Total Standard Deviation in ln(k): 5.9251657439000525"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 5.9251657439000525""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root
Total Standard Deviation in ln(k): 5.9251657439000525
""",
)

entry(
    index = 2,
    label = "Root_3R->O",
    kinetics = ArrheniusBM(A=(34.1,'m^3/(mol*s)'), n=0, w0=(315500,'J/mol'), E0=(36014.4,'J/mol'), Tmin=(250,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_3R->O',), comment="""BM rule fitted to 1 training reactions at node Root_3R->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_3R->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 3,
    label = "Root_N-3R->O",
    kinetics = ArrheniusBM(A=(1.04017e-07,'m^3/(mol*s)'), n=4.04149, w0=(310528,'J/mol'), E0=(2135.58,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10995225829276445, var=7.54020302365519, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-3R->O',), comment="""BM rule fitted to 18 training reactions at node Root_N-3R->O
    Total Standard Deviation in ln(k): 5.781150231644904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.781150231644904""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-3R->O
Total Standard Deviation in ln(k): 5.781150231644904
""",
)

entry(
    index = 4,
    label = "Root_N-3R->O_3BrCClFHINPSSi->Cl",
    kinetics = ArrheniusBM(A=(510289,'m^3/(mol*s)'), n=0.692613, w0=(300000,'J/mol'), E0=(8806.86,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_3BrCClFHINPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.88387e-06,'m^3/(mol*s)'), n=3.57522, w0=(311147,'J/mol'), E0=(23750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17662791490568566, var=0.5483874520419095, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl',), comment="""BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
    Total Standard Deviation in ln(k): 1.9283589487425359"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 1.9283589487425359""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl
Total Standard Deviation in ln(k): 1.9283589487425359
""",
)

entry(
    index = 6,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing",
    kinetics = ArrheniusBM(A=(34.523,'m^3/(mol*s)'), n=1.38052, w0=(309500,'J/mol'), E0=(40704.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.015367999328624692, var=0.21698482956507725, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
    Total Standard Deviation in ln(k): 0.9724513489512048"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 0.9724513489512048""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing
Total Standard Deviation in ln(k): 0.9724513489512048
""",
)

entry(
    index = 7,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing",
    kinetics = ArrheniusBM(A=(1.48974e-10,'m^3/(mol*s)'), n=4.85095, w0=(311500,'J/mol'), E0=(-2505.94,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23618086951167397, var=0.2334539577524654, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing',), comment="""BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
    Total Standard Deviation in ln(k): 1.562048588033709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 1.562048588033709""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing
Total Standard Deviation in ln(k): 1.562048588033709
""",
)

entry(
    index = 8,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O",
    kinetics = ArrheniusBM(A=(0.00721,'m^3/(mol*s)'), n=2.333, w0=(309500,'J/mol'), E0=(19464.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_4R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O",
    kinetics = ArrheniusBM(A=(445623,'m^3/(mol*s)'), n=0.212885, w0=(309500,'J/mol'), E0=(55633.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.427090335129738, var=6.5404163862659415, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
    Total Standard Deviation in ln(k): 8.71261126623084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 8.71261126623084""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_3CHS-inRing_Ext-3CHS-R_N-4R!H->O
Total Standard Deviation in ln(k): 8.71261126623084
""",
)

entry(
    index = 10,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S",
    kinetics = ArrheniusBM(A=(0.0785,'m^3/(mol*s)'), n=2.33, w0=(272500,'J/mol'), E0=(15465.3,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_3CHS->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S",
    kinetics = ArrheniusBM(A=(1.39231e-10,'m^3/(mol*s)'), n=4.85981, w0=(314500,'J/mol'), E0=(3476.48,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2358834996923041, var=0.22333041480891982, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S',), comment="""BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
    Total Standard Deviation in ln(k): 1.540066754957607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 1.540066754957607""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S
Total Standard Deviation in ln(k): 1.540066754957607
""",
)

entry(
    index = 12,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C",
    kinetics = ArrheniusBM(A=(1.18834e-10,'m^3/(mol*s)'), n=4.88467, w0=(309500,'J/mol'), E0=(4491.77,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.23250419071495698, var=0.19133646726638645, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
    Total Standard Deviation in ln(k): 1.4610930844693082"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.4610930844693082""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C
Total Standard Deviation in ln(k): 1.4610930844693082
""",
)

entry(
    index = 13,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C",
    kinetics = ArrheniusBM(A=(9679.71,'m^3/(mol*s)'), n=0.282982, w0=(342000,'J/mol'), E0=(39708.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.26467239873145e-14, var=3.447156939379594, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
    Total Standard Deviation in ln(k): 3.722095547627742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 3.722095547627742""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_N-3CH->C
Total Standard Deviation in ln(k): 3.722095547627742
""",
)

entry(
    index = 14,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.44583e-10,'m^3/(mol*s)'), n=4.86373, w0=(309500,'J/mol'), E0=(4005.29,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2976968437149465, var=0.31045207930784685, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.8649848557079767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.8649848557079767""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.8649848557079767
""",
)

entry(
    index = 15,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.1943,'m^3/(mol*s)'), n=1.83879, w0=(309500,'J/mol'), E0=(38275.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05745959212384381, var=0.1847590674613678, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C',), comment="""BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 1.006078329085345"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.006078329085345""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C
Total Standard Deviation in ln(k): 1.006078329085345
""",
)

entry(
    index = 16,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(31781.3,'m^3/(mol*s)'), n=0.303106, w0=(309500,'J/mol'), E0=(62117.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1173174075763179, var=1.0353963844147254, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C',), comment="""BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 2.334674088953271"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.334674088953271""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 2.334674088953271
""",
)

entry(
    index = 17,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(86.1,'m^3/(mol*s)'), n=1.36, w0=(309500,'J/mol'), E0=(33227.5,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(65100,'m^3/(mol*s)'), n=0.45, w0=(309500,'J/mol'), E0=(44226.7,'J/mol'), Tmin=(600,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(4.42979,'m^3/(mol*s)'), n=1.67963, w0=(309500,'J/mol'), E0=(68389.1,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-3R->O_N-3BrCClFHINPSSi->Cl_N-3CHS-inRing_N-3CHS->S_3CH->C_Ext-3C-R_N-Sp-4R!H-3C_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

