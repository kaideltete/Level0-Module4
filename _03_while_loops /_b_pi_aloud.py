"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math



    # TODO) Place the first 20 digits of pi into a variable as a string
    #  3.1415926535897932384

    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit

    # TODO) Use a while loop to keep asking for the next digit of pi

        # TODO) If they are correct, print "correct".
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    u_score = 0

    q1 = simpledialog.askstring(title='1?',prompt="digit 1")
    q2 = simpledialog.askstring(title='2?',prompt="digit 2")
    q3 = simpledialog.askstring(title='3?',prompt="digit 3")
    q4 = simpledialog.askstring(title='4?',prompt="digit 4")
    q5 = simpledialog.askstring(title='5?',prompt="digit 5")
    q6 = simpledialog.askstring(title='6?',prompt="digit 6")
    q7 = simpledialog.askstring(title='7?',prompt="digit 7")
    q8 = simpledialog.askstring(title='8?',prompt="digit 8")
    q9 = simpledialog.askstring(title='9?',prompt="digit 9")
    q10 = simpledialog.askstring(title='10?',prompt="digit 10")
    q11 = simpledialog.askstring(title='11?',prompt="digit 11")
    q12 = simpledialog.askstring(title='12?',prompt="digit 12")
    q13 = simpledialog.askstring(title='13?',prompt="digit 13")
    q14 = simpledialog.askstring(title='14?',prompt="digit 14")
    q15 = simpledialog.askstring(title='15?',prompt="digit 15")
    q16 = simpledialog.askstring(title='16?',prompt="digit 16")
    q17 = simpledialog.askstring(title='17?',prompt="digit 17")
    q18 = simpledialog.askstring(title='18?',prompt="digit 18")
    q19 = simpledialog.askstring(title='19?',prompt="digit 19")
    q20 = simpledialog.askstring(title='20?',prompt="digit 20")

    if (q1 == "3"):
        u_score += 1
    if (q2 == "1"):
        u_score += 1
    if (q3 == "4"):
        u_score += 1
    if (q4 == "1"):
        u_score += 1
    if (q5 == "5"):
        u_score += 1
    if (q6 == "9"):
        u_score += 1
    if (q7 == "2"):
        u_score += 1
    if (q8 == "6"):
        u_score += 1
    if (q9 == "5"):
        u_score += 1
    if (q10 == "3"):
        u_score += 1
    if (q11 == "5"):
        u_score += 1
    if (q12 == "8"):
        u_score += 1
    if (q13 == "9"):
        u_score += 1
    if (q14 == "7"):
        u_score += 1
    if (q15 == "9"):
        u_score += 1
    if (q16 == "3"):
        u_score += 1
    if (q17 == "2"):
        u_score += 1
    if (q18 == "3"):
        u_score += 1
    if (q19 == "8"):
        u_score += 1
    if (q20 == "8"):
        u_score += 1








        messagebox.showinfo(message=str(u_score))
