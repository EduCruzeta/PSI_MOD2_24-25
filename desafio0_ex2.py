# le do utilixador uma hora e indica a parte do dia

hora = int(input("hora: "))

if hora >= 5 and hora <= 7:
    print("madrugada")
elif hora >= 8 and hora <= 12:
    print("manhã")
elif hora >= 13 and hora <= 19:
    print("Tarde")
else:
    print("noite")