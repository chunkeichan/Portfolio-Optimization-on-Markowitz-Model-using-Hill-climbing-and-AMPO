import numpy as np
import pandas as pd
from params import df, stocklist, risk_free_rate


def findRi(stocklist, rec=0):
    """Overall returns of each stock in a portfolio"""
    Ri_list = []
    for i, item in enumerate(stocklist):
        start_pi = df.loc[0, stocklist[i]]
        end_pi = df.loc[df.index[-1], stocklist[i]]
        Ri = (end_pi-start_pi)/start_pi
        Ri_list.append(Ri)

    if rec == 1:
        with open("./process/return.csv", "a") as file:
            elements = ', '.join(map(str, Ri_list))
            file.write("%s\n" % elements)

    return Ri_list


def findRlog(df, rec=0):
    """Daily log returns of each stock in a portfolio"""
    df = df.set_index("Date")
    df_shifted = df.shift(periods=1)
    df = df.divide(df_shifted)

    array = df.to_numpy()
    array = np.log10(array)
    array = np.nan_to_num(array)

    if rec == 1:
        data = pd.DataFrame(array)
        data.to_excel("./process/Rlog.xlsx")

    return array


def findStdi(df, rec=0):
    """Standard deviations of the daily log returns of each stock in a portfolio"""
    array = findRlog(df, rec)

    if rec == 1:
        data = pd.DataFrame(array)
        data.to_excel("./process/Rlog_std.xlsx")

    return np.std(array, axis=0)


def findCorr(df, rec=0):
    """Correlated variances of each stock in a portfolio"""
    array = findRlog(df, rec)
    array = np.corrcoef(array, rowvar=False)

    if rec == 1:
        data = pd.DataFrame(array)
        data.to_excel("./process/corr.xlsx")

    return array


def findRisk(df, stocklist, weighting, rec=0):
    """Risks of the portfolio"""
    df_var = pd.DataFrame(index=stocklist, columns=stocklist)
    for i, stock in enumerate(stocklist):
        for j, stock in enumerate(stocklist):
            std = findStdi(df, rec)
            corr_array = findCorr(df, rec)

            var = weighting[i] * weighting[j] * \
                std[i] * std[j] * corr_array[i, j]
            df_var.iloc[i, j] = var

    risk = np.sqrt(df_var.sum().sum())

    if rec == 1:
        df_var.to_excel("./process/var.xlsx")

    return risk


def findSharpratio(variables, rec=0):
    """Sharp ratio of the portfolio"""
    Ri = findRi(stocklist, rec)
    weighting = variables
    risk = findRisk(df, stocklist, weighting, rec)
    sharpRatio = (np.dot(Ri, weighting) - risk_free_rate) / risk
    print("Sharp Ratio: %s" % sharpRatio)

    return sharpRatio


def eqconstHandler(variables):
    """For the optimizaiton problem, the input weighting must be with a sum of 100% and restricted to no more than 25% of the portfolio."""
    # The input weighting must be with a sum of 100%
    solutions = [np.abs(x) / sum(np.abs(variables)) for x in variables]

    # Restrict shares of each stock to no more than 25% of the portfolio
    values = 0
    for i, value in enumerate(solutions):
        if value < 0.25:
            values += 1

    if values == 10:
        return solutions
    else:
        return [0 for x in variables]


def inputSharpratio(variables):
    """AMPO is an optimization method for finding the minimum fitness. To suit the calculations of AMPO, the return value was modified to 1/Sharp Ratio."""
    eqconsts = eqconstHandler(variables)
    sr = findSharpratio(eqconsts)
    if sr <= 0:
        sr = 10**(-10)

    return 1 / sr


def verifySharpratio(variables, rec=0):
    """To verify the sharp ratio of the portfolio"""
    Ri = findRi(stocklist, rec)
    weighting = variables
    risk = findRisk(df, stocklist, weighting, rec)
    sharpRatio = (np.dot(Ri, weighting) - risk_free_rate) / risk
    print("Sharp Ratio: %s" % sharpRatio)

    return sharpRatio, np.dot(Ri, weighting), risk
