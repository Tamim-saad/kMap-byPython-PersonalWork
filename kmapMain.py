import time
import pygame

# start = time.time()
txtArr = [0, 1, 3, 2, 4, 5, 7, 6, 12, 13, 15, 14, 8, 9, 11, 10]
middle = [0] * 16

x = 120
y = 120
d = 1
gap = 150


def permut_size_4(ans):
    permut_4 = []

    permut_4.append(str(ans[3] + ans[1] + ans[0] + ans[2]))
    permut_4.append(str(ans[3] + ans[1] + ans[2] + ans[0]))
    permut_4.append(str(ans[3] + ans[0] + ans[1] + ans[2]))
    permut_4.append(str(ans[3] + ans[2] + ans[1] + ans[0]))
    permut_4.append(str(ans[3] + ans[0] + ans[2] + ans[1]))
    permut_4.append(str(ans[3] + ans[2] + ans[0] + ans[1]))

    permut_4.append(str(ans[1] + ans[3] + ans[0] + ans[2]))
    permut_4.append(str(ans[1] + ans[3] + ans[2] + ans[0]))
    permut_4.append(str(ans[0] + ans[3] + ans[1] + ans[2]))
    permut_4.append(str(ans[2] + ans[3] + ans[1] + ans[0]))
    permut_4.append(str(ans[0] + ans[3] + ans[2] + ans[1]))
    permut_4.append(str(ans[2] + ans[3] + ans[0] + ans[1]))

    permut_4.append(str(ans[1] + ans[0] + ans[3] + ans[2]))
    permut_4.append(str(ans[1] + ans[2] + ans[3] + ans[0]))
    permut_4.append(str(ans[0] + ans[1] + ans[3] + ans[2]))
    permut_4.append(str(ans[2] + ans[1] + ans[3] + ans[0]))
    permut_4.append(str(ans[0] + ans[2] + ans[3] + ans[1]))
    permut_4.append(str(ans[2] + ans[0] + ans[3] + ans[1]))

    permut_4.append(str(ans[1] + ans[0] + ans[2] + ans[3]))
    permut_4.append(str(ans[1] + ans[2] + ans[0] + ans[3]))
    permut_4.append(str(ans[0] + ans[1] + ans[2] + ans[3]))
    permut_4.append(str(ans[2] + ans[1] + ans[0] + ans[3]))
    permut_4.append(str(ans[0] + ans[2] + ans[1] + ans[3]))
    permut_4.append(str(ans[2] + ans[0] + ans[1] + ans[3]))
    return permut_4


def include_size1(middle):
    size1 = ["abcd", "abcD", "abCD", "abCd", "aBcd", "aBcD", "aBCD", "aBCd",
             "ABcd", "ABcD", "ABCD", "ABCd", "Abcd", "AbcD", "AbCD", "AbCd"]
    must_of_size1 = []
    i = 0
    while i < 16:
        if i == 0 and middle[i] == 1 and middle[i + 1] == 0 and middle[i + 4] == 0 and middle[i + 12] == 0 and middle[
            i + 3] == 0:
            must_of_size1.append(size1[i])
        elif i == 12 and middle[i] == 1 and middle[i + 1] == 0 and middle[i - 4] == 0 and middle[i - 12] == 0 and \
                middle[i + 3] == 0:
            must_of_size1.append(size1[i])
        elif i == 3 and middle[i] == 1 and middle[i - 1] == 0 and middle[i + 4] == 0 and middle[i + 12] == 0 and middle[
            i - 3] == 0:
            must_of_size1.append(size1[i])
        elif i == 15 and middle[i] == 1 and middle[i - 1] == 0 and middle[i - 4] == 0 and middle[i - 12] == 0 and \
                middle[i - 3] == 0:
            must_of_size1.append(size1[i])

        elif (i % 4 == 0):
            if middle[i] == 1 and middle[i + 1] == 0 and middle[i + 3] == 0 and middle[i - 4] == 0 and middle[
                i + 4] == 0:
                must_of_size1.append(size1[i])
        elif ((i + 1) % 4 == 0):
            if middle[i] == 1 and middle[i - 1] == 0 and middle[i - 3] == 0 and middle[i - 4] == 0 and middle[
                i + 4] == 0:
                must_of_size1.append(size1[i])
        elif (i < 4):
            if middle[i] == 1 and middle[i - 1] == 0 and middle[i + 1] == 0 and middle[i + 4] == 0 and middle[
                i + 12] == 0:
                must_of_size1.append(size1[i])
        elif (i == 13 or i == 14):
            if middle[i] == 1 and middle[i - 1] == 0 and middle[i + 1] == 0 and middle[i - 4] == 0 and middle[
                i - 12] == 0:
                must_of_size1.append(size1[i])
        else:
            if middle[i] == 1 and middle[i - 1] == 0 and middle[i + 1] == 0 and middle[i - 4] == 0 and middle[
                i + 4] == 0:
                must_of_size1.append(size1[i])
        i += 1

    return must_of_size1


