"""
Created on 27 Nov 2022

@author: Rogier van Staveren
"""

PROJECTOR_CONFIGS = {
    "all": {
        "commands": [
            "3d",
            "amxdd",
            "appmod",
            "asp",
            "audiosour",
            "autopower",
            "baud",
            "bc",
            "blank",
            "bri",
            "broadcasting",
            "color",
            "con",
            "ct",
            "directpower",
            "freeze",
            "highaltitude",
            "ins",
            "lampm",
            "lpsaver",
            "ltim",
            "ltim2",
            "macaddr",
            "menu",
            "micvol",
            "modelname",
            "mute",
            "pow",
            "pp",
            "prjlogincode",
            "qas",
            "rr",
            "sharp",
            "sour",
            "standbymic",
            "standbymnt",
            "standbynet",
            "vol",
        ],
        "sources": [
            "dp",
            "dvia",
            "dvid",
            "hdbaset",
            "hdmi",
            "hdmi2",
            "network",
            "rgb",
            "rgb2",
            "rgb3",
            "svid",
            "usbdisplay",
            "usbreader",
            "vid",
            "wireless",
            "ypbr",
            "ypbr2",
        ],
        "poweron_time": 100,
        "poweroff_time": 100,
    },
    "w1110": {
        "commands": [
            "3d",
            "appmod",
            "asp",
            "baud",
            "bc",
            "blank",
            "bri",
            "color",
            "con",
            "ct",
            "directpower",
            "highaltitude",
            "lampm",
            "ltim",
            "modelname",
            "mute",
            "pow",
            "pp",
            "qas",
            "sharp",
            "sour",
            "vol",
        ],
        "sources": [
            "hdmi",
            "hdmi2",
            "rgb",
            "vid",
            "ypbr",
        ],
        "poweron_time": 100,
        "poweroff_time": 100,
    },
}

BAUD_RATES = [2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200]

POSITIONS = {
    "ft": "front_table",
    "re": "rear_table",
    "rc": "rear_ceiling",
    "fc": "front_ceiling",
}

LAMP_MODES = {
    "lnor": "normal",
    "seco": "smart_eco_image_care",
    "seco2": "smart_eco_lamp_care",
    "seco3": "smart_eco_lumen_care",
    "dualbr": "dual_brightness",
    "dualre": "dual_reliable",
    "single": "single_alternative",
    "singleeco": "single_alternative_eco",
}

PICTURE_MODES = {
    "cine": "cinema",
    "std": "standard",
    "threed": "3d",
}
