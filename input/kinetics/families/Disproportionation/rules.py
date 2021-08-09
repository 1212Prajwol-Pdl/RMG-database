#!/usr/bin/env python
# encoding: utf-8

name = "Disproportionation/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(376.004,'m^3/(mol*s)'), n=1.32463, w0=(569887,'J/mol'), E0=(21450.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.019566362811271082, var=2.4889726407938015, Tref=1000.0, N=342, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 342 training reactions at node Root
    Total Standard Deviation in ln(k): 3.211927638128808"""),
    rank = 11,
    shortDesc = """BM rule fitted to 342 training reactions at node Root
Total Standard Deviation in ln(k): 3.211927638128808""",
    longDesc = 
"""
BM rule fitted to 342 training reactions at node Root
Total Standard Deviation in ln(k): 3.211927638128808
""",
)

entry(
    index = 2,
    label = "Root_Ext-4R-R",
    kinetics = ArrheniusBM(A=(96.6769,'m^3/(mol*s)'), n=1.4784, w0=(571344,'J/mol'), E0=(18246.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.023806133575254174, var=4.354768259798452, Tref=1000.0, N=135, data_mean=0.0, correlation='Root_Ext-4R-R',), comment="""BM rule fitted to 135 training reactions at node Root_Ext-4R-R
    Total Standard Deviation in ln(k): 4.243311906414749"""),
    rank = 11,
    shortDesc = """BM rule fitted to 135 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.243311906414749""",
    longDesc = 
"""
BM rule fitted to 135 training reactions at node Root_Ext-4R-R
Total Standard Deviation in ln(k): 4.243311906414749
""",
)

entry(
    index = 3,
    label = "Root_4R->C",
    kinetics = ArrheniusBM(A=(35.5152,'m^3/(mol*s)'), n=1.44517, w0=(546415,'J/mol'), E0=(73312.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12522187230111068, var=1.1734510493376187, Tref=1000.0, N=47, data_mean=0.0, correlation='Root_4R->C',), comment="""BM rule fitted to 47 training reactions at node Root_4R->C
    Total Standard Deviation in ln(k): 2.4862760495141174"""),
    rank = 11,
    shortDesc = """BM rule fitted to 47 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4862760495141174""",
    longDesc = 
"""
BM rule fitted to 47 training reactions at node Root_4R->C
Total Standard Deviation in ln(k): 2.4862760495141174
""",
)

entry(
    index = 4,
    label = "Root_N-4R->C",
    kinetics = ArrheniusBM(A=(3387.41,'m^3/(mol*s)'), n=1.08971, w0=(575553,'J/mol'), E0=(54089.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03515102778772548, var=1.211059357699349, Tref=1000.0, N=160, data_mean=0.0, correlation='Root_N-4R->C',), comment="""BM rule fitted to 160 training reactions at node Root_N-4R->C
    Total Standard Deviation in ln(k): 2.2944928717519932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 160 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2944928717519932""",
    longDesc = 
"""
BM rule fitted to 160 training reactions at node Root_N-4R->C
Total Standard Deviation in ln(k): 2.2944928717519932
""",
)

entry(
    index = 5,
    label = "Root_Ext-4R-R_5R!H-u0",
    kinetics = ArrheniusBM(A=(68.6702,'m^3/(mol*s)'), n=1.59823, w0=(568744,'J/mol'), E0=(18547.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.012794612197295947, var=2.4615989411265002, Tref=1000.0, N=82, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0',), comment="""BM rule fitted to 82 training reactions at node Root_Ext-4R-R_5R!H-u0
    Total Standard Deviation in ln(k): 3.1774730690155226"""),
    rank = 11,
    shortDesc = """BM rule fitted to 82 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1774730690155226""",
    longDesc = 
"""
BM rule fitted to 82 training reactions at node Root_Ext-4R-R_5R!H-u0
Total Standard Deviation in ln(k): 3.1774730690155226
""",
)

entry(
    index = 6,
    label = "Root_Ext-4R-R_N-5R!H-u0",
    kinetics = ArrheniusBM(A=(53726.2,'m^3/(mol*s)'), n=0.0998033, w0=(575368,'J/mol'), E0=(36433.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08419456077927288, var=0.7407726835973188, Tref=1000.0, N=53, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0',), comment="""BM rule fitted to 53 training reactions at node Root_Ext-4R-R_N-5R!H-u0
    Total Standard Deviation in ln(k): 1.9369825616759917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 53 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 1.9369825616759917""",
    longDesc = 
"""
BM rule fitted to 53 training reactions at node Root_Ext-4R-R_N-5R!H-u0
Total Standard Deviation in ln(k): 1.9369825616759917
""",
)

entry(
    index = 7,
    label = "Root_4R->C_1R!H->O",
    kinetics = ArrheniusBM(A=(1.62546e+09,'m^3/(mol*s)'), n=-0.811648, w0=(649667,'J/mol'), E0=(103005,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.08580691686234, var=50.11563954133438, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_1R!H->O',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
    Total Standard Deviation in ln(k): 26.970410167962328"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
Total Standard Deviation in ln(k): 26.970410167962328""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_1R!H->O
Total Standard Deviation in ln(k): 26.970410167962328
""",
)

