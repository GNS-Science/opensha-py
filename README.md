README.md

# opensha-py

A python bridge for opensha based on [py4j.org](https://www.py4j.org/#welcome-to-py4j)

Taking the example from 
https://github.com/opensha/opensha-core/blob/master/src/org/opensha/sha/examples/HazardCurveCalcExample.java
and wrapping it with a py4j gateway. 

Now, we can do this in python...

```python
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

## 1.0 Python setup

prerequisites:
 - python3
 - py4j 

## 2.0 Java compile

Note the opensha-py project is cloned into a folder containing the main opensha repos - see https://github.com/opensha/opensha-commons/blob/master/README.md)

The class path includes:

- the 'fat' opensha Jar file
- the py4j Jar
 
```bash
javac -cp opensha-core/build/libs/opensha-core-all.jar:opensha-py/share/py4j/py4j0.10.9.jar:. opensha-py/src/java/HazardCurveCalcGateway.java 
```

## 3.0 Run the Java gateway server (background)... 

```bash
java -cp opensha-core/build/libs/opensha-core-all.jar:opensha-py/share/py4j/py4j0.10.9.jar:. opensha-py/src/java/HazardCurveCalcGateway.java src/java/HazardCurveCalcGateway
```

## 4.0 Call HazardCurveCalc from python client

```bash
python opensha-py/src/test_gateway.py 
```




