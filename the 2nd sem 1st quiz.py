'''

The command (print()).
    As you notice the [print()] is a function that implies a single line of space. And as you can see there is no attribute inside of it.'''

print()
print("Convert The Following:")
print("----------------------")

while True:
    conversion_available=[
    (1, " Meter"," Centemeter"),
    (2, " Inches"," Feet"),
    (3, " Kilograms"," Grams"),
    (4, " Hour", " Year/s")
    ]
    
    print()
    print("Conversion Available:")
    '''
    
              
    In this statement it commands to input the number you are going to choose, from the index number given at the Conversion Available. So the coversion available will shown on the output terminal.

As you will notice the figure (f"), { }
in line 34. for-loop. 
---------------------------------------
1) (f") The f-string:
    It implies for the user to combine string      and integers with in the statement.

2) { } The curly braces:
    It implies for all the value inside of it      is consider as a subject to view in the        output.'''   
    for conversion_number, from_unit, to_unit in conversion_available: 
       print(f"{conversion_number}){from_unit}  to {to_unit}")    
    print()
    '''
    
    
in this part it prompt for the user to choose an index number. We will notice the attribute of [- 1], in line(43) on conversion index value,it implies to view the output of the index number which will starts from number [1].

Without this [-1], the output will start from number[2]. The 1st number will not be able to consider. '''
    conversion = input("Choose a number of conversion to use\n: ")
    conversion_index = int(conversion)-1
    '''
    
In this line we are going to define the index number for the user to choose an index number only to input, attribute are not included.'''
    conversion_number, from_unit, to_unit = conversion_available[conversion_index]
    '''    

this will be the next to prompt after choosing an index number.''' 
    from_value = float(input(f"  Enter how many{from_unit} =  "))
    '''

   
This is the figure for the function in evaluation which we call choices. The [if] stands for if-statement.''' 
    if conversion_number == 1:
        to_value = from_value * 100
        print(f"{from_value} {from_unit} is equal to\n{to_value} {to_unit} ")
        print("-------------------------------------")
        
    elif conversion_number == 2:
        to_value = from_value / 12
        print(f"{from_value} {from_unit} is equal to\n{to_value} {to_unit} ") 
        print("-------------------------------------")
        
    elif conversion_number == 3:
        to_value = from_value * 1000
        print(f"{from_value} {from_unit} is equal to\n{to_value} {to_unit} ") 
        print("-------------------------------------")
        
    elif conversion_number == 4:
        to_value = from_value / 8640
        print(f"{from_value} {from_unit} is equal to\n{to_value} {to_unit} ") 
        print("-------------------------------------")  
                     
                     