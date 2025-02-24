import random

ns = [
    14,
    404,
    635,
    710,
    449,
    369,
    59,
    470,
    814,
    5855,
    66,
    575,
    280,
    182,
    4649,
    768,
    488,
    20,
    14,
    66,
    994,
    583,
    750,
    84,
    7864,
    159,
    16,
    905,
    752,
    476,
    264,
    34,
    610,
    378,
    886,
    893,
    56,
    599,
    75,
    345,
    97,
    925,
    942,
    478,
    3932,
    989,
    44,
    809,
    704,
    255,
    929,
    144,
    149,
    626,
    94,
    854,
    569,
    993,
    991,
    535,
    843,
    833,
    917,
    83,
    30,
    27,
    194,
    40,
    124,
    45,
    167,
    512,
    545,
    915,
    310,
    34,
    8922,
    227,
    279,
    679,
    25,
    701,
    617,
    796,
    957,
    99,
    691,
    61,
    10,
    978,
    574,
    826,
    9705,
    13,
    15,
    702,
    870,
    30,
    2461,
    219,
]


def get_question():  # this will just ask the user to change the base of a number from decimal to binary
    n = random.choice(ns)
    return {
        "type": 0,
        "question": f"Convert {n} to binary.",
        "answer": bin(n)[2:]
    }
