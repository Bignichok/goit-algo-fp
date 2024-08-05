def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожної страви
    item_ratios = [(name, item["calories"] / item["cost"]) for name, item in items.items()]
    # Сортуємо страви за співвідношенням калорій до вартості у спадному порядку
    item_ratios.sort(key=lambda x: x[1], reverse=True)
    
    total_cost = 0
    total_calories = 0
    chosen_items = []
    
    for name, ratio in item_ratios:
        cost = items[name]["cost"]
        calories = items[name]["calories"]
        if total_cost + cost <= budget:
            total_cost += cost
            total_calories += calories
            chosen_items.append(name)
    
    return chosen_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо таблицю для зберігання максимальних калорій для кожного бюджету
    dp = [0] * (budget + 1)
    # Зберігаємо предмети, які були обрані для кожного бюджету
    selected_items = [[] for _ in range(budget + 1)]
    
    for name, item in items.items():
        cost = item["cost"]
        calories = item["calories"]
        # Проходимо в зворотному порядку, щоб уникнути використання одного і того ж предмета більше одного разу
        for current_budget in range(budget, cost - 1, -1):
            if dp[current_budget - cost] + calories > dp[current_budget]:
                dp[current_budget] = dp[current_budget - cost] + calories
                selected_items[current_budget] = selected_items[current_budget - cost] + [name]
    
    return selected_items[budget], dp[budget]

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
budget = 150


greedy_chosen_items, greedy_total_calories = greedy_algorithm(items, budget)
print(f"Chosen items - greedy_algorithm: {greedy_chosen_items}")
print(f"Total calories - greedy_algorithm: {greedy_total_calories}")

dynamic_chosen_items, dynamic_total_calories = dynamic_programming(items, budget)
print(f"Chosen items - dynamic_programming: {dynamic_chosen_items}")
print(f"Total calories - dynamic_programming: {greedy_total_calories}")
