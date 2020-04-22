from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
hazard_calc_app = gateway.entry_point

print('HazardCurve calculation with default timespan = 30 years')
hazard_calc_app.execute(34.2, -118.344)

print('HazardCurve calculation with timespan = 50 years')
hazard_calc_app.setTimeSpan(50)
hazard_calc_app.execute(34.2, -118.344)