entry(
    index = 8,
    label = "Root_4R->C_N-1R!H->O",
    kinetics = ArrheniusBM(A=(32.8727,'m^3/(mol*s)'), n=1.45284, w0=(539375,'J/mol'), E0=(71363.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.11560467303236154, var=1.3562699046663553, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O',), comment="""BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
    Total Standard Deviation in ln(k): 2.6251584578491243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
Total Standard Deviation in ln(k): 2.6251584578491243""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_4R->C_N-1R!H->O
Total Standard Deviation in ln(k): 2.6251584578491243
""",
)

entry(
    index = 9,
    label = "Root_N-4R->C_1R!H-inRing",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=1.1, w0=(494000,'J/mol'), E0=(151289,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_1R!H-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_1R!H-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 10,
    label = "Root_N-4R->C_N-1R!H-inRing",
    kinetics = ArrheniusBM(A=(3377.42,'m^3/(mol*s)'), n=1.09003, w0=(576066,'J/mol'), E0=(54089.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.037976312980583335, var=1.2147272357691645, Tref=1000.0, N=159, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing',), comment="""BM rule fitted to 159 training reactions at node Root_N-4R->C_N-1R!H-inRing
    Total Standard Deviation in ln(k): 2.304929919372466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 159 training reactions at node Root_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.304929919372466""",
    longDesc = 
"""
BM rule fitted to 159 training reactions at node Root_N-4R->C_N-1R!H-inRing
Total Standard Deviation in ln(k): 2.304929919372466
""",
)

entry(
    index = 11,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C",
    kinetics = ArrheniusBM(A=(2231.7,'m^3/(mol*s)'), n=0.974787, w0=(547115,'J/mol'), E0=(53916.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0848420165754884, var=8.745616214288694, Tref=1000.0, N=61, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C',), comment="""BM rule fitted to 61 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
    Total Standard Deviation in ln(k): 8.654334356075745"""),
    rank = 11,
    shortDesc = """BM rule fitted to 61 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 8.654334356075745""",
    longDesc = 
"""
BM rule fitted to 61 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C
Total Standard Deviation in ln(k): 8.654334356075745
""",
)

entry(
    index = 12,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C",
    kinetics = ArrheniusBM(A=(98.4903,'m^3/(mol*s)'), n=1.58193, w0=(631571,'J/mol'), E0=(21404.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023862179099613193, var=2.2730418105526637, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
    Total Standard Deviation in ln(k): 3.0824161949245337"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 3.0824161949245337""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C
Total Standard Deviation in ln(k): 3.0824161949245337
""",
)

entry(
    index = 13,
    label = "Root_Ext-4R-R_N-5R!H-u0_1R!H->O",
    kinetics = ArrheniusBM(A=(4.00926e+06,'m^3/(mol*s)'), n=0.0695165, w0=(679500,'J/mol'), E0=(25903.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5906659597197343e-15, var=8.110181091599317e-08, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
    Total Standard Deviation in ln(k): 0.0005709160669089575"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
Total Standard Deviation in ln(k): 0.0005709160669089575""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_1R!H->O
Total Standard Deviation in ln(k): 0.0005709160669089575
""",
)

entry(
    index = 14,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O",
    kinetics = ArrheniusBM(A=(55213.1,'m^3/(mol*s)'), n=0.0954458, w0=(571284,'J/mol'), E0=(36656.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0612476304543983, var=0.6317432420708076, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O',), comment="""BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
    Total Standard Deviation in ln(k): 1.7472976140813643"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
Total Standard Deviation in ln(k): 1.7472976140813643""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O
Total Standard Deviation in ln(k): 1.7472976140813643
""",
)

entry(
    index = 15,
    label = "Root_4R->C_1R!H->O_2R!H->C",
    kinetics = ArrheniusBM(A=(6.61174e+07,'m^3/(mol*s)'), n=-1.09962e-06, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.7507532944488107, var=36.13951493076956, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
    Total Standard Deviation in ln(k): 21.475698718431726"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 21.475698718431726""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_1R!H->O_2R!H->C
Total Standard Deviation in ln(k): 21.475698718431726
""",
)

entry(
    index = 16,
    label = "Root_4R->C_1R!H->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(638000,'J/mol'), E0=(77506.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 17,
    label = "Root_4R->C_N-1R!H->O_4C-u1",
    kinetics = ArrheniusBM(A=(32.6054,'m^3/(mol*s)'), n=1.45385, w0=(539393,'J/mol'), E0=(71344.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.115378840738277, var=1.354328609269, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1',), comment="""BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
    Total Standard Deviation in ln(k): 2.622919560556252"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
Total Standard Deviation in ln(k): 2.622919560556252""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_4R->C_N-1R!H->O_4C-u1
Total Standard Deviation in ln(k): 2.622919560556252
""",
)

entry(
    index = 18,
    label = "Root_4R->C_N-1R!H->O_N-4C-u1",
    kinetics = ArrheniusBM(A=(7.38116e+06,'m^3/(mol*s)'), n=-7.68901e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=15.80567206157525, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_N-4C-u1',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
    Total Standard Deviation in ln(k): 7.970094538116895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
Total Standard Deviation in ln(k): 7.970094538116895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1
Total Standard Deviation in ln(k): 7.970094538116895
""",
)

entry(
    index = 19,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(357.109,'m^3/(mol*s)'), n=1.20693, w0=(569125,'J/mol'), E0=(45095.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06985474913508474, var=0.3429093852723291, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.349456538762701"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.349456538762701
""",
)

entry(
    index = 20,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N",
    kinetics = ArrheniusBM(A=(2884.45,'m^3/(mol*s)'), n=1.16, w0=(576434,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.030308384546994627, var=0.728796800114764, Tref=1000.0, N=151, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N',), comment="""BM rule fitted to 151 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N
    Total Standard Deviation in ln(k): 1.787585965795661"""),
    rank = 11,
    shortDesc = """BM rule fitted to 151 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.787585965795661""",
    longDesc = 
"""
BM rule fitted to 151 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N
Total Standard Deviation in ln(k): 1.787585965795661
""",
)

entry(
    index = 21,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S",
    kinetics = ArrheniusBM(A=(1.27667e-13,'m^3/(mol*s)'), n=4.8323, w0=(527000,'J/mol'), E0=(-25280,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=10.214760863631724, var=288.9982061655396, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
    Total Standard Deviation in ln(k): 59.74561884662232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
Total Standard Deviation in ln(k): 59.74561884662232""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S
Total Standard Deviation in ln(k): 59.74561884662232
""",
)

entry(
    index = 22,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S",
    kinetics = ArrheniusBM(A=(5064.11,'m^3/(mol*s)'), n=0.882266, w0=(547797,'J/mol'), E0=(56818.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.9901957820215684, var=5.123459107250625, Tref=1000.0, N=59, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S',), comment="""BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
    Total Standard Deviation in ln(k): 7.025658841678099"""),
    rank = 11,
    shortDesc = """BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
Total Standard Deviation in ln(k): 7.025658841678099""",
    longDesc = 
"""
BM rule fitted to 59 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S
Total Standard Deviation in ln(k): 7.025658841678099
""",
)

entry(
    index = 23,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O",
    kinetics = ArrheniusBM(A=(49.4192,'m^3/(mol*s)'), n=1.71995, w0=(632750,'J/mol'), E0=(4933.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.27168087925620377, var=0.8748541283484499, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
    Total Standard Deviation in ln(k): 2.557716908155005"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.557716908155005""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O
Total Standard Deviation in ln(k): 2.557716908155005
""",
)

entry(
    index = 24,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O",
    kinetics = ArrheniusBM(A=(196.581,'m^3/(mol*s)'), n=1.41443, w0=(630846,'J/mol'), E0=(25712.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6465178771302686, var=5.903507461689984, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O',), comment="""BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
    Total Standard Deviation in ln(k): 6.495348563129981"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 6.495348563129981""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O
Total Standard Deviation in ln(k): 6.495348563129981
""",
)

entry(
    index = 25,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(666.949,'m^3/(mol*s)'), n=0.732044, w0=(571409,'J/mol'), E0=(35647,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07175587484815095, var=4.185130263823438, Tref=1000.0, N=44, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS',), comment="""BM rule fitted to 44 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 4.2814961551130475"""),
    rank = 11,
    shortDesc = """BM rule fitted to 44 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 4.2814961551130475""",
    longDesc = 
"""
BM rule fitted to 44 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 4.2814961551130475
""",
)

entry(
    index = 26,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS",
    kinetics = ArrheniusBM(A=(529272,'m^3/(mol*s)'), n=-0.232924, w0=(570500,'J/mol'), E0=(54575.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.510450627765164, var=8.919115069446692, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
    Total Standard Deviation in ln(k): 12.294783654476149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 12.294783654476149""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS
Total Standard Deviation in ln(k): 12.294783654476149
""",
)

entry(
    index = 27,
    label = "Root_4R->C_1R!H->O_2R!H->C_4C-u1",
    kinetics = ArrheniusBM(A=(8.49e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(298,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C_4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 28,
    label = "Root_4R->C_1R!H->O_2R!H->C_N-4C-u1",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_1R!H->O_2R!H->C_N-4C-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_1R!H->O_2R!H->C_N-4C-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 29,
    label = "Root_4R->C_N-1R!H->O_4C-u1_2R!H->O",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(601500,'J/mol'), E0=(75469.3,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_2R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_2R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 30,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O",
    kinetics = ArrheniusBM(A=(11.22,'m^3/(mol*s)'), n=1.58905, w0=(537878,'J/mol'), E0=(25138,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02357625121623182, var=0.9615458001543306, Tref=1000.0, N=41, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O',), comment="""BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
    Total Standard Deviation in ln(k): 2.0250487905268435"""),
    rank = 11,
    shortDesc = """BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
Total Standard Deviation in ln(k): 2.0250487905268435""",
    longDesc = 
"""
BM rule fitted to 41 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O
Total Standard Deviation in ln(k): 2.0250487905268435
""",
)

entry(
    index = 31,
    label = "Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.81e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_N-4C-u1_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 32,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1",
    kinetics = ArrheniusBM(A=(324.71,'m^3/(mol*s)'), n=1.21139, w0=(577357,'J/mol'), E0=(43789,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.06587093377643148, var=0.37537174784171157, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1
    Total Standard Deviation in ln(k): 1.393757709198133"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1
Total Standard Deviation in ln(k): 1.393757709198133
""",
)

entry(
    index = 33,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_N-2R!H-u1",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_N-2R!H-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_N-2R!H-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_N-2R!H-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 34,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O",
    kinetics = ArrheniusBM(A=(613.064,'m^3/(mol*s)'), n=1.3975, w0=(675231,'J/mol'), E0=(45084.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.3998789493794574, var=2.6350817520182876, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O
    Total Standard Deviation in ln(k): 4.258994377007544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 4.258994377007544""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O
Total Standard Deviation in ln(k): 4.258994377007544
""",
)

entry(
    index = 35,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O",
    kinetics = ArrheniusBM(A=(4124.94,'m^3/(mol*s)'), n=1.10698, w0=(567127,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03190174638168377, var=0.7598692275108695, Tref=1000.0, N=138, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O',), comment="""BM rule fitted to 138 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O
    Total Standard Deviation in ln(k): 1.8276922959016524"""),
    rank = 11,
    shortDesc = """BM rule fitted to 138 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8276922959016524""",
    longDesc = 
"""
BM rule fitted to 138 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O
Total Standard Deviation in ln(k): 1.8276922959016524
""",
)

entry(
    index = 36,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(515000,'J/mol'), E0=(35435.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_5R!H->S_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 37,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(13575.8,'m^3/(mol*s)'), n=0.910694, w0=(559800,'J/mol'), E0=(79601.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.377705965622395, var=11.377932221615472, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O
    Total Standard Deviation in ln(k): 12.736345700347497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O
Total Standard Deviation in ln(k): 12.736345700347497""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O
Total Standard Deviation in ln(k): 12.736345700347497
""",
)

entry(
    index = 38,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O",
    kinetics = ArrheniusBM(A=(364335,'m^3/(mol*s)'), n=0.0730606, w0=(541641,'J/mol'), E0=(22347.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8316354847005705, var=9.880333151549518, Tref=1000.0, N=39, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O',), comment="""BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O
    Total Standard Deviation in ln(k): 8.391019608118176"""),
    rank = 11,
    shortDesc = """BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 8.391019608118176""",
    longDesc = 
"""
BM rule fitted to 39 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O
Total Standard Deviation in ln(k): 8.391019608118176
""",
)

entry(
    index = 39,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C",
    kinetics = ArrheniusBM(A=(2.41e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 40,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C",
    kinetics = ArrheniusBM(A=(49.2818,'m^3/(mol*s)'), n=1.72032, w0=(626071,'J/mol'), E0=(4884.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2680323142748556, var=0.8590264676555326, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
    Total Standard Deviation in ln(k): 2.531510284743583"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
Total Standard Deviation in ln(k): 2.531510284743583""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C
Total Standard Deviation in ln(k): 2.531510284743583
""",
)

entry(
    index = 41,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(24800.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_5R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 42,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N",
    kinetics = ArrheniusBM(A=(83.4523,'m^3/(mol*s)'), n=1.56579, w0=(633542,'J/mol'), E0=(4156.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.050073540842616185, var=0.8970933949991728, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
    Total Standard Deviation in ln(k): 2.0245980336293217"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0245980336293217""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N
Total Standard Deviation in ln(k): 2.0245980336293217
""",
)

entry(
    index = 43,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing",
    kinetics = ArrheniusBM(A=(1.53682e+09,'m^3/(mol*s)'), n=-1.42949, w0=(609250,'J/mol'), E0=(-35735.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.6012394520288673, var=7.28163223287886, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
    Total Standard Deviation in ln(k): 11.945454824247122"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
Total Standard Deviation in ln(k): 11.945454824247122""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing
Total Standard Deviation in ln(k): 11.945454824247122
""",
)

entry(
    index = 44,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing",
    kinetics = ArrheniusBM(A=(658.403,'m^3/(mol*s)'), n=0.734851, w0=(569607,'J/mol'), E0=(35871.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.138311198365524, var=3.503711777709149, Tref=1000.0, N=42, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing',), comment="""BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
    Total Standard Deviation in ln(k): 4.100019678130609"""),
    rank = 11,
    shortDesc = """BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
Total Standard Deviation in ln(k): 4.100019678130609""",
    longDesc = 
"""
BM rule fitted to 42 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing
Total Standard Deviation in ln(k): 4.100019678130609
""",
)

entry(
    index = 45,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.14598e+07,'m^3/(mol*s)'), n=-0.250704, w0=(551500,'J/mol'), E0=(87668.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0020271280872269535, var=11.703768372124149, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.863446506949544"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.863446506949544""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.863446506949544
""",
)

entry(
    index = 46,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C",
    kinetics = ArrheniusBM(A=(105812,'m^3/(mol*s)'), n=0.0187788, w0=(551500,'J/mol'), E0=(28711.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09646707572050597, var=2.8085567758521424, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
    Total Standard Deviation in ln(k): 3.602064841653377"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 3.602064841653377""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_1CNS->C
Total Standard Deviation in ln(k): 3.602064841653377
""",
)

entry(
    index = 47,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C",
    kinetics = ArrheniusBM(A=(1.2e+06,'m^3/(mol*s)'), n=-0.34, w0=(684500,'J/mol'), E0=(61113.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_N-1CNS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 48,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(238.765,'m^3/(mol*s)'), n=1.21316, w0=(539359,'J/mol'), E0=(86188.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2757097255835443, var=2.081818967207214, Tref=1000.0, N=32, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN',), comment="""BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 3.5852719866530367"""),
    rank = 11,
    shortDesc = """BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 3.5852719866530367""",
    longDesc = 
"""
BM rule fitted to 32 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 3.5852719866530367
""",
)

entry(
    index = 49,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(194.83,'m^3/(mol*s)'), n=1.19577, w0=(532611,'J/mol'), E0=(24515.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03635238884000083, var=0.3518434550884663, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN',), comment="""BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 1.2804742097448631"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.2804742097448631""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.2804742097448631
""",
)

entry(
    index = 50,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 51,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(246.827,'m^3/(mol*s)'), n=1.2433, w0=(581125,'J/mol'), E0=(29015.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.09502092991108324, var=0.9409657996420207, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 2.183407074220283"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 2.183407074220283
""",
)

entry(
    index = 52,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H",
    kinetics = ArrheniusBM(A=(209.849,'m^3/(mol*s)'), n=1.2433, w0=(591250,'J/mol'), E0=(59125,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5787018105298811, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
    Total Standard Deviation in ln(k): 1.4540246495725655"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H
Total Standard Deviation in ln(k): 1.4540246495725655
""",
)

entry(
    index = 53,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(4e+08,'m^3/(mol*s)'), n=0, w0=(664000,'J/mol'), E0=(66400,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 54,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(513.762,'m^3/(mol*s)'), n=1.41595, w0=(676167,'J/mol'), E0=(42049.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24125165006325738, var=1.681521152142946, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.2057696726226546"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.2057696726226546""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.2057696726226546
""",
)

entry(
    index = 55,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(1.58084e+07,'m^3/(mol*s)'), n=3.20208e-07, w0=(551367,'J/mol'), E0=(55136.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.011789206171092194, var=2.8781024455425017, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
    Total Standard Deviation in ln(k): 3.4306483869182207"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.4306483869182207""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl
Total Standard Deviation in ln(k): 3.4306483869182207
""",
)

entry(
    index = 56,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl",
    kinetics = ArrheniusBM(A=(2735.05,'m^3/(mol*s)'), n=1.16251, w0=(569049,'J/mol'), E0=(50332,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.035865360436771535, var=0.691318013833344, Tref=1000.0, N=123, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl',), comment="""BM rule fitted to 123 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
    Total Standard Deviation in ln(k): 1.7569616942085442"""),
    rank = 11,
    shortDesc = """BM rule fitted to 123 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7569616942085442""",
    longDesc = 
"""
BM rule fitted to 123 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl
Total Standard Deviation in ln(k): 1.7569616942085442
""",
)

entry(
    index = 57,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(6.59305e+06,'m^3/(mol*s)'), n=-0.444118, w0=(559211,'J/mol'), E0=(63662.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.009769853108535528, var=0.7831560796192673, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C
    Total Standard Deviation in ln(k): 1.7986598508847353"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C
Total Standard Deviation in ln(k): 1.7986598508847353""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C
Total Standard Deviation in ln(k): 1.7986598508847353
""",
)

entry(
    index = 58,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 59,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R",
    kinetics = ArrheniusBM(A=(305492,'m^3/(mol*s)'), n=0.10765, w0=(533150,'J/mol'), E0=(-9548.19,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.9137888076093055, var=24.31972011819098, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R',), comment="""BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R
    Total Standard Deviation in ln(k): 17.207434104657864"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R
Total Standard Deviation in ln(k): 17.207434104657864""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R
Total Standard Deviation in ln(k): 17.207434104657864
""",
)

entry(
    index = 60,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C",
    kinetics = ArrheniusBM(A=(279957,'m^3/(mol*s)'), n=0.0420024, w0=(537391,'J/mol'), E0=(27952.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.981371878981554, var=3.415352740901857, Tref=1000.0, N=23, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C',), comment="""BM rule fitted to 23 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C
    Total Standard Deviation in ln(k): 6.170643829197089"""),
    rank = 11,
    shortDesc = """BM rule fitted to 23 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C
Total Standard Deviation in ln(k): 6.170643829197089""",
    longDesc = 
"""
BM rule fitted to 23 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C
Total Standard Deviation in ln(k): 6.170643829197089
""",
)

entry(
    index = 61,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C",
    kinetics = ArrheniusBM(A=(1.73886e+08,'m^3/(mol*s)'), n=-0.404463, w0=(572083,'J/mol'), E0=(82336.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09683884537484436, var=0.5518766835273604, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C
    Total Standard Deviation in ln(k): 1.7325993572449294"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C
Total Standard Deviation in ln(k): 1.7325993572449294""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C
Total Standard Deviation in ln(k): 1.7325993572449294
""",
)

entry(
    index = 62,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS",
    kinetics = ArrheniusBM(A=(55.6945,'m^3/(mol*s)'), n=1.72025, w0=(616333,'J/mol'), E0=(3477.11,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.500126634572629, var=0.7252921215150004, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
    Total Standard Deviation in ln(k): 2.9639138510069802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 2.9639138510069802""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 2.9639138510069802
""",
)

entry(
    index = 63,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_N-Sp-2R!H-1NOS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 64,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS",
    kinetics = ArrheniusBM(A=(59.8209,'m^3/(mol*s)'), n=1.70856, w0=(627071,'J/mol'), E0=(3874.96,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.670548251915558, var=10.579644690906186, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
    Total Standard Deviation in ln(k): 15.743157681510466"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 15.743157681510466""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 15.743157681510466
""",
)

entry(
    index = 65,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS",
    kinetics = ArrheniusBM(A=(98.661,'m^3/(mol*s)'), n=1.49399, w0=(642600,'J/mol'), E0=(9688.41,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6696723449848017, var=10.141110319932299, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
    Total Standard Deviation in ln(k): 10.579257555140929"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 10.579257555140929""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS
Total Standard Deviation in ln(k): 10.579257555140929
""",
)

entry(
    index = 66,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(25000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(-3048.12,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 67,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(36930.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 68,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(369.528,'m^3/(mol*s)'), n=0.78611, w0=(563000,'J/mol'), E0=(33786.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7867370154131448, var=7.365610222510332, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.417508555389395"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.417508555389395""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.417508555389395
""",
)

entry(
    index = 69,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C",
    kinetics = ArrheniusBM(A=(15130,'m^3/(mol*s)'), n=0.089261, w0=(563000,'J/mol'), E0=(26998.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.012478487768258238, var=6.0294641330369885, Tref=1000.0, N=21, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C',), comment="""BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
    Total Standard Deviation in ln(k): 4.953973387722041"""),
    rank = 11,
    shortDesc = """BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 4.953973387722041""",
    longDesc = 
"""
BM rule fitted to 21 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C
Total Standard Deviation in ln(k): 4.953973387722041
""",
)

entry(
    index = 70,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C",
    kinetics = ArrheniusBM(A=(251642,'m^3/(mol*s)'), n=0.0103012, w0=(655500,'J/mol'), E0=(56562.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.2985004027350566, var=3.9379753946346447, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
    Total Standard Deviation in ln(k): 7.240826806817084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 7.240826806817084""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C
Total Standard Deviation in ln(k): 7.240826806817084
""",
)

entry(
    index = 71,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C",
    kinetics = ArrheniusBM(A=(139119,'m^3/(mol*s)'), n=0.393409, w0=(551500,'J/mol'), E0=(94763.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.03855023334194839, var=13.933814951879814, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
    Total Standard Deviation in ln(k): 7.580140111770488"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.580140111770488""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C
Total Standard Deviation in ln(k): 7.580140111770488
""",
)

entry(
    index = 72,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(51372.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 73,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(7.12697e+07,'m^3/(mol*s)'), n=-0.748184, w0=(539000,'J/mol'), E0=(72567.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02125563531416367, var=0.2985131025077501, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 1.1487202443958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 1.1487202443958""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 1.1487202443958
""",
)

entry(
    index = 74,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(392.124,'m^3/(mol*s)'), n=1.21675, w0=(540929,'J/mol'), E0=(76129.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4447562759433383, var=1.1889408313494727, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 3.3034124091003325"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.3034124091003325""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.3034124091003325
""",
)

entry(
    index = 75,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(0.160367,'m^3/(mol*s)'), n=2.13656, w0=(533833,'J/mol'), E0=(53383.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014718234167879004, var=2.338943902760151, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 3.102943366630338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 3.102943366630338""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 3.102943366630338
""",
)

entry(
    index = 76,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(306.327,'m^3/(mol*s)'), n=1.1953, w0=(531400,'J/mol'), E0=(29200.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2742028208888681, var=2.015285812352148, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 3.534889015648708"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 3.534889015648708""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 3.534889015648708
""",
)

entry(
    index = 77,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 78,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(154.363,'m^3/(mol*s)'), n=1.19601, w0=(537250,'J/mol'), E0=(53725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0774457332350715, var=1.2806334483339823, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 4.975810062508253"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 4.975810062508253""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 4.975810062508253
""",
)

entry(
    index = 79,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 80,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O",
    kinetics = ArrheniusBM(A=(4147.31,'m^3/(mol*s)'), n=0.9029, w0=(612000,'J/mol'), E0=(51367.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8754987103028704, var=0.28030785144339526, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
    Total Standard Deviation in ln(k): 3.2611345968802175"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
Total Standard Deviation in ln(k): 3.2611345968802175""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O
Total Standard Deviation in ln(k): 3.2611345968802175
""",
)

entry(
    index = 81,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O",
    kinetics = ArrheniusBM(A=(207.556,'m^3/(mol*s)'), n=1.2433, w0=(550250,'J/mol'), E0=(17424.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.6172896801193773, var=3.9362754729278144, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
    Total Standard Deviation in ln(k): 5.528383327536255"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 5.528383327536255""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O
Total Standard Deviation in ln(k): 5.528383327536255
""",
)

entry(
    index = 82,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 83,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(648000,'J/mol'), E0=(64800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_N-Sp-2R!H-1R!H_N-1R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 84,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1",
    kinetics = ArrheniusBM(A=(239.565,'m^3/(mol*s)'), n=1.49891, w0=(676688,'J/mol'), E0=(41452.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.01523784344134606, var=3.0299958991895446, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1',), comment="""BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
    Total Standard Deviation in ln(k): 3.527905014060273"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 3.527905014060273""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1
Total Standard Deviation in ln(k): 3.527905014060273
""",
)

entry(
    index = 85,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1",
    kinetics = ArrheniusBM(A=(1.72553e+08,'m^3/(mol*s)'), n=-0.207634, w0=(675125,'J/mol'), E0=(74900.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.1433111407657404, var=4.597661629890631, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
    Total Standard Deviation in ln(k): 7.171225793847845"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 7.171225793847845""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1
Total Standard Deviation in ln(k): 7.171225793847845
""",
)

entry(
    index = 86,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(9.06644e+06,'m^3/(mol*s)'), n=1.22618e-07, w0=(545200,'J/mol'), E0=(54520,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004724030202329742, var=3.265960879878607, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.634820575424553"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.634820575424553""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.634820575424553
""",
)

entry(
    index = 87,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=9.94521e-08, w0=(543667,'J/mol'), E0=(54366.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.6982780719772782e-09, var=3.9764236524905177, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
    Total Standard Deviation in ln(k): 3.9976366135869816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976366135869816""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R
Total Standard Deviation in ln(k): 3.9976366135869816
""",
)

entry(
    index = 88,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C",
    kinetics = ArrheniusBM(A=(6e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 89,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.33333e+08,'m^3/(mol*s)'), n=0, w0=(640000,'J/mol'), E0=(64000,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 90,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H",
    kinetics = ArrheniusBM(A=(10625.6,'m^3/(mol*s)'), n=1.05901, w0=(556138,'J/mol'), E0=(56909.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.011574927054009095, var=0.540873409494222, Tref=1000.0, N=40, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H',), comment="""BM rule fitted to 40 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H
    Total Standard Deviation in ln(k): 1.5034470264012012"""),
    rank = 11,
    shortDesc = """BM rule fitted to 40 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H
Total Standard Deviation in ln(k): 1.5034470264012012""",
    longDesc = 
"""
BM rule fitted to 40 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H
Total Standard Deviation in ln(k): 1.5034470264012012
""",
)

entry(
    index = 91,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H",
    kinetics = ArrheniusBM(A=(2277.63,'m^3/(mol*s)'), n=1.14344, w0=(575271,'J/mol'), E0=(40836.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.016101693429247926, var=0.6272827465175661, Tref=1000.0, N=83, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H',), comment="""BM rule fitted to 83 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H
    Total Standard Deviation in ln(k): 1.6282304231574636"""),
    rank = 11,
    shortDesc = """BM rule fitted to 83 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H
Total Standard Deviation in ln(k): 1.6282304231574636""",
    longDesc = 
"""
BM rule fitted to 83 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H
Total Standard Deviation in ln(k): 1.6282304231574636
""",
)

entry(
    index = 92,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C",
    kinetics = ArrheniusBM(A=(695006,'m^3/(mol*s)'), n=-5.08253e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.6643208264050226e-08, var=3.6973873113656555, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C
    Total Standard Deviation in ln(k): 3.854823279288445"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C
Total Standard Deviation in ln(k): 3.854823279288445""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C
Total Standard Deviation in ln(k): 3.854823279288445
""",
)

entry(
    index = 93,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C",
    kinetics = ArrheniusBM(A=(170642,'m^3/(mol*s)'), n=-0.0229586, w0=(563000,'J/mol'), E0=(44342.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017421915734380358, var=0.2897958796752784, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C
    Total Standard Deviation in ln(k): 1.122976530061591"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 1.122976530061591""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C
Total Standard Deviation in ln(k): 1.122976530061591
""",
)

entry(
    index = 94,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C",
    kinetics = ArrheniusBM(A=(300404,'m^3/(mol*s)'), n=0.109166, w0=(526062,'J/mol'), E0=(-10751,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-3.666598232892827, var=32.12897226433206, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C
    Total Standard Deviation in ln(k): 20.575882804071394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C
Total Standard Deviation in ln(k): 20.575882804071394""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C
Total Standard Deviation in ln(k): 20.575882804071394
""",
)

entry(
    index = 95,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.9053e+06,'m^3/(mol*s)'), n=-0.0575532, w0=(561500,'J/mol'), E0=(17540.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1352806081598749, var=1.2535632058264505, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C
    Total Standard Deviation in ln(k): 2.5844552807383243"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.5844552807383243""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C
Total Standard Deviation in ln(k): 2.5844552807383243
""",
)

entry(
    index = 96,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R",
    kinetics = ArrheniusBM(A=(5.08213e+06,'m^3/(mol*s)'), n=6.07908e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8756592302892024e-09, var=0.1974069254280893, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R
    Total Standard Deviation in ln(k): 0.8907138061354173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R
Total Standard Deviation in ln(k): 0.8907138061354173""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R
Total Standard Deviation in ln(k): 0.8907138061354173
""",
)

entry(
    index = 97,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R",
    kinetics = ArrheniusBM(A=(268859,'m^3/(mol*s)'), n=0.0425885, w0=(537150,'J/mol'), E0=(23318.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8761845950983916, var=2.5646964026580705, Tref=1000.0, N=20, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R',), comment="""BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R
    Total Standard Deviation in ln(k): 5.411985808564966"""),
    rank = 11,
    shortDesc = """BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R
Total Standard Deviation in ln(k): 5.411985808564966""",
    longDesc = 
"""
BM rule fitted to 20 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R
Total Standard Deviation in ln(k): 5.411985808564966
""",
)

entry(
    index = 98,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.88128e+10,'m^3/(mol*s)'), n=-1.24306, w0=(527500,'J/mol'), E0=(82876.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.31841107973975963, var=1.8828679713191403, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.5508779259239467"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.5508779259239467""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.5508779259239467
""",
)

entry(
    index = 99,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_5BrClF->Br",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_5BrClF->Br',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_5BrClF->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_5BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_5BrClF->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 100,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br",
    kinetics = ArrheniusBM(A=(8.31038e+06,'m^3/(mol*s)'), n=5.87668e-08, w0=(574000,'J/mol'), E0=(57400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.49879411919521677, var=0.6771973937398439, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br
    Total Standard Deviation in ln(k): 2.902988227680156"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br
Total Standard Deviation in ln(k): 2.902988227680156""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br
Total Standard Deviation in ln(k): 2.902988227680156
""",
)

entry(
    index = 101,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C",
    kinetics = ArrheniusBM(A=(1.21e+07,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(56131,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 102,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(55.5201,'m^3/(mol*s)'), n=1.72068, w0=(603700,'J/mol'), E0=(5726.82,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4974265036478005, var=0.715585916381764, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
    Total Standard Deviation in ln(k): 2.945667077087709"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
Total Standard Deviation in ln(k): 2.945667077087709""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C
Total Standard Deviation in ln(k): 2.945667077087709
""",
)

entry(
    index = 103,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R",
    kinetics = ArrheniusBM(A=(1.81e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57475.1,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_Ext-5COS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 104,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O",
    kinetics = ArrheniusBM(A=(56.1763,'m^3/(mol*s)'), n=1.71849, w0=(627000,'J/mol'), E0=(-1662.01,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.406650984474472, var=12.833305395099408, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
    Total Standard Deviation in ln(k): 20.766233586810195"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
Total Standard Deviation in ln(k): 20.766233586810195""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O
Total Standard Deviation in ln(k): 20.766233586810195
""",
)

entry(
    index = 105,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O",
    kinetics = ArrheniusBM(A=(1.07806e+06,'m^3/(mol*s)'), n=0.108494, w0=(620000,'J/mol'), E0=(40682.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4665362756364059, var=1.0112505540522367, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
    Total Standard Deviation in ln(k): 3.1881824236693816"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
Total Standard Deviation in ln(k): 3.1881824236693816""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O
Total Standard Deviation in ln(k): 3.1881824236693816
""",
)

entry(
    index = 106,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C",
    kinetics = ArrheniusBM(A=(4.03222e+07,'m^3/(mol*s)'), n=-1.06537e-07, w0=(655500,'J/mol'), E0=(-8267.17,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04053193339062449, var=4.55660944302888, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
    Total Standard Deviation in ln(k): 4.381189858959989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
Total Standard Deviation in ln(k): 4.381189858959989""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C
Total Standard Deviation in ln(k): 4.381189858959989
""",
)

entry(
    index = 107,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C",
    kinetics = ArrheniusBM(A=(96.2519,'m^3/(mol*s)'), n=1.49685, w0=(623250,'J/mol'), E0=(11940.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.1881264617506124, var=7.255212047919393, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
    Total Standard Deviation in ln(k): 10.89765951374958"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
Total Standard Deviation in ln(k): 10.89765951374958""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C
Total Standard Deviation in ln(k): 10.89765951374958
""",
)

entry(
    index = 108,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(1.95674e+14,'m^3/(mol*s)'), n=-2.62051, w0=(563000,'J/mol'), E0=(78808.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6866916065168047, var=12.384246969584773, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 8.780270891603362"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 8.780270891603362""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 8.780270891603362
""",
)

entry(
    index = 109,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F",
    kinetics = ArrheniusBM(A=(4.00219,'m^3/(mol*s)'), n=0.935699, w0=(563000,'J/mol'), E0=(-13795.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.5126089217500143, var=5.218490701299982, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F
    Total Standard Deviation in ln(k): 10.892707775163595"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F
Total Standard Deviation in ln(k): 10.892707775163595""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F
Total Standard Deviation in ln(k): 10.892707775163595
""",
)

entry(
    index = 110,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F",
    kinetics = ArrheniusBM(A=(381823,'m^3/(mol*s)'), n=-0.0814186, w0=(563000,'J/mol'), E0=(43158.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.24139628340299113, var=0.13915146575739962, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F
    Total Standard Deviation in ln(k): 1.3543498790734485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 1.3543498790734485""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F
Total Standard Deviation in ln(k): 1.3543498790734485
""",
)

entry(
    index = 111,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(9051.47,'m^3/(mol*s)'), n=0.136253, w0=(563000,'J/mol'), E0=(20782.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.018387893583959775, var=6.296144302882482, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 5.076505827734783"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 5.076505827734783""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 5.076505827734783
""",
)

entry(
    index = 112,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(1.66755e+06,'m^3/(mol*s)'), n=-0.23625, w0=(655500,'J/mol'), E0=(59158.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7188074371175652, var=14.293900834944544, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 14.410531609996482"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 14.410531609996482""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 14.410531609996482
""",
)

entry(
    index = 113,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(54738.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_N-Sp-2R!H-1CNS_Ext-2R!H-R_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 114,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(9.60603e+07,'m^3/(mol*s)'), n=-0.76, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.240168944759434e-11, var=0.22100123677280187, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
    Total Standard Deviation in ln(k): 0.9424413690506191"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 0.9424413690506191""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 0.9424413690506191
""",
)

entry(
    index = 115,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1.18657e+07,'m^3/(mol*s)'), n=-0.535705, w0=(539000,'J/mol'), E0=(62675.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02943015260025164, var=0.2695439251071153, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C',), comment="""BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 1.114755843552044"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.114755843552044""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 1.114755843552044
""",
)

entry(
    index = 116,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.06797e+08,'m^3/(mol*s)'), n=-0.78492, w0=(539000,'J/mol'), E0=(84630,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03522779878346413, var=2.05397231782131, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R',), comment="""BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.961635478692932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.961635478692932""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.961635478692932
""",
)

entry(
    index = 117,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(2.19e+08,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 118,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=1.87, w0=(566000,'J/mol'), E0=(56600,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 119,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(553500,'J/mol'), E0=(55350,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 120,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(0.0114734,'m^3/(mol*s)'), n=2.46068, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4906384915362034, var=2.392248234980461, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 4.33346261042941"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 4.33346261042941""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 4.33346261042941
""",
)

entry(
    index = 121,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(4.94404e+12,'m^3/(mol*s)'), n=-1.73557, w0=(527500,'J/mol'), E0=(93449.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.37764528928363966, var=3.164125845297428, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 4.514878240788361"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.514878240788361""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 4.514878240788361
""",
)

entry(
    index = 122,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 123,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(300.243,'m^3/(mol*s)'), n=1.19833, w0=(537250,'J/mol'), E0=(29683.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2165437484371654, var=0.019967687252929005, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.8273630043291497"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8273630043291497""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.8273630043291497
""",
)

entry(
    index = 124,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(196000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 125,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(0.81,'m^3/(mol*s)'), n=1.87, w0=(547000,'J/mol'), E0=(54700,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 126,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(625500,'J/mol'), E0=(52086.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 127,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->N",
    kinetics = ArrheniusBM(A=(0.92,'m^3/(mol*s)'), n=1.94, w0=(598500,'J/mol'), E0=(35577.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_1R!H->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 128,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_2R!H->N",
    kinetics = ArrheniusBM(A=(0.46,'m^3/(mol*s)'), n=1.94, w0=(511500,'J/mol'), E0=(51150,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 129,
    label = "Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-2R!H->N",
    kinetics = ArrheniusBM(A=(1.8,'m^3/(mol*s)'), n=1.94, w0=(589000,'J/mol'), E0=(45647.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-2R!H->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-2R!H->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_4BrClFHNOS->N_2R!H-u1_Sp-2R!H-1R!H_N-1R!H->O_N-2R!H->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 130,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O",
    kinetics = ArrheniusBM(A=(685.497,'m^3/(mol*s)'), n=1.2742, w0=(675125,'J/mol'), E0=(67512.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6545272470348775, var=1.0910977558270665, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O
    Total Standard Deviation in ln(k): 3.7385993729398286"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O
Total Standard Deviation in ln(k): 3.7385993729398286""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O
Total Standard Deviation in ln(k): 3.7385993729398286
""",
)

entry(
    index = 131,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O",
    kinetics = ArrheniusBM(A=(2993.6,'m^3/(mol*s)'), n=1.25306, w0=(678250,'J/mol'), E0=(62415.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.013924778778159438, var=0.0697178358083764, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O
    Total Standard Deviation in ln(k): 0.5643198425092989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O
Total Standard Deviation in ln(k): 0.5643198425092989""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O
Total Standard Deviation in ln(k): 0.5643198425092989
""",
)

entry(
    index = 132,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 133,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_2R!H->C",
    kinetics = ArrheniusBM(A=(7.94176e+07,'m^3/(mol*s)'), n=2.19788e-06, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9426404480036046, var=9.694606240475355, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_2R!H->C
    Total Standard Deviation in ln(k): 11.1229818930801"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_2R!H->C
Total Standard Deviation in ln(k): 11.1229818930801""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_2R!H->C
Total Standard Deviation in ln(k): 11.1229818930801
""",
)

entry(
    index = 134,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-2R!H->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(662000,'J/mol'), E0=(48035.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_N-4BrFHO-u1_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 135,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O",
    kinetics = ArrheniusBM(A=(3.66667e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 136,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(4.91226e+06,'m^3/(mol*s)'), n=-4.48064e-08, w0=(544944,'J/mol'), E0=(54494.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.23044180294496538, var=1.6164595104630008, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
    Total Standard Deviation in ln(k): 3.127820904665338"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.127820904665338""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O
Total Standard Deviation in ln(k): 3.127820904665338
""",
)

entry(
    index = 137,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(9.99999e+06,'m^3/(mol*s)'), n=1.28714e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 138,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1e+08,'m^3/(mol*s)'), n=0, w0=(536000,'J/mol'), E0=(53600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 139,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(224906,'m^3/(mol*s)'), n=0.68216, w0=(559860,'J/mol'), E0=(75168.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.2561543583988001, var=0.4129158804865062, Tref=1000.0, N=25, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN',), comment="""BM rule fitted to 25 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.9318172265296603"""),
    rank = 11,
    shortDesc = """BM rule fitted to 25 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9318172265296603""",
    longDesc = 
"""
BM rule fitted to 25 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9318172265296603
""",
)

entry(
    index = 140,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(19350.4,'m^3/(mol*s)'), n=0.958615, w0=(549933,'J/mol'), E0=(31810.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.11399513282765794, var=0.5635742527421312, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.791406283047767"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.791406283047767""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.791406283047767
""",
)

entry(
    index = 141,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1",
    kinetics = ArrheniusBM(A=(755.644,'m^3/(mol*s)'), n=1.22505, w0=(574364,'J/mol'), E0=(48181.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03983770151325215, var=0.2423625443324332, Tref=1000.0, N=66, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1',), comment="""BM rule fitted to 66 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1
    Total Standard Deviation in ln(k): 1.087032432115698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 66 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1
Total Standard Deviation in ln(k): 1.087032432115698""",
    longDesc = 
"""
BM rule fitted to 66 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1
Total Standard Deviation in ln(k): 1.087032432115698
""",
)

entry(
    index = 142,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1",
    kinetics = ArrheniusBM(A=(13393.7,'m^3/(mol*s)'), n=0.983523, w0=(578794,'J/mol'), E0=(55095.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.009119479355011118, var=0.24707455522313157, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1
    Total Standard Deviation in ln(k): 1.0193988035450119"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1
Total Standard Deviation in ln(k): 1.0193988035450119""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1
Total Standard Deviation in ln(k): 1.0193988035450119
""",
)

entry(
    index = 143,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(340825,'m^3/(mol*s)'), n=2.54075e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 144,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(439643,'m^3/(mol*s)'), n=-0.127198, w0=(563000,'J/mol'), E0=(51412.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.02881366541377465, var=0.36799765200146745, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R',), comment="""BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R
    Total Standard Deviation in ln(k): 1.288524775740925"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.288524775740925""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R
Total Standard Deviation in ln(k): 1.288524775740925
""",
)

entry(
    index = 145,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(453885,'m^3/(mol*s)'), n=-0.170943, w0=(563000,'J/mol'), E0=(60013.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0019763864790805982, var=0.28553446389121523, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 1.0762045027742295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.0762045027742295""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 1.0762045027742295
""",
)

entry(
    index = 146,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_1C-inRing",
    kinetics = ArrheniusBM(A=(0.000675,'m^3/(mol*s)'), n=2.7, w0=(483500,'J/mol'), E0=(33691.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_1C-inRing',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_1C-inRing
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_1C-inRing
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 147,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing",
    kinetics = ArrheniusBM(A=(2.76566e+11,'m^3/(mol*s)'), n=-1.97465, w0=(532143,'J/mol'), E0=(85301,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.973277909816123, var=17.711488651991015, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing',), comment="""BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing
    Total Standard Deviation in ln(k): 13.394916177818356"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 13.394916177818356""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing
Total Standard Deviation in ln(k): 13.394916177818356
""",
)

entry(
    index = 148,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(1.94e+06,'m^3/(mol*s)'), n=0, w0=(561500,'J/mol'), E0=(38387.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_N-2R!H->C_Ext-4R-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 149,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=1.90562e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 150,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C",
    kinetics = ArrheniusBM(A=(282342,'m^3/(mol*s)'), n=0.0353791, w0=(538361,'J/mol'), E0=(56808,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.7776793605580838, var=2.506891214621528, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C',), comment="""BM rule fitted to 18 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C
    Total Standard Deviation in ln(k): 5.128098416540662"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C
Total Standard Deviation in ln(k): 5.128098416540662""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C
Total Standard Deviation in ln(k): 5.128098416540662
""",
)

entry(
    index = 151,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C",
    kinetics = ArrheniusBM(A=(4.41543e+06,'m^3/(mol*s)'), n=-0.210085, w0=(526250,'J/mol'), E0=(40381.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.41287904047369567, var=0.2970389119041833, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C
    Total Standard Deviation in ln(k): 2.1299907275479635"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C
Total Standard Deviation in ln(k): 2.1299907275479635""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C
Total Standard Deviation in ln(k): 2.1299907275479635
""",
)

entry(
    index = 152,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_6R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(70216.9,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 153,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_Ext-1C-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 154,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(8.08788e+06,'m^3/(mol*s)'), n=3.53638e-08, w0=(597250,'J/mol'), E0=(59725,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20545120611205125, var=0.09590933447913423, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 1.137060122257262"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.137060122257262""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.137060122257262
""",
)

entry(
    index = 155,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 156,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(573833,'J/mol'), E0=(26375.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.16479020172419373, var=0.14297914762848185, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
    Total Standard Deviation in ln(k): 1.1720878594844713"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 1.1720878594844713""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 1.1720878594844713
""",
)

entry(
    index = 157,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N",
    kinetics = ArrheniusBM(A=(6.23614e-40,'m^3/(mol*s)'), n=13.8207, w0=(648500,'J/mol'), E0=(-47906.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.127611593067805, var=3.4257180582824334, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
    Total Standard Deviation in ln(k): 9.056260864310659"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 9.056260864310659""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 9.056260864310659
""",
)

entry(
    index = 158,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C",
    kinetics = ArrheniusBM(A=(4.82e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 159,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(13428.6,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_5COS->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 160,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O",
    kinetics = ArrheniusBM(A=(1.25258e+07,'m^3/(mol*s)'), n=-0.25, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-5.6129510735315866e-09, var=0.029913004620106633, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
    Total Standard Deviation in ln(k): 0.34672649236279346"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
Total Standard Deviation in ln(k): 0.34672649236279346""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O
Total Standard Deviation in ln(k): 0.34672649236279346
""",
)

entry(
    index = 161,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O",
    kinetics = ArrheniusBM(A=(644,'m^3/(mol*s)'), n=1.19, w0=(513500,'J/mol'), E0=(39978.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_N-1NOS->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 162,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C",
    kinetics = ArrheniusBM(A=(1.90317e+07,'m^3/(mol*s)'), n=-4.02332e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=1.6812080230698707, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
    Total Standard Deviation in ln(k): 2.599367689841769"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
Total Standard Deviation in ln(k): 2.599367689841769""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C
Total Standard Deviation in ln(k): 2.599367689841769
""",
)

entry(
    index = 163,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C",
    kinetics = ArrheniusBM(A=(1.81e+08,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(56990.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_N-5COS->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 164,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(648000,'J/mol'), E0=(54170.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 165,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N",
    kinetics = ArrheniusBM(A=(0.014,'m^3/(mol*s)'), n=2.69, w0=(598500,'J/mol'), E0=(17401.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_N-2R!H->C_N-1NOS->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 166,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(8500,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(13198.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 167,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H",
    kinetics = ArrheniusBM(A=(7.23e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(95940.9,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_Ext-6R!H-R_N-Sp-7R!H-6R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 168,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(289.202,'m^3/(mol*s)'), n=0.356422, w0=(563000,'J/mol'), E0=(-16850.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.2701926044037593, var=2.3235668362315063, Tref=1000.0, N=8, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R',), comment="""BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R
    Total Standard Deviation in ln(k): 8.759869401335612"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R
Total Standard Deviation in ln(k): 8.759869401335612""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R
Total Standard Deviation in ln(k): 8.759869401335612
""",
)

entry(
    index = 169,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(4.48112e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(-2237.01,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.962553966144821, var=30.525942939233207, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 16.007259100198073"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198073""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 16.007259100198073
""",
)

entry(
    index = 170,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(30000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(16338,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-1CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-1CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-1CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 171,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(26666.7,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(12108.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 172,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_6CCl->C",
    kinetics = ArrheniusBM(A=(10833.3,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(13433.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_6CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_6CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_6CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_6CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 173,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_N-6CCl->C",
    kinetics = ArrheniusBM(A=(250000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(44398.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_N-6CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_N-6CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_N-6CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_N-6R!H->F_N-6CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 174,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(119000,'m^3/(mol*s)'), n=-0.224934, w0=(563000,'J/mol'), E0=(-21.5028,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.038121700752081863, var=4.702777027231642, Tref=1000.0, N=16, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS',), comment="""BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 4.443229038854819"""),
    rank = 11,
    shortDesc = """BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.443229038854819""",
    longDesc = 
"""
BM rule fitted to 16 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 4.443229038854819
""",
)

entry(
    index = 175,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS",
    kinetics = ArrheniusBM(A=(1.68714e+16,'m^3/(mol*s)'), n=-3.31041, w0=(563000,'J/mol'), E0=(66353.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.1093955463446234, var=24.094403248658786, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
    Total Standard Deviation in ln(k): 10.115315847721718"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 10.115315847721718""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS
Total Standard Deviation in ln(k): 10.115315847721718
""",
)

entry(
    index = 176,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_6R!H->C",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(47009.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 177,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_N-6R!H->C",
    kinetics = ArrheniusBM(A=(300000,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(57975.7,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_N-2R!H->C_Ext-1CNS-R_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 178,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(7.5e+07,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 179,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(7.33333e+07,'m^3/(mol*s)'), n=-0.68, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 180,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(4.22222e+08,'m^3/(mol*s)'), n=-1, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 181,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.05153e+07,'m^3/(mol*s)'), n=-0.536672, w0=(539000,'J/mol'), E0=(59819.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.023769647185996015, var=0.16901129801950632, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 0.8838890423757649"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.8838890423757649""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 0.8838890423757649
""",
)

entry(
    index = 182,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(1.12583e+07,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-2CN-R
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 183,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=-4.60922e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 184,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(3.89177e+08,'m^3/(mol*s)'), n=-0.776484, w0=(539000,'J/mol'), E0=(85460.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0366763005874044, var=1.4524396831142532, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 2.5082022027668103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 2.5082022027668103""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 2.5082022027668103
""",
)

entry(
    index = 185,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(7.72985e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.8988603214016866e-11, var=0.21353467287039427, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 0.9263843112218227"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9263843112218227""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 0.9263843112218227
""",
)

entry(
    index = 186,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1",
    kinetics = ArrheniusBM(A=(0.82,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 187,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1",
    kinetics = ArrheniusBM(A=(1.6,'m^3/(mol*s)'), n=1.87, w0=(524000,'J/mol'), E0=(52400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 188,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(72883.1,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_Ext-5R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 189,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3e+06,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(75719.2,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 190,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(8.44601e+06,'m^3/(mol*s)'), n=2.93231e-07, w0=(679500,'J/mol'), E0=(67950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.0843154882448665e-08, var=1.8552134513562086, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C
    Total Standard Deviation in ln(k): 2.7305739833623313"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C
Total Standard Deviation in ln(k): 2.7305739833623313""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C
Total Standard Deviation in ln(k): 2.7305739833623313
""",
)

entry(
    index = 191,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(662000,'J/mol'), E0=(66200,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 192,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C",
    kinetics = ArrheniusBM(A=(2.28942e+07,'m^3/(mol*s)'), n=4.50201e-07, w0=(688167,'J/mol'), E0=(68816.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.7976940806867016e-08, var=0.12330149351029779, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C
    Total Standard Deviation in ln(k): 0.7039490583503162"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C
Total Standard Deviation in ln(k): 0.7039490583503162""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C
Total Standard Deviation in ln(k): 0.7039490583503162
""",
)

entry(
    index = 193,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(648500,'J/mol'), E0=(59320.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 194,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.10064e+07,'m^3/(mol*s)'), n=1.3093e-08, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.5586460192786372e-08, var=0.6944264527262918, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.6705909874654379"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909874654379""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.6705909874654379
""",
)

entry(
    index = 195,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(3.85891e+06,'m^3/(mol*s)'), n=-1.48775e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6669698280313657, var=3.368805659110193, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 5.355355787726706"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.355355787726706""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 5.355355787726706
""",
)

entry(
    index = 196,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(4.47213e+06,'m^3/(mol*s)'), n=7.10656e-08, w0=(536000,'J/mol'), E0=(53600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=5.180580787960471, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 4.5629553043324895"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.5629553043324895""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 4.5629553043324895
""",
)

entry(
    index = 197,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-1CN-R_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 198,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C",
    kinetics = ArrheniusBM(A=(90288.4,'m^3/(mol*s)'), n=0.757979, w0=(550263,'J/mol'), E0=(46903.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.48409313623384026, var=1.4796734705312395, Tref=1000.0, N=19, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C',), comment="""BM rule fitted to 19 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C
    Total Standard Deviation in ln(k): 3.6549108391656917"""),
    rank = 11,
    shortDesc = """BM rule fitted to 19 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C
Total Standard Deviation in ln(k): 3.6549108391656917""",
    longDesc = 
"""
BM rule fitted to 19 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C
Total Standard Deviation in ln(k): 3.6549108391656917
""",
)

entry(
    index = 199,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C",
    kinetics = ArrheniusBM(A=(143229,'m^3/(mol*s)'), n=0.755305, w0=(590250,'J/mol'), E0=(75463.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.25369337052123964, var=0.41472444603439707, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C
    Total Standard Deviation in ln(k): 1.9284519352481626"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C
Total Standard Deviation in ln(k): 1.9284519352481626""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C
Total Standard Deviation in ln(k): 1.9284519352481626
""",
)

entry(
    index = 200,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C",
    kinetics = ArrheniusBM(A=(23314.3,'m^3/(mol*s)'), n=0.956427, w0=(541000,'J/mol'), E0=(29930.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.2585319778373009, var=1.8847114188678595, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C
    Total Standard Deviation in ln(k): 3.4017742203309167"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 3.4017742203309167""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C
Total Standard Deviation in ln(k): 3.4017742203309167
""",
)

entry(
    index = 201,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C",
    kinetics = ArrheniusBM(A=(16039.5,'m^3/(mol*s)'), n=0.960818, w0=(608000,'J/mol'), E0=(60800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 202,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F",
    kinetics = ArrheniusBM(A=(5.27632e+06,'m^3/(mol*s)'), n=0.134627, w0=(619889,'J/mol'), E0=(61988.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.007433453574601324, var=0.5933475869225935, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F
    Total Standard Deviation in ln(k): 1.5629055766274802"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F
Total Standard Deviation in ln(k): 1.5629055766274802""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F
Total Standard Deviation in ln(k): 1.5629055766274802
""",
)

entry(
    index = 203,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F",
    kinetics = ArrheniusBM(A=(747.542,'m^3/(mol*s)'), n=1.22638, w0=(567175,'J/mol'), E0=(48496.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03971782905404656, var=0.23968336745483407, Tref=1000.0, N=57, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F',), comment="""BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F
    Total Standard Deviation in ln(k): 1.0812610746597526"""),
    rank = 11,
    shortDesc = """BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F
Total Standard Deviation in ln(k): 1.0812610746597526""",
    longDesc = 
"""
BM rule fitted to 57 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F
Total Standard Deviation in ln(k): 1.0812610746597526
""",
)

entry(
    index = 204,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O",
    kinetics = ArrheniusBM(A=(165.835,'m^3/(mol*s)'), n=1.5823, w0=(640500,'J/mol'), E0=(49223.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.888347326583373, var=4.6009210074755265, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O
    Total Standard Deviation in ln(k): 9.044699417413472"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O
Total Standard Deviation in ln(k): 9.044699417413472""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O
Total Standard Deviation in ln(k): 9.044699417413472
""",
)

entry(
    index = 205,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O",
    kinetics = ArrheniusBM(A=(17135.7,'m^3/(mol*s)'), n=0.94751, w0=(570567,'J/mol'), E0=(57056.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02681123750681873, var=0.2830122458351904, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O
    Total Standard Deviation in ln(k): 1.1338618326987222"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O
Total Standard Deviation in ln(k): 1.1338618326987222""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O
Total Standard Deviation in ln(k): 1.1338618326987222
""",
)

entry(
    index = 206,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(241000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 207,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(243381,'m^3/(mol*s)'), n=-0.0657956, w0=(563000,'J/mol'), E0=(45053.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.07902957589859533, var=0.4289792140924304, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 1.5115981797931959"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.5115981797931959""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.5115981797931959
""",
)

entry(
    index = 208,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(7.63851e+10,'m^3/(mol*s)'), n=-1.66846, w0=(563000,'J/mol'), E0=(76043.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08182587765052184, var=0.42867703851117955, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.5181615284492185"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.5181615284492185""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.5181615284492185
""",
)

entry(
    index = 209,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=1.21757e-08, w0=(563000,'J/mol'), E0=(49391.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 210,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-2C-R",
    kinetics = ArrheniusBM(A=(50000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(27880,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 211,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.15904e+14,'m^3/(mol*s)'), n=-2.7703, w0=(529400,'J/mol'), E0=(94774.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.11292509904717, var=15.268989674889728, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R
    Total Standard Deviation in ln(k): 13.142470530797763"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 13.142470530797763""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R
Total Standard Deviation in ln(k): 13.142470530797763
""",
)

entry(
    index = 212,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.03e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_Sp-5C#4R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 213,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R",
    kinetics = ArrheniusBM(A=(313620,'m^3/(mol*s)'), n=0.0160288, w0=(539000,'J/mol'), E0=(21446.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.3998776626917502, var=4.805516167249488, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R',), comment="""BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R
    Total Standard Deviation in ln(k): 7.911958065005258"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.911958065005258""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R
Total Standard Deviation in ln(k): 7.911958065005258
""",
)

entry(
    index = 214,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.19177e+10,'m^3/(mol*s)'), n=-1.26703, w0=(539000,'J/mol'), E0=(103393,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.4786924374036347, var=1.3117887922780007, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R',), comment="""BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 3.4988350306544995"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.4988350306544995""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 3.4988350306544995
""",
)

entry(
    index = 215,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(5.9127e+07,'m^3/(mol*s)'), n=-0.525, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.560376353633591, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 1.5007103918898554"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.5007103918898554""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.5007103918898554
""",
)

entry(
    index = 216,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(480000,'m^3/(mol*s)'), n=0, w0=(527500,'J/mol'), E0=(52750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_N-Sp-2R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 217,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(51500,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_N-4R->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 218,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 219,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(8.03333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_N-5BrCClF->C_N-5BrClF->Br_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 220,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N",
    kinetics = ArrheniusBM(A=(55.3682,'m^3/(mol*s)'), n=1.72068, w0=(548000,'J/mol'), E0=(42013.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.0406619764046778, var=0.11093145697366305, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
    Total Standard Deviation in ln(k): 3.2824331527498067"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N
Total Standard Deviation in ln(k): 3.2824331527498067
""",
)

entry(
    index = 221,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(625500,'J/mol'), E0=(26769.7,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 222,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N",
    kinetics = ArrheniusBM(A=(0.0294,'m^3/(mol*s)'), n=2.69, w0=(662000,'J/mol'), E0=(33510,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 223,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(635000,'J/mol'), E0=(6334.04,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_N-1NOS->N_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 224,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(2.85561e+07,'m^3/(mol*s)'), n=-0.375, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.305460834090209e-17, var=0.06912283083491383, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
    Total Standard Deviation in ln(k): 0.5270693322083513"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R
Total Standard Deviation in ln(k): 0.5270693322083513
""",
)

entry(
    index = 225,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(3.01e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 226,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS",
    kinetics = ArrheniusBM(A=(1.20333e+07,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_N-Sp-5COS-4CCNOSS_2R!H->C_5COS->C_N-Sp-5C=4CNS
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 227,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(4.49801e+12,'m^3/(mol*s)'), n=-2.64586, w0=(563000,'J/mol'), E0=(-15430.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.42246606188086244, var=5.144396230674122, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R
    Total Standard Deviation in ln(k): 5.608464569423865"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 5.608464569423865""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R
Total Standard Deviation in ln(k): 5.608464569423865
""",
)

entry(
    index = 228,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(1.73553e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(2192.14,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448168, var=2.873931729472134, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 8.32960223996552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 8.32960223996552
""",
)

entry(
    index = 229,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C",
    kinetics = ArrheniusBM(A=(89.2545,'m^3/(mol*s)'), n=0.712772, w0=(563000,'J/mol'), E0=(20080.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.05866258300491033, var=0.8142501988139011, Tref=1000.0, N=12, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C',), comment="""BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
    Total Standard Deviation in ln(k): 1.9563824247024373"""),
    rank = 11,
    shortDesc = """BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 1.9563824247024373""",
    longDesc = 
"""
BM rule fitted to 12 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 1.9563824247024373
""",
)

entry(
    index = 230,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C",
    kinetics = ArrheniusBM(A=(2934.33,'m^3/(mol*s)'), n=0.199046, w0=(563000,'J/mol'), E0=(-13426.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.0184169204690345, var=44.604819545587816, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
    Total Standard Deviation in ln(k): 23.485516947456276"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 23.485516947456276""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 23.485516947456276
""",
)

entry(
    index = 231,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C",
    kinetics = ArrheniusBM(A=(1.47637e+08,'m^3/(mol*s)'), n=-0.906138, w0=(563000,'J/mol'), E0=(58234.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1366416601998153e-14, var=67.49420639145738, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
    Total Standard Deviation in ln(k): 16.469872495385907"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 16.469872495385907""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_6R!H->C
Total Standard Deviation in ln(k): 16.469872495385907
""",
)

entry(
    index = 232,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C",
    kinetics = ArrheniusBM(A=(70000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(14365.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_N-Sp-6R!H-1CNS_N-6R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 233,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(51295.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.5913196686293954e-15, var=9.002053350725235e-30, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.0013181888456245e-14"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.0013181888456245e-14""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.0013181888456245e-14
""",
)

entry(
    index = 234,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(9.19239e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 235,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 236,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H",
    kinetics = ArrheniusBM(A=(5.5e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H-5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 237,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C",
    kinetics = ArrheniusBM(A=(6.91356e+06,'m^3/(mol*s)'), n=-0.24, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.494092434445075e-11, var=1.7801088207517621, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C',), comment="""BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
    Total Standard Deviation in ln(k): 2.6747319505637615"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 2.6747319505637615""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C
Total Standard Deviation in ln(k): 2.6747319505637615
""",
)

entry(
    index = 238,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C",
    kinetics = ArrheniusBM(A=(1.23686e+06,'m^3/(mol*s)'), n=-0.0613002, w0=(539000,'J/mol'), E0=(76866.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.032960842251921633, var=1.4060476388514789, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
    Total Standard Deviation in ln(k): 2.459968486668792"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 2.459968486668792""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_N-Sp-5C-1C
Total Standard Deviation in ln(k): 2.459968486668792
""",
)

entry(
    index = 239,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_N-5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 240,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(679500,'J/mol'), E0=(67950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_4BrFHO->O_2R!H->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 241,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_4FH->H",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-8.33353e-08, w0=(666000,'J/mol'), E0=(66600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_4FH->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_4FH->H
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_4FH->H
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_4FH->H
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 242,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_N-4FH->H",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(732500,'J/mol'), E0=(73250,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_N-4FH->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_N-4FH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_N-4FH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_1R!H->O_N-4BrClFHO->Cl_4BrFHO-u1_N-4BrFHO->O_2R!H->C_N-4FH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 243,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=1.32246e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 244,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=1.32246e-07, w0=(547500,'J/mol'), E0=(54750,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 245,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(536000,'J/mol'), E0=(53600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_N-Sp-2R!H-1CN_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 246,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C",
    kinetics = ArrheniusBM(A=(7.96614e+06,'m^3/(mol*s)'), n=0.0113769, w0=(549500,'J/mol'), E0=(31319.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.57933824089956, var=6.631008439246482, Tref=1000.0, N=18, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C',), comment="""BM rule fitted to 18 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C
    Total Standard Deviation in ln(k): 9.13052861804733"""),
    rank = 11,
    shortDesc = """BM rule fitted to 18 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C
Total Standard Deviation in ln(k): 9.13052861804733""",
    longDesc = 
"""
BM rule fitted to 18 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C
Total Standard Deviation in ln(k): 9.13052861804733
""",
)

entry(
    index = 247,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_N-1CN->C",
    kinetics = ArrheniusBM(A=(400,'m^3/(mol*s)'), n=1.5, w0=(564000,'J/mol'), E0=(56400,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_N-1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_N-1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 248,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1",
    kinetics = ArrheniusBM(A=(389623,'m^3/(mol*s)'), n=0.622256, w0=(601400,'J/mol'), E0=(76722.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06444327232775564, var=1.6805779652774666, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1
    Total Standard Deviation in ln(k): 2.7607983379523846"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.7607983379523846""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1
Total Standard Deviation in ln(k): 2.7607983379523846
""",
)

entry(
    index = 249,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_N-2NO-u1",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_N-2NO-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_N-2NO-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_N-2NO-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 250,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(32402.1,'m^3/(mol*s)'), n=0.958122, w0=(540786,'J/mol'), E0=(33319.5,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.422899719753104, var=3.715959696668631, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 7.439617585281791"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.439617585281791""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R
Total Standard Deviation in ln(k): 7.439617585281791
""",
)

entry(
    index = 251,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.78009e+07,'m^3/(mol*s)'), n=-1.4487e-08, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.939681085063708e-09, var=1.5683487451695521, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 2.5106045647845394"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 2.5106045647845394""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C
Total Standard Deviation in ln(k): 2.5106045647845394
""",
)

entry(
    index = 252,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(55750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 253,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(545000,'J/mol'), E0=(54500,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 254,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(671000,'J/mol'), E0=(67100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_N-1CN->C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 255,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(541149,'m^3/(mol*s)'), n=0.403881, w0=(608333,'J/mol'), E0=(60833.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.022300353306577345, var=1.0935717572740768, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R
    Total Standard Deviation in ln(k): 2.152462324155837"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.152462324155837""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R
Total Standard Deviation in ln(k): 2.152462324155837
""",
)

entry(
    index = 256,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.15443e+07,'m^3/(mol*s)'), n=7.06236e-08, w0=(612167,'J/mol'), E0=(61216.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4502455195451049e-08, var=1.4663745010001799, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.4276129521491097"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129521491097""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.4276129521491097
""",
)

entry(
    index = 257,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_2R!H->C",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(604500,'J/mol'), E0=(60450,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_2R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_2R!H->C
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_2R!H->C
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 258,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(708500,'J/mol'), E0=(70850,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 259,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C",
    kinetics = ArrheniusBM(A=(1698.31,'m^3/(mol*s)'), n=1.13428, w0=(564451,'J/mol'), E0=(61347,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.08712027928361499, var=0.6477846645583142, Tref=1000.0, N=51, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C',), comment="""BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C
    Total Standard Deviation in ln(k): 1.8324076234493285"""),
    rank = 11,
    shortDesc = """BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C
Total Standard Deviation in ln(k): 1.8324076234493285""",
    longDesc = 
"""
BM rule fitted to 51 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C
Total Standard Deviation in ln(k): 1.8324076234493285
""",
)

entry(
    index = 260,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C",
    kinetics = ArrheniusBM(A=(467.561,'m^3/(mol*s)'), n=1.27907, w0=(590333,'J/mol'), E0=(59033.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613378453951, var=0.20755570191645634, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C
    Total Standard Deviation in ln(k): 1.0133382627124077"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C
Total Standard Deviation in ln(k): 1.0133382627124077""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C
Total Standard Deviation in ln(k): 1.0133382627124077
""",
)

entry(
    index = 261,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_1CN->C",
    kinetics = ArrheniusBM(A=(3.33333e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 262,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_N-1CN->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(625500,'J/mol'), E0=(52192.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_N-1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_N-1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_2R!H->O_N-1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 263,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(22942.7,'m^3/(mol*s)'), n=0.937831, w0=(564150,'J/mol'), E0=(56415,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02026081281131671, var=0.4060083698755218, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 1.328299420169498"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.328299420169498""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 1.328299420169498
""",
)

entry(
    index = 264,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN",
    kinetics = ArrheniusBM(A=(11330.1,'m^3/(mol*s)'), n=0.961232, w0=(583400,'J/mol'), E0=(58340,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.029729958794657493, var=0.00022219016772130848, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN
    Total Standard Deviation in ln(k): 0.10458105954761464"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 0.10458105954761464""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN
Total Standard Deviation in ln(k): 0.10458105954761464
""",
)

entry(
    index = 265,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(303175,'m^3/(mol*s)'), n=-0.111661, w0=(563000,'J/mol'), E0=(43789.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06280058472454314, var=0.4657321858695851, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 1.525913324082989"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.525913324082989""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R
Total Standard Deviation in ln(k): 1.525913324082989
""",
)

entry(
    index = 266,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=-2.36961e-08, w0=(563000,'J/mol'), E0=(46150.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 267,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.84881e+06,'m^3/(mol*s)'), n=-0.20598, w0=(527000,'J/mol'), E0=(41321.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21905329352532726, var=0.032645318643083954, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.9126010054174031"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.9126010054174031""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.9126010054174031
""",
)

entry(
    index = 268,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(5.32091e+09,'m^3/(mol*s)'), n=-1.53013, w0=(527000,'J/mol'), E0=(82940.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.017169179667466, var=65.76214778089908, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
    Total Standard Deviation in ln(k): 26.350561270439204"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 26.350561270439204""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 26.350561270439204
""",
)

entry(
    index = 269,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(84300,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(76679.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 270,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(333333,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 271,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R",
    kinetics = ArrheniusBM(A=(184833,'m^3/(mol*s)'), n=0.253796, w0=(539000,'J/mol'), E0=(41435,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.17104141259095512, var=0.5785482016943025, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R
    Total Standard Deviation in ln(k): 1.9546010265636136"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.9546010265636136""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R
Total Standard Deviation in ln(k): 1.9546010265636136
""",
)

entry(
    index = 272,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(3.64528e+12,'m^3/(mol*s)'), n=-1.79636, w0=(539000,'J/mol'), E0=(98649,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.8063818183571493, var=2.3587336488257837, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 5.10499104691853"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.10499104691853""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 5.10499104691853
""",
)

entry(
    index = 273,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(1.0567e+06,'m^3/(mol*s)'), n=-3.77148e-07, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.40783940538389e-07, var=0.13070575990533037, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C
    Total Standard Deviation in ln(k): 0.7247772695623997"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 0.7247772695623997""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C
Total Standard Deviation in ln(k): 0.7247772695623997
""",
)

entry(
    index = 274,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C",
    kinetics = ArrheniusBM(A=(52.6504,'m^3/(mol*s)'), n=1.30971, w0=(539000,'J/mol'), E0=(84482.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.9314258761508287, var=6.079801862706496, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C
    Total Standard Deviation in ln(k): 9.795955081698624"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 9.795955081698624""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C
Total Standard Deviation in ln(k): 9.795955081698624
""",
)

entry(
    index = 275,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(2.3e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 276,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.52e+08,'m^3/(mol*s)'), n=-0.7, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Sp-2R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 277,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(39690.4,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 278,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(0.029,'m^3/(mol*s)'), n=2.69, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_4R->O_N-5R!H->C_Sp-2R!H-1NOS_N-2R!H->C_1NOS->N_2NO->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 279,
    label = "Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R",
    kinetics = ArrheniusBM(A=(3.47e+08,'m^3/(mol*s)'), n=-0.75, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_N-1R!H->C_N-4R->O_N-5R!H->N_Sp-5COS-4CCNOSS_N-5COS->O_1NOS->O_Ext-4CNS-R_Ext-4CNS-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 280,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(7.54412e+23,'m^3/(mol*s)'), n=-5.95405, w0=(563000,'J/mol'), E0=(-21733.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.4651220185719553, var=0.00013304009117722307, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 3.70433431901914"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.70433431901914""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_Ext-2R!H-R_6R!H->F_Ext-1CNS-R_Ext-1CNS-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 3.70433431901914
""",
)

entry(
    index = 281,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(10764.4,'m^3/(mol*s)'), n=2.27217e-08, w0=(563000,'J/mol'), E0=(16874.4,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.771694150424663e-09, var=0.015898769668625846, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 0.25277770633652485"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.25277770633652485""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 0.25277770633652485
""",
)

entry(
    index = 282,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R",
    kinetics = ArrheniusBM(A=(20268,'m^3/(mol*s)'), n=-1.58689e-07, w0=(563000,'J/mol'), E0=(13257,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.017646221985221817, var=1.5520525800818628, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R',), comment="""BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
    Total Standard Deviation in ln(k): 2.5418643131300547"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 2.5418643131300547""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R
Total Standard Deviation in ln(k): 2.5418643131300547
""",
)

entry(
    index = 283,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R",
    kinetics = ArrheniusBM(A=(7.76152e+14,'m^3/(mol*s)'), n=-3.14885, w0=(563000,'J/mol'), E0=(6358.26,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.9625539661448175, var=15.77167145155166, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
    Total Standard Deviation in ln(k): 12.892557544298015"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 12.892557544298015""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_N-6R!H->C_Ext-1CNS-R
Total Standard Deviation in ln(k): 12.892557544298015
""",
)

entry(
    index = 284,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(6.5e+06,'m^3/(mol*s)'), n=-0.5, w0=(539000,'J/mol'), E0=(53900,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-2CN-R_N-5R!H->C_Ext-1CN-R_Ext-1CN-R_Ext-2CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 285,
    label = "Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6.00999e+06,'m^3/(mol*s)'), n=-0.32, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.7581858468390404e-17, var=2.2148373801805805e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.00943469601266542"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.00943469601266542""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_4R->C_N-1R!H->O_4C-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_Ext-1C-R_5R!H->C_Sp-5C-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.00943469601266542
""",
)

entry(
    index = 286,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Ext-2R!H-R_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 287,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(547500,'J/mol'), E0=(54750,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_4BrClFHO->Cl_Ext-2R!H-R_N-5R!H->O_Sp-2R!H-1CN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 288,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(9.42781e+06,'m^3/(mol*s)'), n=7.41307e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-2.251782926091247, var=10.999261591440549, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R
    Total Standard Deviation in ln(k): 12.306476931827527"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R
Total Standard Deviation in ln(k): 12.306476931827527""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R
Total Standard Deviation in ln(k): 12.306476931827527
""",
)

entry(
    index = 289,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(373885,'m^3/(mol*s)'), n=0.242329, w0=(549500,'J/mol'), E0=(-12231.2,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.029276721674584397, var=1.5973964986306355, Tref=1000.0, N=10, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R',), comment="""BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.6073072206241084"""),
    rank = 11,
    shortDesc = """BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6073072206241084""",
    longDesc = 
"""
BM rule fitted to 10 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.6073072206241084
""",
)

entry(
    index = 290,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C",
    kinetics = ArrheniusBM(A=(48788.1,'m^3/(mol*s)'), n=0.958373, w0=(620167,'J/mol'), E0=(62016.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.1706622755278215, var=2.959645032278743, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C
    Total Standard Deviation in ln(k): 6.390232327854832"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C
Total Standard Deviation in ln(k): 6.390232327854832""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C
Total Standard Deviation in ln(k): 6.390232327854832
""",
)

entry(
    index = 291,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C",
    kinetics = ArrheniusBM(A=(26.4912,'m^3/(mol*s)'), n=1.82399, w0=(573250,'J/mol'), E0=(52118.1,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.20148362850470902, var=0.27147237417689896, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C
    Total Standard Deviation in ln(k): 1.5507676079238173"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C
Total Standard Deviation in ln(k): 1.5507676079238173""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C
Total Standard Deviation in ln(k): 1.5507676079238173
""",
)

entry(
    index = 292,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(4352.07,'m^3/(mol*s)'), n=1.07411, w0=(538000,'J/mol'), E0=(61866.9,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.014637613800328297, var=0.22185089850149414, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.9810292110218426"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.9810292110218426""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.9810292110218426
""",
)

entry(
    index = 293,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.08008e+07,'m^3/(mol*s)'), n=2.89777e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=5.031374851813639e-08, var=0.27285596210542634, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.0471858513505898"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0471858513505898""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.0471858513505898
""",
)

entry(
    index = 294,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(1.67e+06,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 295,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(557500,'J/mol'), E0=(46201.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 296,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.4572e+07,'m^3/(mol*s)'), n=-6.53027e-08, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.508120210243694e-08, var=1.904472164786679, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 2.766586936706844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.766586936706844""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 2.766586936706844
""",
)

entry(
    index = 297,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 298,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 299,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-1CN-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 300,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(1.41421e+07,'m^3/(mol*s)'), n=7.62613e-07, w0=(616000,'J/mol'), E0=(61600,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 1.9651578851126479"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN
Total Standard Deviation in ln(k): 1.9651578851126479
""",
)

entry(
    index = 301,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_N-Sp-2R!H-1CN",
    kinetics = ArrheniusBM(A=(5e+07,'m^3/(mol*s)'), n=0, w0=(604500,'J/mol'), E0=(60450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_N-Sp-2R!H-1CN',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_N-Sp-2R!H-1CN
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 302,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(6174.17,'m^3/(mol*s)'), n=1.01405, w0=(568764,'J/mol'), E0=(81740,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.02845914146193634, var=0.06418696518627641, Tref=1000.0, N=36, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C',), comment="""BM rule fitted to 36 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C
    Total Standard Deviation in ln(k): 0.579407950810781"""),
    rank = 11,
    shortDesc = """BM rule fitted to 36 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 0.579407950810781""",
    longDesc = 
"""
BM rule fitted to 36 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C
Total Standard Deviation in ln(k): 0.579407950810781
""",
)

entry(
    index = 303,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C",
    kinetics = ArrheniusBM(A=(802.19,'m^3/(mol*s)'), n=1.20292, w0=(554100,'J/mol'), E0=(55410,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.04832358391751214, var=0.7431423470863505, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C
    Total Standard Deviation in ln(k): 1.8496120347877278"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.8496120347877278""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C
Total Standard Deviation in ln(k): 1.8496120347877278
""",
)

entry(
    index = 304,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(556.026,'m^3/(mol*s)'), n=1.27907, w0=(574750,'J/mol'), E0=(57475,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.03980613384668196, var=0.21353467318894948, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N
    Total Standard Deviation in ln(k): 1.0263997235150666"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.0263997235150666""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.0263997235150666
""",
)

entry(
    index = 305,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N",
    kinetics = ArrheniusBM(A=(330.615,'m^3/(mol*s)'), n=1.27907, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 306,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(1940.87,'m^3/(mol*s)'), n=1.21164, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0064379313563148, var=3.9869403856980674, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
    Total Standard Deviation in ln(k): 6.531658057906698"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 6.531658057906698""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R
Total Standard Deviation in ln(k): 6.531658057906698
""",
)

entry(
    index = 307,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(106197,'m^3/(mol*s)'), n=0.766309, w0=(568400,'J/mol'), E0=(56840,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5277744666923911, var=1.6533397896703033, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 3.903800192919043"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.903800192919043""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 3.903800192919043
""",
)

entry(
    index = 308,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(12117.9,'m^3/(mol*s)'), n=1.00928, w0=(557833,'J/mol'), E0=(55783.3,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0270949316202428, var=0.4642231890447657, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 1.4339824344550103"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.4339824344550103""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.4339824344550103
""",
)

entry(
    index = 309,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R",
    kinetics = ArrheniusBM(A=(444.29,'m^3/(mol*s)'), n=1.44792, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.202693327970796, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
    Total Standard Deviation in ln(k): 4.987000417702588"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 4.987000417702588""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_Ext-2CN-R
Total Standard Deviation in ln(k): 4.987000417702588
""",
)

entry(
    index = 310,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_1CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 311,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C",
    kinetics = ArrheniusBM(A=(11361.3,'m^3/(mol*s)'), n=0.960818, w0=(621500,'J/mol'), E0=(62150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4478648794535599, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
    Total Standard Deviation in ln(k): 1.1252886418431154"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C
Total Standard Deviation in ln(k): 1.1252886418431154
""",
)

entry(
    index = 312,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(100000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(32997.4,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_5BrCClFNO->O_2R!H->C_N-4R->C_Ext-2C-R_Ext-2C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 313,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C",
    kinetics = ArrheniusBM(A=(783000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 314,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C",
    kinetics = ArrheniusBM(A=(763000,'m^3/(mol*s)'), n=0, w0=(515000,'J/mol'), E0=(46820.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Ext-1C-R_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 315,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 316,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C",
    kinetics = ArrheniusBM(A=(7.19e-07,'m^3/(mol*s)'), n=3.13, w0=(515000,'J/mol'), E0=(44168.1,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_Ext-5BrCClF-R_2R!H->C_N-1C-inRing_Ext-1C-R_Sp-7R!H-1C_N-4R->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 317,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(6947.79,'m^3/(mol*s)'), n=0.711644, w0=(539000,'J/mol'), E0=(38216.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.21986040092572778, var=0.9617008253159017, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 2.5183835086482866"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.5183835086482866""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R
Total Standard Deviation in ln(k): 2.5183835086482866
""",
)

entry(
    index = 318,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(3.62392e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.9663235732869484, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C
    Total Standard Deviation in ln(k): 1.9706898352295663"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 1.9706898352295663""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C
Total Standard Deviation in ln(k): 1.9706898352295663
""",
)

entry(
    index = 319,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_N-Sp-7R!H-1C",
    kinetics = ArrheniusBM(A=(4.58e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(88195,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_N-Sp-7R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_N-Sp-7R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_N-Sp-7R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 320,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=-3.92367e-08, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 321,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.45e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 322,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(1.21e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 323,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(964000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(91985.9,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 324,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(2.41e+06,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_N-Sp-6R!H-1C_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 325,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=-1.30785e-08, w0=(563000,'J/mol'), E0=(20314.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R',), comment="""BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 326,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(67500,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(16605.5,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_Sp-7R!H-6C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 327,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C",
    kinetics = ArrheniusBM(A=(13571.8,'m^3/(mol*s)'), n=2.80368e-06, w0=(563000,'J/mol'), E0=(20084.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.432406102244557e-08, var=0.6296916452046188, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C',), comment="""BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
    Total Standard Deviation in ln(k): 1.5908198917220893"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 1.5908198917220893""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-6C-R_N-Sp-7R!H-6C
Total Standard Deviation in ln(k): 1.5908198917220893
""",
)

entry(
    index = 328,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 329,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(936268,'m^3/(mol*s)'), n=2.37741e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=9.423714773231596e-08, var=0.4365798833415042, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 1.3246127386242141"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.3246127386242141""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 1.3246127386242141
""",
)

entry(
    index = 330,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(1.11534e+06,'m^3/(mol*s)'), n=1.21072e-07, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2712594181390784e-07, var=0.1823142204075943, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 0.8559875021807728"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8559875021807728""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8559875021807728
""",
)

entry(
    index = 331,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(29186.3,'m^3/(mol*s)'), n=0.807763, w0=(549500,'J/mol'), E0=(15513.8,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.09758905201122342, var=2.521665006783426, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 3.428668064045563"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.428668064045563""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 3.428668064045563
""",
)

entry(
    index = 332,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_2NO->N",
    kinetics = ArrheniusBM(A=(720,'m^3/(mol*s)'), n=1.5, w0=(576500,'J/mol'), E0=(57650,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 333,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(1.09848e+07,'m^3/(mol*s)'), n=2.56317e-07, w0=(642000,'J/mol'), E0=(64200,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.610921668180418e-17, var=1.9951707322968388, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_N-2NO->N
    Total Standard Deviation in ln(k): 2.831698574028343"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_N-2NO->N
Total Standard Deviation in ln(k): 2.831698574028343""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_1CN->C_N-2NO->N
Total Standard Deviation in ln(k): 2.831698574028343
""",
)

entry(
    index = 334,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_2NO->N",
    kinetics = ArrheniusBM(A=(240,'m^3/(mol*s)'), n=1.5, w0=(534500,'J/mol'), E0=(53450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 335,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_N-2NO->N",
    kinetics = ArrheniusBM(A=(480,'m^3/(mol*s)'), n=1.5, w0=(612000,'J/mol'), E0=(63725,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_N-2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_N-2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_N-2R!H->C_2NO-u1_N-1CN->C_N-2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 336,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(78431,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 337,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(74023.8,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 338,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 339,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H",
    kinetics = ArrheniusBM(A=(1.73205e+07,'m^3/(mol*s)'), n=3.73492e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=6.458191251135313e-17, var=0.1655219496203035, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
    Total Standard Deviation in ln(k): 0.8156142143252552"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 0.8156142143252552""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H
Total Standard Deviation in ln(k): 0.8156142143252552
""",
)

entry(
    index = 340,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2.3811e+07,'m^3/(mol*s)'), n=1.98531e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-8.202772333702684e-09, var=0.36033976853782135, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
    Total Standard Deviation in ln(k): 1.2034085547674045"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.2034085547674045""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R
Total Standard Deviation in ln(k): 1.2034085547674045
""",
)

entry(
    index = 341,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(616000,'J/mol'), E0=(61600,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_4BrFO->F_Ext-2R!H-R_Sp-2R!H-1CN_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 342,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(3.42889e+06,'m^3/(mol*s)'), n=0.0943025, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.15763622943115357, var=0.16967390154763967, Tref=1000.0, N=17, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R',), comment="""BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 1.2218512178023146"""),
    rank = 11,
    shortDesc = """BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2218512178023146""",
    longDesc = 
"""
BM rule fitted to 17 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R
Total Standard Deviation in ln(k): 1.2218512178023146
""",
)

entry(
    index = 343,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(2.27078e+06,'m^3/(mol*s)'), n=0.239995, w0=(559767,'J/mol'), E0=(91079.6,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.12126588445248404, var=1.0425590787321457, Tref=1000.0, N=15, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 2.351638586514042"""),
    rank = 11,
    shortDesc = """BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 2.351638586514042""",
    longDesc = 
"""
BM rule fitted to 15 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 2.351638586514042
""",
)

entry(
    index = 344,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1024.08,'m^3/(mol*s)'), n=1.2742, w0=(627000,'J/mol'), E0=(62700,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.4022427239635986, var=0.6339690082228475, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 2.606873697786484"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 2.606873697786484""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 2.606873697786484
""",
)

entry(
    index = 345,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5.05321e+06,'m^3/(mol*s)'), n=5.7905e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.008309038741054636, var=0.1488420045984497, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.7943047219021818"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7943047219021818""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.7943047219021818
""",
)

entry(
    index = 346,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(898.241,'m^3/(mol*s)'), n=1.23094, w0=(554750,'J/mol'), E0=(55475,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.515969144547229, var=0.6725830965819513, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R
    Total Standard Deviation in ln(k): 2.94051145118457"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.94051145118457""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R
Total Standard Deviation in ln(k): 2.94051145118457
""",
)

entry(
    index = 347,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_2R!H->C",
    kinetics = ArrheniusBM(A=(1.5055e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 348,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 349,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N",
    kinetics = ArrheniusBM(A=(467.561,'m^3/(mol*s)'), n=1.27907, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570074, var=0.9609060278364029, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N
    Total Standard Deviation in ln(k): 3.469757305105129"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N
Total Standard Deviation in ln(k): 3.469757305105129
""",
)

entry(
    index = 350,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N",
    kinetics = ArrheniusBM(A=(661.23,'m^3/(mol*s)'), n=1.27907, w0=(601500,'J/mol'), E0=(60150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.5988305691570073, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N
    Total Standard Deviation in ln(k): 1.5045994199924806"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N
Total Standard Deviation in ln(k): 1.5045994199924806
""",
)

entry(
    index = 351,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 352,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_N-2R!H->C",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_N-Sp-2R!H-1N_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 353,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_Ext-1CN-R_Ext-1CN-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 354,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(1.01037e+07,'m^3/(mol*s)'), n=6.89869e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.6641677013186936, var=0.9829722947411796, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
    Total Standard Deviation in ln(k): 3.6563568444685712"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 3.6563568444685712""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C
Total Standard Deviation in ln(k): 3.6563568444685712
""",
)

entry(
    index = 355,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(500,'m^3/(mol*s)'), n=1.5, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 356,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 357,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(8982.49,'m^3/(mol*s)'), n=1.03352, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.38747860357218106, var=1.0474269127416715, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 3.0252879292358665"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 3.0252879292358665""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 3.0252879292358665
""",
)

entry(
    index = 358,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(558500,'J/mol'), E0=(55850,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 359,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(684500,'J/mol'), E0=(68450,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_N-Sp-2CN-1CCNN_N-1CN->C_N-2CN->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 360,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.08e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 361,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Sp-8R!H-1C",
    kinetics = ArrheniusBM(A=(2.16e+08,'m^3/(mol*s)'), n=-0.75, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Sp-8R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Sp-8R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Sp-8R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_Sp-8R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 362,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_N-Sp-8R!H-1C",
    kinetics = ArrheniusBM(A=(2.89e+07,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(83476.8,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_N-Sp-8R!H-1C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_N-Sp-8R!H-1C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_N-Sp-8R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-4C-R_Ext-1C-R_N-Sp-8R!H-1C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 363,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(2.56e+07,'m^3/(mol*s)'), n=-0.35, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-4C-R_Ext-1C-R_Sp-7R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 364,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 365,
    label = "Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-Sp-5C-4C",
    kinetics = ArrheniusBM(A=(843000,'m^3/(mol*s)'), n=0, w0=(539000,'J/mol'), E0=(53900,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-Sp-5C-4C',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-Sp-5C-4C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_5R!H-u0_1R!H->C_N-5R!H->S_N-5BrCClFNO->O_5BrCClF->C_N-Sp-5C#4R_4R->C_Ext-1C-R_Sp-6R!H-1C_Ext-1C-R_N-Sp-5C-4C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 366,
    label = "Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R",
    kinetics = ArrheniusBM(A=(10000,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(20643.5,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_Ext-4R-R_N-5R!H-u0_N-1R!H->O_Sp-2R!H-1CNS_N-1CNS-inRing_2R!H->C_Ext-1CNS-R_Sp-6R!H-1CNS_6R!H->C_Ext-1CNS-R_Ext-6C-R_Ext-7R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 367,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(774450,'m^3/(mol*s)'), n=-1.98908e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=7.107495827623396e-08, var=0.2355817332363053, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 0.973033685645405"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.973033685645405""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 0.973033685645405
""",
)

entry(
    index = 368,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_N-5BrCFINOPSSi->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 369,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.0119e+06,'m^3/(mol*s)'), n=-2.72185e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=8.371635008370871e-08, var=0.1168666827194647, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 0.6853343203143046"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 0.6853343203143046""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 0.6853343203143046
""",
)

entry(
    index = 370,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 371,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.8e+07,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(46024.6,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 372,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(1175.26,'m^3/(mol*s)'), n=1.21164, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0064379313563148, var=0.3339094409755069, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 3.687172635934617"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.687172635934617""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.687172635934617
""",
)

entry(
    index = 373,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_Ext-2R!H-R_Ext-5R!H-R_N-Sp-6R!H#5R!H_Ext-5R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 374,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(1.5e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 375,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=1.03647e-07, w0=(538000,'J/mol'), E0=(53800,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 376,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F",
    kinetics = ArrheniusBM(A=(21.4925,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.1003516016859414, var=0.2670935974246947, Tref=1000.0, N=11, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F',), comment="""BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F
    Total Standard Deviation in ln(k): 1.2882088189626515"""),
    rank = 11,
    shortDesc = """BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.2882088189626515""",
    longDesc = 
"""
BM rule fitted to 11 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F
Total Standard Deviation in ln(k): 1.2882088189626515
""",
)

entry(
    index = 377,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F",
    kinetics = ArrheniusBM(A=(6.60524e+06,'m^3/(mol*s)'), n=-2.68923e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.35386389886163966, var=0.40673745976559184, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F',), comment="""BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F
    Total Standard Deviation in ln(k): 2.1676445540720453"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1676445540720453""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F
Total Standard Deviation in ln(k): 2.1676445540720453
""",
)

entry(
    index = 378,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_4BrO->Br",
    kinetics = ArrheniusBM(A=(2.37e+06,'m^3/(mol*s)'), n=0, w0=(514500,'J/mol'), E0=(51450,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 379,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br",
    kinetics = ArrheniusBM(A=(20404.6,'m^3/(mol*s)'), n=0.86546, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.047786475748374746, var=1.3701966154302267, Tref=1000.0, N=14, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br',), comment="""BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br
    Total Standard Deviation in ln(k): 2.4667171416766123"""),
    rank = 11,
    shortDesc = """BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 2.4667171416766123""",
    longDesc = 
"""
BM rule fitted to 14 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 2.4667171416766123
""",
)

entry(
    index = 380,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_4BrO->Br",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(607000,'J/mol'), E0=(60700,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_4BrO->Br',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_4BrO->Br
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_4BrO->Br
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 381,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br",
    kinetics = ArrheniusBM(A=(1012.18,'m^3/(mol*s)'), n=1.27582, w0=(633667,'J/mol'), E0=(63366.7,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.8153629076042856, var=1.5584477908283234, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br
    Total Standard Deviation in ln(k): 4.5513178164909815"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 4.5513178164909815""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br
Total Standard Deviation in ln(k): 4.5513178164909815
""",
)

entry(
    index = 382,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(5.43331e+06,'m^3/(mol*s)'), n=1.20513e-07, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.2226403499953882, var=3.6672937428446057, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.911064333455957"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.911064333455957""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.911064333455957
""",
)

entry(
    index = 383,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2.51983e+06,'m^3/(mol*s)'), n=4.88435e-07, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.8790579300723155e-07, var=0.3603399442820822, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 1.203409299744614"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.203409299744614""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 1.203409299744614
""",
)

entry(
    index = 384,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 385,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C",
    kinetics = ArrheniusBM(A=(800102,'m^3/(mol*s)'), n=0.163791, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06361006619736874, var=0.06603124804374166, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C',), comment="""BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C
    Total Standard Deviation in ln(k): 0.6749719598709518"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 0.6749719598709518""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C
Total Standard Deviation in ln(k): 0.6749719598709518
""",
)

entry(
    index = 386,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_N-2R!H->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(571000,'J/mol'), E0=(57100,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_N-2R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_N-2R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_N-2R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 387,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_2N-u1",
    kinetics = ArrheniusBM(A=(1.2,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 388,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_N-2N-u1",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_2R!H->N_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 389,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(577500,'J/mol'), E0=(57750,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 390,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_N-2CO->C",
    kinetics = ArrheniusBM(A=(2.4,'m^3/(mol*s)'), n=2, w0=(625500,'J/mol'), E0=(55881.2,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_N-2CO->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_N-1CN->C_Sp-2R!H-1N_N-2R!H->N_N-2CO->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 391,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R",
    kinetics = ArrheniusBM(A=(2.44948e+07,'m^3/(mol*s)'), n=3.91461e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=4.305460834090209e-17, var=0.32880390778633084, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
    Total Standard Deviation in ln(k): 1.1495436707873932"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.1495436707873932""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R
Total Standard Deviation in ln(k): 1.1495436707873932
""",
)

entry(
    index = 392,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_5R!H->O",
    kinetics = ArrheniusBM(A=(1.3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 393,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_N-5R!H->O",
    kinetics = ArrheniusBM(A=(1e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_N-5R!H->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_N-5R!H->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_N-5R!H->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 394,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1",
    kinetics = ArrheniusBM(A=(170,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 395,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1",
    kinetics = ArrheniusBM(A=(330,'m^3/(mol*s)'), n=1.5, w0=(548000,'J/mol'), E0=(54800,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_N-1CN->C_N-2CN->C_N-2N-u1
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 396,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.06667e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 397,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(1.05e+06,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 398,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-2C-R",
    kinetics = ArrheniusBM(A=(602222,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-2C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-2C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-2C-R_N-5R!H->Cl_5BrCFINOPSSi->C_Ext-2C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 399,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=-1.57583e-09, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 400,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(901998,'m^3/(mol*s)'), n=3.77371e-08, w0=(549500,'J/mol'), E0=(54950,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.0763652085225523e-17, var=3.9331302308647265e-05, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.01257263051719242"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01257263051719242""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-1C-R
Total Standard Deviation in ln(k): 0.01257263051719242
""",
)

entry(
    index = 401,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(538000,'J/mol'), E0=(53800,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_N-Sp-2R!H-1CN_1CN->C_2R!H->C_Ext-1C-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 402,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R",
    kinetics = ArrheniusBM(A=(18.9153,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035160543507311, var=0.15570237264362138, Tref=1000.0, N=7, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R',), comment="""BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R
    Total Standard Deviation in ln(k): 1.0431909321781416"""),
    rank = 11,
    shortDesc = """BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.0431909321781416""",
    longDesc = 
"""
BM rule fitted to 7 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R
Total Standard Deviation in ln(k): 1.0431909321781416
""",
)

entry(
    index = 403,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(26.8761,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344721, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 6.907809337393689"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 6.907809337393689
""",
)

entry(
    index = 404,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 405,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_5BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_5BrCClINOPSSi->O',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_5BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_5BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_5BrCClINOPSSi->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 406,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O",
    kinetics = ArrheniusBM(A=(6.66178e+06,'m^3/(mol*s)'), n=-2.56283e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.04726554057179082, var=0.05914869985566957, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O
    Total Standard Deviation in ln(k): 0.6063193488291327"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.6063193488291327""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O
Total Standard Deviation in ln(k): 0.6063193488291327
""",
)

entry(
    index = 407,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R",
    kinetics = ArrheniusBM(A=(11841.3,'m^3/(mol*s)'), n=0.932034, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.051462352195148865, var=1.3863207513923612, Tref=1000.0, N=13, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R',), comment="""BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R
    Total Standard Deviation in ln(k): 2.4897200318547332"""),
    rank = 11,
    shortDesc = """BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.4897200318547332""",
    longDesc = 
"""
BM rule fitted to 13 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R
Total Standard Deviation in ln(k): 2.4897200318547332
""",
)

entry(
    index = 408,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_2NO->N",
    kinetics = ArrheniusBM(A=(3.6,'m^3/(mol*s)'), n=2, w0=(590000,'J/mol'), E0=(59000,'J/mol'), Tmin=(300,'K'), Tmax=(2500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_2NO->N',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_2NO->N
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_2NO->N
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 409,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N",
    kinetics = ArrheniusBM(A=(2.88674e+06,'m^3/(mol*s)'), n=5.26425e-07, w0=(655500,'J/mol'), E0=(65550,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=2.413897921625164, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N
    Total Standard Deviation in ln(k): 3.1147015559000413"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N
Total Standard Deviation in ln(k): 3.1147015559000413""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N
Total Standard Deviation in ln(k): 3.1147015559000413
""",
)

entry(
    index = 410,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_5R!H->Cl",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_5R!H->Cl',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_5R!H->Cl
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_5R!H->Cl
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 411,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=-8.33353e-08, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl
    Total Standard Deviation in ln(k): 0.0"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 0.0""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl
Total Standard Deviation in ln(k): 0.0
""",
)

entry(
    index = 412,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Ext-6R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 413,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 414,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 415,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C",
    kinetics = ArrheniusBM(A=(105.671,'m^3/(mol*s)'), n=1.44792, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.07994677116248543, var=0.2503740114467667, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C
    Total Standard Deviation in ln(k): 1.2039883366696844"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 1.2039883366696844""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C
Total Standard Deviation in ln(k): 1.2039883366696844
""",
)

entry(
    index = 416,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(2.5e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 417,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 418,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(3e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_N-4BrFO-u1_N-2R!H->O_Sp-2CN-1CCNN_1CN->C_2CN->C_Ext-2C-R_Ext-2C-R_N-5R!H->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 419,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 420,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C",
    kinetics = ArrheniusBM(A=(900000,'m^3/(mol*s)'), n=0, w0=(549500,'J/mol'), E0=(54950,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_4BrFHO->H_Sp-2R!H-1CN_2R!H->C_1CN->C_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R_N-Sp-6R!H-5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 421,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R",
    kinetics = ArrheniusBM(A=(15.5169,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.10035159271588616, var=0.0, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R
    Total Standard Deviation in ln(k): 0.25213968019066874"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.25213968019066874""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R
Total Standard Deviation in ln(k): 0.25213968019066874
""",
)

entry(
    index = 422,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(21.9442,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 423,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-1C-R",
    kinetics = ArrheniusBM(A=(8e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 424,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-5CCl-R",
    kinetics = ArrheniusBM(A=(8e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-5CCl-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-5CCl-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-5CCl-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_Ext-5CCl-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 425,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_5CCl->C",
    kinetics = ArrheniusBM(A=(4e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_5CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_5CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 426,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_N-5CCl->C",
    kinetics = ArrheniusBM(A=(6.66667e+06,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_N-5CCl->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_N-5CCl->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_N-5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_N-5R!H->F_N-5BrCClINOPSSi->O_N-5CCl->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 427,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(43216.4,'m^3/(mol*s)'), n=0.807763, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.044600708811499516, var=0.1387658964498666, Tref=1000.0, N=9, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C',), comment="""BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C
    Total Standard Deviation in ln(k): 0.8588518561398296"""),
    rank = 11,
    shortDesc = """BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8588518561398296""",
    longDesc = 
"""
BM rule fitted to 9 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C
Total Standard Deviation in ln(k): 0.8588518561398296
""",
)

entry(
    index = 428,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C",
    kinetics = ArrheniusBM(A=(643.182,'m^3/(mol*s)'), n=1.21164, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.06690106479011634, var=4.77344894659504, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C
    Total Standard Deviation in ln(k): 4.548083243181481"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 4.548083243181481""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C
Total Standard Deviation in ln(k): 4.548083243181481
""",
)

entry(
    index = 429,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1C-R",
    kinetics = ArrheniusBM(A=(5e+06,'m^3/(mol*s)'), n=0, w0=(655500,'J/mol'), E0=(65550,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_N-2R!H->C_N-4BrO->Br_N-2NO->N_Ext-1C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 430,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_5CF->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 431,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_N-5CF->C",
    kinetics = ArrheniusBM(A=(2e+07,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_N-5CF->C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_N-5CF->C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-1C-R_Ext-2R!H-R_N-5R!H->Cl_N-5CF->C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 432,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Ext-5C-R",
    kinetics = ArrheniusBM(A=(0.00558313,'m^3/(mol*s)'), n=2.89583, w0=(551500,'J/mol'), E0=(55150,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=2.4053866559415926, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Ext-5C-R',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Ext-5C-R
    Total Standard Deviation in ln(k): 8.008842950292529"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 8.008842950292529""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Ext-5C-R
Total Standard Deviation in ln(k): 8.008842950292529
""",
)

entry(
    index = 433,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 434,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C",
    kinetics = ArrheniusBM(A=(2e+06,'m^3/(mol*s)'), n=0, w0=(551500,'J/mol'), E0=(55150,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_N-Sp-2R!H-1C_Ext-2R!H-R_2R!H->C_5R!H->C_Ext-5C-R_N-Sp-6R!H=5C
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 435,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R_Ext-2R!H-R",
    kinetics = ArrheniusBM(A=(2.2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R_Ext-2R!H-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R_Ext-2R!H-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_Ext-2R!H-R_5R!H->F_Ext-1C-R_Ext-1C-R_Ext-2R!H-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 436,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R",
    kinetics = ArrheniusBM(A=(19337.9,'m^3/(mol*s)'), n=0.908733, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.050175799781273386, var=0.03404324048259046, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R',), comment="""BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
    Total Standard Deviation in ln(k): 0.495959717071232"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.495959717071232""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R
Total Standard Deviation in ln(k): 0.495959717071232
""",
)

entry(
    index = 437,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(1.514e+07,'m^3/(mol*s)'), n=2.61625e-07, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=3.036502523045642e-08, var=0.36467594120944413, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 1.2106276063144492"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 1.2106276063144492""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 1.2106276063144492
""",
)

entry(
    index = 438,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(32.9163,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.5096568970344717, var=0.9609060278364027, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 5.758265666606295"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 5.758265666606295""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 5.758265666606295
""",
)

entry(
    index = 439,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C",
    kinetics = ArrheniusBM(A=(4.24245,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=4.528059738902607, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
    Total Standard Deviation in ln(k): 8.059031284357149"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 8.059031284357149""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_5R!H->C
Total Standard Deviation in ln(k): 8.059031284357149
""",
)

entry(
    index = 440,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C",
    kinetics = ArrheniusBM(A=(97510.5,'m^3/(mol*s)'), n=0.605822, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.5032189656781574, var=0.9399316159026726, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
    Total Standard Deviation in ln(k): 3.2079613302398537"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.2079613302398537""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_N-Sp-5R!H-1C_N-5R!H->C
Total Standard Deviation in ln(k): 3.2079613302398537
""",
)

entry(
    index = 441,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_5R!H->C",
    kinetics = ArrheniusBM(A=(1.20499e+07,'m^3/(mol*s)'), n=6.26727e-08, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-1.3454565106531903e-18, var=0.00013774025631438147, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_5R!H->C
    Total Standard Deviation in ln(k): 0.023528131175717372"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.023528131175717372""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_5R!H->C
Total Standard Deviation in ln(k): 0.023528131175717372
""",
)

entry(
    index = 442,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_N-5R!H->C",
    kinetics = ArrheniusBM(A=(31.0338,'m^3/(mol*s)'), n=1.81747, w0=(563000,'J/mol'), E0=(56300,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.509656897034472, var=0.0, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_N-5R!H->C',), comment="""BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_N-5R!H->C
    Total Standard Deviation in ln(k): 3.793107781493648"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.793107781493648""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_Ext-1C-R_N-5R!H->C
Total Standard Deviation in ln(k): 3.793107781493648
""",
)

entry(
    index = 443,
    label = "Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R",
    kinetics = ArrheniusBM(A=(1.2e+07,'m^3/(mol*s)'), n=0, w0=(563000,'J/mol'), E0=(56300,'J/mol'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R',), comment="""BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-4R->C_N-1R!H-inRing_N-4BrClFHNOS->N_N-1R!H->O_N-4BrClFHO->Cl_N-4BrFHO->H_4BrFO-u1_N-4BrFO->F_1CN->C_Sp-2R!H-1C_2R!H->C_N-4BrO->Br_Ext-1C-R_Sp-5R!H-1C_5R!H->C_Ext-5C-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

