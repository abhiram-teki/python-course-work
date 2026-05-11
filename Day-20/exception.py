try:
    balance=100
    wd=-2000
    if wd<0:
        raise Exception('Please enter positive number')
except Exception as e:
    print(f"Error occured: {e}")
else:
    print("No Error")
finally:
    print('End')
