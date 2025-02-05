# Implement 2 classes, the first one is the Boss and the second one is the Worker.

# Worker has a property 'boss', and its value must be an instance of Boss.

# You can reassign this value, but you should check whether the new value is Boss. 
# Each Boss has a list of his own workers. You should implement a method that allows you to add workers to a Boss. 
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

# You can refactor the existing code.


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def add_worker(self, worker):
        # Checking the worker is an instance of Worker
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Wrong input")

    def get_workers(self):
        #Return the list of workers
        return self._workers  

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None  # Private variable to store boss
        self.set_boss(boss)  # Initialize the boss

    def set_boss(self, new_boss):
        # Check if the new boss is an instance of Boss
        if isinstance(new_boss, Boss):  
            if self._boss:
                self._boss.get_workers().remove(self)  # Remove the worker from the old boss's list if changing
            self._boss = new_boss
            self._boss.add_worker(self)  # Add worker to the new boss's list
        else:
            raise ValueError("Wrong input")

    def get_boss(self):
        return self._boss  # Getter to return the boss

boss1 = Boss(1, "Vova", "Beetroot")
boss2 = Boss(2, "Vasj", "Logicpower")

worker1 = Worker(1, "Alexander", "Beetroot",boss1)
# worker1.set_boss(boss1)
worker2 = Worker(2, "Daria", "Beetroot", boss1)
# worker2.set_boss(boss1)

worker3 = Worker(3, "Ostap", "Logicpower", boss2)

# Changing boss for worker1
worker1.set_boss(boss2)

# Output workers for each boss
print([worker.name for worker in boss1.get_workers()])  # Should print: ['Daria']
print([worker.name for worker in boss2.get_workers()])  # Should print: ['Ostap', 'Alexander']
