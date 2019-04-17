# temperature conversion
while True:
    w = input('1 for celsius to Fahrenheit\n2 for Fahrenheit to celsius\n')
    if not w.isdigit():
        print('wrong selection')
    else:
        w = int(w)
        if w == 1:
            celsius = input('enter celsius')
            if not celsius.isdigit():
                print('must be numbers')
            else:
                celsius = int(celsius)
                print('for',celsius,'celsius', 'Fahrenheit is',(((celsius*9)/5)+32),end='\n\n')
        elif w == 2:
            fohrenheit = input('enter fohrenheit')
            if not fohrenheit.isdigit():
                print('must be numbers')
            else:
                fohrenheit = int(fohrenheit)
                print('for',fohrenheit,'Fahrenheit','celsius is',(((fohrenheit-32)*5)/9), end='\n\n')
                
    if input('1 for continue, press any other key for exit')=="1":
        continue
    break
