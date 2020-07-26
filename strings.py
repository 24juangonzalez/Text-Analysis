# Date - 4/9/20
def textAnalysis(phrase):
#pass a phrase it will print all upper,lower

#digit ,space ,length and other char count
    uppercase = 0
    lowercase = 0
    digit = 0
    space = -0
    otherChar = 0
    length = len(phrase)

    for i in phrase:  # run loop from first element to last
        if i == " ":  # set i equal to space
            space += 1
        elif i.islower():  # if i is lower case add 1
            lowercase += 1
        elif i.isupper():  # if i is upper case add 1
            uppercase += 1
        elif i.isdigit():  # if i digit
            digit += 1
        else:  # else add 1 to special character
         otherChar += 1
# print all count types with 2 spaces.
    print("---Text Analysis---")
    print("Char Type Count")
    print("Upper case %2d" % (uppercase))
    print("Lower case %2d" % (lowercase))
    print("Digit %2d" % (digit))
    print("White Space %2d" % (space))
    print("Other %2d" % (otherChar))
    print("Total %2d" % (length))


def countLetter(char, phrase):
    # convert letters to upper case and lower case
    Upperchar = char.upper()
    Lowerchar = char.lower()
    count = 0
    for i in phrase:  #from start to finish
        if i == Upperchar or i == Lowerchar:  # if upper or lower case count by 1
            count += 1
    return count  # return count


def countWord(word, phrase):  # count word in phrase
    Upperword = word.upper()  # first convert in upper and lower case
    Lowerword = word.lower()
    count = 0
    words = phrase.split()  # split string by space in list
    for i in words:  # run loop in list element
    # if word is equal to uppercase word or lower case ,first convert it
        if i.upper() == Upperword or i.lower() == Lowerword:
            count += 1
    return count


def caseConvert(phrase):
    Phrase = ""
    words = phrase.split()  # split by space and store in list
    for i in words:  # loop
    # if word begin by vowels convert into upper case and store into phrase
        if i[0] == "a" or i[0] == "e" or i[0] == "i" or i[0] == "o" or i[0] == "u":
            Phrase += i.upper()
    # if word begins with upper case convert into uppercase
        elif i[0] == "A" or i[0] == "E" or i[0] == "I" or i[0] == "O" or i[0] == "U":
            Phrase += i.upper()
    # if start by special constants
        elif i[0] == "r" or i[0] == "s" or i[0] == "t" or i[0] == "l" or i[0] == "n":
            Phrase += i.lower()
        elif i[0] == "R" or i[0] == "S" or i[0] == "T" or i[0] == "L" or i[0] == "N":
            Phrase += i.lower()
        else:
    # all other words add to phrase
            Phrase += i

        Phrase += " "
    # and return phrase
    return Phrase

if __name__ == "__main__":
    # enter phrase
    phrase = input("Enter a phrase:")
    textAnalysis(phrase)
    # enter letter
    letter = input("Enter a letter to find in your phrase:")[0]
    print("The letter \"", letter, "\" occurs ", countLetter(letter, phrase), " time(s).")
    # enter word
    word = input("Enter a word to find in your phrase:")

    print("The word \"", word, "\" occurs ", countWord(word, phrase), " time(s).")
    # convert vowel and special constants
    print("phrase is ", caseConvert(phrase))
