thruten = []
i = 1

while i <= 10:
    thruten.append(i)
    i += 1

print("all thru ten: " + str(thruten))

eventhruten = []
j = 1

while j <= 10:
    if j % 2 == 0:
        eventhruten.append(j)
    j += 1

print("even thru ten: " + str(eventhruten))
