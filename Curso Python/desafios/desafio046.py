from time import sleep
for c in range(10, -1, -1):
    sleep(1)
    print(c)
for f in range(0, 4):
    sleep(0.5)
    print('''\033[1;34m----
          -----**>><<**\033[m''')
    (0.3)
    print('''\033[1;32m---  -
          ---    --**>><   <**\033[m''')
    (0.6)
    print('''\033[1;34m----
          --- --**>>  <  <**\033[m''')
print('FIM')