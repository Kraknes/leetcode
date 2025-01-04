class Solution:
    def romanToInt(self, s: str) -> int:
        int = 0
        x = s[::-1]
        y = []

        for i in range(len(x)):
            if x[i] == "I":
                y.insert(i,1)
            elif x[i] == "V":
                y.insert(i,5)
            elif x[i] == "X":
                y.insert(i,10)
            elif x[i] == "L":
                y.insert(i,50)
            elif x[i] == "C":
                y.insert(i,100)
            elif x[i] == "D":
                y.insert(i,500)
            elif x[i] == "M":
                y.insert(i,1000)

        for i in range(len(y)):
            if y[i-1] > y[i] and i != 0:
                if y[i] == 1:
                    int -= 1
                elif y[i] == 5:
                    int -= 5
                elif y[i] == 10:
                    int -= 10
                elif y[i] == 50:
                    int += 50
                elif y[i] == 100:
                    int -= 100
                elif y[i] == 500:
                    int -= 500
                elif y[i] == 1000:
                    int += 1000
            elif y[i] == 1:
                int += 1
            elif y[i] == 5:
                int += 5
            elif y[i] == 10:
                int += 10
            elif y[i] == 50:
                int += 50
            elif y[i] == 100:
                int += 100
            elif y[i] == 500:
                int += 500
            elif y[i] == 1000:
                int += 1000
        return int