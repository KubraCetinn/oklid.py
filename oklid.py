
import math

def euclidean_distance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    distance = math.sqrt(distance)
    return distance

while True:

    x1 = float(input("Birinci noktanın x koordinatını girin: "))
    y1 = float(input("Birinci noktanın y koordinatını girin: "))
    z1 = float(input("Birinci noktanın z koordinatını girin: "))
    
    x2 = float(input("İkinci noktanın x koordinatını girin: "))
    y2 = float(input("İkinci noktanın y koordinatını girin: "))
    z2 = float(input("İkinci noktanın z koordinatını girin: "))
    
    point1 = [x1, y1, z1]
    point2 = [x2, y2, z2]
    
    result = euclidean_distance(point1, point2)
    print("Mesafe:", result)
    
    restart = input("Yeniden başlatmak için 'devam' yazın, çıkmak için 'q' ya da 'quit' yazın: ")
    if restart.lower() == 'q' or restart.lower() == 'quit':
        break
    elif restart.lower() != 'devam':
        print("Geçersiz giriş. Program sonlandırılıyor.")
        break
    
    
    