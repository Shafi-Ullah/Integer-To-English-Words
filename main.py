import time


class Solution(object):
    one_to_nineteen = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    ten_ninety = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    start = 0

    def numberToWords(self, num):
        if num == 0 and self.start == 0:
            return "Zero"
        self.start = 1
        if num == 0:
            return ""
        elif num < 20:
            return self.one_to_nineteen[num]
        elif num < 100:
            integer = num // 10
            reminder = num % 10
            answer = self.ten_ninety[integer] + " " + self.one_to_nineteen[reminder]
            return answer.strip()
        elif num < 1000:
            integer = num // 100
            reminder = num % 100
            answer = (
                self.one_to_nineteen[integer]
                + " Hundred "
                + self.numberToWords(reminder)
            )
            return answer.strip()
        elif num < 10**6:
            integer = num // 1000
            reminder = num % 1000
            answer = (
                self.numberToWords(integer)
                + " Thousand "
                + self.numberToWords(reminder)
            )
            return answer.strip()
        elif num < 10**9:
            integer = num // 10**6
            reminder = num % 10**6
            answer = (
                self.numberToWords(integer) + " Million " + self.numberToWords(reminder)
            )
            return answer.strip()
        elif num < 10**12:
            integer = num // 10**9
            reminder = num % 10**9
            answer = (
                self.numberToWords(integer) + " Billion " + self.numberToWords(reminder)
            )
            return answer.strip()


user = int(input("Enter integer valid number: "))
time1 = time.perf_counter()
a = Solution()
print(a.numberToWords(user))
print(time.perf_counter() - time1)
