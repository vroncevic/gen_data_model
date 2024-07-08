#!/bin/bash
#
# @brief   gen_data_model
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2022
# @company None, free software to use 2022
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_data_model_coverage.xml gen_data_model_coverage.json .coverage
rm -rf fresh_new/ new_simple_test/ full_simple/ full_simple_new/ latest_pro/ simple.py model_base.py latest_pro.py
ats_coverage_run.py -n gen_data_model -p ../README.md
rm -rf fresh_new/ new_simple_test/ full_simple/ full_simple_new/ latest_pro/ simple.py model_base.py latest_pro.py
python3 -m coverage run -m --source=../gen_data_model unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_data_model_coverage.xml 
python3 -m coverage json -o gen_data_model_coverage.json
python3 -m coverage report --format=markdown -m