def get_minterm(middle):
    minterm = [0] * 16

    if (middle[0] == 1): minterm[0] = 1
    if (middle[1] == 1): minterm[1] = 1
    if (middle[2] == 1): minterm[3] = 1
    if (middle[3] == 1): minterm[2] = 1

    if (middle[4] == 1): minterm[4] = 1
    if (middle[5] == 1): minterm[5] = 1
    if (middle[6] == 1): minterm[7] = 1
    if (middle[7] == 1): minterm[6] = 1

    if (middle[8] == 1): minterm[12] = 1
    if (middle[9] == 1): minterm[13] = 1
    if (middle[10] == 1): minterm[14] = 1
    if (middle[11] == 1): minterm[15] = 1

    if (middle[12] == 1): minterm[8] = 1
    if (middle[13] == 1): minterm[9] = 1
    if (middle[14] == 1): minterm[11] = 1
    if (middle[15] == 1): minterm[10] = 1

    # ------------------------------------------------------
    if (middle[0] == -1): minterm[0] = -1
    if (middle[1] == -1): minterm[1] = -1
    if (middle[2] == -1): minterm[3] = -1
    if (middle[3] == -1): minterm[2] = -1

    if (middle[4] == -1): minterm[4] = -1
    if (middle[5] == -1): minterm[5] = -1
    if (middle[6] == -1): minterm[7] = -1
    if (middle[7] == -1): minterm[6] = -1

    if (middle[8] == -1): minterm[12] = -1
    if (middle[9] == -1): minterm[13] = -1
    if (middle[10] == -1): minterm[14] = -1
    if (middle[11] == -1): minterm[15] = -1

    if (middle[12] == -1): minterm[8] = -1
    if (middle[13] == -1): minterm[9] = -1
    if (middle[14] == -1): minterm[11] = -1
    if (middle[15] == -1): minterm[10] = -1

    return minterm


