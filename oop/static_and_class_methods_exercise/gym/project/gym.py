from project.customer import Customer
from project.equipment import Equipment
from project.exerciseplan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = self.find_by_id(self.subscriptions, subscription_id)
        customer = self.find_by_id(self.customers, subscription.customer_id)
        trainer = self.find_by_id(self.trainers, subscription.trainer_id)
        equipment = self.find_by_id(self.equipment, equipment.id)

    def find_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity
