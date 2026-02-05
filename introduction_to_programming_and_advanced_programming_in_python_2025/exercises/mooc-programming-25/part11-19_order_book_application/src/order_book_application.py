# Write your solution here
# If you use the classes made in the previous exercise, copy them here
class Task:
    id = 0
    def __init__(self, description: str, programmer: str, workload: int):
        self.description = description
        self.programmer  = programmer
        self.workload    = workload
        self.status      = False

        Task.id += 1
        self.id          = Task.id

    def __str__(self):
        msg1 = f"{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} "
        msg2 = (("" if self.status else "not ") + "finished").upper()
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

    def mark_finished(self, id):
        for order in self.__orders:
            if order.id == id:
                order.mark_finished()
                return
        raise ValueError(f"non-existent id {id}")

    def finished_orders(self):
        return [order for order in self.__orders if order.status == True]

    def unfinished_orders(self):
        return [order for order in self.__orders if order.status == False]

    def status_of_programmer(self, programmer):
        if programmer not in self.__programmers:
            raise ValueError(f"programmer {programmer} not found")
        
        finished_tasks    = [order.workload for order in self.finished_orders() if order.programmer == programmer]
        finished_count    = len(finished_tasks)
        finished_workload = sum(finished_tasks)

        unfinished_tasks    = [order.workload for order in self.unfinished_orders() if order.programmer == programmer]
        unfinished_count    = len(unfinished_tasks)
        unfinished_workload = sum(unfinished_tasks)

        return (finished_count, unfinished_count, finished_workload, unfinished_workload)

class TaskApplication:
    def __init__(self):
        self.__order_book = OrderBook()

    def add_order(self):
        description = input("description: ")
        programmer_and_workload = input("programmer and workload estimate: ")

        try:
            parts = programmer_and_workload.split()
            if len(parts) != 2:
                print("erroneous input")
                return

            programmer, workload = parts
            workload = int(workload)

            self.__order_book.add_order(description, programmer, workload)
            print("added!")
        except ValueError:
            print("erroneous input")

    def list_finished_tasks(self):
        finished = self.__order_book.finished_orders()
        if len(finished) == 0:
            print("no finished tasks")
        else:
            for order in finished:
                print(order)

    def list_unfinished_tasks(self):
        unfinished = self.__order_book.unfinished_orders()
        if len(unfinished) == 0:
            print("no unfinished tasks")
        else:
            for order in unfinished:
                print(order)

    def mark_finished(self):
        try:
            id = int(input("id: "))
            self.__order_book.mark_finished(id)
            print("marked as finished")
        except ValueError:
            print("erroneous input")

    def programmers(self):
        for programmer in self.__order_book.programmers():
            print(programmer)

    def status_of_programmer(self):
        try:
            programmer = input("programmer: ")
            (finished_tasks, unfinished_tasks, finished_workload, unfinished_workload) = self.__order_book.status_of_programmer(programmer)
            print(f"tasks: finished {finished_tasks} not finished {unfinished_tasks}, hours: done {finished_workload} scheduled {unfinished_workload}")
        except ValueError:
            print("erroneous input")

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add order")
        print("2 list finished tasks")
        print("3 list unfinished tasks")
        print("4 mark task as finished")
        print("5 programmers")
        print("6 status of programmer")

    def execute(self):
        self.help()
        while True:
            print()
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_order()
            elif command == "2":
                self.list_finished_tasks()
            elif command == "3":
                self.list_unfinished_tasks()
            elif command == "4":
                self.mark_finished()
            elif command == "5":
                self.programmers()
            elif command == "6":
                self.status_of_programmer()
            else:
                self.help()
def main():
    TaskApplication().execute()

main()
####################################################################
# PART 1
####################################################################
# commands:
# 0 exit
# 1 add order
# 2 list finished tasks
# 3 list unfinished tasks
# 4 mark task as finished
# 5 programmers
# 6 status of programmer

# command: 1
# description: program the next facebook
# programmer and workload estimate: jonah 1000
# added!

# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric 25
# added!

# command: 1
# description: program an app for music theory revision
# programmer and workload estimate: nina 12
# added!

# command: 1
# description: program the next twitter
# programmer and workload estimate: jonah 55
# added!

# command: 2
# no finished tasks

# command: 3
# 1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
# 2: program mobile app for workload accounting (25 hours), programmer eric NOT FINISHED
# 3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED
# 4: program the next twitter (55 hours), programmer jonah NOT FINISHED

# command: 4
# id: 2
# marked as finished

# command: 4
# id: 4
# marked as finished

# command: 2
# 2: program mobile app for workload accounting (25 hours), programmer eric FINISHED
# 4: program the next twitter (55 hours), programmer jonah FINISHED

# command: 3
# 1: program the next facebook (1000 hours), programmer jonah NOT FINISHED
# 3: program an app for music theory revision (12 hours), programmer nina NOT FINISHED

# command: 5
# jonah
# eric
# nina

# command: 6
# programmer: jonah
# tasks: finished 1 not finished 1, hours: done 55 scheduled 1000

####################################################################
# PART 2
####################################################################
# Sample output
# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric xxx
# erroneous input

# command: 1
# description: program mobile app for workload accounting
# programmer and workload estimate: eric
# erroneous input

# command: 4
# id: 1000000
# erroneous input

# command: 4
# id: XXXX
# erroneous input

# command: 6
# programmer: unknownprogrammer
# erroneous input
