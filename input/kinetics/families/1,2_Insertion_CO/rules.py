#!/usr/bin/env python
# encoding: utf-8

name = "1,2_Insertion_CO/rules"
shortDesc = ""
longDesc = """

"""
entry(
    index = 1,
    label = "Root",
    kinetics = ArrheniusBM(A=(4.78288e+06,'m^3/(mol*s)'), n=-0.116196, w0=(721375,'J/mol'), E0=(367834,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=1.059655531095249, var=44.66439062129143, Tref=1000.0, N=8, data_mean=0.0, correlation='Root',), comment="""BM rule fitted to 8 training reactions at node Root
    Total Standard Deviation in ln(k): 16.060380822072638"""),
    rank = 11,
    shortDesc = """BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 16.060380822072638""",
    longDesc = 
"""
BM rule fitted to 8 training reactions at node Root
Total Standard Deviation in ln(k): 16.060380822072638
""",
)

entry(
    index = 2,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(0.0123847,'m^3/(mol*s)'), n=2.69664, w0=(732667,'J/mol'), E0=(328447,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.005092483834448143, var=12.100279875618146, Tref=1000.0, N=6, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 6.986357678898654"""),
    rank = 11,
    shortDesc = """BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 6.986357678898654""",
    longDesc = 
"""
BM rule fitted to 6 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 6.986357678898654
""",
)

entry(
    index = 3,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H",
    kinetics = ArrheniusBM(A=(5.72552e+13,'m^3/(mol*s)'), n=-2.43579, w0=(687500,'J/mol'), E0=(400369,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.532965083379061, var=78.35122624677618, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H',), comment="""BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
    Total Standard Deviation in ln(k): 29.13451823103456"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 29.13451823103456""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H
Total Standard Deviation in ln(k): 29.13451823103456
""",
)

entry(
    index = 4,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(1.27e-07,'m^3/(mol*s)'), n=3.7, w0=(750500,'J/mol'), E0=(244047,'J/mol'), Tmin=(300,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 5,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O",
    kinetics = ArrheniusBM(A=(0.0670668,'m^3/(mol*s)'), n=2.55683, w0=(729100,'J/mol'), E0=(343813,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0035061595450414855, var=1.7872549530080575, Tref=1000.0, N=5, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O',), comment="""BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
    Total Standard Deviation in ln(k): 2.6889047888192392"""),
    rank = 11,
    shortDesc = """BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.6889047888192392""",
    longDesc = 
"""
BM rule fitted to 5 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O
Total Standard Deviation in ln(k): 2.6889047888192392
""",
)

entry(
    index = 6,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(9.26653e+18,'m^3/(mol*s)'), n=-4.11331, w0=(719500,'J/mol'), E0=(396512,'J/mol'), Tmin=(303.03,'K'), Tmax=(2000,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 7,
    label = "Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H",
    kinetics = ArrheniusBM(A=(0.000538,'m^3/(mol*s)'), n=3.29, w0=(655500,'J/mol'), E0=(448068,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H',), comment="""BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_N-2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 8,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H",
    kinetics = ArrheniusBM(A=(2890,'m^3/(mol*s)'), n=1.16, w0=(763500,'J/mol'), E0=(346508,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_1CsH->H
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

entry(
    index = 9,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H",
    kinetics = ArrheniusBM(A=(0.0430735,'m^3/(mol*s)'), n=2.62791, w0=(720500,'J/mol'), E0=(345663,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.004089009511262693, var=2.3537540883916734, Tref=1000.0, N=4, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H',), comment="""BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
    Total Standard Deviation in ln(k): 3.0859282883429664"""),
    rank = 11,
    shortDesc = """BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.0859282883429664""",
    longDesc = 
"""
BM rule fitted to 4 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H
Total Standard Deviation in ln(k): 3.0859282883429664
""",
)

entry(
    index = 10,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(0.253032,'m^3/(mol*s)'), n=2.34614, w0=(720500,'J/mol'), E0=(343443,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-0.0026699747910795724, var=4.36094264845777, Tref=1000.0, N=3, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R',), comment="""BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
    Total Standard Deviation in ln(k): 4.193170705903081"""),
    rank = 11,
    shortDesc = """BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.193170705903081""",
    longDesc = 
"""
BM rule fitted to 3 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R
Total Standard Deviation in ln(k): 4.193170705903081
""",
)

entry(
    index = 11,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(1.16312,'m^3/(mol*s)'), n=2.09403, w0=(720500,'J/mol'), E0=(337793,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=-4.42539995393569e-06, var=10.373291544404179, Tref=1000.0, N=2, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 6.456780598481218"""),
    rank = 11,
    shortDesc = """BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.456780598481218""",
    longDesc = 
"""
BM rule fitted to 2 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 6.456780598481218
""",
)

entry(
    index = 12,
    label = "Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R",
    kinetics = ArrheniusBM(A=(88.9,'m^3/(mol*s)'), n=1.51, w0=(720500,'J/mol'), E0=(330828,'J/mol'), Tmin=(300,'K'), Tmax=(1500,'K'), uncertainty=RateUncertainty(mu=0.0, var=33.13686319048999, Tref=1000.0, N=1, data_mean=0.0, correlation='Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R',), comment="""BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
    Total Standard Deviation in ln(k): 11.540182761524994"""),
    rank = 11,
    shortDesc = """BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994""",
    longDesc = 
"""
BM rule fitted to 1 training reactions at node Root_2Br1sCbCdCl1sCsCtF1sHI1sNSSidSis->H_N-1COCbCdCsCtHNOSSidSis->O_N-1CsH->H_Ext-1Cs-R_Ext-1Cs-R_Ext-1Cs-R
Total Standard Deviation in ln(k): 11.540182761524994
""",
)

