def countv(n):
    count=0
    vol='aeiouAEIOU'
    for i in n:
        if i in vol:
            count+=1
    print(f"The number of vowels is {count}")

sen=input('What is your string? ')
countv(sen)
