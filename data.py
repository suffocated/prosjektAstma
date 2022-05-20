import matplotlib.pyplot as plt

plt.plot(
    [4,6, 15, 24, 44, 66, 79, 80], 
    [4, 3, 4, 5, 3,4,7,7]
    )

plt.ylabel('Antall folk som bruker medisin')
plt.xlabel('Alder')
plt.suptitle('Menn og kvinner, brukt stmamedisin \n (Brukt medisin siste 14 dager)')

plt.show()
