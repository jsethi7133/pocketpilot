class RulesEngine:
    def __init__(self):
        self.rules = {
            'salary': 'Income',
            'payroll': 'Income',
            'rent': 'Rent',
            'house rent': 'Rent',
            'uber': 'Transport',
            'ola': 'Transport',
            'swiggy': 'Food',
            'zomato': 'Food',
            'amazon': 'Shopping',
            'flipkart': 'Shopping',
            'netflix': 'Subscriptions',
            'spotify': 'Subscriptions',
            'grocery': 'Groceries',
            'groceries': 'Groceries'
        }

    def apply(self, description: str) -> str:
        d = (description or '').lower()
        for k, v in self.rules.items():
            if k in d:
                return v
        return 'uncategorized'