def implicant_reduce(implicant):
    loop = 0
    while loop < 1:
        i = 0
        while i < len(implicant):
            ans = implicant[i]

            checkArr = []
            if len(ans) == 1:
                checkArr.append(ans[0])
            if len(ans) == 2:
                checkArr.append(ans[0] + ans[1])
                checkArr.append(ans[1] + ans[0])
            if len(ans) == 3:
                checkArr.append(str(ans[1] + ans[0] + ans[2]))
                checkArr.append(str(ans[1] + ans[2] + ans[0]))
                checkArr.append(str(ans[0] + ans[1] + ans[2]))
                checkArr.append(str(ans[2] + ans[1] + ans[0]))
                checkArr.append(str(ans[0] + ans[2] + ans[1]))
                checkArr.append(str(ans[2] + ans[0] + ans[1]))

            j = i + 1
            while j < len(implicant):
                tostr = implicant[j]
                x = 0
                while x < len(checkArr):
                    if (checkArr[x] in tostr) == True:
                        implicant.pop(j)
                        break
                    x += 1
                j += 1
            i += 1
        loop += 1

    # -------------------------------2nd phase-------------------------------

    i = 0
    while i < len(implicant) - 1:
        ans = implicant[i]

        # ----------------------------------------------------
        j = i + 1
        while j < len(implicant):
            to = str(implicant[j])
            # -------------------------------------------------
            toCheck = []
            if len(to) == 1:
                toCheck.append(to[0])
            if len(to) == 2:
                toCheck.append(to[0] + to[1])
                toCheck.append(to[1] + to[0])
            if len(to) == 3:
                toCheck.append(str(to[1] + to[0] + to[2]))
                toCheck.append(str(to[1] + to[2] + to[0]))
                toCheck.append(str(to[0] + to[1] + to[2]))
                toCheck.append(str(to[2] + to[1] + to[0]))
                toCheck.append(str(to[0] + to[2] + to[1]))
                toCheck.append(str(to[2] + to[0] + to[1]))
            # -------------------------------------------------
            x = 0
            while x < len(toCheck):
                n = str(toCheck[x])

                if (ans in n) == True:  # and j< len(checkArr):
                    implicant.pop(j)
                    break
                x += 1

            j += 1
        i += 1

    return implicant


def epi_check(to, check):
    len4 = ["abcd", "abcD", "abCd", "abCD", "aBcd", "aBcD", "aBCd", "aBCD",
            "Abcd", "AbcD", "AbCd", "AbCD", "ABcd", "ABcD", "ABCd", "ABCD"]
    i = 0
    final_bool = False
    while i < 16:
        all_list = permut_size_4(len4[i])
        check_bool = False
        to_bool = False

        j = 0
        while j < len(all_list):
            if (check in all_list[j]) == True: check_bool = True
            if (to in all_list[j]) == True: to_bool = True
            j += 1

        if (check_bool == True and to_bool == False):
            final_bool = True

        i += 1
    return final_bool


def dont_care_epi_check(implicant, middle):
    len4 = ["abcd", "abcD", "abCd", "abCD", "aBcd", "aBcD", "aBCd", "aBCD",
            "Abcd", "AbcD", "AbCd", "AbCD", "ABcd", "ABcD", "ABCd", "ABCD"]

    loop = len(implicant) - 1
    while loop >= 0:
        # -------------------------------------------
        temp_list = []
        x = 0
        while x < len(implicant):
            if (loop != x): temp_list.append(implicant[x])
            x += 1

        # --------------------------------------------
        check = implicant[loop]

        combined_rest_minterm = combined_minterm(temp_list)
        current_minterm = covered_minterm(check)
        # -------------------------------------------------
        current_minterm_list = []

        for n in range(16):
            if (current_minterm[n] == 1 and combined_rest_minterm[n] == 0):
                current_minterm_list.append(n)

        real_minterm = get_minterm(middle)

        # for n in range(len(current_minterm_list)):
        flag = False
        for x in range(len(current_minterm_list)):
            # if middle[current_minterm_list[x]]==1:
            if real_minterm[current_minterm_list[x]] == 1:
                # if middle[x]==1:
                flag = True
        if flag == False:
            implicant.pop(loop)
        loop -= 1
        # -------------------------------------------------------
    return implicant


def covered_minterm(check):
    len4 = ["abcd", "abcD", "abCd", "abCD", "aBcd", "aBcD", "aBCd", "aBCD",
            "Abcd", "AbcD", "AbCd", "AbCD", "ABcd", "ABcD", "ABCd", "ABCD"]
    covered = []
    i = 0
    while i < 16:
        all_list = permut_size_4(len4[i])
        check_bool = False

        j = 0
        while j < len(all_list):
            if (check in all_list[j]) == True: check_bool = True
            j += 1

        if (check_bool == True):
            covered.append(1)
        else:
            covered.append(0)
        i += 1

    return covered


def combined_minterm(list):
    final_minterm = [0] * 16
    for i in range(len(list)):
        temp_minterm = covered_minterm(list[i])
        for j in range(16):
            if (temp_minterm[j] == 1 or final_minterm[j] == 1): final_minterm[j] = 1

    return final_minterm


