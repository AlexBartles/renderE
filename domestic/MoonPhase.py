# uncompyle6 version 3.9.3
# Python bytecode version base 2.2 (60717)
# Decompiled from: Python 3.13.2 (main, Feb  4 2025, 14:51:09) [Clang 16.0.0 (clang-1600.0.26.6)]
# Embedded file name: MoonPhase.py
# Compiled at: 2007-01-12 11:33:26
import time
from math import *
__todaysJulianDate = 0

def __toRad(degrees):
    degrees = degrees % 360.0
    return degrees * 0.0174532925199433
    return


def __JDtoDate(jd):
    event_date = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    jd = jd + 0.5
    z = int(jd)
    f = jd - z
    if z < 2299161:
        a = z
    else:
        a1 = (z - 1867216.25) / 36524.25
        a = z + 1 + a1 - int(a1 / 4)
    b = a + 1524
    c = int((b - 122.1) / 365.25)
    d = int(365.25 * c)
    e = int((b - d) / 30.6001)
    day = b - d - int(30.6001 * e) + f
    if e < 14:
        event_date[1] = e - 1
    else:
        event_date[1] = e - 13
    if event_date[1] > 2:
        event_date[0] = c - 4716
    else:
        event_date[0] = c - 4715
    event_date[2] = int(day)
    day = day - event_date[2]
    day = day * 24
    event_date[3] = int(day)
    day = day - event_date[3]
    day = day * 60
    event_date[4] = int(day)
    day = day - event_date[4]
    day = day * 60
    event_date[5] = int(day)
    event_date[8] = -1
    return time.localtime(time.mktime(tuple(event_date)))
    return


def __DatetoJD(event_date):
    y = event_date[0]
    m = event_date[1]
    d = event_date[2]
    h = float(event_date[3])
    h = h + event_date[4] / 60.0
    jd = 367 * y - int(7 * (y + int((m + 9) / 12)) / 4) + int(275 * m / 9) + d + 1721013.5 + h / 24.0 + 1
    return jd
    return


