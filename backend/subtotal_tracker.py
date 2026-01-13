class Friend:
    def __init__(self, name: str):
        self.name = name
        self.subtotal = 0

    def add_item(self, item_price: float):
        self.subtotal += item_price

    def remove_item(self, item_price: float):
        self.subtotal -= item_price

    def get_subtotal(self) -> float:
        return self.subtotal
    
    def get_name(self):
        return self.name

if __name__ == "__main__":
    friend1 = Friend('Jacob')
    friend2 = Friend('Jessica')
    friend3 = Friend('Ryan')
    friend4 = Friend('Lexi')

    item1 = 25.50
    item2 = 50.25
    item3 = 10.33
    item4 = 27.19

    print(f"\n===Test Functions===\n")
    print(f"Before operations:")
    print(f"\n{friend1.get_name()}'s total: ${friend1.get_subtotal()}")
    print(f"{friend2.get_name()}'s total: ${friend2.get_subtotal()}")
    print(f"{friend3.get_name()}'s total: ${friend3.get_subtotal()}")
    print(f"{friend4.get_name()}'s total: ${friend4.get_subtotal()}")

    friend1.add_item(item1)
    friend2.add_item(item2)
    friend3.add_item(item3)
    friend4.add_item(item4)

    print(f"\nAfter adding items:")
    print(f"\n{friend1.get_name()}'s total: ${friend1.get_subtotal()}")
    print(f"{friend2.get_name()}'s total: ${friend2.get_subtotal()}")
    print(f"{friend3.get_name()}'s total: ${friend3.get_subtotal()}")
    print(f"{friend4.get_name()}'s total: ${friend4.get_subtotal()}")

    friend1.remove_item(item1)
    friend2.remove_item(item2)
    friend3.remove_item(item3)
    friend4.remove_item(item4)

    print(f"\nAfter removing items:")
    print(f"\n{friend1.get_name()}'s total: ${friend1.get_subtotal()}")
    print(f"{friend2.get_name()}'s total: ${friend2.get_subtotal()}")
    print(f"{friend3.get_name()}'s total: ${friend3.get_subtotal()}")
    print(f"{friend4.get_name()}'s total: ${friend4.get_subtotal()}")