
#The power of the string is the maximum length of a non-empty substring that contains only one unique character.

#Given a string s, return the power of s.

#my notes ------------------------------------------------------------------------

#loop through each character

#keep track of current longest character - start at 0

class Solution:
    def maxPower(self, s: str) -> int:

        current_letter = ''

        previous_letter = ''

        max_letter_counter = 0

        letter_counter = 0

        for element in s:

            current_letter = element
            print("current_letter is " + current_letter)
            print("previous_letter is " + previous_letter)

            print("the current letter count is " + str(letter_counter))


            if(not previous_letter):
                #this lets me know we are at the start and should not compare
                previous_letter = current_letter
                letter_counter = letter_counter + 1
                max_letter_counter = 1
            elif(current_letter != previous_letter):
                #letter is different, end current count and compare to max count
                previous_letter = current_letter
                if(letter_counter > max_letter_counter):
                    max_letter_counter = letter_counter
                letter_counter = 1
            elif(current_letter == previous_letter):
                previous_letter = current_letter
                letter_counter = letter_counter + 1
                if(letter_counter > max_letter_counter):
                    max_letter_counter = letter_counter

        return max_letter_counter
