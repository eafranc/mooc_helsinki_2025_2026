# Write your solution here

def is_it_valid(pic: str):
    """
    Finnish PICs follow the format ddmmyyXyyyz, where: 
    - ddmmyy contains the date of birth,
    - X is the marker for century,
    - yyy is the personal identifier
    - z is a control character.
    
    The program should check the validity by these three criteria:
    - The first half of the code is a valid, existing date in the format ddmmyy.
    - The century marker is either + (1800s), - (1900s) or A (2000s).
    - The control character is valid.
    
    The control character is calculated by taking the nine-digit number
    created by the date of birth and the personal identifier, dividing this by 31,
    and selecting the character at the index specified by the remainder from the
    string 0123456789ABCDEFHJKLMNPRSTUVWXY. For example, if the remainder was 12,
    the control character would be C.
    """
    from datetime import datetime
    try:
        pic_day                 = int(pic[0:2])
        pic_month               = int(pic[2:4])
        pic_year                = int(pic[4:6])
        pic_century_marker      = pic[6]
        pic_personal_identifier = pic[7:10]
        pic_control_character   = pic[10]
        check_control_char      = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    except:
        return False # Function will return False if the chars which are supposed to be digits aren't so
    if len(pic) != 11:
        return False
    if pic_century_marker not in "+-A":
        return False
    else:
        if   pic_century_marker == "+":
            pic_year += 1800
        elif pic_century_marker == "-":
            pic_year += 1900
        elif pic_century_marker == "A":
            pic_year += 2000
    try:
        birth_date = datetime(pic_year, pic_month, pic_day)
    except:
        return False
    birth_date_and_personal_identifier = int(pic[0:6] + str(pic_personal_identifier))
    if check_control_char[birth_date_and_personal_identifier % 31] != pic_control_character:
        return False
    return True

if __name__ == "__main__":
    print(is_it_valid("230827-906F"))
    print(is_it_valid("120488+246L"))
    print(is_it_valid("310823A9877"))
# Valid PICs:
# - 230827-906F
# - 120488+246L
# - 310823A9877
