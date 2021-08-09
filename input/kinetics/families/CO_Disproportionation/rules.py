#!/usr/bin/env python
# encoding: utf-8

name = "CO_Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(2.22426e+08,'m^3/(mol*s)'), n=-0.301764, w0=(544981,'J/mol'), E0=(51732.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.006388822537056984, var=1.4712210763951121, Tref=1000.0, N=54, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 54 training reactions at node Root
    Total Standard Deviation in ln(k): 2.4476737264596995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 2.4476737264596995""",
    longDesc = 
"""
BM rule fitted to 54 training reactions at node Root
Total Standard Deviation in ln(k): 2.4476737264596995
""",
)

entry(
    index = 2,
    label = "Root_4R->F",
    kinetics = ArrheniusBM(A=(1.69721e+18,'m^3/(mol*s)'), n=-3.86209, w0=(568500,'J/mol'), E0=(73454.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.1771326855856117, var=6.417877063601093, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->F',), comment="""BM rule fitted to 3 training reactions at node Root_4R->F
    Total Standard Deviation in ln(k): 10.54888410757313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.54888410757313""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->F
Total Standard Deviation in ln(k): 10.54888410757313
""",
)

entry(
    index = 3,
    label = "Root_N-4R->F",
    kinetics = ArrheniusBM(A=(2.11366e+08,'m^3/(mol*s)'), n=-0.294736, w0=(543598,'J/mol'), E0=(51369.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0012520580635417735, var=1.4643578437736127, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_N-4R->F',), comment="""BM rule fitted to 51 training reactions at node Root_N-4R->F
    Total Standard Deviation in ln(k): 2.4290889073111277"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4290889073111277""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_N-4R->F
Total Standard Deviation in ln(k): 2.4290889073111277
""",
)

entry(
    index = 4,
    label = "Root_4R->F_2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(3.6499e+06,'m^3/(mol*s)'), n=-0.423216, w0=(456500,'J/mol'), E0=(49548.8,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->F_2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->F_2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.52184e-07, w0=(624500,'J/mol'), E0=(62450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->F_N-2Br1sCl1sF1sHI1s->F1s
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 6,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(4.93018e+06,'m^3/(mol*s)'), n=0.259157, w0=(448250,'J/mol'), E0=(44825,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.032573794078536895, var=4.955525486373488, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 4.54458638506556"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 4.54458638506556""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 4.54458638506556
""",
)

