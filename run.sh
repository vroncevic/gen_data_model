#!/bin/bash
#
# @brief   gen_data_model
# @version 2.3.7
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "django_model" --type django --output "./demo"
python3 main.py create --name "flask_model" --type flask --output "./demo"
python3 main.py create --name "sqlalchemy_model" --type sqlalchemy --output "./demo"
