#!/usr/bin/env python
# encoding: utf-8

name = "R_Recombination/rules"
shortDesc = ""
longDesc = """
For some reason the definition of Cs_rad::

 Cs_rad
 1 * C 1 

which is not mutually exclusive from its L2 siblings such as::

 Cd_rad
 1 * C 1 {2,D}, {3,S}
 2   C 0 {1,D}
 3   R 0 {1,S}

is apparently not causing a problem
"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(3.34248e+08,'m^3/(mol*s)'), n=-0.479358, w0=(179992,'J/mol'), E0=(2239.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07377458621450995, var=10.745123605525569, Tref=1000.0, N=319, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 319 training reactions at node Root
    Total Standard Deviation in ln(k): 6.756835819025755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 319 training reactions at node Root
Total Standard Deviation in ln(k): 6.756835819025755""",
    longDesc = 
"""
BM rule fitted to 319 training reactions at node Root
Total Standard Deviation in ln(k): 6.756835819025755
""",
)

entry(
    index = 2,
    label = "Root_1R->H",
    kinetics = ArrheniusBM(A=(3.8102e+10,'m^3/(mol*s)'), n=-1.19264, w0=(206165,'J/mol'), E0=(20616.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2614119885692391, var=25.289002599723965, Tref=1000.0, N=121, data_mean=0.0, correlation='Root_1R->H',), comment="""BM rule fitted to 121 training reactions at node Root_1R->H
    Total Standard Deviation in ln(k): 10.738260313901904"""),
    rank = 11,
    shortDesc = """BM rule fitted to 121 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 10.738260313901904""",
    longDesc = 
"""
BM rule fitted to 121 training reactions at node Root_1R->H
Total Standard Deviation in ln(k): 10.738260313901904
""",
)

entry(
    index = 3,
    label = "Root_N-1R->H",
    kinetics = ArrheniusBM(A=(4.4438e+07,'m^3/(mol*s)'), n=-0.17547, w0=(163997,'J/mol'), E0=(-646.551,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06784511775063312, var=5.760464436525256, Tref=1000.0, N=198, data_mean=0.0, correlation='Root_N-1R->H',), comment="""BM rule fitted to 198 training reactions at node Root_N-1R->H
    Total Standard Deviation in ln(k): 4.982023275186087"""),
    rank = 11,
    shortDesc = """BM rule fitted to 198 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.982023275186087""",
    longDesc = 
"""
BM rule fitted to 198 training reactions at node Root_N-1R->H
Total Standard Deviation in ln(k): 4.982023275186087
""",
)

