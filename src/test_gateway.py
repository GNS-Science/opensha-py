from py4j.java_gateway import JavaGateway

gateway = JavaGateway()
hazard_calc_app = gateway.entry_point

# print('HazardCurve calculation with default timespan = 30 years')
# hazard_calc_app.execute(34.2, -118.344)

print('HazardCurve calculation with timespan = 50 years')
hazard_calc_app.setTimeSpan(50)
res = hazard_calc_app.execute(34.2, -118.344)


print()
print("Result")

print("Earthquake rupture forecast (ERF)")
print("=================================")
for line in res.info():
	print(line)
print()

print("Site parameters")
print("===============")
for line in res.siteParameters():
	print(line)
print()


print("PGA curve")
print("=========")
for point in res.pgaCurve()[29:-15]:
	print(point.getX(), point.getY())
print('...\n')

print("SA curve")
print("=========")
for point in res.saCurve()[29:-15]:
	print(point.getX(), point.getY())
print('...\n')

