#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_carbene/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(9.78959e+36,'m^3/(mol*s)'), n=-9.26339, w0=(568520,'J/mol'), E0=(215623,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5069527339930501, var=11.078516729527172, Tref=1000.0, N=25, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 25 training reactions at node Root
    Total Standard Deviation in ln(k): 7.9463921821915"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 7.9463921821915""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root
Total Standard Deviation in ln(k): 7.9463921821915
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.2452e-26,'m^3/(mol*s)'), n=8.92699, w0=(563625,'J/mol'), E0=(33963.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8071030706521074, var=93.94425025667427, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 21.458760255202325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 21.458760255202325""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 21.458760255202325
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(5.55251e+06,'m^3/(mol*s)'), n=-0.310407, w0=(570824,'J/mol'), E0=(57082.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.031843025753362175, var=10.661257638723207, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 6.625784646463903"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.625784646463903""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 6.625784646463903
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(3.63226e-07,'m^3/(mol*s)'), n=3.20783, w0=(454500,'J/mol'), E0=(45450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5438904038945364, var=0.008206778568974105, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 1.5481703045100408"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 1.5481703045100408""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 1.5481703045100408
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s",
    kinetics = ArrheniusBM(A=(2.01051e+12,'m^3/(mol*s)'), n=-2.21106, w0=(600000,'J/mol'), E0=(201898,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-9.63079803293357, var=577.2745399809592, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
    Total Standard Deviation in ln(k): 72.36482901307559"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 72.36482901307559""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s
Total Standard Deviation in ln(k): 72.36482901307559
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(5660.64,'m^3/(mol*s)'), n=-0.0175809, w0=(539200,'J/mol'), E0=(53920,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0848021773500138, var=11.931633825938562, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
    Total Standard Deviation in ln(k): 7.13786622111491"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 7.13786622111491""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 7.13786622111491
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(4.61758e+07,'m^3/(mol*s)'), n=-0.400452, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0419529894091338, var=0.11001473470189206, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s',), comment="""BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
    Total Standard Deviation in ln(k): 0.7703494571952925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 0.7703494571952925""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s
Total Standard Deviation in ln(k): 0.7703494571952925
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(214000,'m^3/(mol*s)'), n=0, w0=(529000,'J/mol'), E0=(113414,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(3200,'m^3/(mol*s)'), n=0, w0=(380000,'J/mol'), E0=(38000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(1.00824e-07,'m^3/(mol*s)'), n=3.1317, w0=(515000,'J/mol'), E0=(580.194,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5486944081657859, var=11.420385480293012, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s
    Total Standard Deviation in ln(k): 10.66600589758599"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s
Total Standard Deviation in ln(k): 10.66600589758599""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s
Total Standard Deviation in ln(k): 10.66600589758599
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s",
    kinetics = ArrheniusBM(A=(947270,'m^3/(mol*s)'), n=0.260326, w0=(642500,'J/mol'), E0=(306326,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.314389410026602, var=91.70161665088662, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s
    Total Standard Deviation in ln(k): 25.012584539151778"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s
Total Standard Deviation in ln(k): 25.012584539151778""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s
Total Standard Deviation in ln(k): 25.012584539151778
""",
)

entry(
    index = 12,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 13,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s",
    kinetics = ArrheniusBM(A=(47898.6,'m^3/(mol*s)'), n=-0.412447, w0=(562250,'J/mol'), E0=(56225,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.791492089283419, var=8.112746543343587, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
    Total Standard Deviation in ln(k): 7.698737163487375"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 7.698737163487375""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s
Total Standard Deviation in ln(k): 7.698737163487375
""",
)

entry(
    index = 14,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs",
    kinetics = ArrheniusBM(A=(1.89529e+06,'m^3/(mol*s)'), n=0.011582, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.020986416531298856, var=0.0724196226211752, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs
    Total Standard Deviation in ln(k): 0.5922218252841055"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs
Total Standard Deviation in ln(k): 0.5922218252841055""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs
Total Standard Deviation in ln(k): 0.5922218252841055
""",
)

entry(
    index = 15,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs",
    kinetics = ArrheniusBM(A=(1.33863e+08,'m^3/(mol*s)'), n=-0.537796, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04894184607890469, var=0.08258735315105603, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs',), comment="""BM rule fitted to 9 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs
    Total Standard Deviation in ln(k): 0.6990905386106441"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs
Total Standard Deviation in ln(k): 0.6990905386106441""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs
Total Standard Deviation in ln(k): 0.6990905386106441
""",
)

entry(
    index = 16,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(2.53881,'m^3/(mol*s)'), n=1.26919, w0=(583000,'J/mol'), E0=(96168.2,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(321,'m^3/(mol*s)'), n=0, w0=(447000,'J/mol'), E0=(44700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_4CbCdCl1sCsCtF1sH->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(7.21841e-98,'m^3/(mol*s)'), n=30.6922, w0=(647667,'J/mol'), E0=(-30281.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-36.17174314146646, var=1117.2133875366187, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 157.89152977059396"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 157.89152977059396""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 157.89152977059396
""",
)

entry(
    index = 19,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_N-3Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(2.25e+11,'m^3/(mol*s)'), n=-2.85, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_N-3Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_N-3Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_N-3Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_N-3Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 20,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(302939,'m^3/(mol*s)'), n=-0.602721, w0=(555333,'J/mol'), E0=(55533.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.039338863304941726, var=2.030759405409962, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s',), comment="""BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.955683391701264"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.955683391701264""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.955683391701264
""",
)

entry(
    index = 21,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-2Br1sCl1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.33736e+17,'m^3/(mol*s)'), n=-4.54388, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-2Br1sCl1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-2Br1sCl1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_N-2Br1sCl1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 22,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(6.23333e+06,'m^3/(mol*s)'), n=-0.146, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 23,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(1.05212e+06,'m^3/(mol*s)'), n=0.0895127, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.47428387515166337, var=0.06288991772562845, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 1.6944127300954472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 1.6944127300954472
""",
)

entry(
    index = 24,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3.43491e+08,'m^3/(mol*s)'), n=-0.665687, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.054507644641452926, var=0.030906577146168814, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 0.4893916509466332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 0.4893916509466332
""",
)

entry(
    index = 25,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R",
    kinetics = ArrheniusBM(A=(2.13e+07,'m^3/(mol*s)'), n=-0.274, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-4CbCdCt-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 26,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.325e+06,'m^3/(mol*s)'), n=0.0073, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(33.15,'m^3/(mol*s)'), n=1.475, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_4CsF1sH->H",
    kinetics = ArrheniusBM(A=(1.7,'m^3/(mol*s)'), n=-0.71, w0=(627000,'J/mol'), E0=(62700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_4CsF1sH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_4CsF1sH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_4CsF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_4CsF1sH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H",
    kinetics = ArrheniusBM(A=(8.60518e+06,'m^3/(mol*s)'), n=0.108311, w0=(658000,'J/mol'), E0=(311945,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3006148579604344, var=3.843624111345615, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H
    Total Standard Deviation in ln(k): 7.198192297764078"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H
Total Standard Deviation in ln(k): 7.198192297764078""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H
Total Standard Deviation in ln(k): 7.198192297764078
""",
)

entry(
    index = 30,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H",
    kinetics = ArrheniusBM(A=(6.21796e+08,'m^3/(mol*s)'), n=-1.68024, w0=(583000,'J/mol'), E0=(-40149,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.480938579353241, var=7.009747379363687, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H
    Total Standard Deviation in ln(k): 6.516110450515046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H
Total Standard Deviation in ln(k): 6.516110450515046""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H
Total Standard Deviation in ln(k): 6.516110450515046
""",
)

entry(
    index = 31,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_N-5CsH->H",
    kinetics = ArrheniusBM(A=(739000,'m^3/(mol*s)'), n=0, w0=(500000,'J/mol'), E0=(50000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_N-5CsH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_N-5CsH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_N-5CsH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_N-5CsH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(4933.33,'m^3/(mol*s)'), n=0.797, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_4Br1sCbCdCsCtF1sH->Cs_Ext-4Cs-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(36700,'m^3/(mol*s)'), n=0.498, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt",
    kinetics = ArrheniusBM(A=(4.06627e+08,'m^3/(mol*s)'), n=-0.685418, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.053647963869693845, var=0.029065280330606125, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt',), comment="""BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
    Total Standard Deviation in ln(k): 0.476571991887303"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.476571991887303""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt
Total Standard Deviation in ln(k): 0.476571991887303
""",
)

entry(
    index = 35,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_4CsF1s->F1s",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(658000,'J/mol'), E0=(307107,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_4CsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_4CsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_4CsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_4CsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_N-4CsF1s->F1s",
    kinetics = ArrheniusBM(A=(4e+07,'m^3/(mol*s)'), n=0, w0=(658000,'J/mol'), E0=(307107,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_N-4CsF1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_N-4CsF1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_N-4CsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Br1s_N-4CbCdCl1sCsCtF1sH->Cl1s_3Br1sCl1sF1sHI1s->F1s_N-4CsF1sH->H_N-4CsF1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_3Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(0.109762,'m^3/(mol*s)'), n=1.4247, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_3Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_3Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 38,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_N-3Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(1.01504e+27,'m^3/(mol*s)'), n=-7.09688, w0=(583000,'J/mol'), E0=(58300,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_N-3Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-5Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->Cl1s_2Br1sCl1sHI1s->Cl1s_5CsH->H_N-3Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 39,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0.465, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H",
    kinetics = ArrheniusBM(A=(4.54161e+08,'m^3/(mol*s)'), n=-0.709186, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.052492247434476294, var=0.01116623172253938, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
    Total Standard Deviation in ln(k): 0.34373121019806296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.34373121019806296""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H
Total Standard Deviation in ln(k): 0.34373121019806296
""",
)

entry(
    index = 41,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.91963e+09,'m^3/(mol*s)'), n=-0.927006, w0=(584000,'J/mol'), E0=(58400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.787034462320638, var=0.09796882358847864, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
    Total Standard Deviation in ln(k): 2.6049550376933333"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R
Total Standard Deviation in ln(k): 2.6049550376933333
""",
)

entry(
    index = 42,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.985e+07,'m^3/(mol*s)'), n=-0.324, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(203,'m^3/(mol*s)'), n=1.249, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(131500,'m^3/(mol*s)'), n=0.313, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd",
    kinetics = ArrheniusBM(A=(1.08e+07,'m^3/(mol*s)'), n=-0.272, w0=(584000,'J/mol'), E0=(58400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCl1sF1sHI1s->F1s_N-4Br1sCbCdCl1sCsCtF1sHI1sNOSSidSis->Cl1s_N-4Br1sCbCdCsCtF1sH->Cs_Ext-4CbCdCt-R_Ext-6R!H-R_N-Sp-6R!H-4CbCdCt_N-Sp-7R!H=6R!H_Ext-7R!H-R_N-4CbCdCt->Cd
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

