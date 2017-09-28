numbers = {
    0:"",
    1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    20:'twenty',
    30:'thirty',
    40:'forty',
    50:'fifty',
    60:'sixty',
    70:'seventy',
    80:'eighty',
    90:'nintey'
}

def num_to_word(n):
    if n == 1000:
        return "onethousand"
    word = ""
    num = n % 100
    word += numbers[num] if num in numbers else numbers[num - num%10] + numbers[num%10]
    n //= 100
    if n != 0:
        if num != 0:
            word = "and"+word
        num = n % 10
        word = numbers[num] + "hundred" + word
    return word

def number_letter_count(n):
    total = 0
    for i in range(1,n+1):
        print(i, num_to_word(i), len(num_to_word(i)))
        total += len(num_to_word(i))
    return total

print(number_letter_count(1000))
