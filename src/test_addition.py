from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
random = gateway.jvm.java.util.Random()
number1 = random.nextInt(10) 
number2 = random.nextInt(10)
addition_app = gateway.entry_point

#both python and java should add the same....
assert addition_app.addition(number1, number2) == number1 + number2



