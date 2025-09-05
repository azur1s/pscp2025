"""asdasdasdasd"""
total = float(input())
service_cost = total * 0.1
service_cost_capped = max(min(service_cost, 1000), 50)

vat = (total + service_cost_capped) * 0.07

cost = total + service_cost_capped + vat
print(f"{cost:.2f}")