entry(
    index = 4,
    label = "Root_1R->H_2R->S",
    kinetics = ArrheniusBM(A=(1.01224e+07,'m^3/(mol*s)'), n=0.564397, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.2992478270622168, var=17.016792941748268, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_2R->S',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
    Total Standard Deviation in ln(k): 14.046820587721712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.046820587721712""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_2R->S
Total Standard Deviation in ln(k): 14.046820587721712
""",
)

entry(
    index = 5,
    label = "Root_1R->H_N-2R->S",
    kinetics = ArrheniusBM(A=(3.1339e+11,'m^3/(mol*s)'), n=-1.64233, w0=(206792,'J/mol'), E0=(20679.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25204320385070017, var=25.513311003475184, Tref=1000.0, N=118, data_mean=0.0, correlation='Root_1R->H_N-2R->S',), comment="""BM rule fitted to 118 training reactions at node Root_1R->H_N-2R->S
    Total Standard Deviation in ln(k): 10.75933215618205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 118 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 10.75933215618205""",
    longDesc = 
"""
BM rule fitted to 118 training reactions at node Root_1R->H_N-2R->S
Total Standard Deviation in ln(k): 10.75933215618205
""",
)

entry(
    index = 6,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.26705e+12,'m^3/(mol*s)'), n=-1.46915, w0=(108577,'J/mol'), E0=(65727.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6983396054086685, var=9.172661085067283, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 7.826243245450038"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.826243245450038""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 7.826243245450038
""",
)

entry(
    index = 7,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N",
    kinetics = ArrheniusBM(A=(1.17262e+07,'m^3/(mol*s)'), n=-0.0071624, w0=(167892,'J/mol'), E0=(43.1071,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05427297080421426, var=5.479247615241512, Tref=1000.0, N=185, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N',), comment="""BM rule fitted to 185 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
    Total Standard Deviation in ln(k): 4.829006569697728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 185 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.829006569697728""",
    longDesc = 
"""
BM rule fitted to 185 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N
Total Standard Deviation in ln(k): 4.829006569697728
""",
)

entry(
    index = 8,
    label = "Root_1R->H_2R->S_Ext-2S-R",
    kinetics = ArrheniusBM(A=(6.94752e+06,'m^3/(mol*s)'), n=1.02083, w0=(181500,'J/mol'), E0=(18150,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_2R->S_Ext-2S-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_2R->S_Ext-2S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.73764e+07,'m^3/(mol*s)'), n=0.123265, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10067081692156987, var=4.813044730771074, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing',), comment="""BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 4.651060370806105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.651060370806105""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 4.651060370806105
""",
)

entry(
    index = 10,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing",
    kinetics = ArrheniusBM(A=(1.52297e+12,'m^3/(mol*s)'), n=-1.92716, w0=(206925,'J/mol'), E0=(20692.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.36836016202802835, var=29.33122463089578, Tref=1000.0, N=107, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing',), comment="""BM rule fitted to 107 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
    Total Standard Deviation in ln(k): 11.782834278083056"""),
    rank = 11,
    shortDesc = """BM rule fitted to 107 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 11.782834278083056""",
    longDesc = 
"""
BM rule fitted to 107 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing
Total Standard Deviation in ln(k): 11.782834278083056
""",
)

entry(
    index = 11,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.41611e+06,'m^3/(mol*s)'), n=0.712045, w0=(102750,'J/mol'), E0=(64998.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.531937953533989, var=56.91099830373965, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
    Total Standard Deviation in ln(k): 18.972687167623597"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 18.972687167623597""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R
Total Standard Deviation in ln(k): 18.972687167623597
""",
)

entry(
    index = 12,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(6.8848e+06,'m^3/(mol*s)'), n=0.139797, w0=(126500,'J/mol'), E0=(12650,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.053315102751840954, var=1.9676215119596228, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
    Total Standard Deviation in ln(k): 2.946038184336049"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.946038184336049""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R
Total Standard Deviation in ln(k): 2.946038184336049
""",
)

entry(
    index = 13,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(7.77583e+11,'m^3/(mol*s)'), n=-1.69331, w0=(162481,'J/mol'), E0=(16248.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04272521898826717, var=16.1380596903716, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl',), comment="""BM rule fitted to 27 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 8.160812433030072"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 8.160812433030072""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl
Total Standard Deviation in ln(k): 8.160812433030072
""",
)

entry(
    index = 14,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl",
    kinetics = ArrheniusBM(A=(3.64416e+06,'m^3/(mol*s)'), n=0.170335, w0=(168816,'J/mol'), E0=(380.613,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05722785724472212, var=4.516851493432054, Tref=1000.0, N=158, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl',), comment="""BM rule fitted to 158 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
    Total Standard Deviation in ln(k): 4.404429126085538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 158 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.404429126085538""",
    longDesc = 
"""
BM rule fitted to 158 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl
Total Standard Deviation in ln(k): 4.404429126085538
""",
)

entry(
    index = 15,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(6.68844e+06,'m^3/(mol*s)'), n=0.105537, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3705566296084406, var=9.640462010212294, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 7.155567474279537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 7.155567474279537""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 7.155567474279537
""",
)

entry(
    index = 16,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H",
    kinetics = ArrheniusBM(A=(4.63064e+07,'m^3/(mol*s)'), n=0.141464, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00871465232674572, var=0.8676704064877683, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
    Total Standard Deviation in ln(k): 1.8892833304748036"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.8892833304748036""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H
Total Standard Deviation in ln(k): 1.8892833304748036
""",
)

entry(
    index = 17,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(1.72503e+12,'m^3/(mol*s)'), n=-1.95172, w0=(206554,'J/mol'), E0=(20655.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.38197268809793355, var=29.639840705613498, Tref=1000.0, N=102, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 102 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 11.874006121546502"""),
    rank = 11,
    shortDesc = """BM rule fitted to 102 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.874006121546502""",
    longDesc = 
"""
BM rule fitted to 102 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.874006121546502
""",
)

entry(
    index = 18,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->H",
    kinetics = ArrheniusBM(A=(30255.8,'m^3/(mol*s)'), n=0.454367, w0=(216000,'J/mol'), E0=(21600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3774142242586176, var=47.94959741791935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->H
    Total Standard Deviation in ln(k): 14.830194859219086"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->H
Total Standard Deviation in ln(k): 14.830194859219086""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_2BrCClFHNO->H
Total Standard Deviation in ln(k): 14.830194859219086
""",
)

entry(
    index = 19,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H",
    kinetics = ArrheniusBM(A=(6.50652e+07,'m^3/(mol*s)'), n=0.123367, w0=(213500,'J/mol'), E0=(21350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03757162961902423, var=0.10534383787595203, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H
    Total Standard Deviation in ln(k): 0.7450722393365657"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H
Total Standard Deviation in ln(k): 0.7450722393365657""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H
Total Standard Deviation in ln(k): 0.7450722393365657
""",
)

entry(
    index = 20,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0",
    kinetics = ArrheniusBM(A=(1.00575e+30,'m^3/(mol*s)'), n=-7.13103, w0=(103500,'J/mol'), E0=(10350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3449650629055383, var=32.90236135536008, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
    Total Standard Deviation in ln(k): 12.366023063582485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.366023063582485""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0
Total Standard Deviation in ln(k): 12.366023063582485
""",
)

entry(
    index = 21,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0",
    kinetics = ArrheniusBM(A=(9.47835e+55,'m^3/(mol*s)'), n=-15.6524, w0=(100500,'J/mol'), E0=(101570,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.18264876511744, var=140.54926538472893, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
    Total Standard Deviation in ln(k): 29.250873199202463"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.250873199202463""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0
Total Standard Deviation in ln(k): 29.250873199202463
""",
)

entry(
    index = 22,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.10796e+07,'m^3/(mol*s)'), n=0.0974081, w0=(117833,'J/mol'), E0=(11783.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1078476173045317, var=4.129322638654681, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
    Total Standard Deviation in ln(k): 6.857305717290992"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.857305717290992""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R
Total Standard Deviation in ln(k): 6.857305717290992
""",
)

entry(
    index = 23,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C",
    kinetics = ArrheniusBM(A=(9.47322e+11,'m^3/(mol*s)'), n=-1.68228, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04258022072656074, var=14.564286288315193, Tref=1000.0, N=26, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C',), comment="""BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
    Total Standard Deviation in ln(k): 7.757692883732186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.757692883732186""",
    longDesc = 
"""
BM rule fitted to 26 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C
Total Standard Deviation in ln(k): 7.757692883732186
""",
)

entry(
    index = 24,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C",
    kinetics = ArrheniusBM(A=(3.24625e+12,'m^3/(mol*s)'), n=-2.82209, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 25,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S",
    kinetics = ArrheniusBM(A=(145838,'m^3/(mol*s)'), n=0.753601, w0=(129812,'J/mol'), E0=(5059.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01924599192859901, var=4.3901722599967155, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S
    Total Standard Deviation in ln(k): 4.248825629558483"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S
Total Standard Deviation in ln(k): 4.248825629558483""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S
Total Standard Deviation in ln(k): 4.248825629558483
""",
)

entry(
    index = 26,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S",
    kinetics = ArrheniusBM(A=(5.30075e+08,'m^3/(mol*s)'), n=-0.730921, w0=(170897,'J/mol'), E0=(17089.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.029663480512531676, var=3.244372144231063, Tref=1000.0, N=150, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S',), comment="""BM rule fitted to 150 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S
    Total Standard Deviation in ln(k): 3.6854883962609857"""),
    rank = 11,
    shortDesc = """BM rule fitted to 150 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S
Total Standard Deviation in ln(k): 3.6854883962609857""",
    longDesc = 
"""
BM rule fitted to 150 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S
Total Standard Deviation in ln(k): 3.6854883962609857
""",
)

entry(
    index = 27,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(6.4769e+06,'m^3/(mol*s)'), n=-0.220906, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04719635125001107, var=0.22911507772565162, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.0781696235914124"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0781696235914124""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0781696235914124
""",
)

entry(
    index = 28,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing",
    kinetics = ArrheniusBM(A=(4.4197e+06,'m^3/(mol*s)'), n=0.173431, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1097017345178382, var=0.8159359144189625, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
    Total Standard Deviation in ln(k): 2.086493076125835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing
Total Standard Deviation in ln(k): 2.086493076125835
""",
)

entry(
    index = 29,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(9.42e+06,'m^3/(mol*s)'), n=0.408, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.02093e+07,'m^3/(mol*s)'), n=0.125846, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47660747185827573, var=1.386468955460086, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 3.5580500164857103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5580500164857103""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 3.5580500164857103
""",
)

entry(
    index = 31,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5.22915e+07,'m^3/(mol*s)'), n=0.181361, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1489920501984019, var=0.10041008290210698, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.0096033162086009"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.0096033162086009
""",
)

entry(
    index = 32,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C",
    kinetics = ArrheniusBM(A=(1.19126e+16,'m^3/(mol*s)'), n=-3.23373, w0=(205913,'J/mol'), E0=(20591.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14489572106123946, var=19.664165295246654, Tref=1000.0, N=86, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C',), comment="""BM rule fitted to 86 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C
    Total Standard Deviation in ln(k): 9.253916036429995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 86 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C
Total Standard Deviation in ln(k): 9.253916036429995""",
    longDesc = 
"""
BM rule fitted to 86 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C
Total Standard Deviation in ln(k): 9.253916036429995
""",
)

entry(
    index = 33,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(1.20394e+06,'m^3/(mol*s)'), n=0.104003, w0=(210000,'J/mol'), E0=(21000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.771734598650268, var=149.35385046921377, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C',), comment="""BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C
    Total Standard Deviation in ln(k): 36.4892330886327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C
Total Standard Deviation in ln(k): 36.4892330886327""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C
Total Standard Deviation in ln(k): 36.4892330886327
""",
)

entry(
    index = 34,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_2CNO->C",
    kinetics = ArrheniusBM(A=(5.37e+07,'m^3/(mol*s)'), n=0.15395, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0638883423777328, var=3.290805964782287, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_2CNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_2CNO->C
    Total Standard Deviation in ln(k): 6.309791736806655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_2CNO->C
Total Standard Deviation in ln(k): 6.309791736806655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_2CNO->C
Total Standard Deviation in ln(k): 6.309791736806655
""",
)

entry(
    index = 35,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_N-2CNO->C",
    kinetics = ArrheniusBM(A=(1.62e+08,'m^3/(mol*s)'), n=0, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(2100,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_N-2CNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_N-2CNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_N-2CNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_N-2BrCClFHNO->H_N-2CNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C",
    kinetics = ArrheniusBM(A=(505,'m^3/(mol*s)'), n=0, w0=(152500,'J/mol'), E0=(15250,'J/mol'), Tmin=(2000,'K'), Tmax=(4000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C",
    kinetics = ArrheniusBM(A=(2.85423e+08,'m^3/(mol*s)'), n=-0.30578, w0=(93700,'J/mol'), E0=(9370,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06262066178409414, var=1.5701960652574938, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
    Total Standard Deviation in ln(k): 2.669421041068438"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.669421041068438""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C
Total Standard Deviation in ln(k): 2.669421041068438
""",
)

entry(
    index = 38,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R",
    kinetics = ArrheniusBM(A=(58500,'m^3/(mol*s)'), n=0, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(473,'K'), Tmax=(703,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_N-3R!H-u0_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C",
    kinetics = ArrheniusBM(A=(1.45488e+12,'m^3/(mol*s)'), n=-1.37297, w0=(152500,'J/mol'), E0=(15250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C",
    kinetics = ArrheniusBM(A=(3.65367e+06,'m^3/(mol*s)'), n=0.2352, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4709502203626317, var=0.4813240235668652, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
    Total Standard Deviation in ln(k): 2.5741274836274104"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-1N-R_Ext-1N-R_N-2R->C
Total Standard Deviation in ln(k): 2.5741274836274104
""",
)

entry(
    index = 41,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(7.80997e+11,'m^3/(mol*s)'), n=-1.65202, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.034611252876244294, var=15.220620338308771, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R',), comment="""BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 7.908158883307205"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.908158883307205""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R
Total Standard Deviation in ln(k): 7.908158883307205
""",
)

entry(
    index = 42,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S",
    kinetics = ArrheniusBM(A=(1.74988e+07,'m^3/(mol*s)'), n=0.493661, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.478850108957965, var=26.3269780808117, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S
    Total Standard Deviation in ln(k): 19.027089367324724"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S
Total Standard Deviation in ln(k): 19.027089367324724""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S
Total Standard Deviation in ln(k): 19.027089367324724
""",
)

entry(
    index = 43,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S",
    kinetics = ArrheniusBM(A=(50703.9,'m^3/(mol*s)'), n=0.81198, w0=(135417,'J/mol'), E0=(927.677,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.013013201930370349, var=1.089617427613244, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S
    Total Standard Deviation in ln(k): 2.1253340172990236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S
Total Standard Deviation in ln(k): 2.1253340172990236""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S
Total Standard Deviation in ln(k): 2.1253340172990236
""",
)

entry(
    index = 44,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing",
    kinetics = ArrheniusBM(A=(1.78615e+07,'m^3/(mol*s)'), n=-0.201613, w0=(174600,'J/mol'), E0=(17460,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11015935443403409, var=1.565093210578706, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing
    Total Standard Deviation in ln(k): 2.784779762310175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing
Total Standard Deviation in ln(k): 2.784779762310175""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing
Total Standard Deviation in ln(k): 2.784779762310175
""",
)

entry(
    index = 45,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing",
    kinetics = ArrheniusBM(A=(1.9066e+09,'m^3/(mol*s)'), n=-0.930764, w0=(170485,'J/mol'), E0=(17048.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04847770841316443, var=4.089363478047652, Tref=1000.0, N=135, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing',), comment="""BM rule fitted to 135 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing
    Total Standard Deviation in ln(k): 4.175813574813192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 135 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing
Total Standard Deviation in ln(k): 4.175813574813192""",
    longDesc = 
"""
BM rule fitted to 135 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing
Total Standard Deviation in ln(k): 4.175813574813192
""",
)

entry(
    index = 46,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.03082e+09,'m^3/(mol*s)'), n=-1.0508, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 47,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(2.68977e+06,'m^3/(mol*s)'), n=-0.120159, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8040217460360854, var=0.956881531786605, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 3.9811934407228455"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.9811934407228455""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 3.9811934407228455
""",
)

entry(
    index = 48,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(249317,'m^3/(mol*s)'), n=0.611, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_4R!H-inRing_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(6.44369e+06,'m^3/(mol*s)'), n=0.245, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(3.62e+07,'m^3/(mol*s)'), n=0.228, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.2e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1200,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_N-Sp-4R!H-3R!H_Ext-4R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-6R!H-R_N-Sp-3R!H-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 52,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing",
    kinetics = ArrheniusBM(A=(6.57146e+11,'m^3/(mol*s)'), n=-1.15161, w0=(208929,'J/mol'), E0=(20892.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.270917886540425, var=6.8423082775215365, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing
    Total Standard Deviation in ln(k): 5.9246453808620565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 5.9246453808620565""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing
Total Standard Deviation in ln(k): 5.9246453808620565
""",
)

entry(
    index = 53,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(6.6121e+16,'m^3/(mol*s)'), n=-3.59767, w0=(205646,'J/mol'), E0=(20564.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18156983648172517, var=18.416341000121324, Tref=1000.0, N=79, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing',), comment="""BM rule fitted to 79 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing
    Total Standard Deviation in ln(k): 9.059378761363076"""),
    rank = 11,
    shortDesc = """BM rule fitted to 79 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 9.059378761363076""",
    longDesc = 
"""
BM rule fitted to 79 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing
Total Standard Deviation in ln(k): 9.059378761363076
""",
)

entry(
    index = 54,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(0.0587856,'m^3/(mol*s)'), n=1.23403, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.19792168232489574, var=159.0161966093964, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 25.77732562198916"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 25.77732562198916""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 25.77732562198916
""",
)

entry(
    index = 55,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_3BrClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0.65, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_3BrClFINOPSSi->S',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_3BrClFINOPSSi->S
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 56,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S",
    kinetics = ArrheniusBM(A=(3.71173e+10,'m^3/(mol*s)'), n=-2.14879, w0=(213500,'J/mol'), E0=(21350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04213411807251456, var=13.328725399400641, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S',), comment="""BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S
    Total Standard Deviation in ln(k): 7.424857078011851"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 7.424857078011851""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S
Total Standard Deviation in ln(k): 7.424857078011851
""",
)

entry(
    index = 57,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R",
    kinetics = ArrheniusBM(A=(2.63e+08,'m^3/(mol*s)'), n=-1.1, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(300,'K'), Tmax=(600,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_Ext-2NO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N",
    kinetics = ArrheniusBM(A=(122000,'m^3/(mol*s)'), n=0.2, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(300,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_3R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N",
    kinetics = ArrheniusBM(A=(2.98483e+08,'m^3/(mol*s)'), n=-0.304134, w0=(94833.3,'J/mol'), E0=(9483.33,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009765358261953589, var=1.0633988791636333, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
    Total Standard Deviation in ln(k): 2.091843615577922"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 2.091843615577922""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N
Total Standard Deviation in ln(k): 2.091843615577922
""",
)

entry(
    index = 60,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F",
    kinetics = ArrheniusBM(A=(7.55127e+16,'m^3/(mol*s)'), n=-2.84018, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.190757124072162, var=40.29238522544371, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
    Total Standard Deviation in ln(k): 13.204602397811962"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.204602397811962""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F
Total Standard Deviation in ln(k): 13.204602397811962
""",
)

entry(
    index = 61,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F",
    kinetics = ArrheniusBM(A=(4.429e+10,'m^3/(mol*s)'), n=-1.35498, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09095334304044748, var=10.339636390645506, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F',), comment="""BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
    Total Standard Deviation in ln(k): 6.674812771516251"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 6.674812771516251""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F
Total Standard Deviation in ln(k): 6.674812771516251
""",
)

entry(
    index = 62,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(106000,'m^3/(mol*s)'), n=1.21, w0=(113000,'J/mol'), E0=(11300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S_Ext-1S-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S_Ext-1S-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 63,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R",
    kinetics = ArrheniusBM(A=(69181.1,'m^3/(mol*s)'), n=0.764865, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03639418016190122, var=1.0362331955515207, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R
    Total Standard Deviation in ln(k): 2.1321735605013337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.1321735605013337""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R
Total Standard Deviation in ln(k): 2.1321735605013337
""",
)

entry(
    index = 64,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C",
    kinetics = ArrheniusBM(A=(7.2585e+08,'m^3/(mol*s)'), n=-0.542354, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0176552933751294, var=0.44853869368471316, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C
    Total Standard Deviation in ln(k): 1.3869918867664563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C
Total Standard Deviation in ln(k): 1.3869918867664563""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C
Total Standard Deviation in ln(k): 1.3869918867664563
""",
)

entry(
    index = 65,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C",
    kinetics = ArrheniusBM(A=(3.5471e+06,'m^3/(mol*s)'), n=-0.0529334, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02594719581388334, var=0.43953349774332723, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C
    Total Standard Deviation in ln(k): 1.394279639884687"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C
Total Standard Deviation in ln(k): 1.394279639884687""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C
Total Standard Deviation in ln(k): 1.394279639884687
""",
)

entry(
    index = 66,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br",
    kinetics = ArrheniusBM(A=(9.64386e+07,'m^3/(mol*s)'), n=-0.352578, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.040635725976253576, var=7.8073931435364425, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br
    Total Standard Deviation in ln(k): 5.7036729918334395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br
Total Standard Deviation in ln(k): 5.7036729918334395""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br
Total Standard Deviation in ln(k): 5.7036729918334395
""",
)

entry(
    index = 67,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br",
    kinetics = ArrheniusBM(A=(2.50729e+09,'m^3/(mol*s)'), n=-0.983829, w0=(172968,'J/mol'), E0=(17296.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05708547078263674, var=3.9569655747475454, Tref=1000.0, N=124, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br',), comment="""BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br
    Total Standard Deviation in ln(k): 4.131274505445221"""),
    rank = 11,
    shortDesc = """BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br
Total Standard Deviation in ln(k): 4.131274505445221""",
    longDesc = 
"""
BM rule fitted to 124 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br
Total Standard Deviation in ln(k): 4.131274505445221
""",
)

entry(
    index = 68,
    label = "Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.54095e+09,'m^3/(mol*s)'), n=-1.00262, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_Ext-3R!H-R_Sp-4R!H-3R!H_Ext-2BrCClFHNO-R_Ext-5R!H-R_Ext-5R!H-R_N-Sp-6R!H-5R!H_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 69,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(8.04193e+08,'m^3/(mol*s)'), n=-0.845814, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(1.37622e+07,'m^3/(mol*s)'), n=0.334657, w0=(213500,'J/mol'), E0=(21350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23376307002435073, var=0.4691992284914867, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.9605502128300374"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.9605502128300374""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.9605502128300374
""",
)

entry(
    index = 71,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    kinetics = ArrheniusBM(A=(7.69748e+06,'m^3/(mol*s)'), n=0.34703, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.17670662526750916, var=0.2944266044399326, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
    Total Standard Deviation in ln(k): 1.531777629147324"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.531777629147324""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
Total Standard Deviation in ln(k): 1.531777629147324
""",
)

entry(
    index = 72,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO",
    kinetics = ArrheniusBM(A=(6.82319e+12,'m^3/(mol*s)'), n=-2.01749, w0=(205069,'J/mol'), E0=(20506.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18540633469842815, var=6.514348956655073, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO',), comment="""BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO
    Total Standard Deviation in ln(k): 5.582575040323019"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO
Total Standard Deviation in ln(k): 5.582575040323019""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO
Total Standard Deviation in ln(k): 5.582575040323019
""",
)

entry(
    index = 73,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO",
    kinetics = ArrheniusBM(A=(2.65161e+19,'m^3/(mol*s)'), n=-4.62957, w0=(205980,'J/mol'), E0=(20598,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24039630947774476, var=24.917995095590125, Tref=1000.0, N=50, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO',), comment="""BM rule fitted to 50 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO
    Total Standard Deviation in ln(k): 10.611232900357814"""),
    rank = 11,
    shortDesc = """BM rule fitted to 50 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO
Total Standard Deviation in ln(k): 10.611232900357814""",
    longDesc = 
"""
BM rule fitted to 50 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO
Total Standard Deviation in ln(k): 10.611232900357814
""",
)

entry(
    index = 74,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(2.0806e+08,'m^3/(mol*s)'), n=-0.868801, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12945354743023155, var=5.1318961303883475, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 4.866724612199362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 4.866724612199362""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 4.866724612199362
""",
)

entry(
    index = 75,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_N-3BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(4.68475e-16,'m^3/(mol*s)'), n=4.33877, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25723459591819103, var=7.004167867984415e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_N-3BrClFINOPSSi->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_N-3BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 0.6463180818742409"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_N-3BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 0.6463180818742409""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_N-3BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 0.6463180818742409
""",
)

entry(
    index = 76,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0",
    kinetics = ArrheniusBM(A=(4.0327e+10,'m^3/(mol*s)'), n=-2.16678, w0=(211500,'J/mol'), E0=(21150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05006066963114396, var=13.05927273070639, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0',), comment="""BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0
    Total Standard Deviation in ln(k): 7.370415170411402"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0
Total Standard Deviation in ln(k): 7.370415170411402""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0
Total Standard Deviation in ln(k): 7.370415170411402
""",
)

entry(
    index = 77,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_N-3ClFO-u0",
    kinetics = ArrheniusBM(A=(43950,'m^3/(mol*s)'), n=1, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(298,'K'), Tmax=(6000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_N-3ClFO-u0',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_N-3ClFO-u0
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_N-3ClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_N-3ClFO-u0
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R",
    kinetics = ArrheniusBM(A=(1.59771e+09,'m^3/(mol*s)'), n=-0.461068, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_Ext-1N-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 79,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N",
    kinetics = ArrheniusBM(A=(5.02e+08,'m^3/(mol*s)'), n=-0.429, w0=(83500,'J/mol'), E0=(8350,'J/mol'), Tmin=(400,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(100500,'J/mol'), E0=(10050,'J/mol'), Tmin=(200,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_1BrCClFINOPSSi->N_Ext-2R-R_3R!H-u0_N-2R->C_N-3R!H->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 81,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.87184e+19,'m^3/(mol*s)'), n=-3.55022, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23844641059262153, var=57.603460518953376, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
    Total Standard Deviation in ln(k): 15.814438099976186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 15.814438099976186""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R
Total Standard Deviation in ln(k): 15.814438099976186
""",
)

entry(
    index = 82,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.50438,'m^3/(mol*s)'), n=1.32867, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.907893749026945, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 12.331391329213428"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 12.331391329213428""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 12.331391329213428
""",
)

entry(
    index = 83,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.44945e+11,'m^3/(mol*s)'), n=-1.65317, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06481005529642031, var=7.5123365383781815, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O',), comment="""BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 5.657545930082855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 5.657545930082855""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O
Total Standard Deviation in ln(k): 5.657545930082855
""",
)

entry(
    index = 84,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04415470256864107, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
    Total Standard Deviation in ln(k): 0.11094146374030418"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C
Total Standard Deviation in ln(k): 0.11094146374030418
""",
)

entry(
    index = 85,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C",
    kinetics = ArrheniusBM(A=(129687,'m^3/(mol*s)'), n=0.801692, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3723820346018363, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
    Total Standard Deviation in ln(k): 0.9356332527684328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C
Total Standard Deviation in ln(k): 0.9356332527684328
""",
)

entry(
    index = 86,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO",
    kinetics = ArrheniusBM(A=(1.72215e+10,'m^3/(mol*s)'), n=-0.966317, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10086383407124434, var=0.31828891958274713, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO
    Total Standard Deviation in ln(k): 1.3844401162810993"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO
Total Standard Deviation in ln(k): 1.3844401162810993""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO
Total Standard Deviation in ln(k): 1.3844401162810993
""",
)

entry(
    index = 87,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO",
    kinetics = ArrheniusBM(A=(2.54838e+07,'m^3/(mol*s)'), n=-0.0939246, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.01831998695603225, var=0.7884553774065861, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO
    Total Standard Deviation in ln(k): 1.826134827396411"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO
Total Standard Deviation in ln(k): 1.826134827396411""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO
Total Standard Deviation in ln(k): 1.826134827396411
""",
)

entry(
    index = 88,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(27200,'m^3/(mol*s)'), n=0.504, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(252000,'m^3/(mol*s)'), n=0.34, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_N-2R->C_Ext-2BrFO-R_Ext-1BrCFO-R_Ext-3R!H-R_Ext-4R!H-R_Ext-3R!H-R_Ext-4R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R_Ext-5R!H-R_Ext-5R!H-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.25036e+09,'m^3/(mol*s)'), n=-0.684209, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05786324957266782, var=2.477475527142565, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R
    Total Standard Deviation in ln(k): 3.300837759866975"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 3.300837759866975""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R
Total Standard Deviation in ln(k): 3.300837759866975
""",
)

entry(
    index = 91,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(2.6786e+09,'m^3/(mol*s)'), n=-1.00932, w0=(173767,'J/mol'), E0=(17376.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05767488446129188, var=3.9211923730535494, Tref=1000.0, N=120, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R',), comment="""BM rule fitted to 120 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R
    Total Standard Deviation in ln(k): 4.114688338849182"""),
    rank = 11,
    shortDesc = """BM rule fitted to 120 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.114688338849182""",
    longDesc = 
"""
BM rule fitted to 120 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.114688338849182
""",
)

entry(
    index = 92,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C",
    kinetics = ArrheniusBM(A=(7.39762e+08,'m^3/(mol*s)'), n=-0.50372, w0=(175000,'J/mol'), E0=(17500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2591908809794792, var=0.33015705878329676, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C
    Total Standard Deviation in ln(k): 1.8031400124190624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C
Total Standard Deviation in ln(k): 1.8031400124190624""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C
Total Standard Deviation in ln(k): 1.8031400124190624
""",
)

entry(
    index = 93,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.57e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 94,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(1.35338e+07,'m^3/(mol*s)'), n=0.337482, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06473678945074876, var=0.16285884646625434, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C
    Total Standard Deviation in ln(k): 0.971681599438312"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C
Total Standard Deviation in ln(k): 0.971681599438312""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C
Total Standard Deviation in ln(k): 0.971681599438312
""",
)

entry(
    index = 95,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(229500,'J/mol'), E0=(22950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2BrCClFHNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2BrCClFHNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 96,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(3.46747e+06,'m^3/(mol*s)'), n=0.414179, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 97,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(3.156e+06,'m^3/(mol*s)'), n=0.461, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 98,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C",
    kinetics = ArrheniusBM(A=(7.22657e+07,'m^3/(mol*s)'), n=0.062, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-Sp-4R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 99,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(6.25048e+13,'m^3/(mol*s)'), n=-2.40539, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.18648777379443102, var=5.911229331536541, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C',), comment="""BM rule fitted to 28 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C
    Total Standard Deviation in ln(k): 5.342678614359075"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C
Total Standard Deviation in ln(k): 5.342678614359075""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C
Total Standard Deviation in ln(k): 5.342678614359075
""",
)

entry(
    index = 100,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_N-2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0.493, w0=(193000,'J/mol'), E0=(19300,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_N-2BrCClFHNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_N-2BrCClFHNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 101,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(2.72557e+19,'m^3/(mol*s)'), n=-4.63452, w0=(205990,'J/mol'), E0=(20599,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24103402355448392, var=24.909949774168037, Tref=1000.0, N=49, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO',), comment="""BM rule fitted to 49 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO
    Total Standard Deviation in ln(k): 10.611219541006793"""),
    rank = 11,
    shortDesc = """BM rule fitted to 49 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO
Total Standard Deviation in ln(k): 10.611219541006793""",
    longDesc = 
"""
BM rule fitted to 49 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO
Total Standard Deviation in ln(k): 10.611219541006793
""",
)

entry(
    index = 102,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_N-Sp-3C-2BrCClFHNO",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_N-Sp-3C-2BrCClFHNO',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_N-Sp-3C-2BrCClFHNO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_N-Sp-3C-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_N-Sp-3C-2BrCClFHNO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 103,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_Ext-2BrCClFHNO-R_3BrClFINOPSSi->Cl_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(2.33308e+10,'m^3/(mol*s)'), n=-1.82282, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11147627596384697, var=1.6145749306996577, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C
    Total Standard Deviation in ln(k): 2.8274263163872684"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C
Total Standard Deviation in ln(k): 2.8274263163872684""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C
Total Standard Deviation in ln(k): 2.8274263163872684
""",
)

entry(
    index = 105,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_N-2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(1.22604e+11,'m^3/(mol*s)'), n=-2.86567, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9878236278062753, var=1.2163224389653687e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_N-2BrCClFHNO->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_N-2BrCClFHNO->C
    Total Standard Deviation in ln(k): 2.488960590959741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 2.488960590959741""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 2.488960590959741
""",
)

entry(
    index = 106,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(5363.42,'m^3/(mol*s)'), n=1.12404, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 107,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(8.80412e+08,'m^3/(mol*s)'), n=-0.526391, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06493732654408726, var=6.326293338934057, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 5.205493606140169"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.205493606140169""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 5.205493606140169
""",
)

entry(
    index = 108,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C",
    kinetics = ArrheniusBM(A=(4.75713e+18,'m^3/(mol*s)'), n=-3.60639, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06907926633917837, var=1.665069358592386, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C
    Total Standard Deviation in ln(k): 2.7604273558419017"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C
Total Standard Deviation in ln(k): 2.7604273558419017""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C
Total Standard Deviation in ln(k): 2.7604273558419017
""",
)

entry(
    index = 109,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C",
    kinetics = ArrheniusBM(A=(1.47249e+09,'m^3/(mol*s)'), n=-0.901927, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11630594908302783, var=7.491462990867245, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C
    Total Standard Deviation in ln(k): 5.779293576341325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C
Total Standard Deviation in ln(k): 5.779293576341325""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C
Total Standard Deviation in ln(k): 5.779293576341325
""",
)

entry(
    index = 110,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(45504,'m^3/(mol*s)'), n=0.740315, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6642490346951677, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 1.6689674238572052"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 1.6689674238572052""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 1.6689674238572052
""",
)

entry(
    index = 111,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(3940,'m^3/(mol*s)'), n=1.25, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_N-3R!H->C_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 112,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_2C-inRing",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_2C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_2C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 113,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing",
    kinetics = ArrheniusBM(A=(1.79861e+10,'m^3/(mol*s)'), n=-0.973503, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0958344498312535, var=0.3102582992770782, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing
    Total Standard Deviation in ln(k): 1.3574442477537638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing
Total Standard Deviation in ln(k): 1.3574442477537638""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing
Total Standard Deviation in ln(k): 1.3574442477537638
""",
)

entry(
    index = 114,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R",
    kinetics = ArrheniusBM(A=(8.93312e+06,'m^3/(mol*s)'), n=1.21726e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03493343527170485, var=0.1377896602703477, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R
    Total Standard Deviation in ln(k): 0.8319307059655043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R
Total Standard Deviation in ln(k): 0.8319307059655043""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R
Total Standard Deviation in ln(k): 0.8319307059655043
""",
)

entry(
    index = 115,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R",
    kinetics = ArrheniusBM(A=(1.04452e-09,'m^3/(mol*s)'), n=4.64208, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-3R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 116,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(5.53592e+10,'m^3/(mol*s)'), n=-1.21163, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1099607804141567, var=2.984013279092352, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 3.7393222293506367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.7393222293506367""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 3.7393222293506367
""",
)

entry(
    index = 117,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=1.02942e-07, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Sp-3R!H-2R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 118,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R",
    kinetics = ArrheniusBM(A=(8.69957e+07,'m^3/(mol*s)'), n=1.4253e-07, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0307128888740362, var=2.413897921625167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
    Total Standard Deviation in ln(k): 5.704432432467972"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 5.704432432467972""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_N-Sp-3R!H-2R
Total Standard Deviation in ln(k): 5.704432432467972
""",
)

entry(
    index = 119,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1",
    kinetics = ArrheniusBM(A=(40.9293,'m^3/(mol*s)'), n=1.24752, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.12987327669238594, var=1.292644311997628, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1',), comment="""BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1
    Total Standard Deviation in ln(k): 2.6055886222411524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1
Total Standard Deviation in ln(k): 2.6055886222411524""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1
Total Standard Deviation in ln(k): 2.6055886222411524
""",
)

entry(
    index = 120,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1",
    kinetics = ArrheniusBM(A=(4.48557e+10,'m^3/(mol*s)'), n=-1.36272, w0=(173019,'J/mol'), E0=(17301.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0938559356794285, var=3.1224451969130254, Tref=1000.0, N=105, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1',), comment="""BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1
    Total Standard Deviation in ln(k): 3.7782744204661256"""),
    rank = 11,
    shortDesc = """BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1
Total Standard Deviation in ln(k): 3.7782744204661256""",
    longDesc = 
"""
BM rule fitted to 105 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1
Total Standard Deviation in ln(k): 3.7782744204661256
""",
)

entry(
    index = 121,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_2R->C",
    kinetics = ArrheniusBM(A=(7.57968e+08,'m^3/(mol*s)'), n=-0.508605, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.700128153501157, var=0.7225535388437543, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_2R->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_2R->C
    Total Standard Deviation in ln(k): 3.4632039141850433"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_2R->C
Total Standard Deviation in ln(k): 3.4632039141850433""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_2R->C
Total Standard Deviation in ln(k): 3.4632039141850433
""",
)

entry(
    index = 122,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_N-2R->C",
    kinetics = ArrheniusBM(A=(6.03e+07,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_N-2R->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_N-2R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_1CFO->C_N-2R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(2.09978e+06,'m^3/(mol*s)'), n=0.6, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 124,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C",
    kinetics = ArrheniusBM(A=(7.09e+06,'m^3/(mol*s)'), n=0.412, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_3C-inRing_Ext-3C-R_Ext-4R!H-R_Sp-5R!H=4R!H_2BrCClFHNO->C_Ext-5R!H-R_Ext-6R!H-R_N-Sp-6R!H-3C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.25707e+13,'m^3/(mol*s)'), n=-2.14843, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3076395202358357, var=8.05345241626535, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R
    Total Standard Deviation in ln(k): 6.462122178004688"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.462122178004688""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 6.462122178004688
""",
)

entry(
    index = 126,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(6.3138e+15,'m^3/(mol*s)'), n=-3.1737, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11802100062222387, var=5.132209248830105, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R
    Total Standard Deviation in ln(k): 4.838138164973991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.838138164973991""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R
Total Standard Deviation in ln(k): 4.838138164973991
""",
)

entry(
    index = 127,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.65e+19,'m^3/(mol*s)'), n=-4.58697, w0=(206085,'J/mol'), E0=(20608.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24515495939800688, var=26.116802253147934, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R',), comment="""BM rule fitted to 41 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R
    Total Standard Deviation in ln(k): 10.861085823349509"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R
Total Standard Deviation in ln(k): 10.861085823349509""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R
Total Standard Deviation in ln(k): 10.861085823349509
""",
)

entry(
    index = 128,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(5.36397e+18,'m^3/(mol*s)'), n=-4.96866, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22211687486691387, var=1.3845043931026126, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 2.916953422434711"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 2.916953422434711""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 2.916953422434711
""",
)

entry(
    index = 129,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_3ClFO->F",
    kinetics = ArrheniusBM(A=(2.43544e+08,'m^3/(mol*s)'), n=-1.28386, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11573884318841776, var=8.167824510081237e-20, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_3ClFO->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_3ClFO->F
    Total Standard Deviation in ln(k): 0.29080111411167947"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_3ClFO->F
Total Standard Deviation in ln(k): 0.29080111411167947""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_3ClFO->F
Total Standard Deviation in ln(k): 0.29080111411167947
""",
)

entry(
    index = 130,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F",
    kinetics = ArrheniusBM(A=(2.23503e+12,'m^3/(mol*s)'), n=-2.36178, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09661524904732072, var=0.021787926085924853, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F
    Total Standard Deviation in ln(k): 0.5386654892096138"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F
Total Standard Deviation in ln(k): 0.5386654892096138""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F
Total Standard Deviation in ln(k): 0.5386654892096138
""",
)

entry(
    index = 131,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(3522.05,'m^3/(mol*s)'), n=0.853275, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 132,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(8.45019e+07,'m^3/(mol*s)'), n=-0.118123, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5532200357416281, var=23.930171509944422, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 11.196858273429699"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.196858273429699""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O
Total Standard Deviation in ln(k): 11.196858273429699
""",
)

entry(
    index = 133,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.27162e+15,'m^3/(mol*s)'), n=-2.49184, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07963154977082264, var=2.3775375900976465, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R
    Total Standard Deviation in ln(k): 3.2912335802658776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.2912335802658776""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R
Total Standard Deviation in ln(k): 3.2912335802658776
""",
)

entry(
    index = 134,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(2.16447e+13,'m^3/(mol*s)'), n=-2.06111, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(3.10296e+12,'m^3/(mol*s)'), n=-1.74695, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11681749425995298, var=8.153590580517864, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 6.017930621888624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 6.017930621888624""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 6.017930621888624
""",
)

entry(
    index = 136,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl",
    kinetics = ArrheniusBM(A=(2.8155e+07,'m^3/(mol*s)'), n=-0.647062, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25939252028378723, var=6.518324262210912, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl
    Total Standard Deviation in ln(k): 5.7700309533029905"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl
Total Standard Deviation in ln(k): 5.7700309533029905""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl
Total Standard Deviation in ln(k): 5.7700309533029905
""",
)

entry(
    index = 137,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl",
    kinetics = ArrheniusBM(A=(3.10939e+06,'m^3/(mol*s)'), n=0.0816605, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2663673814050671, var=4.274201607365413, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl
    Total Standard Deviation in ln(k): 4.813882608128103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl
Total Standard Deviation in ln(k): 4.813882608128103""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl
Total Standard Deviation in ln(k): 4.813882608128103
""",
)

entry(
    index = 138,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R",
    kinetics = ArrheniusBM(A=(89.4,'m^3/(mol*s)'), n=1.54, w0=(136000,'J/mol'), E0=(13600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_1BrCFOS->S_N-2R->S_Ext-1S-R_3R!H->C_Ext-2BrCFO-R_Ext-2BrCFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.668e+09,'m^3/(mol*s)'), n=-0.7, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_Sp-3R!H-1BrCFO_N-2C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 140,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_2C-inRing",
    kinetics = ArrheniusBM(A=(5.7e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(1100,'K'), Tmax=(1400,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_2C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_2C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_2C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 141,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.11666e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.002722009781568e-09, var=2.946768157108522e-17, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing
    Total Standard Deviation in ln(k): 3.350243706446033e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 3.350243706446033e-08""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing
Total Standard Deviation in ln(k): 3.350243706446033e-08
""",
)

entry(
    index = 142,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.08094e+12,'m^3/(mol*s)'), n=-1.80793, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.16306382646369957, var=3.607899736329323, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 4.217596573522154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.217596573522154""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.217596573522154
""",
)

entry(
    index = 143,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R",
    kinetics = ArrheniusBM(A=(39.2281,'m^3/(mol*s)'), n=1.25113, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1702924000069968, var=1.2729812194748986, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R
    Total Standard Deviation in ln(k): 2.6897421601996387"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R
Total Standard Deviation in ln(k): 2.6897421601996387""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R
Total Standard Deviation in ln(k): 2.6897421601996387
""",
)

entry(
    index = 144,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C",
    kinetics = ArrheniusBM(A=(1.03801e+08,'m^3/(mol*s)'), n=-0.329513, w0=(171167,'J/mol'), E0=(17116.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011034068842652745, var=2.1438234853945657, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C',), comment="""BM rule fitted to 57 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C
    Total Standard Deviation in ln(k): 2.963017079414105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C
Total Standard Deviation in ln(k): 2.963017079414105""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C
Total Standard Deviation in ln(k): 2.963017079414105
""",
)

entry(
    index = 145,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C",
    kinetics = ArrheniusBM(A=(7.1955e+11,'m^3/(mol*s)'), n=-1.8352, w0=(175219,'J/mol'), E0=(17521.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1361305935903668, var=3.1108510248580625, Tref=1000.0, N=48, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C',), comment="""BM rule fitted to 48 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C
    Total Standard Deviation in ln(k): 3.877909166307529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 48 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C
Total Standard Deviation in ln(k): 3.877909166307529""",
    longDesc = 
"""
BM rule fitted to 48 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C
Total Standard Deviation in ln(k): 3.877909166307529
""",
)

entry(
    index = 146,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(6.89789e+06,'m^3/(mol*s)'), n=0.320215, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1549432204692236, var=11.814250086846588, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C
    Total Standard Deviation in ln(k): 9.792515455476376"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 9.792515455476376""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C
Total Standard Deviation in ln(k): 9.792515455476376
""",
)

entry(
    index = 147,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.08205e+16,'m^3/(mol*s)'), n=-3.48495, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.14561585273135627, var=1.1378792789242484, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C',), comment="""BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 2.5043484397519826"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.5043484397519826""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.5043484397519826
""",
)

entry(
    index = 148,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C",
    kinetics = ArrheniusBM(A=(1.38548e+08,'m^3/(mol*s)'), n=-0.161826, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.46230175566570203, var=1.6235518990246747, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C
    Total Standard Deviation in ln(k): 3.7159690928250226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 3.7159690928250226""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C
Total Standard Deviation in ln(k): 3.7159690928250226
""",
)

entry(
    index = 149,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1685906856221542, var=1.2199197501340515e-20, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C
    Total Standard Deviation in ln(k): 0.4235946877142727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 0.4235946877142727""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C
Total Standard Deviation in ln(k): 0.4235946877142727
""",
)

entry(
    index = 150,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F",
    kinetics = ArrheniusBM(A=(2.07198e+23,'m^3/(mol*s)'), n=-6.06291, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2303967924961832, var=23.859319948027856, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F',), comment="""BM rule fitted to 27 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F
    Total Standard Deviation in ln(k): 10.37121594447686"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 10.37121594447686""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F
Total Standard Deviation in ln(k): 10.37121594447686
""",
)

entry(
    index = 151,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(1.98054e+08,'m^3/(mol*s)'), n=-0.157873, w0=(207214,'J/mol'), E0=(20721.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03323129140190401, var=4.083175804719619, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F',), comment="""BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F
    Total Standard Deviation in ln(k): 4.134437743330804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.134437743330804""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F
Total Standard Deviation in ln(k): 4.134437743330804
""",
)

entry(
    index = 152,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_4R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(6.59422e+18,'m^3/(mol*s)'), n=-5.00764, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24335262526890036, var=0.7631371318398467, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C
    Total Standard Deviation in ln(k): 2.362729621191561"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.362729621191561""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C
Total Standard Deviation in ln(k): 2.362729621191561
""",
)

entry(
    index = 154,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_3ClO->O",
    kinetics = ArrheniusBM(A=(46800,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(1500,'K'), Tmax=(1900,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_3ClO->O',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_3ClO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_3ClO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 155,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_N-3ClO->O",
    kinetics = ArrheniusBM(A=(2.10676e+12,'m^3/(mol*s)'), n=-2.35568, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7562341902167689, var=0.0003508720633189637, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_N-3ClO->O',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_N-3ClO->O
    Total Standard Deviation in ln(k): 4.450200573228515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_N-3ClO->O
Total Standard Deviation in ln(k): 4.450200573228515""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_N-3R!H->C_N-3BrClFINOPSSi->S_3ClFO-u0_2BrCClFHNO->C_N-3ClFO->F_N-3ClO->O
Total Standard Deviation in ln(k): 4.450200573228515
""",
)

entry(
    index = 156,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1437.61,'m^3/(mol*s)'), n=1.09579, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_3R!H->F_Ext-2C-R_N-4R!H->Cl_N-4BrCFINOPSSi->O_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 157,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(3.61359e+11,'m^3/(mol*s)'), n=-1.4048, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5081716130487877, var=0.010089181152057276, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 1.4781785445817037"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 1.4781785445817037""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 1.4781785445817037
""",
)

entry(
    index = 158,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(6.91241e+11,'m^3/(mol*s)'), n=-1.58733, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.10134339370307534, var=10.628530947643105, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R
    Total Standard Deviation in ln(k): 6.790354231358722"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.790354231358722""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R
Total Standard Deviation in ln(k): 6.790354231358722
""",
)

entry(
    index = 159,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(37020.1,'m^3/(mol*s)'), n=0.273829, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2813461468811242, var=9.153871538629625, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 6.772299157089461"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 6.772299157089461""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 6.772299157089461
""",
)

entry(
    index = 160,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.53709e+30,'m^3/(mol*s)'), n=-7.08241, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_N-3BrCCl->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 161,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 162,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_N-4R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 163,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_3R!H->Cl",
    kinetics = ArrheniusBM(A=(410.863,'m^3/(mol*s)'), n=1.33656, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_3R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_3R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_3R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_N-3R!H->Cl",
    kinetics = ArrheniusBM(A=(9.27055e+16,'m^3/(mol*s)'), n=-3.45017, w0=(142500,'J/mol'), E0=(14250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.9467326792358834, var=3.292694350191029e-30, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_N-3R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_N-3R!H->Cl
    Total Standard Deviation in ln(k): 9.916413766924332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 9.916413766924332""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_1BrCFO->Br_Ext-2R-R_Ext-2R-R_Ext-2R-R_N-3R!H->Cl
Total Standard Deviation in ln(k): 9.916413766924332
""",
)

entry(
    index = 165,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R",
    kinetics = ArrheniusBM(A=(28.6108,'m^3/(mol*s)'), n=1.28701, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3508873204812941, var=1.2500735143094257, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R
    Total Standard Deviation in ln(k): 3.1230542962373744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.1230542962373744""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R
Total Standard Deviation in ln(k): 3.1230542962373744
""",
)

entry(
    index = 166,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(6.33097e+06,'m^3/(mol*s)'), n=-0.126595, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0011948175063002551, var=0.7118458320730411, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 1.6944162165011283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.6944162165011283""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.6944162165011283
""",
)

entry(
    index = 167,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(3.24036e+06,'m^3/(mol*s)'), n=3.5707e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.04752486418241179, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 0.43703622037861506"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.43703622037861506""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 0.43703622037861506
""",
)

entry(
    index = 168,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(6.44843e+07,'m^3/(mol*s)'), n=-0.33011, w0=(170692,'J/mol'), E0=(17069.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.007840303370106824, var=2.904139988716051, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R',), comment="""BM rule fitted to 39 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 3.4360760458189366"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 3.4360760458189366""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 3.4360760458189366
""",
)

entry(
    index = 169,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C",
    kinetics = ArrheniusBM(A=(2.44758e+08,'m^3/(mol*s)'), n=-0.38487, w0=(173429,'J/mol'), E0=(17342.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09783914920751006, var=1.5818145024506736, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C
    Total Standard Deviation in ln(k): 2.767186469137196"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C
Total Standard Deviation in ln(k): 2.767186469137196""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C
Total Standard Deviation in ln(k): 2.767186469137196
""",
)

entry(
    index = 170,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C",
    kinetics = ArrheniusBM(A=(4.80024e+07,'m^3/(mol*s)'), n=6.30828e-07, w0=(167875,'J/mol'), E0=(16787.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.387840458293542, var=0.625071592528832, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C
    Total Standard Deviation in ln(k): 2.559446520732723"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 2.559446520732723""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C
Total Standard Deviation in ln(k): 2.559446520732723
""",
)

entry(
    index = 171,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.36186e+10,'m^3/(mol*s)'), n=-1.36614, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13905875430346895, var=3.0720203380695703, Tref=1000.0, N=28, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R',), comment="""BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 3.8631290821312803"""),
    rank = 11,
    shortDesc = """BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 3.8631290821312803""",
    longDesc = 
"""
BM rule fitted to 28 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 3.8631290821312803
""",
)

entry(
    index = 172,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F",
    kinetics = ArrheniusBM(A=(5.63705e+14,'m^3/(mol*s)'), n=-3.04465, w0=(190375,'J/mol'), E0=(19037.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06410791560827912, var=2.0005216620447737, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F
    Total Standard Deviation in ln(k): 2.9965684202389125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F
Total Standard Deviation in ln(k): 2.9965684202389125""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F
Total Standard Deviation in ln(k): 2.9965684202389125
""",
)

entry(
    index = 173,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F",
    kinetics = ArrheniusBM(A=(5.29338e+12,'m^3/(mol*s)'), n=-2.04261, w0=(160250,'J/mol'), E0=(16025,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2188203771082984, var=0.4100118899161277, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F
    Total Standard Deviation in ln(k): 1.8334753316096015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F
Total Standard Deviation in ln(k): 1.8334753316096015""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F
Total Standard Deviation in ln(k): 1.8334753316096015
""",
)

entry(
    index = 174,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 175,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(5.18836e+06,'m^3/(mol*s)'), n=0.456743, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5242084718808067, var=0.5312435062659123, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 10.315975449803545"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 10.315975449803545""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 10.315975449803545
""",
)

entry(
    index = 176,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(3.4e+37,'m^3/(mol*s)'), n=-9.01, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.31505e+15,'m^3/(mol*s)'), n=-3.25554, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1368410772724631, var=1.8388070881481082, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 3.0622951156366054"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.0622951156366054""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 3.0622951156366054
""",
)

entry(
    index = 178,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.73542e+08,'m^3/(mol*s)'), n=-0.178898, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.047258352406939305, var=0.3305689258860327, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.271364493187482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.271364493187482""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R
Total Standard Deviation in ln(k): 1.271364493187482
""",
)

entry(
    index = 179,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16859068623744072, var=2.6680577494410207e-18, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.42359469231336816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.42359469231336816""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_N-4R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.42359469231336816
""",
)

entry(
    index = 180,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(1.78243e+26,'m^3/(mol*s)'), n=-6.75722, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2200869646324603, var=13.952702897420224, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 8.041332804775314"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 8.041332804775314""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 8.041332804775314
""",
)

entry(
    index = 181,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.90326e+19,'m^3/(mol*s)'), n=-5.05673, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24285086742318812, var=25.994086081870154, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R
    Total Standard Deviation in ln(k): 10.831198711279306"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 10.831198711279306""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R
Total Standard Deviation in ln(k): 10.831198711279306
""",
)

entry(
    index = 182,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(5.10689e+09,'m^3/(mol*s)'), n=-0.518773, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4143547313068659, var=1.0355157002903412, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C',), comment="""BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C
    Total Standard Deviation in ln(k): 3.0811165558337175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C
Total Standard Deviation in ln(k): 3.0811165558337175""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C
Total Standard Deviation in ln(k): 3.0811165558337175
""",
)

entry(
    index = 183,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_N-2BrCClFHNO->C",
    kinetics = ArrheniusBM(A=(700000,'m^3/(mol*s)'), n=0.493, w0=(229500,'J/mol'), E0=(22950,'J/mol'), Tmin=(200,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_N-2BrCClFHNO->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_N-2BrCClFHNO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_N-2BrCClFHNO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 184,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(5.61544e+19,'m^3/(mol*s)'), n=-5.23414, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24050933138795957, var=5.741630276837548e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 0.6042948040013694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.6042948040013694""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-2BrCClFHNO-R_N-4R!H->C_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.6042948040013694
""",
)

entry(
    index = 185,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(1.64994e+14,'m^3/(mol*s)'), n=-2.23152, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_Sp-3BrBrCCClCl=2C_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 186,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R",
    kinetics = ArrheniusBM(A=(503936,'m^3/(mol*s)'), n=0.201599, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4909903565862887, var=28.077794572380718, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
    Total Standard Deviation in ln(k): 11.856431408305532"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.856431408305532""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R
Total Standard Deviation in ln(k): 11.856431408305532
""",
)

entry(
    index = 187,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(1.17037e+12,'m^3/(mol*s)'), n=-1.62373, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl",
    kinetics = ArrheniusBM(A=(58730.6,'m^3/(mol*s)'), n=0.120563, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2253742378444487, var=12.06288429377589, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl
    Total Standard Deviation in ln(k): 7.52904528271911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 7.52904528271911""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl
Total Standard Deviation in ln(k): 7.52904528271911
""",
)

entry(
    index = 189,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_N-4R!H->Cl",
    kinetics = ArrheniusBM(A=(3.21509e+31,'m^3/(mol*s)'), n=-7.40295, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_N-4R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_N-4R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_N-4R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_Sp-4C-2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_Sp-4C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 191,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_N-Sp-4C-2C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_N-Sp-4C-2C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_N-Sp-4C-2C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_1BrCFO-inRing_2R->C_Ext-1BrCFO-R_N-Sp-3R!H-1BrCFO_Ext-2C-R_N-2C-inRing_4R!H->C_N-Sp-4C-2C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(1.59358e+07,'m^3/(mol*s)'), n=-0.376247, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006393725549276232, var=1.6311549262143017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 2.576445635305223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.576445635305223""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 2.576445635305223
""",
)

entry(
    index = 193,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H",
    kinetics = ArrheniusBM(A=(24.5417,'m^3/(mol*s)'), n=1.3063, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4220851556899367, var=1.3511068571537062, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
    Total Standard Deviation in ln(k): 3.390761827754295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H
Total Standard Deviation in ln(k): 3.390761827754295
""",
)

entry(
    index = 194,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(3.41997e+06,'m^3/(mol*s)'), n=2.03379e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0701791321551761e-07, var=1.3573949411693382, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
    Total Standard Deviation in ln(k): 2.3356628470831757"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 2.3356628470831757""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R
Total Standard Deviation in ln(k): 2.3356628470831757
""",
)

entry(
    index = 195,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 196,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C",
    kinetics = ArrheniusBM(A=(3.5e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_N-Sp-4R!H-2R_N-4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 197,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_Sp-3C#1CCCFFFOOO",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(700,'K'), Tmax=(1300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_Sp-3C#1CCCFFFOOO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_Sp-3C#1CCCFFFOOO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_Sp-3C#1CCCFFFOOO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_Sp-3C#1CCCFFFOOO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO",
    kinetics = ArrheniusBM(A=(6.29468e+07,'m^3/(mol*s)'), n=-0.348266, w0=(170632,'J/mol'), E0=(17063.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012449634654873082, var=2.5825066432818704, Tref=1000.0, N=38, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO',), comment="""BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO
    Total Standard Deviation in ln(k): 3.2529257132976235"""),
    rank = 11,
    shortDesc = """BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO
Total Standard Deviation in ln(k): 3.2529257132976235""",
    longDesc = 
"""
BM rule fitted to 38 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO
Total Standard Deviation in ln(k): 3.2529257132976235
""",
)

entry(
    index = 199,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(7.47266e+07,'m^3/(mol*s)'), n=-0.301656, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10484907111357072, var=0.14300243224887577, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0215437259820683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0215437259820683""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R
Total Standard Deviation in ln(k): 1.0215437259820683
""",
)

entry(
    index = 200,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(9.00812e+08,'m^3/(mol*s)'), n=-0.526094, w0=(173600,'J/mol'), E0=(17360,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4603972334580036, var=0.7845823970354294, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 2.932504259689219"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 2.932504259689219""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 2.932504259689219
""",
)

entry(
    index = 201,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(7.23e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_N-Sp-3C-1CFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 202,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C",
    kinetics = ArrheniusBM(A=(4.92788e+07,'m^3/(mol*s)'), n=6.58532e-07, w0=(200167,'J/mol'), E0=(20016.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21365566951395373, var=0.364774989589063, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C
    Total Standard Deviation in ln(k): 1.7476152162867555"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C
Total Standard Deviation in ln(k): 1.7476152162867555""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C
Total Standard Deviation in ln(k): 1.7476152162867555
""",
)

entry(
    index = 203,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_N-1CFO->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 204,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl",
    kinetics = ArrheniusBM(A=(8.48039e+08,'m^3/(mol*s)'), n=-0.908718, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17032404644494584, var=3.9774485718859824, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl
    Total Standard Deviation in ln(k): 4.426101635073538"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl
Total Standard Deviation in ln(k): 4.426101635073538""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl
Total Standard Deviation in ln(k): 4.426101635073538
""",
)

entry(
    index = 205,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl",
    kinetics = ArrheniusBM(A=(2.53626e+12,'m^3/(mol*s)'), n=-1.8378, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10717442740911076, var=1.508621620199134, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl',), comment="""BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl
    Total Standard Deviation in ln(k): 2.7316175649602186"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl
Total Standard Deviation in ln(k): 2.7316175649602186""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl
Total Standard Deviation in ln(k): 2.7316175649602186
""",
)

entry(
    index = 206,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C",
    kinetics = ArrheniusBM(A=(4.65661e+17,'m^3/(mol*s)'), n=-4.05953, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.08553242456755385, var=2.544325486723694, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C
    Total Standard Deviation in ln(k): 3.4126468711912907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C
Total Standard Deviation in ln(k): 3.4126468711912907""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C
Total Standard Deviation in ln(k): 3.4126468711912907
""",
)

entry(
    index = 207,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_N-2R->C",
    kinetics = ArrheniusBM(A=(1e+06,'m^3/(mol*s)'), n=6.47128e-08, w0=(242500,'J/mol'), E0=(24250,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.0434282959044e-09, var=5.9295617506961076e-18, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_N-2R->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_N-2R->C
    Total Standard Deviation in ln(k): 1.5041036112530567e-08"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_N-2R->C
Total Standard Deviation in ln(k): 1.5041036112530567e-08""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_N-2R->C
Total Standard Deviation in ln(k): 1.5041036112530567e-08
""",
)

entry(
    index = 208,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_3BrClNO->O",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_3BrClNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_3BrClNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_3BrClNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_3BrClNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 209,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O",
    kinetics = ArrheniusBM(A=(5.65757e+12,'m^3/(mol*s)'), n=-2.05341, w0=(158429,'J/mol'), E0=(15842.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.22151872720741464, var=0.4029210089163483, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O
    Total Standard Deviation in ln(k): 1.8291065407526694"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O
Total Standard Deviation in ln(k): 1.8291065407526694""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O
Total Standard Deviation in ln(k): 1.8291065407526694
""",
)

entry(
    index = 210,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1685906856221542, var=1.2199197501340515e-20, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.4235946877142727"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.4235946877142727""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.4235946877142727
""",
)

entry(
    index = 212,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(7.17948e+35,'m^3/(mol*s)'), n=-8.45106, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_Sp-5R!H=4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C",
    kinetics = ArrheniusBM(A=(1.12754e+08,'m^3/(mol*s)'), n=-0.120184, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27558012711070856, var=0.03551433839169183, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
    Total Standard Deviation in ln(k): 1.0702096829950607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 1.0702096829950607""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C
Total Standard Deviation in ln(k): 1.0702096829950607
""",
)

entry(
    index = 214,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.17733e+28,'m^3/(mol*s)'), n=-7.14817, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.20069573856436548, var=12.172962432766036, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R',), comment="""BM rule fitted to 12 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R
    Total Standard Deviation in ln(k): 7.498735779179855"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.498735779179855""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R
Total Standard Deviation in ln(k): 7.498735779179855
""",
)

entry(
    index = 215,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(5.12997e+21,'m^3/(mol*s)'), n=-5.85334, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.25656558522039663, var=1.7098429034420757e-17, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 0.6446371570845955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.6446371570845955""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.6446371570845955
""",
)

entry(
    index = 216,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5.88255e+21,'m^3/(mol*s)'), n=-5.40115, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24619592183496516, var=6.6520927213876994e-18, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.6185827233488472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.6185827233488472""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.6185827233488472
""",
)

entry(
    index = 217,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(3.08364e+07,'m^3/(mol*s)'), n=0.127561, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002073932384585363, var=0.5992814607467375, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R
    Total Standard Deviation in ln(k): 1.5571418941131459"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.5571418941131459""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.5571418941131459
""",
)

entry(
    index = 218,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C",
    kinetics = ArrheniusBM(A=(6.22465e+06,'m^3/(mol*s)'), n=0.377948, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8006883955311086, var=2.313585216729668, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C
    Total Standard Deviation in ln(k): 5.0610769810352565"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C
Total Standard Deviation in ln(k): 5.0610769810352565""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C
Total Standard Deviation in ln(k): 5.0610769810352565
""",
)

entry(
    index = 219,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C",
    kinetics = ArrheniusBM(A=(2.7416e+10,'m^3/(mol*s)'), n=-0.740932, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9895520210946384, var=2.792360228610262, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C
    Total Standard Deviation in ln(k): 5.8362954449323405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C
Total Standard Deviation in ln(k): 5.8362954449323405""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C
Total Standard Deviation in ln(k): 5.8362954449323405
""",
)

entry(
    index = 220,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_4R!H->F",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(163500,'J/mol'), E0=(16350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 221,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-4R!H->F",
    kinetics = ArrheniusBM(A=(2.53123,'m^3/(mol*s)'), n=1.5854, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-4R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-4R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_Ext-3BrCCl-R_Ext-2C-R_Ext-3BrCCl-R_Ext-3BrCCl-R_N-4R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R",
    kinetics = ArrheniusBM(A=(10.4062,'m^3/(mol*s)'), n=1.35186, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.622854080197693, var=2.276579561256968, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R
    Total Standard Deviation in ln(k): 17.152586198863744"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 17.152586198863744""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R
Total Standard Deviation in ln(k): 17.152586198863744
""",
)

entry(
    index = 223,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.18e+06,'m^3/(mol*s)'), n=-0.085, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C",
    kinetics = ArrheniusBM(A=(2.90265e+10,'m^3/(mol*s)'), n=-1.39113, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 225,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C",
    kinetics = ArrheniusBM(A=(500000,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_Sp-5R!H-4R!H_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(297.12,'m^3/(mol*s)'), n=0.971996, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6005523355889325, var=0.015436303854962363, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
    Total Standard Deviation in ln(k): 1.757999611670846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.757999611670846""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R
Total Standard Deviation in ln(k): 1.757999611670846
""",
)

entry(
    index = 227,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R",
    kinetics = ArrheniusBM(A=(0.004135,'m^3/(mol*s)'), n=2.525, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_N-Sp-4R!H-2R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 228,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C",
    kinetics = ArrheniusBM(A=(5.15543e+06,'m^3/(mol*s)'), n=5.67594e-08, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.7836333533627092, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
    Total Standard Deviation in ln(k): 1.7746529918743192"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C
Total Standard Deviation in ln(k): 1.7746529918743192
""",
)

entry(
    index = 229,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.505e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(200,'K'), Tmax=(300,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 230,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O",
    kinetics = ArrheniusBM(A=(3.98057e+07,'m^3/(mol*s)'), n=-0.177778, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7575655256097555e-10, var=0.3524344370596106, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O
    Total Standard Deviation in ln(k): 1.1901348113338472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O
Total Standard Deviation in ln(k): 1.1901348113338472""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O
Total Standard Deviation in ln(k): 1.1901348113338472
""",
)

entry(
    index = 231,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O",
    kinetics = ArrheniusBM(A=(6.38746e+07,'m^3/(mol*s)'), n=-0.353708, w0=(169897,'J/mol'), E0=(16989.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018626155107460924, var=2.6883519748654434, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O',), comment="""BM rule fitted to 29 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O
    Total Standard Deviation in ln(k): 3.333802030499223"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O
Total Standard Deviation in ln(k): 3.333802030499223""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O
Total Standard Deviation in ln(k): 3.333802030499223
""",
)

entry(
    index = 232,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(1.02e+08,'m^3/(mol*s)'), n=-0.32, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_Sp-3C-1CFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(7.39463e+07,'m^3/(mol*s)'), n=-0.300554, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5494627794051327, var=0.0009400122881587426, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_N-Sp-3C-1CFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 1.4420241625831092"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 1.4420241625831092""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Ext-3C-R_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 1.4420241625831092
""",
)

entry(
    index = 234,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.8435e+08,'m^3/(mol*s)'), n=-0.384133, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.002848069424167245, var=0.7068009850805346, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R
    Total Standard Deviation in ln(k): 1.6925659381508393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.6925659381508393""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.6925659381508393
""",
)

entry(
    index = 235,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_1CFO->C",
    kinetics = ArrheniusBM(A=(1.07304e+09,'m^3/(mol*s)'), n=-0.543343, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2886192288092503, var=0.16825203022957477, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_1CFO->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_1CFO->C
    Total Standard Deviation in ln(k): 1.547486922797643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 1.547486922797643""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 1.547486922797643
""",
)

entry(
    index = 236,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_3C-inRing",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 238,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing",
    kinetics = ArrheniusBM(A=(5.06714e+07,'m^3/(mol*s)'), n=6.89728e-07, w0=(210750,'J/mol'), E0=(21075,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4050962349406467, var=0.37287211026855344, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing
    Total Standard Deviation in ln(k): 2.2419862270185504"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing
Total Standard Deviation in ln(k): 2.2419862270185504""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing
Total Standard Deviation in ln(k): 2.2419862270185504
""",
)

entry(
    index = 239,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.16936e+08,'m^3/(mol*s)'), n=-0.641774, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11641395651429741, var=4.763658847086996, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R
    Total Standard Deviation in ln(k): 4.667993620595698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.667993620595698""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.667993620595698
""",
)

entry(
    index = 240,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(8.38198e+12,'m^3/(mol*s)'), n=-2.04029, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13612114977802428, var=1.081187676966171, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R
    Total Standard Deviation in ln(k): 2.42653997864881"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.42653997864881""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.42653997864881
""",
)

entry(
    index = 241,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_3BrFNO->O",
    kinetics = ArrheniusBM(A=(1.51e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_3BrFNO->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_3BrFNO->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_3BrFNO->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_3BrFNO->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 242,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_N-3BrFNO->O",
    kinetics = ArrheniusBM(A=(7.69755e+11,'m^3/(mol*s)'), n=-1.60178, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.051067813654825205, var=7.585023663413628, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_N-3BrFNO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_N-3BrFNO->O
    Total Standard Deviation in ln(k): 5.649536262812517"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_N-3BrFNO->O
Total Standard Deviation in ln(k): 5.649536262812517""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_N-3BrFNO->O
Total Standard Deviation in ln(k): 5.649536262812517
""",
)

entry(
    index = 243,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(2.8599e+18,'m^3/(mol*s)'), n=-4.29922, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05423172982666015, var=4.994967851853473, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R
    Total Standard Deviation in ln(k): 4.616728196700281"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.616728196700281""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 4.616728196700281
""",
)

entry(
    index = 244,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C",
    kinetics = ArrheniusBM(A=(4.70873e+13,'m^3/(mol*s)'), n=-2.38972, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2666282494062589, var=0.2168575770257239, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C
    Total Standard Deviation in ln(k): 1.6034846412167179"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C
Total Standard Deviation in ln(k): 1.6034846412167179""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C
Total Standard Deviation in ln(k): 1.6034846412167179
""",
)

entry(
    index = 245,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_N-1CFO->C",
    kinetics = ArrheniusBM(A=(5.15e+07,'m^3/(mol*s)'), n=-0.24, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(1.11044e+18,'m^3/(mol*s)'), n=-4.05666, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16859068623744072, var=2.6680577494410207e-18, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C_Ext-3C-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C_Ext-3C-R
    Total Standard Deviation in ln(k): 0.42359469231336816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.42359469231336816""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-2C-R_N-4R!H->C_Ext-3C-R_N-5R!H->C_Ext-3C-R
Total Standard Deviation in ln(k): 0.42359469231336816
""",
)

entry(
    index = 247,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(3.4e+37,'m^3/(mol*s)'), n=-9.01, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_Sp-3C=2BrBrCCClClFFHHNNOO_2BrCClFHNO->C_Ext-3C-R_4R!H->C_Ext-4C-R_N-Sp-5R!H=4C_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 249,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13714718440316642, var=8.664624001896876e-21, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R',), comment="""BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R
    Total Standard Deviation in ln(k): 0.34459091577245393"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.34459091577245393""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R
Total Standard Deviation in ln(k): 0.34459091577245393
""",
)

entry(
    index = 250,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-2BrCClFHNO-R",
    kinetics = ArrheniusBM(A=(1.45378e+22,'m^3/(mol*s)'), n=-5.35972, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30038578742325317, var=2.2125349285209346e-18, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-2BrCClFHNO-R',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-2BrCClFHNO-R
    Total Standard Deviation in ln(k): 0.7547381623368691"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.7547381623368691""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-2BrCClFHNO-R
Total Standard Deviation in ln(k): 0.7547381623368691
""",
)

entry(
    index = 251,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1.80332e+07,'m^3/(mol*s)'), n=0.127561, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03119957587204572, var=5.060225472910453, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.58803141017077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.58803141017077""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.58803141017077
""",
)

entry(
    index = 252,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.62598e+07,'m^3/(mol*s)'), n=0.255122, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06239915174409146, var=9.629649721936181e-35, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.15678178830173736"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 0.15678178830173736""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 0.15678178830173736
""",
)

entry(
    index = 253,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=-9.86414e-08, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 254,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(2871.48,'m^3/(mol*s)'), n=1.36056, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1284797071889134, var=1.414218845306865, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 5.2194258193619625"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 5.2194258193619625""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 5.2194258193619625
""",
)

entry(
    index = 255,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(3.19278e+10,'m^3/(mol*s)'), n=-0.758693, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.495770491077288, var=3.6624363383264167, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R',), comment="""BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 10.10734045585341"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 10.10734045585341""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_N-Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 10.10734045585341
""",
)

entry(
    index = 256,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.05803e+27,'m^3/(mol*s)'), n=-6.59025, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 257,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.98116e+19,'m^3/(mol*s)'), n=-4.24465, w0=(163500,'J/mol'), E0=(16350,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_1BrCClFOS->Cl_2R->C_Ext-2C-R_N-3R!H->F_N-3BrCClINOPSSi->O_N-Sp-3BrBrCCClCl=2C_3BrCCl->Cl_Ext-2C-R_4R!H->Cl_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 258,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing",
    kinetics = ArrheniusBM(A=(3.845,'m^3/(mol*s)'), n=1.52, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing",
    kinetics = ArrheniusBM(A=(0.0239,'m^3/(mol*s)'), n=2.243, w0=(179000,'J/mol'), E0=(17900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Ext-4R!H-R_N-Sp-5R!H-4R!H_Sp-4R!H-2R_N-4R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 260,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(7.05e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_3R!H-u1_Ext-2R-R_Sp-4R!H-2R_Ext-2R-R_5R!H->C_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 261,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.1806e+08,'m^3/(mol*s)'), n=-0.4, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.295485610028406e-10, var=0.38791698138235564, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R
    Total Standard Deviation in ln(k): 1.2486087824174392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.2486087824174392""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R
Total Standard Deviation in ln(k): 1.2486087824174392
""",
)

entry(
    index = 262,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.4799e+07,'m^3/(mol*s)'), n=-4.73122e-08, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.32434502719988945, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R
    Total Standard Deviation in ln(k): 1.141722635385032"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.141722635385032""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.141722635385032
""",
)

entry(
    index = 263,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Sp-3C-1CFO',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Sp-3C-1CFO
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 264,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(1.805e+07,'m^3/(mol*s)'), n=-3.68291e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6909130213063807e-18, var=6.138719718870696e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_N-Sp-3C-1CFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 0.01570709577335618"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 0.01570709577335618""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 0.01570709577335618
""",
)

entry(
    index = 265,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R",
    kinetics = ArrheniusBM(A=(4.85774e+09,'m^3/(mol*s)'), n=-0.980186, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.057207025163742334, var=0.8531276099959063, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R
    Total Standard Deviation in ln(k): 1.9954079399128974"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R
Total Standard Deviation in ln(k): 1.9954079399128974""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R
Total Standard Deviation in ln(k): 1.9954079399128974
""",
)

entry(
    index = 266,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-3C-R",
    kinetics = ArrheniusBM(A=(0.409014,'m^3/(mol*s)'), n=1.85633, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-3C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-3C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-3C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 267,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C",
    kinetics = ArrheniusBM(A=(7.34484e+08,'m^3/(mol*s)'), n=-0.681613, w0=(166571,'J/mol'), E0=(16657.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.32068503033866685, var=1.1176828838344544, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C',), comment="""BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C
    Total Standard Deviation in ln(k): 2.925157677090967"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 2.925157677090967""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C
Total Standard Deviation in ln(k): 2.925157677090967
""",
)

entry(
    index = 268,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C",
    kinetics = ArrheniusBM(A=(5.99728e+06,'m^3/(mol*s)'), n=0.172613, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.05133980563115594, var=4.046392929727605, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C
    Total Standard Deviation in ln(k): 4.161648994111286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 4.161648994111286""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C
Total Standard Deviation in ln(k): 4.161648994111286
""",
)

entry(
    index = 269,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO",
    kinetics = ArrheniusBM(A=(2.15423e+08,'m^3/(mol*s)'), n=-0.472233, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004984121469645847, var=0.41574972010160965, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO
    Total Standard Deviation in ln(k): 1.3051491714099865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO
Total Standard Deviation in ln(k): 1.3051491714099865""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO
Total Standard Deviation in ln(k): 1.3051491714099865
""",
)

entry(
    index = 270,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO",
    kinetics = ArrheniusBM(A=(1.49777e+08,'m^3/(mol*s)'), n=-0.266667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.142704777211466e-08, var=0.5786109659413581, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO
    Total Standard Deviation in ln(k): 1.5249315225351794"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO
Total Standard Deviation in ln(k): 1.5249315225351794""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO
Total Standard Deviation in ln(k): 1.5249315225351794
""",
)

entry(
    index = 271,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(242500,'J/mol'), E0=(24250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_N-2R->C_1CFO->C_N-3C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 272,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(7.26211e+07,'m^3/(mol*s)'), n=-0.41693, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.048519644931502605, var=1.0788940164427216, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 2.2042234354323424"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.2042234354323424""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.2042234354323424
""",
)

entry(
    index = 273,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.44152e+07,'m^3/(mol*s)'), n=-0.550196, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.9534931455874083, var=34.75099486170533, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 19.238745205829638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 19.238745205829638""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 19.238745205829638
""",
)

entry(
    index = 274,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(9.13472e+10,'m^3/(mol*s)'), n=-1.32878, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10529423638649646, var=0.7406563218955247, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R',), comment="""BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 1.9898612994239544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.9898612994239544""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.9898612994239544
""",
)

entry(
    index = 275,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.24e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(9.05135e+16,'m^3/(mol*s)'), n=-3.59877, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16792167373388434, var=1.7635732587478254e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 0.42191375394209873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.42191375394209873""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_3BrClFNO->F_2R->C_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.42191375394209873
""",
)

entry(
    index = 277,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_3BrClN->Br",
    kinetics = ArrheniusBM(A=(2.03554e+14,'m^3/(mol*s)'), n=-2.60504, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1638415524160766, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_3BrClN->Br',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_3BrClN->Br
    Total Standard Deviation in ln(k): 5.4367878201408955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_3BrClN->Br
Total Standard Deviation in ln(k): 5.4367878201408955""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_3BrClN->Br
Total Standard Deviation in ln(k): 5.4367878201408955
""",
)

entry(
    index = 278,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br",
    kinetics = ArrheniusBM(A=(3.22768e+13,'m^3/(mol*s)'), n=-2.33417, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.3724716826868084, var=0.23849155536046607, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br
    Total Standard Deviation in ln(k): 1.9148828464797465"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br
Total Standard Deviation in ln(k): 1.9148828464797465""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br
Total Standard Deviation in ln(k): 1.9148828464797465
""",
)

entry(
    index = 279,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1371471848143452, var=1.1591394844637247e-19, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F',), comment="""BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F
    Total Standard Deviation in ln(k): 0.34459091730149266"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.34459091730149266""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F
Total Standard Deviation in ln(k): 0.34459091730149266
""",
)

entry(
    index = 280,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 281,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_Ext-5R!H-R_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 282,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.92e+07,'m^3/(mol*s)'), n=0.18, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(200,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_5R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 283,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C_Ext-4BrCClINOPSSi-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C_Ext-4BrCClINOPSSi-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C_Ext-4BrCClINOPSSi-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Ext-2C-R_N-5R!H->C_Ext-4BrCClINOPSSi-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 284,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_N-4R!H->F_2BrCClFHNO->C_Sp-4BrCClINOPSSi=3C_Ext-4BrCClINOPSSi-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(8.53922e+07,'m^3/(mol*s)'), n=-0.366667, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1517566980346945e-11, var=0.6179647340096732, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 1.575936938732236"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.575936938732236""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 1.575936938732236
""",
)

entry(
    index = 286,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(4.39875e+10,'m^3/(mol*s)'), n=-1.26204, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0030396131424987095, var=0.36797093961066396, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO',), comment="""BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 1.2237217111697811"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO
Total Standard Deviation in ln(k): 1.2237217111697811""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO
Total Standard Deviation in ln(k): 1.2237217111697811
""",
)

entry(
    index = 288,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(578146,'m^3/(mol*s)'), n=0.175759, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06243996161282631, var=0.8653650783542394, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_N-Sp-3C-1CFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 2.0217891484895985"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 2.0217891484895985""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 2.0217891484895985
""",
)

entry(
    index = 289,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(7.17322e+08,'m^3/(mol*s)'), n=-0.682487, w0=(165500,'J/mol'), E0=(16550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5901830930098657, var=1.4362044171026478, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO',), comment="""BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO
    Total Standard Deviation in ln(k): 3.885381619664692"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 3.885381619664692""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO
Total Standard Deviation in ln(k): 3.885381619664692
""",
)

entry(
    index = 290,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_N-Sp-3C-1CFO",
    kinetics = ArrheniusBM(A=(2.34255e+09,'m^3/(mol*s)'), n=-0.638761, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.140841174280219, var=5.711815422248178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_N-Sp-3C-1CFO',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_N-Sp-3C-1CFO
    Total Standard Deviation in ln(k): 12.682758220790616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 12.682758220790616""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_N-Sp-3C-1CFO
Total Standard Deviation in ln(k): 12.682758220790616
""",
)

entry(
    index = 291,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=1.67934e-07, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C_Ext-1CFO-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_N-4CF->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 292,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(6.90628e+07,'m^3/(mol*s)'), n=-0.319465, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14995901122765223, var=2.2305291506772655, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO_Ext-1CFO-R
    Total Standard Deviation in ln(k): 3.3708444816661607"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO_Ext-1CFO-R
Total Standard Deviation in ln(k): 3.3708444816661607""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_Sp-4R!H-1CFO_Ext-1CFO-R
Total Standard Deviation in ln(k): 3.3708444816661607
""",
)

entry(
    index = 293,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_4R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_4R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_4R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_4R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 294,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_N-4R!H->C",
    kinetics = ArrheniusBM(A=(4.09878e+08,'m^3/(mol*s)'), n=-0.4, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.8811179631144743, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_N-4R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_N-4R!H->C
    Total Standard Deviation in ln(k): 2.749571418511616"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_N-4R!H->C
Total Standard Deviation in ln(k): 2.749571418511616""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_2R->C_Sp-3C-1CFO_Ext-1CFO-R_N-Sp-4R!H-1CFO_N-4R!H->C
Total Standard Deviation in ln(k): 2.749571418511616
""",
)

entry(
    index = 295,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_4R!H->Br",
    kinetics = ArrheniusBM(A=(1.4e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_4R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_4R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_4R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br",
    kinetics = ArrheniusBM(A=(1.40244e+08,'m^3/(mol*s)'), n=-0.486419, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05660625172859984, var=0.9524191860499192, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br',), comment="""BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br
    Total Standard Deviation in ln(k): 2.098687141621911"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br
Total Standard Deviation in ln(k): 2.098687141621911""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br
Total Standard Deviation in ln(k): 2.098687141621911
""",
)

entry(
    index = 297,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(0.0134456,'m^3/(mol*s)'), n=2.34822, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(4.26442e+10,'m^3/(mol*s)'), n=-1.26041, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10235543516142294, var=0.7759547869051413, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R',), comment="""BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 2.0231114265631125"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.0231114265631125""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.0231114265631125
""",
)

entry(
    index = 299,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.65365e+14,'m^3/(mol*s)'), n=-2.594, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.8775975191208785, var=1.1652692990436386, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 16.931897167737755"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R
Total Standard Deviation in ln(k): 16.931897167737755""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R
Total Standard Deviation in ln(k): 16.931897167737755
""",
)

entry(
    index = 300,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->Br",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->Br',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_6R!H->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 301,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13714718393857422, var=4.296246033701425e-20, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br',), comment="""BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br
    Total Standard Deviation in ln(k): 0.3445909148340574"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br
Total Standard Deviation in ln(k): 0.3445909148340574""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br
Total Standard Deviation in ln(k): 0.3445909148340574
""",
)

entry(
    index = 302,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2.26848e+08,'m^3/(mol*s)'), n=-0.55, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.18719384195212638, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C
    Total Standard Deviation in ln(k): 0.8673667472246991"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C
Total Standard Deviation in ln(k): 0.8673667472246991""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C
Total Standard Deviation in ln(k): 0.8673667472246991
""",
)

entry(
    index = 303,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 304,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R",
    kinetics = ArrheniusBM(A=(2.44774e+10,'m^3/(mol*s)'), n=-1.14151, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11100709579342413, var=0.1730059539720224, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R
    Total Standard Deviation in ln(k): 1.1127614966912505"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R
Total Standard Deviation in ln(k): 1.1127614966912505""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R
Total Standard Deviation in ln(k): 1.1127614966912505
""",
)

entry(
    index = 305,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R",
    kinetics = ArrheniusBM(A=(8.65419e+10,'m^3/(mol*s)'), n=-1.4012, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11076293667129158, var=0.13376655749343178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R
    Total Standard Deviation in ln(k): 1.01151286269961"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R
Total Standard Deviation in ln(k): 1.01151286269961""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R
Total Standard Deviation in ln(k): 1.01151286269961
""",
)

entry(
    index = 306,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C",
    kinetics = ArrheniusBM(A=(7.629e+08,'m^3/(mol*s)'), n=-0.689515, w0=(174091,'J/mol'), E0=(17409.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5540778563735251, var=1.325187266826214, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C',), comment="""BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C
    Total Standard Deviation in ln(k): 3.699941854493604"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 3.699941854493604""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C
Total Standard Deviation in ln(k): 3.699941854493604
""",
)

entry(
    index = 307,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_N-1CFO->C",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(71000,'J/mol'), E0=(7100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_N-1CFO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_N-1CFO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_N-1CFO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 308,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl",
    kinetics = ArrheniusBM(A=(2.70046e+07,'m^3/(mol*s)'), n=-0.310596, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05062258054154351, var=0.555601658559399, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl
    Total Standard Deviation in ln(k): 1.6214957155565641"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 1.6214957155565641""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl
Total Standard Deviation in ln(k): 1.6214957155565641
""",
)

entry(
    index = 309,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl",
    kinetics = ArrheniusBM(A=(3.7825e+09,'m^3/(mol*s)'), n=-0.838064, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0315988796402227, var=1.2438535871505778, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl
    Total Standard Deviation in ln(k): 4.827801613908831"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 4.827801613908831""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl
Total Standard Deviation in ln(k): 4.827801613908831
""",
)

entry(
    index = 310,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_3BrFNO->Br",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_3BrFNO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_3BrFNO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_3BrFNO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_3BrFNO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 312,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_N-3BrFNO->Br",
    kinetics = ArrheniusBM(A=(1.02195e+12,'m^3/(mol*s)'), n=-1.67613, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13714718584253066, var=5.228362359963174e-20, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_N-3BrFNO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_N-3BrFNO->Br
    Total Standard Deviation in ln(k): 0.3445909196607333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_N-3BrFNO->Br
Total Standard Deviation in ln(k): 0.3445909196607333""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_N-3BrClFNO->Cl_Ext-1CFO-R_Ext-2R-R_Ext-1CFO-R_N-3BrFNO->Br
Total Standard Deviation in ln(k): 0.3445909196607333
""",
)

entry(
    index = 313,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.54e+40,'m^3/(mol*s)'), n=-10.66, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_N-3BrClFNO->F_N-3BrClNO->O_1CFO->C_N-3BrClN->Br_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_6ClF->Cl",
    kinetics = ArrheniusBM(A=(1.12e+41,'m^3/(mol*s)'), n=-10.8, w0=(205500,'J/mol'), E0=(20550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_6ClF->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_6ClF->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_6ClF->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_N-6ClF->Cl",
    kinetics = ArrheniusBM(A=(4.38538e+32,'m^3/(mol*s)'), n=-8.31613, w0=(205500,'J/mol'), E0=(20550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13714718465443898, var=1.2029905117948116e-19, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_N-6ClF->Cl',), comment="""BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_N-6ClF->Cl
    Total Standard Deviation in ln(k): 0.34459091691250876"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_N-6ClF->Cl
Total Standard Deviation in ln(k): 0.34459091691250876""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_1R->H_N-2R->S_N-2BrCClFHNO-inRing_Ext-2BrCClFHNO-R_3R!H->C_N-3C-inRing_N-Sp-3C=2BrBrCCClClFFHHNNOO_Sp-3C-2BrCClFHNO_Ext-3C-R_4R!H->F_Ext-2BrCClFHNO-R_Ext-3C-R_Ext-3C-R_5R!H->F_N-6R!H->Br_N-6ClF->Cl
Total Standard Deviation in ln(k): 0.34459091691250876
""",
)

entry(
    index = 316,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(7.75e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_4R!H->O_Ext-2R-R_Ext-1CFO-R_6R!H->C_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R",
    kinetics = ArrheniusBM(A=(3.69232e+10,'m^3/(mol*s)'), n=-1.20229, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1712378092162478, var=0.08255313157821662, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R
    Total Standard Deviation in ln(k): 1.0062474524062741"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R
Total Standard Deviation in ln(k): 1.0062474524062741""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R
Total Standard Deviation in ln(k): 1.0062474524062741
""",
)

entry(
    index = 318,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(5.33075e+08,'m^3/(mol*s)'), n=-0.628757, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0654184655381604, var=1.7047547111797594, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 2.781875529915891"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.781875529915891""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R
Total Standard Deviation in ln(k): 2.781875529915891
""",
)

entry(
    index = 319,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_3C-inRing",
    kinetics = ArrheniusBM(A=(3.144e+13,'m^3/(mol*s)'), n=-2.163, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_N-3C-inRing",
    kinetics = ArrheniusBM(A=(1.307e+06,'m^3/(mol*s)'), n=0.192, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_N-Sp-4CF-2R_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 321,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R",
    kinetics = ArrheniusBM(A=(8.09045e+08,'m^3/(mol*s)'), n=-0.842857, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.923656835879974e-09, var=1.2914637284046604, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R
    Total Standard Deviation in ln(k): 2.2782327881968145"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R
Total Standard Deviation in ln(k): 2.2782327881968145""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R
Total Standard Deviation in ln(k): 2.2782327881968145
""",
)

entry(
    index = 322,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.38319e+06,'m^3/(mol*s)'), n=-3.04169e-07, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.3279077205677291, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.1479760049827752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.1479760049827752
""",
)

entry(
    index = 323,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R",
    kinetics = ArrheniusBM(A=(10014.3,'m^3/(mol*s)'), n=0.814498, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.051475620584770475, var=0.500522578161536, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R
    Total Standard Deviation in ln(k): 1.5476380911844276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 1.5476380911844276""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R
Total Standard Deviation in ln(k): 1.5476380911844276
""",
)

entry(
    index = 324,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_5R!H->F",
    kinetics = ArrheniusBM(A=(2.61e+20,'m^3/(mol*s)'), n=-4.16, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_N-5R!H->F",
    kinetics = ArrheniusBM(A=(1.4e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_N-4ClF->Cl_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 326,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF",
    kinetics = ArrheniusBM(A=(3.48129e+07,'m^3/(mol*s)'), n=-0.157514, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.13083693107632094, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF
    Total Standard Deviation in ln(k): 0.32873600772944955"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF
Total Standard Deviation in ln(k): 0.32873600772944955""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF
Total Standard Deviation in ln(k): 0.32873600772944955
""",
)

entry(
    index = 327,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF",
    kinetics = ArrheniusBM(A=(5.67927e+10,'m^3/(mol*s)'), n=-1.26686, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04628379485594601, var=0.016181722463235428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF
    Total Standard Deviation in ln(k): 0.3713080775392354"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF
Total Standard Deviation in ln(k): 0.3713080775392354""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF
Total Standard Deviation in ln(k): 0.3713080775392354
""",
)

entry(
    index = 328,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(7.24e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-1CFO-R_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.55114e+09,'m^3/(mol*s)'), n=-1.1, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6290223088470565e-10, var=2.385481895038608, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
    Total Standard Deviation in ln(k): 3.096314395311866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.096314395311866""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R
Total Standard Deviation in ln(k): 3.096314395311866
""",
)

entry(
    index = 330,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(4.98065e+08,'m^3/(mol*s)'), n=-0.75, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.8575717470917588, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 1.8564883221612534"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.8564883221612534""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 1.8564883221612534
""",
)

entry(
    index = 331,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(9.04e+06,'m^3/(mol*s)'), n=0, w0=(179000,'J/mol'), E0=(17900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 332,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.41e+06,'m^3/(mol*s)'), n=0.13553, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0385813605207894, var=0.9147642637194141, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R
    Total Standard Deviation in ln(k): 4.52689587899475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.52689587899475""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R
Total Standard Deviation in ln(k): 4.52689587899475
""",
)

entry(
    index = 333,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF_Ext-1CFO-R",
    kinetics = ArrheniusBM(A=(1.02e+07,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF_Ext-1CFO-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF_Ext-1CFO-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_Sp-5R!H=4CCFF_Ext-1CFO-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 334,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_3C-inRing",
    kinetics = ArrheniusBM(A=(5.781e+11,'m^3/(mol*s)'), n=-1.568, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_N-3C-inRing",
    kinetics = ArrheniusBM(A=(5.89e+07,'m^3/(mol*s)'), n=-0.278, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_N-3C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_N-3C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_Ext-4CF-R_Sp-3C-1CFO_Sp-4CF-2R_Ext-3C-R_N-Sp-5R!H=4CCFF_N-3C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.14759e+09,'m^3/(mol*s)'), n=-1.3, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.519561616726178, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 4.70987392894025"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 4.70987392894025
""",
)

entry(
    index = 337,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_5R!H->F",
    kinetics = ArrheniusBM(A=(2.8e+06,'m^3/(mol*s)'), n=0, w0=(173000,'J/mol'), E0=(17300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(0.00243875,'m^3/(mol*s)'), n=2.77174, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_N-5R!H->F',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_N-5R!H->F
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_N-3R!H->C_Ext-2R-R_3BrClFNO->Cl_Ext-1CFO-R_Ext-1CFO-R_N-4R!H->Br_4ClF->Cl_Ext-2R-R_Ext-2R-R_N-5R!H->F
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R",
    kinetics = ArrheniusBM(A=(1.24e+10,'m^3/(mol*s)'), n=-1.5, w0=(173000,'J/mol'), E0=(17300,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-1R->H_N-1BrCClFINOPSSi->N_N-1BrCClFOS->Cl_N-1BrCFOS->S_N-1BrCFO-inRing_N-1BrCFO->Br_Ext-1CFO-R_N-3R!H-u1_3R!H->C_Ext-2R-R_N-Sp-3C#1CCCFFFOOO_N-4R!H->O_4CF->C_Sp-3C-1CFO_1CFO->C_Ext-2R-R_Ext-1C-R_Ext-1C-R_Ext-2R-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

