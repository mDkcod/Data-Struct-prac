def number_to_words(num):
    # Handle the special case where the number is zero
    if num == 0:
        return "Zero"

    # List for numbers below 20, including all numbers from 0 to 19
    below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
                "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

    # List for tens multiples
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    
    # List for thousands, millions, billions
    thousands = ["", "Thousand", "Million", "Billion"]

    # Function to convert a number less than 1000 to words
    def word(num):
        if num == 0:
            return ""
        elif num < 20:  # Numbers less than 20
            return below_20[num] + " "
        elif num < 100:  # Numbers between 20 and 99
            return tens[num // 10] + " " + below_20[num % 10] + " "
        else:  # Numbers between 100 and 999
            return below_20[num // 100] + " Hundred " + word(num % 100)
    
    result = ""
    
    # Process each block of 1000
    for i in range(len(thousands)):
        if num % 1000 != 0:  # If the current block is non-zero
            result = word(num % 1000) + thousands[i] + " " + result
        num //= 1000  # Move to the next block

    # Strip any trailing spaces and return the result
    return result.strip()

# Main execution block to test the function
if __name__ == '__main__':
    print(number_to_words(782))  # Example test case
