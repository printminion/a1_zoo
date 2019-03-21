# -*- coding: utf-8 -*-
import pandas as pd


class ZooCalculator:
    animals_df = None
    food_df = None
    zookeeper_df = None

    zoo_df = None

    def __init__(self, animals_data="animals.json", food_data="food.json", zookeeper_data="zookeeper.json"):
        """
        initialize calculator with data as path to JSON or as DataFrame

        :param animals_data: path to json or zookeeper_data
        :param food_data: path to json or zookeeper_data
        :param zookeeper_data: path to json or zookeeper_data
        :type animals_data: string, pd.DataFrame
        :type food_data: string, pd.DataFrame
        :type zookeeper_data: string, pd.DataFrame
        """
        if type(animals_data) is pd.DataFrame:
            self.animals_df = animals_data
        else:
            self.animals_df = pd.read_json(animals_data)

        if type(food_data) is pd.DataFrame:
            self.food_df = food_data
        else:
            self.food_df = pd.read_json(food_data)

        if type(zookeeper_data) is pd.DataFrame:
            self.zookeeper_df = zookeeper_data
        else:
            self.zookeeper_df = pd.read_json(zookeeper_data)

    def merge_data(self):
        """

        :return:
        :rtype: pd.DataFrame
        """
        # @todo: probably add a proper column name for safe merge here
        animals_food_df = self.animals_df.merge(self.food_df)

        # @todo: probably add a proper column name for safe merge here
        zoo_df = animals_food_df.merge(self.zookeeper_df)

        # calculate cost_per_week per animal
        zoo_df['cost_per_day_food'] = \
            zoo_df.amount_of_food_per_day \
            * zoo_df.price_per_kg \
            * zoo_df.number_of_animals

        # calculate cost_per_week_care
        zoo_df['cost_per_day_care'] = \
            (zoo_df.hours_of_care_per_week * zoo_df.hourly_rate * zoo_df.number_of_animals) / 7

        zoo_df['total_cost_per_day_per_animal'] = \
            zoo_df['cost_per_day_food'] + zoo_df['cost_per_day_care']

        self.zoo_df = zoo_df

        return self.zoo_df

    def calculate_total_animals_cost(self):
        """
        :return:
        :rtype: pd.DataFrame
        """

        if self.zoo_df is None:
            self.merge_data()

        # calculate total amount on cost_per_week column
        return self.zoo_df['total_cost_per_day_per_animal'].sum(axis=0)

    def calculate_total_cost_per_compound(self, max_only=False):
        """
        :param max_only: Set to true for only max value
        :return:
        :rtype: pd.Series, float
        """
        if self.zoo_df is None:
            self.merge_data()

        # list compounds
        self.zoo_df.groupby(['compound']).groups.keys()

        # output all compounds with total cost
        total_cost_per_compound = self.zoo_df.groupby(['compound'])['total_cost_per_day_per_animal'].sum()

        # get id of max compound column
        if max_only:
            return total_cost_per_compound.idxmax()
        else:
            return total_cost_per_compound
