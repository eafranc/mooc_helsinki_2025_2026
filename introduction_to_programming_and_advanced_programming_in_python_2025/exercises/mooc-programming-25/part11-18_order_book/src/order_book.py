# Write your solution here:
class Task:
    id = 0 # class attribute

    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.workload    = workload
        self.programmer  = programmer
        self.status      = False

        Task.id += 1
        self.id          = Task.id

    def __str__(self):
        msg1 = f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer}"
        msg2 = ((" not " if self.status == False else " ") + "finished").upper()
        return msg1 + msg2

    def is_finished(self):
        return self.status

    def mark_finished(self):
        self.status = True

class OrderBook:
    def __init__(self):
        self.__orders      = []
        self.__programmers = []
        

    def add_order(self, description, programmer, workload):
        order = Task(description, programmer, workload)
        self.__orders.append(order)

        if programmer not in self.__programmers:
            self.__programmers.append(programmer)

    def all_orders(self):
        return self.__orders

    def programmers(self):
        return self.__programmers

    def mark_finished(self, id: int):
        is_found =  False
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                is_found = True
                break
        if not is_found:
            raise ValueError(f"non-existing id {id}")

    def finished_orders(self):
        return [order for order in self.__orders if order.status == True]
        
    def unfinished_orders(self):
        return [order for order in self.__orders if order.status == False]

    def status_of_programmer(self, programmer: str):
        if programmer not in self.programmers():
            raise ValueError(f"programmer {programmer} not found")
        else:
            finished_tasks    = [order.workload for order in self.finished_orders() if order.programmer == programmer]
            finished_count    = len(finished_tasks)
            finished_workload = sum(finished_tasks)

            unfinished_tasks    = [order.workload for order in self.unfinished_orders() if order.programmer == programmer]
            unfinished_count    = len(unfinished_tasks)
            unfinished_workload = sum(unfinished_tasks)

            return (finished_count, unfinished_count, finished_workload , unfinished_workload)


if __name__ == "__main__":
    ###########################################################################################################
    print("=" * 100)
    print("PART 1")
    print("=" * 100)

    t1 = Task("program hello world", "Eric", 3)
    print(t1.id, t1.description, t1.programmer, t1.workload) # 1 program hello world Eric 3
    print(t1) # 1: program hello world (3 hours), programmer Eric NOT FINISHED
    print(t1.is_finished()) # False
    t1.mark_finished()
    print(t1) # 1: program hello world (3 hours), programmer Eric FINISHED
    print(t1.is_finished()) # True
    t2 = Task("program webstore", "Adele", 10)
    t3 = Task("program mobile app for workload accounting", "Eric", 25)
    print(t2) # 2: program webstore (10 hours), programmer Adele NOT FINISHED
    print(t3) # 3: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
    ###########################################################################################################
    print("=" * 100)
    print("PART 2")
    print("=" * 100)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    for order in orders.all_orders():
        print(order)
# 1: program webstore (10 hours), programmer Adele NOT FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer Eric NOT FINISHED
# 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    print()

    for programmer in orders.programmers():
        print(programmer)
# Adele
# Eric
    ###########################################################################################################
    print("=" * 100)
    print("PART 3")
    print("=" * 100)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Eric", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)

    orders.mark_finished(7)
    orders.mark_finished(8)

    for order in orders.all_orders():
        print(order)
# 1: program webstore (10 hours), programmer Adele FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer Eric FINISHED
# 3: program app for practising mathematics (100 hours), programmer Adele NOT FINISHED
    print("-" * 10)
    print("FINISHED ORDERS")
    finished_orders = orders.finished_orders()
    for order in finished_orders:
        print(order)
    print()
    print("-" * 10)
    print("UNFINISHED ORDERS")    
    unfinished_orders = orders.unfinished_orders()
    for order in unfinished_orders:
        print(order)

    ###########################################################################################################
    print("=" * 100)
    print("PART 4")
    print("=" * 100)

    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(10)
    orders.mark_finished(11)

    status = orders.status_of_programmer("Adele")
    print(status) # (2, 1, 35, 100)
