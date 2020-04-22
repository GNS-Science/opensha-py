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
java -cp share/py4j/py4j0.10.9.jar src/java/AdditionApplication.java &
```

### 1.3 call it from python

```
python src/test_addition.py
```








