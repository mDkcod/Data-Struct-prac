# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def number_to_words(num):
    if num == 0:
        return "Zero"

    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                "Nineteen"]

    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Million", "Billion"]

    def word(num):
        if num == 0:
            return ""
        elif num < 20:
            return below_20[num] + " "
        elif num < 100:
            return tens[num // 10] + " " + below_20[num % 10] + " "
        else:
            return below_20[num // 100] + " Hundred " + word(num % 100)

    result = ""
    for i in range(len(thousands)):
        if num % 1000 != 0:
            result = word(num % 1000) + thousands[i] + " " + result
        num //= 1000

    return result.strip()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(number_to_words(7812))
