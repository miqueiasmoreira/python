A, B, C = map(int, input().split())

maior_ab = (A+B+abs(A-B)) / 2

maior_abc = (maior_ab + C + abs(maior_ab - C)) // 2

print(f"{maior_abc} eh o maior")