# -*- coding: utf-8 -*-
import pandas as pd

from zoo.calculator import ZooCalculator

import unittest


class CalculateTestSuite(unittest.TestCase):

    def setUp(self):
        """
        populate test dataframes
        :return:
        """
        animals_d = {'animal': ["tiger", "leopard", "pelican"],
                     'compound': ["big_cat", "big_cat", "water_bird"],
                     'hours_of_care_per_week': [10, 8, 2],
                     'type_of_food': ["meet", "meat", "fish"],
                     'amount_of_food_per_day': [8, 6, 1.2],
                     'number_of_animals': [4, 2, 8],
                     }
        self.animals_df = pd.DataFrame(data=animals_d)

        food_d = {'type_of_food': ["meat", "fish"],
                  'price_per_kg': [8, 10]}
        self.food_df = pd.DataFrame(data=food_d)

        zookeeper_d = {'compound': ["big_cat", "water_bird"],
                       "hourly_rate": [16, 14]}
        self.zookeeper_df = pd.DataFrame(data=zookeeper_d)

    def test_data_frame_merge_success(self):
        self.assertIsInstance(self.animals_df, pd.DataFrame)
        self.assertIsInstance(self.food_df, pd.DataFrame)
        self.assertIsInstance(self.zookeeper_df, pd.DataFrame)

        zoo_calculator = ZooCalculator(self.animals_df, self.food_df, self.zookeeper_df)

        zoo_df = zoo_calculator.merge_data()
        self.assertIsInstance(zoo_df, pd.DataFrame)

        self.assertEqual(11, len(zoo_df.columns))

    def test_calculations_success(self):
        zoo_calculator = ZooCalculator(self.animals_df, self.food_df, self.zookeeper_df)

        zoo_calculator.merge_data()

        total_cost_per_animal = zoo_calculator.calculate_total_animals_cost()
        # print(total_cost_per_animal)

        self.assertEqual(260.57142857142856, total_cost_per_animal)

        total_cost_per_compound = zoo_calculator.calculate_total_cost_per_compound()
        # print(total_cost_per_compound)

        self.assertListEqual(['big_cat', 'water_bird'], list(total_cost_per_compound.index))

        # get max compound
        total_cost_per_compound = zoo_calculator.calculate_total_cost_per_compound(True)
        # print(total_cost_per_compound)

        self.assertEqual("big_cat", total_cost_per_compound)


if __name__ == '__main__':
    unittest.main()