def __calcMoonPhase(k, phi):
    T = k / 1236.85
    JDE = 2451550.09765 + 29.530588853 * k
    E = 1.0 + T * (-0.002516 + -7.4e-06 * T)
    M = 2.5534 + 29.10535669 * k + T * T * (-2.18e-05 + -1.1e-07 * T)
    M1 = 201.5643 + 385.81693528 * k + T * T * (0.0107438 + T * (1.239e-05 + -5.8e-08 * T))
    F = 160.7108 + 390.67050274 * k + T * T * (-0.0016341 * T * (-2.27e-06 + 1.1e-08 * T))
    O = 124.7746 - 1.5637558 * k + T * T * (0.0020691 + 2.15e-06 * T)
    A = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25]
    A[0] = 0
    A[1] = 299.77 + 0.107408 * k - 0.009173 * T * T
    A[2] = 251.88 + 0.016321 * k
    A[3] = 251.83 + 26.651886 * k
    A[4] = 349.42 + 36.412478 * k
    A[5] = 84.66 + 18.206239 * k
    A[6] = 141.74 + 53.303771 * k
    A[7] = 207.14 + 2.453732 * k
    A[8] = 154.84 + 7.30686 * k
    A[9] = 34.52 + 27.261239 * k
    A[10] = 207.19 + 0.121824 * k
    A[11] = 291.34 + 1.844379 * k
    A[12] = 161.72 + 24.198154 * k
    A[13] = 239.56 + 25.513099 * k
    A[14] = 331.55 + 3.592518 * k
    M = __toRad(M)
    M1 = __toRad(M1)
    F = __toRad(F)
    O = __toRad(O)
    for i in range(15):
        A[i] = __toRad(A[i])

    if phi == 0:
        JDE = JDE - 0.4072 * sin(M1) + 0.17241 * E * sin(M) + 0.01608 * sin(2.0 * M1) + 0.01039 * sin(2.0 * F) + 0.00739 * E * sin(M1 - M) - 0.00514 * E * sin(M1 + M) + 0.00208 * E * E * sin(2.0 * M) - 0.00111 * sin(M1 - 2.0 * F) - 0.00057 * sin(M1 + 2.0 * F) + 0.00056 * E * sin(2.0 * M1 + M) - 0.00042 * sin(3.0 * M1) + 0.00042 * E * sin(M + 2.0 * F) + 0.00038 * E * sin(M - 2.0 * F) - 0.00024 * E * sin(2.0 * M1 - M) - 0.00017 * sin(O) - 7e-05 * sin(M1 + 2.0 * M) + 4e-05 * sin(2.0 * M1 - 2.0 * F) + 4e-05 * sin(3.0 * M) + 3e-05 * sin(M1 + M - 2.0 * F) + 3e-05 * sin(2.0 * M1 + 2.0 * F) - 3e-05 * sin(M1 + M + 2.0 * F) + 3e-05 * sin(M1 - M + 2.0 * F) - 2e-05 * sin(M1 - M - 2.0 * F) - 2e-05 * sin(3.0 * M1 + M) + 2e-05 * sin(4.0 * M1)
    elif phi == 2:
        JDE = JDE - 0.40614 * sin(M1) + 0.17302 * E * sin(M) + 0.01614 * sin(2.0 * M1) + 0.01043 * sin(2.0 * F) + 0.00734 * E * sin(M1 - M) - 0.00515 * E * sin(M1 + M) + 0.00209 * E * E * sin(2.0 * M) - 0.00111 * sin(M1 - 2.0 * F) - 0.00057 * sin(M1 + 2.0 * F) + 0.00056 * E * sin(2.0 * M1 + M) - 0.00042 * sin(3.0 * M1) + 0.00042 * E * sin(M + 2.0 * F) + 0.00038 * E * sin(M - 2.0 * F) - 0.00024 * E * sin(2.0 * M1 - M) - 0.00017 * sin(O) - 7e-05 * sin(M1 + 2.0 * M) + 4e-05 * sin(2.0 * M1 - 2.0 * F) + 4e-05 * sin(3.0 * M) + 3e-05 * sin(M1 + M - 2.0 * F) + 3e-05 * sin(2.0 * M1 + 2.0 * F) - 3e-05 * sin(M1 + M + 2.0 * F) + 3e-05 * sin(M1 - M + 2.0 * F) - 2e-05 * sin(M1 - M - 2.0 * F) - 2e-05 * sin(3.0 * M1 + M) + 2e-05 * sin(4.0 * M1)
    elif phi == 1 or phi == 3:
        JDE = JDE - 0.62801 * sin(M1) + 0.17172 * E * sin(M) - 0.01183 * E * sin(M1 + M) + 0.00862 * sin(2.0 * M1) + 0.00804 * sin(2.0 * F) + 0.00454 * E * sin(M1 - M) + 0.00204 * E * E * sin(2.0 * M) - 0.0018 * sin(M1 - 2.0 * F) - 0.0007 * sin(M1 + 2.0 * F) - 0.0004 * sin(3.0 * M1) - 0.00034 * E * sin(2.0 * M1 - M) + 0.00032 * E * sin(M + 2.0 * F) + 0.00032 * E * sin(M - 2.0 * F) - 0.00028 * E * E * sin(M1 + 2.0 * M) + 0.00027 * E * sin(2.0 * M1 + M) - 0.00017 * sin(O) - 5e-05 * sin(M1 - M - 2.0 * F) + 4e-05 * sin(2.0 * M1 + 2.0 * F) - 4e-05 * sin(M1 + M + 2.0 * F) + 4e-05 * sin(M1 - 2.0 * M) + 3e-05 * sin(M1 + M - 2.0 * F) + 3e-05 * sin(3.0 * M) + 2e-05 * sin(2.0 * M1 - 2.0 * F) + 2e-05 * sin(M1 - M + 2.0 * F) - 2e-05 * sin(3.0 * M1 + M)
        W = 0.00306 - 0.00038 * E * cos(M) + 0.00026 * cos(M1) - 2e-05 * cos(M1 - M) + 2e-05 * cos(M1 + M) + 2e-05 * cos(2.0 * F)
        if phi == 3:
            W = -W
            JDE = JDE + W
        JDE = JDE + 0.000325 * sin(A[1]) + 0.000165 * sin(A[2]) + 0.000164 * sin(A[3]) + 0.000126 * sin(A[4]) + 0.00011 * sin(A[5]) + 6.2e-05 * sin(A[6]) + 6e-05 * sin(A[7]) + 5.6e-05 * sin(A[8]) + 4.7e-05 * sin(A[9]) + 4.2e-05 * sin(A[10]) + 4e-05 * sin(A[11]) + 3.7e-05 * sin(A[12]) + 3.5e-05 * sin(A[13]) + 2.3e-05 * sin(A[14])
    return JDE
    return


def __moonPhaseByLunation(lun, phi):
    k = float(lun) + phi / 4.0
    return __calcMoonPhase(k, phi)
    return


def __obtainCurrentPhases(phi, phaseTime):
    global __todaysJulianDate
    phaseJD = __DatetoJD(phaseTime)
    if phaseJD - __todaysJulianDate >= 0.0:
        return 1
    return 0
    return


def calcPhases(date=None):
    global __todaysJulianDate
    if date is None:
        date = time.localtime(time.time())
    __todaysJulianDate = __DatetoJD(date)
    LUNATION_OFFSET = 953
    START_LUNATION = 978
    END_LUNATION = 1422
    event_date = [[4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4, 4, 4], [4, 4, 4, 4, 4, 4, 4, 4, 4]]
    phases = []
    for lun in range(START_LUNATION, END_LUNATION):
        for phi in range(4):
            JDE = __moonPhaseByLunation(lun - LUNATION_OFFSET, phi)
            event_date[phi] = __JDtoDate(JDE)
            if __obtainCurrentPhases(phi, event_date[phi]):
                phases.append((phi, event_date[phi]))
                if len(phases) >= 4:
                    return phases

    return []
    return


