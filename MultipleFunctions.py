class MultipleFunction():
    
    def OddEven():
        num=int(input("Enter a number:"))
        if(num%2==0):
            print(num,"is Even number")
            message="Even number"
        else:
            print(num,"is Odd number")
            message="Odd number"
        return message
    
    
    def Subfields():
        print("Sub-fields in AI are:")
        fields=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for  AIFields in fields:
            print(AIFields)
           

    
    def Elegible():
        gender=input("Your Gender:")
        age=int(input("Your Age:"))
        if gender=="Male" and age<21 :
            print("NOT ELIGIBLE")
        elif gender=="Female" and age<18:
            print("NOT ELIGIBLE")
        else:
            print("ELIGIBLE")
    
    
    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        total=sub1+sub2+sub3+sub4+sub5
        percentage=((sub1+sub2+sub3+sub4+sub5)/500)*100
        print("Total:",total)
        print("Percentage:",percentage)
    
    
    def triangle():
        height=float(input("Height:"))
        breadth=float(input("Breadth:"))
        area = (height*breadth)/2
        print("Area of Triangle:",area)
        height1=int(input("height1:"))
        height2=int(input("height2:"))
        breadth=int(input("breadth:"))
        perimeter=height1+height2+breadth
        print("Perimeter of Triangle:",perimeter)


    
