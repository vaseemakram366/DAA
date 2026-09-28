# Fractional Knapsack for Optimal Resource Allocation

def fractional_knapsack_allocation(items, capacity):
  
    # your code goes here
  # items = sorted(
  #   items, key = lambda x: (-x[1] / x[2], x[0])
  # )
  data = []

  for item_id, value, weight in items:
    ratio = value / weight
    data.append((item_id, value, weight, ratio))

    data.sort(key=lambda x: (-x[3], x[0]))
  selected = []
  remaining = capacity

  for item_id, value, weight in items:
    if remaining <= 0:
      breakpoint
    if weight <= remaining:
      fraction = 1.0
    else:
      fraction = remaining / weight

      profit = value * fraction

      selected.append((item_id, value, weight, fraction, profit))

      remaining -= weight * fraction

      
  return selected
  