def calculate_result(middle):
    minterm = get_minterm(middle)

    implicant = []

    if (all(middle) != 0):
        implicant.append("1 ")
        return "1 "
    # -------------check horizontal size 8---------------
    if all(middle[0:8]) != 0:
        implicant.append("a")

    if all(middle[8:]) != 0:
        implicant.append("A")

    if all(middle[4:12]) != 0:
        implicant.append("B")

    if (all(middle[0:4]) != 0 and all(middle[12:]) != 0):
        implicant.append("b")

    # -------------check vertical size 8---------------
    if all(middle[0:2]) != 0 and all(middle[4:6]) != 0 and all(middle[8:10]) != 0 and all(middle[12:14]):
        implicant.append("c")

    if all(middle[1:3]) != 0 and all(middle[5:7]) != 0 and all(middle[9:11]) != 0 and all(middle[13:15]):
        implicant.append("D")

    if all(middle[2:4]) != 0 and all(middle[6:8]) != 0 and all(middle[10:12]) != 0 and all(middle[14:]):
        implicant.append("C")

    if all(middle[3:5]) != 0 and all(middle[7:9]) != 0 and all(middle[11:13]) != 0 and middle[15] != 0 and middle[
        0] != 0:
        implicant.append("d")

    # -------------check single line size 4---------------
    size4Manual_hori = ["ab", "aB", "AB", "Ab"]
    size4Manual_verti = ["cd", "cD", "CD", "Cd"]
    i = 0
    while i <= 3:
        if middle[i] != 0 and middle[i + 4] != 0 and middle[i + 8] != 0 and middle[i + 12] != 0:
            implicant.append(size4Manual_verti[i])
        i += 1

    i = 0
    while i <= 12:
        if middle[i] != 0 and middle[i + 1] != 0 and middle[i + 2] != 0 and middle[i + 3] != 0:
            # print(i,'    ',middle)
            implicant.append(size4Manual_hori[i // 4])
        i += 4

    # -------------check square size 4---------------
    size4 = ["ac", "aD", "aC", "ad", "Bc", "BD", "BC", "Bd", "Ac", "AD", "AC", "Ad", "bc",
             "bD", "bC", "bd"]

    i = 0
    while (i < 16):

        if i == 15:
            if middle[0] != 0 and middle[3] != 0 and middle[12] != 0 and middle[15] != 0:
                implicant.append(size4[i])
            i += 1
            continue

        if i >= 12 and i <= 14:
            if middle[i] != 0 and middle[i + 1] != 0 and middle[i - 11] != 0 and middle[i - 12] != 0:
                implicant.append(size4[i])
            i += 1
            continue

        if (i + 1) % 4 == 0:
            if middle[i] != 0 and middle[i - 3] != 0 and middle[i + 1] != 0 and middle[i + 4] != 0:
                implicant.append(size4[i])
            i += 1
            continue

        if middle[i] != 0 and middle[i + 1] != 0 and middle[i + 4] != 0 and middle[i + 5] != 0:
            implicant.append(size4[i])
        i += 1

    # ----------------------check horizontal size 2------------------------
    size2_hori = ["abc", "abD", "abC", "abd", "aBc", "aBD", "aBC", "aBd", "ABc", "ABD", "ABC", "ABd", "Abc", "AbD",
                  "AbC", "Abd"]
    i = 0
    while i < 16:
        if (i + 1) % 4 == 0 and middle[i] != 0 and middle[i - 3] != 0:
            implicant.append(size2_hori[i])
        elif (i + 1) % 4 != 0 and middle[i] != 0 and middle[i + 1] != 0:
            implicant.append(size2_hori[i])
        i += 1

    # ----------------------check vertical size 2------------------------
    size2_verti = ["cda", "cDa", "CDa", "Cda", "cdB", "cDB", "CDB", "CdB", "cdA",
                   "cDA", "CDA", "CdA", "cdb", "cDb", "CDb", "Cdb"]
    i = 0
    while i < 16:
        if i >= 12 and i <= 15 and middle[i] != 0 and middle[i - 12] != 0:
            implicant.append(size2_verti[i])
        if i <= 11 and middle[i] != 0 and middle[i + 4] != 0:
            implicant.append(size2_verti[i])
        i += 1

    # ----------------------check all size 1------------------------
    must_of_size1 = include_size1(middle)

    # ----------------- Determine Prime Implicant--------------------------

    implicant = implicant_reduce(implicant)
    print('PI:----  ', implicant)

    # ----------------- Determine ans--------------------------

    i = len(implicant) - 1
    while i > 0:
        fromstr = implicant[i]
        j = 0
        while j < i:
            tostr = implicant[j]
            if (epi_check(tostr, fromstr)) == False:
                implicant.pop(i)
                break
            j += 1
        i -= 1
    # ---------------------ans 2nd phase-----------------------

    i = len(implicant) - 1
    while i >= 0:
        temp_list = []
        x = 0
        while x < len(implicant):
            if (i != x): temp_list.append(implicant[x])
            x += 1

        if i < 0 or i >= len(implicant): break
        combined_rest_minterm = combined_minterm(temp_list)
        current_minterm = covered_minterm(implicant[i])

        flag = False
        for m in range(16):
            for n in range(16):
                if (current_minterm[n] == 1 and combined_rest_minterm[n] == 0):
                    flag = True
        # print('\n','------------------------------\n',implicant[i],'----',current_minterm,combined_rest_minterm)
        if (flag == False):
            implicant.pop(i)
        i -= 1

    # ---------------------------------------------------------
    implicant = dont_care_epi_check(implicant, middle)
    implicant = implicant + must_of_size1
    print('epi-----  ', implicant)
    return implicant


def beautification(ans):
    final = []
    for x in range(len(ans)):
        fin = ""
        str = ans[x]
        if ('a' in str) == True: fin = fin + "A" + "\'"
        if ('A' in str) == True: fin = fin + "A"
        if ('b' in str) == True: fin = fin + "B" + "\'"
        if ('B' in str) == True: fin = fin + "B"
        if ('c' in str) == True: fin = fin + "C" + "\'"
        if ('C' in str) == True: fin = fin + "C"
        if ('d' in str) == True: fin = fin + "D" + "\'"
        if ('D' in str) == True: fin = fin + "D"
        print(str, '    ', fin)
        final.append(fin)
    return final


# ------------set square coordinate in list formate-----------
imgX = []
i = 1
while (i <= 16):
    if (i % 4 == 1):  imgX.append(x)
    if (i % 4 == 2):  imgX.append(x + gap + d)
    if (i % 4 == 3):  imgX.append(x + 2 * (gap + d))
    if (i % 4 == 0):  imgX.append(x + 3 * (gap + d))
    i += 1

imgY = []
i = 1
while (i <= 16):
    if (i <= 4):            imgY.append(y)
    if (i >= 5 and i <= 8):   imgY.append(y + gap + d)
    if (i >= 9 and i <= 12):  imgY.append(y + 2 * (gap + d))
    if (i >= 13 and i <= 16): imgY.append(y + 3 * (gap + d))
    i += 1

# -----------------declaring variable-----------------
showRresultX = imgX[15] + gap * 2 - 2 * gap / 3
showRresultY = imgY[15] + gap - gap / 3
showresult_box_width = 210
showresult_box_height = 50

variable_scale_X = x
variable_scale_Y = y

upperIndx_X = gap / 2 - 10
upperIndx_Y = gap / 4
lowerIndx_X = -gap / 4 - 5
lowerIndx_Y = -(gap / 2 - 10)


# ---------------------main loop-------------------------

def main():
    pygame.init()
    main_surface = pygame.display.set_mode((800 + 400, 800))
    num_font = pygame.font.SysFont('Courier', 17)
    middle_font = pygame.font.SysFont('Courier', 100)
    result_font = pygame.font.SysFont('Courier', 40)
    text_font = pygame.font.SysFont('Courier', 30)

    variable_img = pygame.image.load("variable_image.png")
    variable_img = pygame.transform.scale(variable_img, (variable_scale_X, variable_scale_Y))
    final = []

    while True:

        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:  break

        # ----------------draw : surface, 16 square & minterm number------------
        main_surface.fill((255, 255, 255))
        # main_surface.fill((250, 250, 250))
        main_surface.blit(variable_img, (2, 2))
        i = 0
        while i < 16:
            pygame.draw.rect(main_surface, (0, 0, 0), pygame.Rect(imgX[i], imgY[i], gap, gap), 2)
            num = num_font.render(str(txtArr[i]), True, (0, 0, 0))
            main_surface.blit(num, (imgX[i] + 125, imgY[i] + 127))
            i += 1
        pygame.draw.rect(main_surface, (0, 0, 0),
                         pygame.Rect(showRresultX, showRresultY, showresult_box_width, showresult_box_height), 2)
        num2 = text_font.render(str('Show Result'), True, (0, 0, 0))
        main_surface.blit(num2, (showRresultX + 5, showRresultY + 5))

        # -----------------upper indexing-----------------------
        num00 = text_font.render(str('00'), True, (0, 0, 0))
        main_surface.blit(num00, (imgX[0] + upperIndx_X, imgY[0] - upperIndx_Y))
        num01 = text_font.render(str('01'), True, (0, 0, 0))
        main_surface.blit(num01, (imgX[1] + upperIndx_X, imgY[1] - upperIndx_Y))
        num11 = text_font.render(str('11'), True, (0, 0, 0))
        main_surface.blit(num11, (imgX[2] + upperIndx_X, imgY[2] - upperIndx_Y))
        num10 = text_font.render(str('10'), True, (0, 0, 0))
        main_surface.blit(num10, (imgX[3] + upperIndx_X, imgY[3] - upperIndx_Y))

        # -----------------left side indexing-----------------------
        main_surface.blit(num00, (imgX[0] + lowerIndx_X, imgY[0] - lowerIndx_Y))
        main_surface.blit(num01, (imgX[4] + lowerIndx_X, imgY[4] - lowerIndx_Y))
        main_surface.blit(num11, (imgX[8] + lowerIndx_X, imgY[8] - lowerIndx_Y))
        main_surface.blit(num10, (imgX[12] + lowerIndx_X, imgY[12] - lowerIndx_Y))

        # ----------------------calculate changing minterm -------------------

        if ev.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x, '   ', y)
            i = 0
            while i < 16:
                if x >= imgX[i] and x <= imgX[i] + gap and y >= imgY[i] and y <= imgY[i] + gap:
                    if middle[i] == 0:
                        middle[i] = 1
                    elif middle[i] == 1:
                        middle[i] = -1
                    elif middle[i] == -1:
                        middle[i] = 0
                    break
                i += 1
            if x >= showRresultX and x <= showRresultX + showresult_box_width and y >= showRresultY and y <= showRresultY + showresult_box_height:
                pre = calculate_result(middle)
                final = beautification(pre)
                print(final)
        # --------------------------------------
        for k in range(len(final)):
            text = str(final[k])
            result_text = result_font.render(text, True, (255, 0, 0))
            main_surface.blit(result_text, (imgX[3] + gap + 70, imgY[0] + gap - 100 + 70 * k))
        # -----------------------draw changed minterm -----------------------
        i = 0
        while i < 16:
            text = str(middle[i])
            if (middle[i] == -1):
                text = str('X')
                mid_text = middle_font.render(text, True, (0, 255, 0))
            elif (middle[i] == 1):
                mid_text = middle_font.render(text, True, (255, 0, 0))
            else : mid_text = middle_font.render(text, True, (0, 0, 0))

            main_surface.blit(mid_text, (imgX[i] + 48, imgY[i] + 27))
            i += 1
        # ------------------------------------------------------

        pygame.display.flip()

    pygame.quit()


main()
