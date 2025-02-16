import time

def display_intro():
    sleep_time = 1
    print(r"""
                                  88         
                                  88         
                                  88         
8b,dPPYba,  ,adPPYba,   ,adPPYba, 88   ,d8   
88P'   "Y8 a8"     "8a a8"     "" 88 ,a8"    
88         8b       d8 8b         8888[      
88         "8a,   ,a8" "8a,   ,aa 88`"Yba,   
88          `"YbbdP"'   `"Ybbd8"' 88   `Y8a  
                                             
    """)
    time.sleep(sleep_time)
    paper = (
        "8b,dPPYba,  ,adPPYYba, 8b,dPPYba,   ,adPPYba, 8b,dPPYba,  \n"
        "88P'    \"8a \"\"     `Y8 88P'    \"8a a8P_____88 88P'   \"Y8  \n"
        "88       d8 ,adPPPPP88 88       d8 8PP\"\"\"\"\"\"\" 88          \n"
        "88b,   ,a8\" 88,    ,88 88b,   ,a8\" \"8b,   ,aa 88          \n"
        "88`YbbdP\"'  `\"8bbdP\"Y8 88`YbbdP\"'   `\"Ybbd8\"' 88          \n"
        "88                     88                                 \n"
        "88                     88                                 \n"
    )
    print(paper)
    time.sleep(sleep_time)
    ascii_art = (
        "                     88                                                       \n"
        "                     \"\"                                                       \n"
        "                                                                              \n"
        ",adPPYba,  ,adPPYba, 88 ,adPPYba, ,adPPYba,  ,adPPYba,  8b,dPPYba, ,adPPYba,  \n"
        "I8[    \"\" a8\"     \"\" 88 I8[    \"\" I8[    \"\" a8\"     \"8a 88P'   \"Y8 I8[    \"\"  \n"
        " `\"Y8ba,  8b         88  `\"Y8ba,   `\"Y8ba,  8b       d8 88          `\"Y8ba,   \n"
        "aa    ]8I \"8a,   ,aa 88 aa    ]8I aa    ]8I \"8a,   ,a8\" 88         aa    ]8I  \n"
        "`\"YbbdP\"'  `\"Ybbd8\"' 88 `\"YbbdP\"' `\"YbbdP\"'  `\"YbbdP\"'  88         `\"YbbdP\"'  \n"
        "                                                                              \n"
    )
    print(ascii_art)
    time.sleep(sleep_time)
