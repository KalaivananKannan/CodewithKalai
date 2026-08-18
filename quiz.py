def conti():
    for i in range(1, 6):
        if i==3:
            continue
        print(i, end="")

# range(1, 6) → numbers: 1, 2, 3, 4, 5.

# Loop starts:
# i=1 → condition false → prints 1.
# i=2 → condition false → prints 2.
# i=3 → condition true → continue → skips printing.
# i=4 → prints 4.
# i=5 → prints 5.

# Final output: 1 2 4 5.

def set():
    a={1,2,3}
    b={3,4,5}
    print(a&b)
set()