entry(
    index = 7,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s",
    kinetics = ArrheniusBM(A=(2.19491e+08,'m^3/(mol*s)'), n=-0.30092, w0=(556311,'J/mol'), E0=(51195.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0014149104702751924, var=1.4438819201272397, Tref=1000.0, N=45, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s',), comment="""BM rule fitted to 45 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s
    Total Standard Deviation in ln(k): 2.4124775541887873"""),
    rank = 11,
    shortDesc = """BM rule fitted to 45 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.4124775541887873""",
    longDesc = 
"""
BM rule fitted to 45 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s
Total Standard Deviation in ln(k): 2.4124775541887873
""",
)

entry(
    index = 8,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(1.5e+06,'m^3/(mol*s)'), n=0, w0=(463500,'J/mol'), E0=(46350,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C",
    kinetics = ArrheniusBM(A=(7.42117e+06,'m^3/(mol*s)'), n=0.222523, w0=(445200,'J/mol'), E0=(44520,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.00919884446391129, var=4.449716835696711, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C
    Total Standard Deviation in ln(k): 4.251971400488752"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 4.251971400488752""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C
Total Standard Deviation in ln(k): 4.251971400488752
""",
)

entry(
    index = 10,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->Br",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(523000,'J/mol'), E0=(52300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_4BrCClHINOPSSi->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 11,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br",
    kinetics = ArrheniusBM(A=(2.19474e+08,'m^3/(mol*s)'), n=-0.300916, w0=(557068,'J/mol'), E0=(51197.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0014216909364421048, var=1.4438491660861983, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br',), comment="""BM rule fitted to 44 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br
    Total Standard Deviation in ln(k): 2.412467267528119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br
Total Standard Deviation in ln(k): 2.412467267528119""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br
Total Standard Deviation in ln(k): 2.412467267528119
""",
)

entry(
    index = 12,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O",
    kinetics = ArrheniusBM(A=(1.81659e+07,'m^3/(mol*s)'), n=1.77075e-07, w0=(436000,'J/mol'), E0=(43600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.249383619443048e-16, var=23.27322198051156, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O
    Total Standard Deviation in ln(k): 9.671308689062275"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O
Total Standard Deviation in ln(k): 9.671308689062275""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O
Total Standard Deviation in ln(k): 9.671308689062275
""",
)

entry(
    index = 13,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O",
    kinetics = ArrheniusBM(A=(3.23956e+06,'m^3/(mol*s)'), n=0.428563, w0=(451333,'J/mol'), E0=(45133.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.058962865712696697, var=2.2227634590816754, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O
    Total Standard Deviation in ln(k): 3.1369944205765936"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O
Total Standard Deviation in ln(k): 3.1369944205765936""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O
Total Standard Deviation in ln(k): 3.1369944205765936
""",
)

entry(
    index = 14,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_4CClHNO->Cl",
    kinetics = ArrheniusBM(A=(1.7e+08,'m^3/(mol*s)'), n=0, w0=(556000,'J/mol'), E0=(55600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_4CClHNO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_4CClHNO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_4CClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_4CClHNO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 15,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl",
    kinetics = ArrheniusBM(A=(2.18878e+08,'m^3/(mol*s)'), n=-0.300755, w0=(557093,'J/mol'), E0=(51177.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0016406632814427692, var=1.4428754000005726, Tref=1000.0, N=43, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl',), comment="""BM rule fitted to 43 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl
    Total Standard Deviation in ln(k): 2.4122050043026655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 43 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl
Total Standard Deviation in ln(k): 2.4122050043026655""",
    longDesc = 
"""
BM rule fitted to 43 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl
Total Standard Deviation in ln(k): 2.4122050043026655
""",
)

entry(
    index = 16,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_4O-u1",
    kinetics = ArrheniusBM(A=(3.3e+06,'m^3/(mol*s)'), n=0, w0=(436000,'J/mol'), E0=(43600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(436000,'J/mol'), E0=(43600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_4BrClHNO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 18,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_4ClH->H",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(514000,'J/mol'), E0=(51400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_4ClH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_4ClH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_4ClH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_4ClH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 19,
    label = "Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_N-4ClH->H",
    kinetics = ArrheniusBM(A=(168431,'m^3/(mol*s)'), n=0.798014, w0=(420000,'J/mol'), E0=(42000,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9676196688144243, var=7.626664266065631, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_N-4ClH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_N-4ClH->H
    Total Standard Deviation in ln(k): 10.48012777674486"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_N-4ClH->H
Total Standard Deviation in ln(k): 10.48012777674486""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->C_N-4BrClHNO->O_N-4ClH->H
Total Standard Deviation in ln(k): 10.48012777674486
""",
)

entry(
    index = 20,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_4CHNO->N",
    kinetics = ArrheniusBM(A=(7.1e+06,'m^3/(mol*s)'), n=0, w0=(535000,'J/mol'), E0=(32601,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_4CHNO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_4CHNO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_4CHNO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_4CHNO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 21,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N",
    kinetics = ArrheniusBM(A=(8.13658e+07,'m^3/(mol*s)'), n=-0.15581, w0=(557619,'J/mol'), E0=(44394.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16414264367473183, var=1.6020531202212942, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N',), comment="""BM rule fitted to 42 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N
    Total Standard Deviation in ln(k): 2.9498567379054927"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N
Total Standard Deviation in ln(k): 2.9498567379054927""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N
Total Standard Deviation in ln(k): 2.9498567379054927
""",
)

entry(
    index = 22,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O",
    kinetics = ArrheniusBM(A=(2.28254e+08,'m^3/(mol*s)'), n=-0.339427, w0=(571500,'J/mol'), E0=(40223.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2639728192470128, var=6.966391627268641, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O
    Total Standard Deviation in ln(k): 5.9545305837073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O
Total Standard Deviation in ln(k): 5.9545305837073""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O
Total Standard Deviation in ln(k): 5.9545305837073
""",
)

entry(
    index = 23,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O",
    kinetics = ArrheniusBM(A=(3.04515e+07,'m^3/(mol*s)'), n=0.00139433, w0=(553833,'J/mol'), E0=(55383.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0009176664181460165, var=1.1337675629896968, Tref=1000.0, N=33, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O',), comment="""BM rule fitted to 33 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O
    Total Standard Deviation in ln(k): 2.1369179733040764"""),
    rank = 11,
    shortDesc = """BM rule fitted to 33 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O
Total Standard Deviation in ln(k): 2.1369179733040764""",
    longDesc = 
"""
BM rule fitted to 33 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O
Total Standard Deviation in ln(k): 2.1369179733040764
""",
)

entry(
    index = 24,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R",
    kinetics = ArrheniusBM(A=(2.28665e+08,'m^3/(mol*s)'), n=-0.339838, w0=(571500,'J/mol'), E0=(40201,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2630632208118352, var=7.0232219623544925, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R
    Total Standard Deviation in ln(k): 5.973783898070804"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R
Total Standard Deviation in ln(k): 5.973783898070804""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R
Total Standard Deviation in ln(k): 5.973783898070804
""",
)

entry(
    index = 25,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_4O-u1",
    kinetics = ArrheniusBM(A=(3.88588e+07,'m^3/(mol*s)'), n=-4.06955e-07, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.5083971249720928, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_4O-u1',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_4O-u1
    Total Standard Deviation in ln(k): 1.4294156489886742"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_4O-u1
Total Standard Deviation in ln(k): 1.4294156489886742""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_4O-u1
Total Standard Deviation in ln(k): 1.4294156489886742
""",
)

entry(
    index = 26,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_N-4O-u1",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_N-4O-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_N-4O-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_N-4O-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 27,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s",
    kinetics = ArrheniusBM(A=(1.11452e+07,'m^3/(mol*s)'), n=0.0963258, w0=(641500,'J/mol'), E0=(64150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08001181554282692, var=0.07550572762546935, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s
    Total Standard Deviation in ln(k): 0.7519019425832452"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s
Total Standard Deviation in ln(k): 0.7519019425832452""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s
Total Standard Deviation in ln(k): 0.7519019425832452
""",
)

entry(
    index = 28,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s",
    kinetics = ArrheniusBM(A=(3.05293e+07,'m^3/(mol*s)'), n=0.00115336, w0=(548177,'J/mol'), E0=(54817.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.000692759889118956, var=1.1389991051393038, Tref=1000.0, N=31, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s',), comment="""BM rule fitted to 31 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s
    Total Standard Deviation in ln(k): 2.141272082679453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 31 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.141272082679453""",
    longDesc = 
"""
BM rule fitted to 31 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s
Total Standard Deviation in ln(k): 2.141272082679453
""",
)

entry(
    index = 29,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.03e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.7339e+08,'m^3/(mol*s)'), n=-0.411376, w0=(571500,'J/mol'), E0=(29071.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11563977351599453, var=6.207103267140937, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C
    Total Standard Deviation in ln(k): 5.285160957741956"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.285160957741956""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C
Total Standard Deviation in ln(k): 5.285160957741956
""",
)

entry(
    index = 31,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_4CH->C",
    kinetics = ArrheniusBM(A=(2.23e+07,'m^3/(mol*s)'), n=0, w0=(621500,'J/mol'), E0=(62150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_4CH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_4CH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_4CH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_4CH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_N-4CH->C",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(661500,'J/mol'), E0=(66150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_N-4CH->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_N-4CH->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_N-4CH->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_2F1sH->F1s_N-4CH->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 33,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C",
    kinetics = ArrheniusBM(A=(2.33445e+07,'m^3/(mol*s)'), n=0.00143838, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.00022787881388778054, var=0.8747955142146696, Tref=1000.0, N=29, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C',), comment="""BM rule fitted to 29 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C
    Total Standard Deviation in ln(k): 1.8756113776900658"""),
    rank = 11,
    shortDesc = """BM rule fitted to 29 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C
Total Standard Deviation in ln(k): 1.8756113776900658""",
    longDesc = 
"""
BM rule fitted to 29 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C
Total Standard Deviation in ln(k): 1.8756113776900658
""",
)

entry(
    index = 34,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_N-4CH->C",
    kinetics = ArrheniusBM(A=(9.0299e+07,'m^3/(mol*s)'), n=6.25553e-08, w0=(558000,'J/mol'), E0=(55800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04970053958702819, var=0.0049443218046344006, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_N-4CH->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_N-4CH->C
    Total Standard Deviation in ln(k): 0.2658404219818662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_N-4CH->C
Total Standard Deviation in ln(k): 0.2658404219818662""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_N-4CH->C
Total Standard Deviation in ln(k): 0.2658404219818662
""",
)

entry(
    index = 35,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(3.2e+07,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_5BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 36,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl",
    kinetics = ArrheniusBM(A=(1.79349e+08,'m^3/(mol*s)'), n=-0.419602, w0=(571500,'J/mol'), E0=(28331,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.28937402210254554, var=7.751828377951696, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl
    Total Standard Deviation in ln(k): 6.308674956567821"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 6.308674956567821""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl
Total Standard Deviation in ln(k): 6.308674956567821
""",
)

entry(
    index = 37,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.95585e+07,'m^3/(mol*s)'), n=0.00191077, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0008055447181538924, var=1.2177185256126948, Tref=1000.0, N=27, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R',), comment="""BM rule fitted to 27 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R
    Total Standard Deviation in ln(k): 2.214254840072623"""),
    rank = 11,
    shortDesc = """BM rule fitted to 27 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.214254840072623""",
    longDesc = 
"""
BM rule fitted to 27 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R
Total Standard Deviation in ln(k): 2.214254840072623
""",
)

entry(
    index = 38,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_5BrNO->O",
    kinetics = ArrheniusBM(A=(6.75927e+07,'m^3/(mol*s)'), n=-0.0404796, w0=(571500,'J/mol'), E0=(52782.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9295487538337235, var=6.106406137879262, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_5BrNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_5BrNO->O
    Total Standard Deviation in ln(k): 9.80204206739676"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_5BrNO->O
Total Standard Deviation in ln(k): 9.80204206739676""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_5BrNO->O
Total Standard Deviation in ln(k): 9.80204206739676
""",
)

entry(
    index = 39,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O",
    kinetics = ArrheniusBM(A=(1.83344e+12,'m^3/(mol*s)'), n=-1.86291, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022262966749359486, var=0.7565835597382505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O
    Total Standard Deviation in ln(k): 1.799691996033835"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O
Total Standard Deviation in ln(k): 1.799691996033835""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O
Total Standard Deviation in ln(k): 1.799691996033835
""",
)

entry(
    index = 40,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(158729,'m^3/(mol*s)'), n=0.454367, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3774142242586179, var=11.446363599543373, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 7.730791870289622"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 7.730791870289622""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl
Total Standard Deviation in ln(k): 7.730791870289622
""",
)

entry(
    index = 41,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(1.99604e+07,'m^3/(mol*s)'), n=-1.05219e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.004387609134351948, var=1.2032027682360833, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 2.210030074154272"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.210030074154272""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 2.210030074154272
""",
)

entry(
    index = 42,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_5BrN->N",
    kinetics = ArrheniusBM(A=(1.24e+17,'m^3/(mol*s)'), n=-3.29, w0=(571500,'J/mol'), E0=(57150,'J/mol'), Tmin=(1140,'K'), Tmax=(1650,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_5BrN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_5BrN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 43,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_N-5BrN->N",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(571500,'J/mol'), E0=(57150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_N-5BrN->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_N-5BrN->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_N-5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_4CHO->O_Ext-4O-R_N-5R!H->C_N-5BrClFINOPSSi->Cl_N-5BrNO->O_N-5BrN->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 44,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 45,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_5R!H->Cl_Ext-4C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 46,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(1.34165e+07,'m^3/(mol*s)'), n=-4.9914e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.5990137911088773e-17, var=0.6909863268735121, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 1.666447807467594"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.666447807467594""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.666447807467594
""",
)

entry(
    index = 47,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O",
    kinetics = ArrheniusBM(A=(4.31934e+07,'m^3/(mol*s)'), n=-1.41881e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.14857644973201087, var=0.525245970335724, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O',), comment="""BM rule fitted to 23 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O
    Total Standard Deviation in ln(k): 1.8262164619636572"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.8262164619636572""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O
Total Standard Deviation in ln(k): 1.8262164619636572
""",
)

entry(
    index = 48,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 49,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_N-Sp-5O-4C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_N-Sp-5O-4C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_N-Sp-5O-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_5BrCFINOPSSi->O_N-Sp-5O-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 50,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C",
    kinetics = ArrheniusBM(A=(7.43475e+07,'m^3/(mol*s)'), n=3.86277e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0485846305060802, var=4.3205696333489305, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C
    Total Standard Deviation in ln(k): 6.801673066506776"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C
Total Standard Deviation in ln(k): 6.801673066506776""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C
Total Standard Deviation in ln(k): 6.801673066506776
""",
)

entry(
    index = 51,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C",
    kinetics = ArrheniusBM(A=(4.30234e+07,'m^3/(mol*s)'), n=-1.43433e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023906337900478924, var=0.5219483824250142, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C
    Total Standard Deviation in ln(k): 1.508406983667591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C
Total Standard Deviation in ln(k): 1.508406983667591""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C
Total Standard Deviation in ln(k): 1.508406983667591
""",
)

entry(
    index = 52,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R",
    kinetics = ArrheniusBM(A=(2.24071e+07,'m^3/(mol*s)'), n=-3.57839e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.7121999401106333e-07, var=4.719499072844586, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R
    Total Standard Deviation in ln(k): 4.355168725520282"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R
Total Standard Deviation in ln(k): 4.355168725520282""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R
Total Standard Deviation in ln(k): 4.355168725520282
""",
)

entry(
    index = 53,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(2.12133e+07,'m^3/(mol*s)'), n=-9.23436e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=16.708497797687528, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R
    Total Standard Deviation in ln(k): 8.19456099691273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R
Total Standard Deviation in ln(k): 8.19456099691273""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R
Total Standard Deviation in ln(k): 8.19456099691273
""",
)

entry(
    index = 54,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(1.14221e+08,'m^3/(mol*s)'), n=1.55224e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21539103398601614, var=0.17547591392225978, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R
    Total Standard Deviation in ln(k): 1.3809639250642105"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3809639250642105""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R
Total Standard Deviation in ln(k): 1.3809639250642105
""",
)

entry(
    index = 55,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C",
    kinetics = ArrheniusBM(A=(4.30915e+07,'m^3/(mol*s)'), n=-1.45507e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2828778235639967, var=0.18670786469732784, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C
    Total Standard Deviation in ln(k): 1.5769884228470683"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C
Total Standard Deviation in ln(k): 1.5769884228470683""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C
Total Standard Deviation in ln(k): 1.5769884228470683
""",
)

entry(
    index = 56,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_N-5CF->C",
    kinetics = ArrheniusBM(A=(1.1408e+07,'m^3/(mol*s)'), n=6.17885e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9378391372904964, var=9.21263144661322, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_N-5CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_N-5CF->C
    Total Standard Deviation in ln(k): 10.953778004404885"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_N-5CF->C
Total Standard Deviation in ln(k): 10.953778004404885""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_N-5CF->C
Total Standard Deviation in ln(k): 10.953778004404885
""",
)

entry(
    index = 57,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 58,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Sp-6R!H-5CF",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Sp-6R!H-5CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Sp-6R!H-5CF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Sp-6R!H-5CF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_Sp-6R!H-5CF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_N-Sp-6R!H-5CF",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_N-Sp-6R!H-5CF',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_N-Sp-6R!H-5CF
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_N-Sp-6R!H-5CF
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-5CF-R_N-Sp-6R!H-5CF
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 60,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_Sp-5CCFF=4C_Ext-4C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 61,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C",
    kinetics = ArrheniusBM(A=(1.17532e+08,'m^3/(mol*s)'), n=2.63538e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.30566038092716397, var=0.29603682536802245, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C
    Total Standard Deviation in ln(k): 1.8587525526849447"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C
Total Standard Deviation in ln(k): 1.8587525526849447""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C
Total Standard Deviation in ln(k): 1.8587525526849447
""",
)

entry(
    index = 62,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=-5.25094e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.2077456298229982e-09, var=0.0, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C
    Total Standard Deviation in ln(k): 8.059662386489944e-09"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C
Total Standard Deviation in ln(k): 8.059662386489944e-09""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C
Total Standard Deviation in ln(k): 8.059662386489944e-09
""",
)

entry(
    index = 63,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(5.73008e+07,'m^3/(mol*s)'), n=-1.21935e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.24792546422855172, var=0.3157005991179311, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R
    Total Standard Deviation in ln(k): 1.7493336207226258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.7493336207226258""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 1.7493336207226258
""",
)

entry(
    index = 64,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-4C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-4C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-4C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 65,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.2e+08,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_5CF->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 66,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(9.00001e+07,'m^3/(mol*s)'), n=-1.0785e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C_Ext-4C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C_Ext-4C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_Ext-4C-R_N-5CF->C_Ext-4C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 67,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(5.98168e+07,'m^3/(mol*s)'), n=-1.21968e-06, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02917145391161383, var=0.0814072959081807, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 0.6452853971787856"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.6452853971787856""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.6452853971787856
""",
)

entry(
    index = 68,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(2.7386e+07,'m^3/(mol*s)'), n=4.35355e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.06648230014354244, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 0.5169041366802003"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.5169041366802003""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 0.5169041366802003
""",
)

entry(
    index = 69,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(3.6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 70,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(7.34848e+07,'m^3/(mol*s)'), n=-2.28001e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.32880390778633084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
    Total Standard Deviation in ln(k): 1.1495436707873932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1495436707873932""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R
Total Standard Deviation in ln(k): 1.1495436707873932
""",
)

entry(
    index = 71,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 72,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2.5e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_N-Sp-6R!H-5C_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(9e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 74,
    label = "Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->F_N-2Br1sCl1sF1sHI1s->Cl1s_N-4BrCClHINOPSSi->Br_N-4CClHNO->Cl_N-4CHNO->N_N-4CHO->O_N-2F1sH->F1s_4CH->C_Ext-4C-R_N-5R!H->Cl_N-5BrCFINOPSSi->O_N-Sp-5CCFF=4C_5CF->C_Ext-5C-R_Sp-6R!H-5C_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

