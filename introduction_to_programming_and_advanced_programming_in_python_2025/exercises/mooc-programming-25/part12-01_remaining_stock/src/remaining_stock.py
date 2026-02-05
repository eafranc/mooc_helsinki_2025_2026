# Write your solution here:
def sort_by_remaining_stock(items: list):
    def order_by_remaining_stock(item: tuple):
        return item[2]

    return sorted(items, key= order_by_remaining_stock) # function sorted keeps original list intact

if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

    for product in sort_by_remaining_stock(products):
        print(f"{product[0]} {product[2]} pcs")
# orange 2 pcs
# apple 3 pcs
# banana 12 pcs
# watermelon 22 pcs
