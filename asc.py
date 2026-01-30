def generate_precise_ascii():
    height = 37
    width = 80
    
    for row in range(height):
        for column in range(width):
            char = ' ' 
            
            if row == 1:
                if 0 <= column <= 10: char = "#"
                elif column == 11: char = "+"
                elif column == 12: char = "-"
                elif 66<= column <= 80: char = "#"
                elif column == 65: char = "-"
            elif row == 2:
                if 0 <= column <= 11: char = "#"
                elif column == 12: char = "-"
                elif column == 13: char = ":"
                elif 26 <= column <= 28: char = ":"
                elif column == 68: char = "-"
                elif 69 <= column <= 80: char = "#"
            elif row == 3:
                if 0 <= column <= 10: char = "#"
                elif column == 11: char = "+"
                elif column == 12: char = "-"
                elif column == 16: char = ":"
                elif column == 24: char = ":"
                elif column == 53: char = ":"
                elif column == 74: char = "-"
                elif 70 <= column <= 81: char = "#"
            elif row == 4:
                if 0 <= column <= 10: char = "#"
                elif column == 11: char = "+"
                elif 23 <= column <= 24: char = ":"
                elif 28<= column <= 30: char = ":"
                elif 30 <= column <= 33: char = "-"
                elif 38<= column <= 40: char = ":"
                elif column == 47: char = ":"
                elif 71 <= column <= 81: char = "#"
            elif row == 5:
                if 0 <= column <= 10:
                    char = "#"
                elif column == 11:
                    char = "-"
                elif 15 <= column <= 17:
                    char = ":"
                elif 21 <= column <= 22:
                    char = ":"
                elif column == 23:
                    char = "-"
                elif 24 <= column <= 27:
                    char = "*"
                elif 28 <= column <= 38:
                    char = "#"
                elif 39 <= column <= 40:
                    char = "="
                elif column == 41:
                    char = ":"
                elif 46 <= column <= 49:
                    char = ":"
                elif 50 <= column <= 57:
                    char = "-"
                elif 70 <= column <= 80:
                    char = "#"
           

            elif row == 5:
                if 0 <= column <= 10: char = "#"
                elif column == 11: char = "-"
                elif 15 <= column <= 17: char = ":"
                elif 21 <= column <= 22: char = ":"
                elif column == 23: char = "-"
                elif 24 <= column <= 27: char = "*"
                elif 28 <= column <= 38: char = "#"
                elif 39 <= column <= 40: char = "="
                elif column == 41: char = ":"
                elif 46 <= column <= 49: char = ":"
                elif 50 <= column <= 57: char = "-"
                elif 70 <= column <= 81: char = "#" 
             
            elif row == 6:
                if 0 <= column <= 9:
                    char = "#"
                elif column == 10:
                    char = "="
                elif column == 11:
                    char = ":"
                elif 14 <= column <= 16:
                    char = ":"
                elif 20 <= column <= 21:
                    char = ":"
                elif column == 22:
                    char = "-"
                elif 23 <= column <= 42:
                    char = "#"
                elif 43 <= column <= 44:
                    char = "+"
                elif 45 <= column <= 54:
                    char = "="
                elif 55 <= column <= 59:
                    char = "-"
                elif 72 <= column <= 80:
                    char = "#"

            elif row == 7:
                if 0 <= column <= 9:
                    char = "#"
                elif column == 10:
                    char = "-"
                elif 11 <= column <= 12:
                    char = ":"
                elif 17 <= column <= 19:
                    char = ":"
                elif column == 20:
                    char = "="
                elif 21 <= column <= 45:
                    char = "#"
                elif column == 46:
                    char = "="
                elif column == 47:
                    char = "+"
                elif 48 <= column <= 54:
                    char = "="
                elif column == 55:
                    char = "-"
                elif column == 56:
                    char = "="
                elif 57 <= column <= 59:
                    char = "-"
                elif 71 <= column <= 80:
                    char = "#"

            elif row == 8:
                if 0 <= column <= 9:
                    char = "#"
                elif column == 10:
                    char = "-"
                elif 11 <= column <= 12:
                    char = ":"
                elif 19 <= column <= 20:
                    char = "="
                elif 21 <= column <= 45:
                    char = "#"
                elif 46 <= column <= 50:
                    char = "+"
                elif 51 <= column <= 56:
                    char = "="
                elif 57 <= column <= 60:
                    char = "-"
                elif 69 <= column <= 70:
                    char = ":"
                elif column == 71:
                    char = "+"
                elif 72 <= column <= 80:
                    char = "#"

            elif row == 9:
                if 0 <= column <= 9:
                    char = "#"
                elif column == 10:
                    char = "*"
                elif 18 <= column <= 19:
                    char = "="
                elif 20 <= column <= 44:
                    char = "#"
                elif 45 <= column <= 47:
                    char = "+"
                elif 48 <= column <= 57:
                    char = "="
                elif 58 <= column <= 60:
                    char = "-"
                elif 69 <= column <= 70:
                    char = ":"
                elif column == 71:
                    char = "#"
                elif 72 <= column <= 73:
                    char = "+"
                elif 74 <= column <= 80:
                    char = "#"

            elif row == 10:
                if 0 <= column <= 10:
                    char = "#"
                elif column == 11:
                    char = ":"
                elif column == 19:
                    char = "="
                elif 20 <= column <= 47:
                    char = "#"
                elif 48 <= column <= 49:
                    char = "+"
                elif 50 <= column <= 55:
                    char = "="
                elif column == 56:
                    char = "-"
                elif column == 57:
                    char = "="
                elif 58 <= column <= 60:
                    char = "-"
                elif 70 <= column <= 71:
                    char = "+"
                elif 72 <= column <= 80:
                    char = "#"

            elif row == 11:
                if 0 <= column <= 10:
                    char = "#"
                elif column == 11:
                    char = ":"
                elif column == 19:
                    char = ":"
                elif column == 20:
                    char = "+"
                elif 21 <= column <= 48:
                    char = "#"
                elif 49 <= column <= 54:
                    char = "="
                elif 55 <= column <= 60:
                    char = "-"
                elif 72 <= column <= 80:
                    char = "#"

            elif row == 12:
                if 0 <= column <= 9:
                    char = "#"
                elif column == 10:
                    char = "="
                elif 11 <= column <= 13:
                    char = ":"
                elif 20 <= column <= 49:
                    char = "#"
                elif 50 <= column <= 51:
                    char = "+"
                elif 52 <= column <= 59:
                    char = "="
                elif column == 60:
                    char = "-"
                elif column == 70:
                    char = ":"
                elif 72 <= column <= 73:
                    char = "#"
                elif column == 74:
                    char = "+"
                elif 75 <= column <= 80:
                    char = "#"   
            
            elif row == 13:
                if 0 <= column <= 10: char = "#"
                elif column == 11: char = "="
                elif 12 <= column <= 15: char = ":"
                elif 19 <= column <= 20: char = ":"
                elif 21 <= column <= 48: char = "#"
                elif 49 <= column <= 61: char = "="
                elif 72 <= column <= 80: char = "#"

            elif row == 14:
                if 0 <= column <= 12: 
                    char = "#"
                elif 13 <= column <= 16: char = ":"
                elif column == 19: char = "="
                elif 20 <= column <= 24: char = "#"
                elif 25 <= column <= 26: char = "+"
                elif 27 <= column <= 44: char = "#"
                elif column == 45: char = "+"
                elif 46 <= column <= 61: char = "="
                elif 72 <= column <= 80: char = "#"

            elif row == 15:
                if 0 <= column <= 12: char = "#"
                elif 13 <= column <= 14: char = "="
                elif column == 15: char = ":"
                elif column == 18: char = ":"
                elif 19 <= column <= 21:
                    char = "#"
                elif 22 <= column <= 23: char = "="
                elif 24 <= column <= 28: char = "-"
                elif 29 <= column <= 32: char = "."
                elif 33 <= column <= 35: char = "-"
                elif 36 <= column <= 41: char = "="
                elif column == 42: char = "+"
                elif 43 <= column <= 49: char = "="
                elif 50 <= column <= 52: char = ":"
                elif 53 <= column <= 60: char = "."
                elif 61 <= column <= 62: char = "="
                elif 68 <= column <= 70: char = "-"
                elif 71 <= column <= 80: char = "#"

            elif row == 16:
                if 0 <= column <= 11: char = "#"
                elif 12 <= column <= 15: char = "="
                elif 18 <= column <= 23:
                    char = "#"
                elif column == 24: char = "="
                elif 25 <= column <= 27: char = "-"
                elif 28 <= column <= 36: char = "."
                elif column == 37: char = ":"
                elif 38 <= column <= 43: char = "="
                elif 44 <= column <= 56: char = "."
                elif 57 <= column <= 63: char = "="
                elif 66 <= column <= 68: char = ":"
                elif column == 66: char = ":"
                elif column == 67: char = "="
                elif column == 68: char = ":"
                elif column == 69: char = ":"


                elif 70 <= column <= 80: char = "#"

            
            elif row == 17:
                if 0 <= column <= 11:
                    char = "#"
                elif column == 12:
                    char = ":"
                elif column == 13:
                    char = "="
                elif 14 <= column <= 15:
                    char = "#"
                elif 16 <= column <= 17:
                    char = "-"
                elif 18 <= column <= 23:
                    char = "#"
                elif column == 24:
                    char = "="
                elif 25 <= column <= 27:
                    char = "-"
                elif column == 28:
                    char = "+"
                elif 29 <= column <= 31:
                    char = "."
                elif 32 <= column <= 34:
                    char = "-"
                elif 35 <= column <= 36:
                    char = "."
                elif 35 <= column <= 36:

                    char = "-"
                elif 38 <= column <= 39:
                    char = "="
                elif 40 <= column <= 42:
                    char = "#"
                elif 43 <= column <= 44:
                    char = "="
                elif 45 <= column <= 58:

                    char = "."
                elif 58 <= column <= 63:
                    char = "="
                elif column == 66:
                    char = ":"
                elif 67 <= column <= 68:
                    char = "="


                elif 69 <= column <= 80:
                    char = "#"

           
            elif row == 18:
                if 0 <= column <= 11: char = "#"
                elif column == 12: char = ":"
                elif column == 13: char = "="
                elif column == 14: char = "#"
                elif column == 15: char = "+"
                elif column == 16: char = "-"
                elif column == 17: char = ":"
                elif 18 <= column <= 27: char = "#"
                elif column == 28: char = "+"
                elif 29 <= column <= 35: char = "-"
                elif 36 <= column <= 42: char = "#"
                elif 43 <= column <= 48: char = "="
                elif column == 49: char = ":"
                elif 50 <= column <= 52: char = "."
                elif column == 53: char = ":"
                elif 54 <= column <= 63: char = "="
                elif column == 64: char = ":"
                elif column == 66: char = ":"

                elif 67 <= column <= 68: char = "="
                elif 69 <= column <= 80: char = "#"

            elif row == 19:
                if 0 <= column <= 11: char = "#"
                elif column == 12: char = "*"
                elif column == 13: char = "="
                elif column == 14: char = "#"
                elif column == 15: char = "+"
                elif 16 <= column <= 17: char = "-"
                elif 18 <= column <= 28: char = "#"
                elif 29 <= column <= 34: char = "+"
                elif 35 <= column <= 42: char = "#"
                elif 43 <= column <= 62: char = "="
                elif 63 <= column <= 64: char = ":"
                elif 65 <= column <= 68: char = "="
                elif 69 <= column <= 80: char = "#"

            elif row == 20:
                if 0 <= column <= 16: char = "#"
                elif 17 <= column <= 18: char = "+"
                elif 19 <= column <= 42: char = "#"
                elif 43 <= column <= 48: char = "="
                elif 49 <= column <= 52: char = "+"
                elif 53 <= column <= 62: char = "="
                elif column == 63: char = ":"
                elif 64 <= column <= 66: char = "="
                elif column == 67: char = "+"
                elif 68 <= column <= 80: char = "#"

            elif row == 21:
                if 0 <= column <= 17: char = "#"
                elif column == 18: char = "+"
                elif 19 <= column <= 41: char = "#"
                elif column == 42: char = "+"
                elif 43 <= column <= 50: char = "="
                elif 51 <= column <= 52: char = "+"
                elif column == 53: char = "="
                elif column == 54: char = "+"
                elif 55 <= column <= 65: char = "="
                elif 66 <= column <= 80: char = "#"

           
            elif row == 22:
                if 0 <= column <= 14: char = "#"
                elif 15 <= column <= 16: char = "*"
                elif 17 <= column <= 41: char = "#"
                elif column == 42: char = "+"
                elif 43 <= column <= 66: char = "="
                elif column == 67: char = "+"
                elif 68 <= column <= 80: char = "#"

            elif row == 23:
                if 0 <= column <= 13: char = "#"
                elif column == 14: char = "*"
                elif column == 15: char = "="
                elif column == 16: char = "."
                elif column == 17: char = "-"
                elif column == 18: char = "="
                elif 19 <= column <= 42: char = "#"
                elif 43 <= column <= 62: char = "="
                elif 63 <= column <= 66: char = "."
                elif 67 <= column <= 80: char = "#"

            elif row == 24:
                if 0 <= column <= 15: char = "#"
                elif column == 16: char = "-"
                elif 17 <= column <= 18: char = "."
                elif 19 <= column <= 39: char = "#"
                elif 40 <= column <= 41: char = "="
                elif column == 42: char = "+"
                elif 43 <= column <= 62: char = "="
                elif 63 <= column <= 64: char = "."
                elif column == 65: char = "-"
                elif column == 66: char = "+"
                elif 67 <= column <= 80: char = "#"

            elif row == 25:
                if 0 <= column <= 17: char = "#"
                elif 18 <= column <= 19: char = "+"
                elif 20 <= column <= 36: char = "#"
                elif 37 <= column <= 40: char = "+"
                elif column == 41: char = "="
                elif column == 42: char = ":"
                elif column == 43: char = "="
                elif 44 <= column <= 47: char = ":"
                elif 48 <= column <= 64: char = "="
                elif 65 <= column <= 80: char = "#"

            elif row == 26:
                if 0 <= column <= 38: char = "#"
                elif 39 <= column <= 43: char = "="
                elif 44 <= column <= 45: char = ":"
                elif 46 <= column <= 62: char = "="
                elif 63 <= column <= 80: char = "#"
            elif row == 27:
                if 0 <= column <= 19: char = "#"
                elif column == 20: char = "+"
                elif 21 <= column <= 35: char = "#"
                elif 36 <= column <= 37: char = "+"
                elif 38 <= column <= 39: char = "="
                elif 40 <= column <= 41: char = ":"
                elif 42 <= column <= 61: char = "="
                elif 62 <= column <= 80: char = "#"

            elif row == 28:
                if 0 <= column <= 18: char = "#"
                elif column == 19: char = "*"
                elif column == 20: char = "-"
                elif 21 <= column <= 29: char = "#"
                elif 30 <= column <= 33: char = "+"
                elif 34 <= column <= 37: char = "#"
                elif column == 38: char = "+"
                elif 39 <= column <= 49: char = "="
                elif 50 <= column <= 53: char = ":"
                elif 54 <= column <= 62: char = "="
                elif 63 <= column <= 80: char = "#"

            elif row == 29:
                if 0 <= column <= 18: char = "#"
                elif 19 <= column <= 20: char = "-"
                elif 21 <= column <= 29: char = "#"
                elif 30 <= column <= 31: char = "+"
                elif 32 <= column <= 35: char = "-"
                elif 36 <= column <= 47: char = "."
                elif 48 <= column <= 52: char = ":"
                elif 53 <= column <= 62: char = "="
                elif 63 <= column <= 80: char = "#"
                
            elif row == 30:
                if 0 <= column <= 17: 
                    char = "#"
                elif column == 18: 
                    char = "="
                elif column == 19: 
                    char = "-"
                elif column == 20: 
                    char = ":"
                elif 21 <= column <= 22: 
                    char = "#"
                elif column == 23: 
                    char = "+"
                elif 24 <= column <= 29: 
                    char = "#"
                elif 30 <= column <= 31: 
                    char = "+"
                elif 32 <= column <= 37: 
                    char = "#"
                elif 38 <= column <= 57: 
                    char = "="
                elif 58 <= column <= 59: 
                    char = ":"
                elif 60 <= column <= 64: 
                    char = "="
                elif column == 65: 
                    char = "+"
                elif 66 <= column <= 80: 
                    char = "#"

            elif row == 31:
                if 0 <= column <= 16: char = "#"
                elif column == 17: char = "*"
                elif column == 18: char = "="
                elif column == 19: char = "-"
                elif column == 20: char = ":"
                elif 21 <= column <= 23: char = "#"
                elif column == 24: char = "-"
                elif 25 <= column <= 36: char = "#"
                elif 37 <= column <= 52: char = "="
                elif 53 <= column <= 54: char = ":"
                elif 55 <= column <= 60: char = "="
                elif column == 61: char = "+"
                elif 62 <= column <= 65: char = "="
                elif column == 66: char = ":"
                elif 67 <= column <= 69: char = "="
                elif 70 <= column <= 80: char = "#"

            elif row == 32:
                if 0 <= column <= 16: char = "#"
                elif 17 <= column <= 18: char = "="
                elif 19 <= column <= 20: char = ":"
                elif 21 <= column <= 24: char = "#"
                elif 25 <= column <= 27: char = "="
                elif 28 <= column <= 35: char = "#"
                elif 36 <= column <= 39: char = "="
                elif 40 <= column <= 44: char = ":"
                elif 45 <= column <= 51: char = "="
                elif 52 <= column <= 57: char = ":"
                elif 58 <= column <= 74: char = "="
                elif 75 <= column <= 80: char = "#"
            elif row == 33:
                if 0 <= column <= 16: char = "#"
                elif column == 17: char = "="
                elif column == 18: char = "-"
                elif 19 <= column <= 20: char = ":"
                elif 21 <= column <= 25: char = "#"
                elif 26 <= column <= 29: char = "="
                elif 30 <= column <= 39: char = "#"
                elif column == 40: char = "="
                elif column == 41: char = "+"
                elif 42 <= column <= 51: char = "="
                elif 52 <= column <= 56: char = ":"
                elif 57 <= column <= 78: char = "="
                elif 79 <= column <= 80: char = "#"

            elif row == 34:
                if 0 <= column <= 16: char = "#"
                elif column == 17: char = "="
                elif 18 <= column <= 19: char = "-"
                elif column == 20: char = ":"
                elif column == 21: char = "-"
                elif 23 <= column <= 28: char = "#"
                elif column == 29: char = "+"
                elif 30 <= column <= 32: char = "="
                elif 33 <= column <= 38: char = "#"
                elif 39 <= column <= 41: char = "="
                elif 42 <= column <= 44: char = "+"
                elif 45 <= column <= 50: char = "="
                elif 51 <= column <= 57: char = ":"
                elif 58 <= column <= 65: char = "="
                elif column == 66: char = "+"
                elif 67 <= column <= 80: char = "="

            elif row == 35:
                if 0 <= column <= 16:
                    char = "#"
                elif 17 <= column <= 18:
                    char = "="
                elif 19 <= column <= 21:
                    char = "-"
                elif 22 <= column <= 29:
                    char = "#"
                elif 30 <= column <= 33:
                    char = "="
                elif column == 34:
                    char = "+"
                elif column == 35:
                    char = "#"
                elif column == 36:
                    char = "+"
                elif 37 <= column <= 46:
                    char = "="
                elif 47 <= column <= 53:
                    char = ":"
                elif column == 54:
                    char = "."
                elif column == 55:
                    char = ":"
                elif 56 <= column <= 60:
                    char = "="
                elif column == 61:
                    char = "+"
                elif column == 62:
                    char = "="
                elif column == 63:
                    char = "+"
                elif 65 <= column <= 80:
                    char = "="

            elif row == 36:
                if 0 <= column <= 16: char = "#"
                elif 17 <= column <= 18: char = "="
                elif 19 <= column <= 20: char = "-"
                elif column == 21: char = "."
                elif 22 <= column <= 32: char = "#"
                elif 33 <= column <= 38: char = "="
                elif 39 <= column <= 49: char = ":"
                elif 50 <= column <= 52: char = "="
                elif column == 53: char = ":"
                elif column == 54: char = "."
                elif column == 55: char = ":"
                elif 56 <= column <= 80: char = "="

            elif row == 37:
                if 0 <= column <= 15: char = "#"
                elif column == 16: char = "*"
                elif 17 <= column <= 19: char = "="
                elif 20 <= column <= 21: char = ".."
                elif column == 22: char = ":"
                elif 23 <= column <= 34: char = "#"
                elif 35 <= column <= 38: char = "="
                elif 39 <= column <= 40: char = "::"
                elif column == 41: char = "="
                elif 42 <= column <= 43: char = "::"
                elif 44 <= column <= 51: char = "="
                elif 52 <= column <= 54: char = "."
                elif 55 <= column <= 57: char = "="
                elif column == 58: char = "+"
                elif 59 <= column <= 68: char = "="
                elif column == 69: char = ":"
                elif 70 <= column <= 80: char = "="
          

            print(char, end='')
        print()

generate_precise_ascii()