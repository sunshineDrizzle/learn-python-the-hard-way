# 车子的数量
cars = 100

# 车子内部的空间
space_in_a_car = 4  # 4和4.0的在本程序中的区别在于表达式cars_driven * space_in_a_car所返回的对象类型

# 司机的数量
drivers = 30

# 乘客的数量
passengers = 90

# 不可驾驶的车子数量
cars_not_driven = cars - drivers

# 可驾驶的车子数量
cars_driven = drivers

# 可拼车的总量
carpool_capacity = cars_driven * space_in_a_car

# 每辆车搭载乘客的平均数量
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")

'''
study drills中提到的错误信息如下：
Traceback (most recent call last):
  File "ex4.py", line 8, in <module>
    average_passengers_per_car = car_pool_capacity / passenger
NameError: name 'car_pool_capacity' is not defined
我的解释是：因为变量名的使用要在赋值之后，前面我们定义的变量名是carpool_capacity
而不是car_pool_capacity，所以会引发变量名错误，后面的passenger事实上在之前也没有定义，
之所以没有报错，我认为是在检测到它的错误之前，程序已经因为car_pool_capacity的错误而中止了。
'''