#!/bin/bash
#
# @brief   gen_data_model
# @version 2.3.7
# @date    Sat Aug 07 07:35:10 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_data_model
pylint gen_data_model > gen_data_model.report
echo "Done"
