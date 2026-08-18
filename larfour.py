print("Largest of four numbers")
a=4
b=3
c=2
d=1
def firlar(a,b,c,d):
	if a>b:
		if a>c:
			if a>d:
				print("a is first largest")
			else:
				print("d is first largest")
		else:
			print("c is first largest")
	else:
		if b>c:
			if b>d:
				print("b is first largest")
			else:
				print("d is first largest")
		else:
			if c>d:
				print("c is first largest")
			else:
				print("d is first largest")
firlar(a,b,c,d)
def seclar(a,b,c,d):
	if a>b:
    		if a>c:
        		if a>d:
            			if b>c:         # a is first
                			if b>d:
                    				print("b is second largest")
                			else:
                    				print("d is second largest")
            			else:
                			if c>d:
                    				print("c is second largest")
                			else:
                    				print("d is second largest")
        		else:
            			if a>b:         # d is first
                			if a>c:
                    				print("a is second largest")
                			else:
                    				print("c is second largest")
            	else:
                	if b>c:
                    print("b is second largest")
                else:
                    print("c is second largest")
    else:
        if a>b:             # c is first
            if a>d:
                print("a is second largest")
            else:
                print("d is second largest")
        else:
            if b>d:
                print("b is second largest")
            else:
                print("d is second largest")
else:
    if b>c:
        if b>d:
            if a>c:         # b is first
                if a>d:
                    print("a is second largest")
                else:
                    print("d is second largest")
            else:
                if c>d:
                    print("c is second largest")
                else:
                    print("d is second largest")
        else:
            if a>b:         # d is first
                if a>c:
                    print("a is second largest")
                else:
                    print("c is second largest")
            else:
                if b>c:
                    print("b is second largest")
                else:
                    print("c is second largest")
    else:
        if a>b:             # c is first
            if a>d:
                print("a is second largest")
            else:
                print("d is second largest")
        else:
            if b>d:
                print("b is second largest")
            else:
                print("d is second largest")

seclar(a,b,c,d)
def thilar(a,b,c,d):
	if a<b:
    if a<c:
        if a<d:
            if b<c:         # a is fourth
                if b<d:
                    print("b is third largest")
                else:
                    print("d is third largest")
            else:
                if c<d:
                    print("c is third largest")
                else:
                    print("d is third largest")
        else:
            if a<b:         # d is fourth
                if a<c:
                    print("a is third largest")
                else:
                    print("c is third largest")
            else:
                if b<c:
                    print("b is third largest")
                else:
                    print("c is third largest")
    else:
        if a<b:             # c is fourth
            if a<d:
                print("a is third largest")
            else:
                print("d is third largest")
        else:
            if b<d:
                print("b is third largest")
            else:
                print("d is third largest")
else:
    if b<c:
        if b<d:
            if a<c:         # b is fourth
                if a<d:
                    print("a is third largest")
                else:
                    print("d is third largest")
            else:
                if c<d:
                    print("c is third largest")
                else:
                    print("d is third largest")
        else:
            if a<b:         # d is fourth
                if a<c:
                    print("a is third largest")
                else:
                    print("c is third largest")
            else:
                if b<c:
                    print("b is third largest")
                else:
                    print("c is third largest")
    else:
        if a<b:             # c is fourth
            if a<d:
                print("a is third largest")
            else:
                print("d is third largest")
        else:
            if b<d:
                print("b is third largest")
            else:
                print("d is third largest")
thilar(a,b,c,d)
def foular(a,b,c,d):
	if a<b:
		if a<c:
			if a<d:
				print("a is fourth largest")
			else:
				print("d is fourth largest")
		else:
			print("c is fourth largest")
	else:
		if b<c:
			if b<d:
				print("b is fourth largest")
			else:
				print("d is fourth largest")
		else:
			if c<d:
				print("c is fourth largest")
			else:
				print("d is fourth largest")
foular(a,b,c,d)