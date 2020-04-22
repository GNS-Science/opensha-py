README.md

# opensha-py

A python bridge for opensha based on py4j.org

## 1. Demo example based on this https://www.py4j.org/#welcome-to-py4j


### 1.1 compile the java application gateway

```
java -cp share/py4j/py4j0.10.9.jar src/java/AdditionApplication.java
```

### 1.2 Run it (background)... 

```
java -cp share/py4j/py4j0.10.9.jar src/java/AdditionApplication &
```

### 1.3 call it from python

```
python src/test_addition.py
```

## 2 HazardCurveCalcGateway demo

Taking the example from 
https://github.com/opensha/opensha-core/blob/master/src/org/opensha/sha/examples/HazardCurveCalcExample.java
and wrapping it with a py4j gateway. Now, we can do this...


```
#!python
from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
hazard_calc_app = gateway.entry_point

print('HazardCurve calculation with default timespan = 30 years')
hazard_calc_app.execute(34.2, -118.344)

print('HazardCurve calculation with timespan = 50 years')
hazard_calc_app.setTimeSpan(50)
hazard_calc_app.execute(34.2, -118.344)
```

NB steps 2.1 and 2.2 below are needed before this works.... 


### 2.1 Compile

```
javac -cp opensha-core/build/libs/opensha-core-all.jar:opensha-py/share/py4j/py4j0.10.9.jar:. opensha-py/src/java/HazardCurveCalcGateway.java 
```

### 2.2 Run it (background)... 

```
java -cp opensha-core/build/libs/opensha-core-all.jar:opensha-py/share/py4j/py4j0.10.9.jar:. opensha-py/src/java/HazardCurveCalcGateway.java src/java/HazardCurveCalcGateway
```

### 2.3 Call it from our python test client

```
python opensha-py/src/test_gateway.py 
```




